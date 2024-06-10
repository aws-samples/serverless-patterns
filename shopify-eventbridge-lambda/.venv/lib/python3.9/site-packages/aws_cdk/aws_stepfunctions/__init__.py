'''
# AWS Step Functions Construct Library

The `aws-cdk-lib/aws-stepfunctions` package contains constructs for building
serverless workflows using objects. Use this in conjunction with the
`aws-cdk-lib/aws-stepfunctions-tasks` package, which contains classes used
to call other AWS services.

Defining a workflow looks like this (for the [Step Functions Job Poller
example](https://docs.aws.amazon.com/step-functions/latest/dg/job-status-poller-sample.html)):

## Example

```python
import aws_cdk.aws_lambda as lambda_

# submit_lambda: lambda.Function
# get_status_lambda: lambda.Function


submit_job = tasks.LambdaInvoke(self, "Submit Job",
    lambda_function=submit_lambda,
    # Lambda's result is in the attribute `guid`
    output_path="$.guid"
)

wait_x = sfn.Wait(self, "Wait X Seconds",
    time=sfn.WaitTime.seconds_path("$.waitSeconds")
)

get_status = tasks.LambdaInvoke(self, "Get Job Status",
    lambda_function=get_status_lambda,
    # Pass just the field named "guid" into the Lambda, put the
    # Lambda's result in a field called "status" in the response
    input_path="$.guid",
    output_path="$.status"
)

job_failed = sfn.Fail(self, "Job Failed",
    cause="AWS Batch Job Failed",
    error="DescribeJob returned FAILED"
)

final_status = tasks.LambdaInvoke(self, "Get Final Job Status",
    lambda_function=get_status_lambda,
    # Use "guid" field as input
    input_path="$.guid",
    output_path="$.Payload"
)

definition = submit_job.next(wait_x).next(get_status).next(sfn.Choice(self, "Job Complete?").when(sfn.Condition.string_equals("$.status", "FAILED"), job_failed).when(sfn.Condition.string_equals("$.status", "SUCCEEDED"), final_status).otherwise(wait_x))

sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition),
    timeout=Duration.minutes(5),
    comment="a super cool state machine"
)
```

You can find more sample snippets and learn more about the service integrations
in the `aws-cdk-lib/aws-stepfunctions-tasks` package.

## State Machine

A `stepfunctions.StateMachine` is a resource that takes a state machine
definition. The definition is specified by its start state, and encompasses
all states reachable from the start state:

```python
start_state = sfn.Pass(self, "StartState")

sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(start_state)
)
```

State machines are made up of a sequence of **Steps**, which represent different actions
taken in sequence. Some of these steps represent *control flow* (like `Choice`, `Map` and `Wait`)
while others represent calls made against other AWS services (like `LambdaInvoke`).
The second category are called `Task`s and they can all be found in the module [`aws-stepfunctions-tasks`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_stepfunctions_tasks-readme.html).

State machines execute using an IAM Role, which will automatically have all
permissions added that are required to make all state machine tasks execute
properly (for example, permissions to invoke any Lambda functions you add to
your workflow). A role will be created by default, but you can supply an
existing one as well.

Set the `removalPolicy` prop to `RemovalPolicy.RETAIN` if you want to retain the execution
history when CloudFormation deletes your state machine.

Alternatively you can specify an existing step functions definition by providing a string or a file that contains the ASL JSON.

```python
sfn.StateMachine(self, "StateMachineFromString",
    definition_body=sfn.DefinitionBody.from_string("{\"StartAt\":\"Pass\",\"States\":{\"Pass\":{\"Type\":\"Pass\",\"End\":true}}}")
)

sfn.StateMachine(self, "StateMachineFromFile",
    definition_body=sfn.DefinitionBody.from_file("./asl.json")
)
```

## State Machine Data

An Execution represents each time the State Machine is run. Every Execution has [State Machine
Data](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-data.html):
a JSON document containing keys and values that is fed into the state machine,
gets modified by individual steps as the state machine progresses, and finally
is produced as output.

By default, the entire Data object is passed into every state, and the return data of the step
becomes new the new Data object. This behavior can be modified by supplying values for `inputPath`,
`resultSelector`, `resultPath` and `outputPath`.

### Manipulating state machine data using inputPath, resultSelector, resultPath and outputPath

These properties impact how each individual step interacts with the state machine data:

* `stateName`: the name of the state in the state machine definition. If not supplied, defaults to the construct id.
* `inputPath`: the part of the data object that gets passed to the step (`itemsPath` for `Map` states)
* `resultSelector`: the part of the step result that should be added to the state machine data
* `resultPath`: where in the state machine data the step result should be inserted
* `outputPath`: what part of the state machine data should be retained
* `errorPath`: the part of the data object that gets returned as the step error
* `causePath`: the part of the data object that gets returned as the step cause

Their values should be a string indicating a [JSON path](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-paths.html) into the State Machine Data object (like `"$.MyKey"`). If absent, the values are treated as if they were `"$"`, which means the entire object.

The following pseudocode shows how AWS Step Functions uses these parameters when executing a step:

```js
// Schematically show how Step Functions evaluates functions.
// [] represents indexing into an object by a using JSON path.

input = state[inputPath]

result = invoke_step(select_parameters(input))

state[resultPath] = result[resultSelector]

state = state[outputPath]
```

Instead of a JSON path string, each of these paths can also have the special value `JsonPath.DISCARD`, which causes the corresponding indexing expression to return an empty object (`{}`). Effectively, that means there will be an empty input object, an empty result object, no effect on the state, or an empty state, respectively.

Some steps (mostly Tasks) have *Parameters*, which are selected differently. See the next section.

See the official documentation on [input and output processing in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-input-output-filtering.html).

### Passing Parameters to Tasks

Tasks take parameters, whose values can be taken from the State Machine Data object. For example, your
workflow may want to start a CodeBuild with an environment variable that is taken from the State Machine data, or pass part of the State Machine Data into an AWS Lambda Function.

In the original JSON-based states language used by AWS Step Functions, you would
add `.$` to the end of a key to indicate that a value needs to be interpreted as
a JSON path. In the CDK API you do not change the names of any keys. Instead, you
pass special values. There are 3 types of task inputs to consider:

* Tasks that accept a "payload" type of input (like AWS Lambda invocations, or posting messages to SNS topics or SQS queues), will take an object of type `TaskInput`, like `TaskInput.fromObject()` or `TaskInput.fromJsonPathAt()`.
* When tasks expect individual string or number values to customize their behavior, you can also pass a value constructed by `JsonPath.stringAt()` or `JsonPath.numberAt()`.
* When tasks expect strongly-typed resources and you want to vary the resource that is referenced based on a name from the State Machine Data, reference the resource as if it was external (using `JsonPath.stringAt()`). For example, for a Lambda function: `Function.fromFunctionName(this, 'ReferencedFunction', JsonPath.stringAt('$.MyFunctionName'))`.

For example, to pass the value that's in the data key of `OrderId` to a Lambda
function as you invoke it, use `JsonPath.stringAt('$.OrderId')`, like so:

```python
import aws_cdk.aws_lambda as lambda_

# order_fn: lambda.Function


submit_job = tasks.LambdaInvoke(self, "InvokeOrderProcessor",
    lambda_function=order_fn,
    payload=sfn.TaskInput.from_object({
        "OrderId": sfn.JsonPath.string_at("$.OrderId")
    })
)
```

The following methods are available:

| Method | Purpose |
|--------|---------|
| `JsonPath.stringAt('$.Field')` | reference a field, return the type as a `string`. |
| `JsonPath.listAt('$.Field')` | reference a field, return the type as a list of strings. |
| `JsonPath.numberAt('$.Field')` | reference a field, return the type as a number. Use this for functions that expect a number argument. |
| `JsonPath.objectAt('$.Field')` | reference a field, return the type as an `IResolvable`. Use this for functions that expect an object argument. |
| `JsonPath.entirePayload` | reference the entire data object (equivalent to a path of `$`). |
| `JsonPath.taskToken` | reference the [Task Token](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token), used for integration patterns that need to run for a long time. |
| `JsonPath.executionId` | reference the Execution Id field of the context object. |
| `JsonPath.executionInput` | reference the Execution Input object of the context object. |
| `JsonPath.executionName` | reference the Execution Name field of the context object. |
| `JsonPath.executionRoleArn` | reference the Execution RoleArn field of the context object. |
| `JsonPath.executionStartTime` | reference the Execution StartTime field of the context object. |
| `JsonPath.stateEnteredTime` | reference the State EnteredTime field of the context object. |
| `JsonPath.stateName` | reference the State Name field of the context object. |
| `JsonPath.stateRetryCount` | reference the State RetryCount field of the context object. |
| `JsonPath.stateMachineId` | reference the StateMachine Id field of the context object. |
| `JsonPath.stateMachineName` | reference the StateMachine Name field of the context object. |

You can also call [intrinsic functions](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html) using the methods on `JsonPath`:

| Method | Purpose |
|--------|---------|
| `JsonPath.array(JsonPath.stringAt('$.Field'), ...)` | make an array from other elements. |
| `JsonPath.arrayPartition(JsonPath.listAt('$.inputArray'), 4)` | partition an array. |
| `JsonPath.arrayContains(JsonPath.listAt('$.inputArray'), 5)` | determine if a specific value is present in an array. |
| `JsonPath.arrayRange(1, 9, 2)` | create a new array containing a specific range of elements. |
| `JsonPath.arrayGetItem(JsonPath.listAt('$.inputArray'), 5)` | get a specified index's value in an array. |
| `JsonPath.arrayLength(JsonPath.listAt('$.inputArray'))` | get the length of an array. |
| `JsonPath.arrayUnique(JsonPath.listAt('$.inputArray'))` | remove duplicate values from an array. |
| `JsonPath.base64Encode(JsonPath.stringAt('$.input'))` | encode data based on MIME Base64 encoding scheme. |
| `JsonPath.base64Decode(JsonPath.stringAt('$.base64'))` | decode data based on MIME Base64 decoding scheme. |
| `JsonPath.hash(JsonPath.objectAt('$.Data'), JsonPath.stringAt('$.Algorithm'))` | calculate the hash value of a given input. |
| `JsonPath.jsonMerge(JsonPath.objectAt('$.Obj1'), JsonPath.objectAt('$.Obj2'))` | merge two JSON objects into a single object. |
| `JsonPath.stringToJson(JsonPath.stringAt('$.ObjStr'))` | parse a JSON string to an object |
| `JsonPath.jsonToString(JsonPath.objectAt('$.Obj'))` | stringify an object to a JSON string |
| `JsonPath.mathRandom(1, 999)` | return a random number. |
| `JsonPath.mathAdd(JsonPath.numberAt('$.value1'), JsonPath.numberAt('$.step'))` | return the sum of two numbers. |
| `JsonPath.stringSplit(JsonPath.stringAt('$.inputString'), JsonPath.stringAt('$.splitter'))` | split a string into an array of values. |
| `JsonPath.uuid()` | return a version 4 universally unique identifier (v4 UUID). |
| `JsonPath.format('The value is {}.', JsonPath.stringAt('$.Value'))` | insert elements into a format string. |

## Amazon States Language

This library comes with a set of classes that model the [Amazon States
Language](https://states-language.net/spec.html). The following State classes
are supported:

* [`Task`](#task)
* [`Pass`](#pass)
* [`Wait`](#wait)
* [`Choice`](#choice)
* [`Parallel`](#parallel)
* [`Succeed`](#succeed)
* [`Fail`](#fail)
* [`Map`](#map)
* [`Distributed Map`](#distributed-map)
* [`Custom State`](#custom-state)

An arbitrary JSON object (specified at execution start) is passed from state to
state and transformed during the execution of the workflow. For more
information, see the States Language spec.

### Task

A `Task` represents some work that needs to be done. Do not use the `Task` class directly.

Instead, use one of the classes in the `aws-cdk-lib/aws-stepfunctions-tasks` module,
which provide a much more ergonomic way to integrate with various AWS services.

### Pass

A `Pass` state passes its input to its output, without performing work.
Pass states are useful when constructing and debugging state machines.

The following example injects some fixed data into the state machine through
the `result` field. The `result` field will be added to the input and the result
will be passed as the state's output.

```python
# Makes the current JSON state { ..., "subObject": { "hello": "world" } }
pass = sfn.Pass(self, "Add Hello World",
    result=sfn.Result.from_object({"hello": "world"}),
    result_path="$.subObject"
)

# Set the next state
next_state = sfn.Pass(self, "NextState")
pass.next(next_state)
```

The `Pass` state also supports passing key-value pairs as input. Values can
be static, or selected from the input with a path.

The following example filters the `greeting` field from the state input
and also injects a field called `otherData`.

```python
pass = sfn.Pass(self, "Filter input and inject data",
    state_name="my-pass-state",  # the custom state name for the Pass state, defaults to 'Filter input and inject data' as the state name
    parameters={ # input to the pass state
        "input": sfn.JsonPath.string_at("$.input.greeting"),
        "other_data": "some-extra-stuff"}
)
```

The object specified in `parameters` will be the input of the `Pass` state.
Since neither `Result` nor `ResultPath` are supplied, the `Pass` state copies
its input through to its output.

Learn more about the [Pass state](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-pass-state.html)

### Wait

A `Wait` state waits for a given number of seconds, or until the current time
hits a particular time. The time to wait may be taken from the execution's JSON
state.

```python
# Wait until it's the time mentioned in the the state object's "triggerTime"
# field.
wait = sfn.Wait(self, "Wait For Trigger Time",
    time=sfn.WaitTime.timestamp_path("$.triggerTime")
)

# Set the next state
start_the_work = sfn.Pass(self, "StartTheWork")
wait.next(start_the_work)
```

### Choice

A `Choice` state can take a different path through the workflow based on the
values in the execution's JSON state:

```python
choice = sfn.Choice(self, "Did it work?")

# Add conditions with .when()
success_state = sfn.Pass(self, "SuccessState")
failure_state = sfn.Pass(self, "FailureState")
choice.when(sfn.Condition.string_equals("$.status", "SUCCESS"), success_state)
choice.when(sfn.Condition.number_greater_than("$.attempts", 5), failure_state)

# Use .otherwise() to indicate what should be done if none of the conditions match
try_again_state = sfn.Pass(self, "TryAgainState")
choice.otherwise(try_again_state)
```

If you want to temporarily branch your workflow based on a condition, but have
all branches come together and continuing as one (similar to how an `if ... then ... else` works in a programming language), use the `.afterwards()` method:

```python
choice = sfn.Choice(self, "What color is it?")
handle_blue_item = sfn.Pass(self, "HandleBlueItem")
handle_red_item = sfn.Pass(self, "HandleRedItem")
handle_other_item_color = sfn.Pass(self, "HanldeOtherItemColor")
choice.when(sfn.Condition.string_equals("$.color", "BLUE"), handle_blue_item)
choice.when(sfn.Condition.string_equals("$.color", "RED"), handle_red_item)
choice.otherwise(handle_other_item_color)

# Use .afterwards() to join all possible paths back together and continue
ship_the_item = sfn.Pass(self, "ShipTheItem")
choice.afterwards().next(ship_the_item)
```

You can add comments to `Choice` states as well as conditions that use `choice.when`.

```python
choice = sfn.Choice(self, "What color is it?",
    comment="color comment"
)
handle_blue_item = sfn.Pass(self, "HandleBlueItem")
handle_other_item_color = sfn.Pass(self, "HanldeOtherItemColor")
choice.when(sfn.Condition.string_equals("$.color", "BLUE"), handle_blue_item,
    comment="blue item comment"
)
choice.otherwise(handle_other_item_color)
```

If your `Choice` doesn't have an `otherwise()` and none of the conditions match
the JSON state, a `NoChoiceMatched` error will be thrown. Wrap the state machine
in a `Parallel` state if you want to catch and recover from this.

#### Available Conditions

see [step function comparison operators](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-choice-state.html#amazon-states-language-choice-state-rules)

* `Condition.isPresent` - matches if a json path is present
* `Condition.isNotPresent` - matches if a json path is not present
* `Condition.isString` - matches if a json path contains a string
* `Condition.isNotString` - matches if a json path is not a string
* `Condition.isNumeric` - matches if a json path is numeric
* `Condition.isNotNumeric` - matches if a json path is not numeric
* `Condition.isBoolean` - matches if a json path is boolean
* `Condition.isNotBoolean` - matches if a json path is not boolean
* `Condition.isTimestamp` - matches if a json path is a timestamp
* `Condition.isNotTimestamp` - matches if a json path is not a timestamp
* `Condition.isNotNull` - matches if a json path is not null
* `Condition.isNull` - matches if a json path is null
* `Condition.booleanEquals` - matches if a boolean field has a given value
* `Condition.booleanEqualsJsonPath` - matches if a boolean field equals a value in a given mapping path
* `Condition.stringEqualsJsonPath` - matches if a string field equals a given mapping path
* `Condition.stringEquals` - matches if a field equals a string value
* `Condition.stringLessThan` - matches if a string field sorts before a given value
* `Condition.stringLessThanJsonPath` - matches if a string field sorts before a value at given mapping path
* `Condition.stringLessThanEquals` - matches if a string field sorts equal to or before a given value
* `Condition.stringLessThanEqualsJsonPath` - matches if a string field sorts equal to or before a given mapping
* `Condition.stringGreaterThan` - matches if a string field sorts after a given value
* `Condition.stringGreaterThanJsonPath` - matches if a string field sorts after a value at a given mapping path
* `Condition.stringGreaterThanEqualsJsonPath` - matches if a string field sorts after or equal to value at a given mapping path
* `Condition.stringGreaterThanEquals` - matches if a string field sorts after or equal to a given value
* `Condition.numberEquals` - matches if a numeric field has the given value
* `Condition.numberEqualsJsonPath` - matches if a numeric field has the value in a given mapping path
* `Condition.numberLessThan` - matches if a numeric field is less than the given value
* `Condition.numberLessThanJsonPath` - matches if a numeric field is less than the value at the given mapping path
* `Condition.numberLessThanEquals` - matches if a numeric field is less than or equal to the given value
* `Condition.numberLessThanEqualsJsonPath` - matches if a numeric field is less than or equal to the numeric value at given mapping path
* `Condition.numberGreaterThan` - matches if a numeric field is greater than the given value
* `Condition.numberGreaterThanJsonPath` - matches if a numeric field is greater than the value at a given mapping path
* `Condition.numberGreaterThanEquals` - matches if a numeric field is greater than or equal to the given value
* `Condition.numberGreaterThanEqualsJsonPath` - matches if a numeric field is greater than or equal to the value at a given mapping path
* `Condition.timestampEquals` - matches if a timestamp field is the same time as the given timestamp
* `Condition.timestampEqualsJsonPath` - matches if a timestamp field is the same time as the timestamp at a given mapping path
* `Condition.timestampLessThan` - matches if a timestamp field is before the given timestamp
* `Condition.timestampLessThanJsonPath` - matches if a timestamp field is before the timestamp at a given mapping path
* `Condition.timestampLessThanEquals` - matches if a timestamp field is before or equal to the given timestamp
* `Condition.timestampLessThanEqualsJsonPath` - matches if a timestamp field is before or equal to the timestamp at a given mapping path
* `Condition.timestampGreaterThan` - matches if a timestamp field is after the timestamp at a given mapping path
* `Condition.timestampGreaterThanJsonPath` - matches if a timestamp field is after the timestamp at a given mapping path
* `Condition.timestampGreaterThanEquals` - matches if a timestamp field is after or equal to the given timestamp
* `Condition.timestampGreaterThanEqualsJsonPath` - matches if a timestamp field is after or equal to the timestamp at a given mapping path
* `Condition.stringMatches` - matches if a field matches a string pattern that can contain a wild card (*) e.g: log-*.txt or *LATEST*. No other characters other than "*" have any special meaning - * can be escaped: \\*

### Parallel

A `Parallel` state executes one or more subworkflows in parallel. It can also
be used to catch and recover from errors in subworkflows.

```python
parallel = sfn.Parallel(self, "Do the work in parallel")

# Add branches to be executed in parallel
ship_item = sfn.Pass(self, "ShipItem")
send_invoice = sfn.Pass(self, "SendInvoice")
restock = sfn.Pass(self, "Restock")
parallel.branch(ship_item)
parallel.branch(send_invoice)
parallel.branch(restock)

# Retry the whole workflow if something goes wrong with exponential backoff
parallel.add_retry(
    max_attempts=1,
    max_delay=Duration.seconds(5),
    jitter_strategy=sfn.JitterType.FULL
)

# How to recover from errors
send_failure_notification = sfn.Pass(self, "SendFailureNotification")
parallel.add_catch(send_failure_notification)

# What to do in case everything succeeded
close_order = sfn.Pass(self, "CloseOrder")
parallel.next(close_order)
```

### Succeed

Reaching a `Succeed` state terminates the state machine execution with a
successful status.

```python
success = sfn.Succeed(self, "We did it!")
```

### Fail

Reaching a `Fail` state terminates the state machine execution with a
failure status. The fail state should report the reason for the failure.
Failures can be caught by encompassing `Parallel` states.

```python
fail = sfn.Fail(self, "Fail",
    error="WorkflowFailure",
    cause="Something went wrong"
)
```

The `Fail` state also supports returning dynamic values as the error and cause that are selected from the input with a path.

```python
fail = sfn.Fail(self, "Fail",
    error_path=sfn.JsonPath.string_at("$.someError"),
    cause_path=sfn.JsonPath.string_at("$.someCause")
)
```

You can also use an intrinsic function that returns a string to specify CausePath and ErrorPath.
The available functions include States.Format, States.JsonToString, States.ArrayGetItem, States.Base64Encode, States.Base64Decode, States.Hash, and States.UUID.

```python
fail = sfn.Fail(self, "Fail",
    error_path=sfn.JsonPath.format("error: {}.", sfn.JsonPath.string_at("$.someError")),
    cause_path="States.Format('cause: {}.', $.someCause)"
)
```

### Map

A `Map` state can be used to run a set of steps for each element of an input array.
A `Map` state will execute the same steps for multiple entries of an array in the state input.

While the `Parallel` state executes multiple branches of steps using the same input, a `Map` state will
execute the same steps for multiple entries of an array in the state input.

```python
map = sfn.Map(self, "Map State",
    max_concurrency=1,
    items_path=sfn.JsonPath.string_at("$.inputForMap"),
    item_selector={
        "item": sfn.JsonPath.string_at("$.Map.Item.Value")
    },
    result_path="$.mapOutput"
)

# The Map iterator can contain a IChainable, which can be an individual or multiple steps chained together.
# Below example is with a Choice and Pass step
choice = sfn.Choice(self, "Choice")
condition1 = sfn.Condition.string_equals("$.item.status", "SUCCESS")
step1 = sfn.Pass(self, "Step1")
step2 = sfn.Pass(self, "Step2")
finish = sfn.Pass(self, "Finish")

definition = choice.when(condition1, step1).otherwise(step2).afterwards().next(finish)

map.item_processor(definition)
```

To define a distributed `Map` state set `itemProcessors` mode to `ProcessorMode.DISTRIBUTED`.
An `executionType` must be specified for the distributed `Map` workflow.

```python
map = sfn.Map(self, "Map State",
    max_concurrency=1,
    items_path=sfn.JsonPath.string_at("$.inputForMap"),
    item_selector={
        "item": sfn.JsonPath.string_at("$.Map.Item.Value")
    },
    result_path="$.mapOutput"
)

map.item_processor(sfn.Pass(self, "Pass State"),
    mode=sfn.ProcessorMode.DISTRIBUTED,
    execution_type=sfn.ProcessorType.STANDARD
)
```

> Visit [Using Map state in Distributed mode to orchestrate large-scale parallel workloads](https://docs.aws.amazon.com/step-functions/latest/dg/use-dist-map-orchestrate-large-scale-parallel-workloads.html) for more details.

### Distributed Map

Step Functions provides a high-concurrency mode for the Map state known as Distributed mode. In this mode, the Map state can accept input from large-scale Amazon S3 data sources. For example, your input can be a JSON or CSV file stored in an Amazon S3 bucket, or a JSON array passed from a previous step in the workflow. A Map state set to Distributed is known as a Distributed Map state. In this mode, the Map state runs each iteration as a child workflow execution, which enables high concurrency of up to 10,000 parallel child workflow executions. Each child workflow execution has its own, separate execution history from that of the parent workflow.

Use the Map state in Distributed mode when you need to orchestrate large-scale parallel workloads that meet any combination of the following conditions:

* The size of your dataset exceeds 256 KB.
* The workflow's execution event history exceeds 25,000 entries.
* You need a concurrency of more than 40 parallel iterations.

A `DistributedMap` state can be used to run a set of steps for each element of an input array with high concurrency.
A `DistributedMap` state will execute the same steps for multiple entries of an array in the state input or from S3 objects.

```python
distributed_map = sfn.DistributedMap(self, "Distributed Map State",
    max_concurrency=1,
    items_path=sfn.JsonPath.string_at("$.inputForMap")
)
distributed_map.item_processor(sfn.Pass(self, "Pass State"))
```

Map states in Distributed mode support multiple sources for an array to iterate:

* JSON array from the state input payload
* objects in an S3 bucket and optional prefix
* JSON array in a JSON file stored in S3
* CSV file stored in S3
* S3 inventory manifest stored in S3

There are multiple classes that implement `IItemReader` that can be used to configure the iterator source.  These can be provided via the optional `itemReader` property.  The default behavior if `itemReader` is omitted is to use the input payload.

Map states in Distributed mode also support writing results of the iterator to an S3 bucket and optional prefix.  Use a `ResultWriter` object provided via the optional `resultWriter` property to configure which S3 location iterator results will be written. The default behavior id `resultWriter` is omitted is to use the state output payload. However, if the iterator results are larger than the 256 kb limit for Step Functions payloads then the State Machine will fail.

```python
import aws_cdk.aws_s3 as s3


# create a bucket
bucket = s3.Bucket(self, "Bucket")

distributed_map = sfn.DistributedMap(self, "Distributed Map State",
    item_reader=sfn.S3JsonItemReader(
        bucket=bucket,
        key="my-key.json"
    ),
    result_writer=sfn.ResultWriter(
        bucket=bucket,
        prefix="my-prefix"
    )
)
distributed_map.item_processor(sfn.Pass(self, "Pass State"))
```

### Custom State

It's possible that the high-level constructs for the states or `stepfunctions-tasks` do not have
the states or service integrations you are looking for. The primary reasons for this lack of
functionality are:

* A [service integration](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-service-integrations.html) is available through Amazon States Language, but not available as construct
  classes in the CDK.
* The state or state properties are available through Step Functions, but are not configurable
  through constructs

If a feature is not available, a `CustomState` can be used to supply any Amazon States Language
JSON-based object as the state definition.

[Code Snippets](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-code-snippet.html#tutorial-code-snippet-1) are available and can be plugged in as the state definition.

Custom states can be chained together with any of the other states to create your state machine
definition. You will also need to provide any permissions that are required to the `role` that
the State Machine uses.

The Retry and Catch fields are available for error handling.
You can configure the Retry field by defining it in the JSON object or by adding it using the `addRetry` method.
However, the Catch field cannot be configured by defining it in the JSON object, so it must be added using the `addCatch` method.

The following example uses the `DynamoDB` service integration to insert data into a DynamoDB table.

```python
import aws_cdk.aws_dynamodb as dynamodb


# create a table
table = dynamodb.Table(self, "montable",
    partition_key=dynamodb.Attribute(
        name="id",
        type=dynamodb.AttributeType.STRING
    )
)

final_status = sfn.Pass(self, "final step")

# States language JSON to put an item into DynamoDB
# snippet generated from https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-code-snippet.html#tutorial-code-snippet-1
state_json = {
    "Type": "Task",
    "Resource": "arn:aws:states:::dynamodb:putItem",
    "Parameters": {
        "TableName": table.table_name,
        "Item": {
            "id": {
                "S": "MyEntry"
            }
        }
    },
    "ResultPath": null
}

# custom state which represents a task to insert data into DynamoDB
custom = sfn.CustomState(self, "my custom task",
    state_json=state_json
)

# catch errors with addCatch
error_handler = sfn.Pass(self, "handle failure")
custom.add_catch(error_handler)

# retry the task if something goes wrong
custom.add_retry(
    errors=[sfn.Errors.ALL],
    interval=Duration.seconds(10),
    max_attempts=5
)

chain = sfn.Chain.start(custom).next(final_status)

sm = sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(chain),
    timeout=Duration.seconds(30),
    comment="a super cool state machine"
)

# don't forget permissions. You need to assign them
table.grant_write_data(sm)
```

## Task Chaining

To make defining work flows as convenient (and readable in a top-to-bottom way)
as writing regular programs, it is possible to chain most methods invocations.
In particular, the `.next()` method can be repeated. The result of a series of
`.next()` calls is called a **Chain**, and can be used when defining the jump
targets of `Choice.on` or `Parallel.branch`:

```python
step1 = sfn.Pass(self, "Step1")
step2 = sfn.Pass(self, "Step2")
step3 = sfn.Pass(self, "Step3")
step4 = sfn.Pass(self, "Step4")
step5 = sfn.Pass(self, "Step5")
step6 = sfn.Pass(self, "Step6")
step7 = sfn.Pass(self, "Step7")
step8 = sfn.Pass(self, "Step8")
step9 = sfn.Pass(self, "Step9")
step10 = sfn.Pass(self, "Step10")
choice = sfn.Choice(self, "Choice")
condition1 = sfn.Condition.string_equals("$.status", "SUCCESS")
parallel = sfn.Parallel(self, "Parallel")
finish = sfn.Pass(self, "Finish")

definition = step1.next(step2).next(choice.when(condition1, step3.next(step4).next(step5)).otherwise(step6).afterwards()).next(parallel.branch(step7.next(step8)).branch(step9.next(step10))).next(finish)

sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition)
)
```

If you don't like the visual look of starting a chain directly off the first
step, you can use `Chain.start`:

```python
step1 = sfn.Pass(self, "Step1")
step2 = sfn.Pass(self, "Step2")
step3 = sfn.Pass(self, "Step3")

definition = sfn.Chain.start(step1).next(step2).next(step3)
```

## Task Credentials

Tasks are executed using the State Machine's execution role. In some cases, e.g. cross-account access, an IAM role can be assumed by the State Machine's execution role to provide access to the resource.
This can be achieved by providing the optional `credentials` property which allows using a fixed role or a json expression to resolve the role at runtime from the task's inputs.

```python
import aws_cdk.aws_lambda as lambda_

# submit_lambda: lambda.Function
# iam_role: iam.Role


# use a fixed role for all task invocations
role = sfn.TaskRole.from_role(iam_role)
# or use a json expression to resolve the role at runtime based on task inputs
# const role = sfn.TaskRole.fromRoleArnJsonPath('$.RoleArn');

submit_job = tasks.LambdaInvoke(self, "Submit Job",
    lambda_function=submit_lambda,
    output_path="$.Payload",
    # use credentials
    credentials=sfn.Credentials(role=role)
)
```

See [the AWS documentation](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-access-cross-acct-resources.html)
to learn more about AWS Step Functions support for accessing resources in other AWS accounts.

## Service Integration Patterns

AWS Step functions integrate directly with other services, either through an optimised integration pattern, or through the AWS SDK.
Therefore, it is possible to change the `integrationPattern` of services, to enable additional functionality of the said AWS Service:

```python
import aws_cdk.aws_glue_alpha as glue

# submit_glue: glue.Job


submit_job = tasks.GlueStartJobRun(self, "Submit Job",
    glue_job_name=submit_glue.job_name,
    integration_pattern=sfn.IntegrationPattern.RUN_JOB
)
```

## State Machine Fragments

It is possible to define reusable (or abstracted) mini-state machines by
defining a construct that implements `IChainable`, which requires you to define
two fields:

* `startState: State`, representing the entry point into this state machine.
* `endStates: INextable[]`, representing the (one or more) states that outgoing
  transitions will be added to if you chain onto the fragment.

Since states will be named after their construct IDs, you may need to prefix the
IDs of states if you plan to instantiate the same state machine fragment
multiples times (otherwise all states in every instantiation would have the same
name).

The class `StateMachineFragment` contains some helper functions (like
`prefixStates()`) to make it easier for you to do this. If you define your state
machine as a subclass of this, it will be convenient to use:

```python
from aws_cdk import Stack
from constructs import Construct
import aws_cdk.aws_stepfunctions as sfn

class MyJob(sfn.StateMachineFragment):

    def __init__(self, parent, id, *, jobFlavor):
        super().__init__(parent, id)

        choice = sfn.Choice(self, "Choice").when(sfn.Condition.string_equals("$.branch", "left"), sfn.Pass(self, "Left Branch")).when(sfn.Condition.string_equals("$.branch", "right"), sfn.Pass(self, "Right Branch"))

        # ...

        self.start_state = choice
        self.end_states = choice.afterwards().end_states

class MyStack(Stack):
    def __init__(self, scope, id):
        super().__init__(scope, id)
        # Do 3 different variants of MyJob in parallel
        parallel = sfn.Parallel(self, "All jobs").branch(MyJob(self, "Quick", job_flavor="quick").prefix_states()).branch(MyJob(self, "Medium", job_flavor="medium").prefix_states()).branch(MyJob(self, "Slow", job_flavor="slow").prefix_states())

        sfn.StateMachine(self, "MyStateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(parallel)
        )
```

A few utility functions are available to parse state machine fragments.

* `State.findReachableStates`: Retrieve the list of states reachable from a given state.
* `State.findReachableEndStates`: Retrieve the list of end or terminal states reachable from a given state.

## Activity

**Activities** represent work that is done on some non-Lambda worker pool. The
Step Functions workflow will submit work to this Activity, and a worker pool
that you run yourself, probably on EC2, will pull jobs from the Activity and
submit the results of individual jobs back.

You need the ARN to do so, so if you use Activities be sure to pass the Activity
ARN into your worker pool:

```python
activity = sfn.Activity(self, "Activity")

# Read this CloudFormation Output from your application and use it to poll for work on
# the activity.
CfnOutput(self, "ActivityArn", value=activity.activity_arn)
```

### Activity-Level Permissions

Granting IAM permissions to an activity can be achieved by calling the `grant(principal, actions)` API:

```python
activity = sfn.Activity(self, "Activity")

role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)

activity.grant(role, "states:SendTaskSuccess")
```

This will grant the IAM principal the specified actions onto the activity.

## Metrics

`Task` object expose various metrics on the execution of that particular task. For example,
to create an alarm on a particular task failing:

```python
# task: sfn.Task

cloudwatch.Alarm(self, "TaskAlarm",
    metric=task.metric_failed(),
    threshold=1,
    evaluation_periods=1
)
```

There are also metrics on the complete state machine:

```python
# state_machine: sfn.StateMachine

cloudwatch.Alarm(self, "StateMachineAlarm",
    metric=state_machine.metric_failed(),
    threshold=1,
    evaluation_periods=1
)
```

And there are metrics on the capacity of all state machines in your account:

```python
cloudwatch.Alarm(self, "ThrottledAlarm",
    metric=sfn.StateTransitionMetric.metric_throttled_events(),
    threshold=10,
    evaluation_periods=2
)
```

## Error names

Step Functions identifies errors in the Amazon States Language using case-sensitive strings, known as error names.
The Amazon States Language defines a set of built-in strings that name well-known errors, all beginning with the `States.` prefix.

* `States.ALL` - A wildcard that matches any known error name.
* `States.Runtime` - An execution failed due to some exception that could not be processed. Often these are caused by errors at runtime, such as attempting to apply InputPath or OutputPath on a null JSON payload. A `States.Runtime` error is not retriable, and will always cause the execution to fail. A retry or catch on `States.ALL` will NOT catch States.Runtime errors.
* `States.DataLimitExceeded` - A States.DataLimitExceeded exception will be thrown for the following:

  * When the output of a connector is larger than payload size quota.
  * When the output of a state is larger than payload size quota.
  * When, after Parameters processing, the input of a state is larger than the payload size quota.
  * See [the AWS documentation](https://docs.aws.amazon.com/step-functions/latest/dg/limits-overview.html) to learn more about AWS Step Functions Quotas.
* `States.HeartbeatTimeout` - A Task state failed to send a heartbeat for a period longer than the HeartbeatSeconds value.
* `States.Timeout` - A Task state either ran longer than the TimeoutSeconds value, or failed to send a heartbeat for a period longer than the HeartbeatSeconds value.
* `States.TaskFailed`- A Task state failed during the execution. When used in a retry or catch, `States.TaskFailed` acts as a wildcard that matches any known error name except for `States.Timeout`.

## Logging

Enable logging to CloudWatch by passing a logging configuration with a
destination LogGroup:

```python
import aws_cdk.aws_logs as logs


log_group = logs.LogGroup(self, "MyLogGroup")

definition = sfn.Chain.start(sfn.Pass(self, "Pass"))

sfn.StateMachine(self, "MyStateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition),
    logs=sfn.LogOptions(
        destination=log_group,
        level=sfn.LogLevel.ALL
    )
)
```

## X-Ray tracing

Enable X-Ray tracing for StateMachine:

```python
definition = sfn.Chain.start(sfn.Pass(self, "Pass"))

sfn.StateMachine(self, "MyStateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition),
    tracing_enabled=True
)
```

See [the AWS documentation](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-xray-tracing.html)
to learn more about AWS Step Functions's X-Ray support.

## State Machine Permission Grants

IAM roles, users, or groups which need to be able to work with a State Machine should be granted IAM permissions.

Any object that implements the `IGrantable` interface (has an associated principal) can be granted permissions by calling:

* `stateMachine.grantStartExecution(principal)` - grants the principal the ability to execute the state machine
* `stateMachine.grantRead(principal)` - grants the principal read access
* `stateMachine.grantTaskResponse(principal)` - grants the principal the ability to send task tokens to the state machine
* `stateMachine.grantExecution(principal, actions)` - grants the principal execution-level permissions for the IAM actions specified
* `stateMachine.grant(principal, actions)` - grants the principal state-machine-level permissions for the IAM actions specified

### Start Execution Permission

Grant permission to start an execution of a state machine by calling the `grantStartExecution()` API.

```python
# definition: sfn.IChainable
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)
state_machine = sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition)
)

# Give role permission to start execution of state machine
state_machine.grant_start_execution(role)
```

The following permission is provided to a service principal by the `grantStartExecution()` API:

* `states:StartExecution` - to state machine

### Read Permissions

Grant `read` access to a state machine by calling the `grantRead()` API.

```python
# definition: sfn.IChainable
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)
state_machine = sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition)
)

# Give role read access to state machine
state_machine.grant_read(role)
```

The following read permissions are provided to a service principal by the `grantRead()` API:

* `states:ListExecutions` - to state machine
* `states:ListStateMachines` - to state machine
* `states:DescribeExecution` - to executions
* `states:DescribeStateMachineForExecution` - to executions
* `states:GetExecutionHistory` - to executions
* `states:ListActivities` - to `*`
* `states:DescribeStateMachine` - to `*`
* `states:DescribeActivity` - to `*`

### Task Response Permissions

Grant permission to allow task responses to a state machine by calling the `grantTaskResponse()` API:

```python
# definition: sfn.IChainable
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)
state_machine = sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition)
)

# Give role task response permissions to the state machine
state_machine.grant_task_response(role)
```

The following read permissions are provided to a service principal by the `grantRead()` API:

* `states:SendTaskSuccess` - to state machine
* `states:SendTaskFailure` - to state machine
* `states:SendTaskHeartbeat` - to state machine

### Execution-level Permissions

Grant execution-level permissions to a state machine by calling the `grantExecution()` API:

```python
# definition: sfn.IChainable
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)
state_machine = sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition)
)

# Give role permission to get execution history of ALL executions for the state machine
state_machine.grant_execution(role, "states:GetExecutionHistory")
```

### Custom Permissions

You can add any set of permissions to a state machine by calling the `grant()` API.

```python
# definition: sfn.IChainable
user = iam.User(self, "MyUser")
state_machine = sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(definition)
)

# give user permission to send task success to the state machine
state_machine.grant(user, "states:SendTaskSuccess")
```

## Import

Any Step Functions state machine that has been created outside the stack can be imported
into your CDK stack.

State machines can be imported by their ARN via the `StateMachine.fromStateMachineArn()` API.
In addition, the StateMachine can be imported via the `StateMachine.fromStateMachineName()` method, as long as they are in the same account/region as the current construct.

```python
app = App()
stack = Stack(app, "MyStack")
sfn.StateMachine.from_state_machine_arn(self, "ViaArnImportedStateMachine", "arn:aws:states:us-east-1:123456789012:stateMachine:StateMachine2E01A3A5-N5TJppzoevKQ")

sfn.StateMachine.from_state_machine_name(self, "ViaResourceNameImportedStateMachine", "StateMachine2E01A3A5-N5TJppzoevKQ")
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
    AssetHashType as _AssetHashType_05b67f2d,
    BundlingOptions as _BundlingOptions_588cc936,
    CfnResource as _CfnResource_9df397a6,
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    IgnoreMode as _IgnoreMode_655a98e8,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    SymlinkFollowMode as _SymlinkFollowMode_047ec1f6,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_logs import ILogGroup as _ILogGroup_3c4fa718
from ..aws_s3 import IBucket as _IBucket_42e086fd
from ..aws_s3_assets import AssetOptions as _AssetOptions_2aa69621


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.ActivityProps",
    jsii_struct_bases=[],
    name_mapping={"activity_name": "activityName"},
)
class ActivityProps:
    def __init__(self, *, activity_name: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a new Step Functions Activity.

        :param activity_name: The name for this activity. Default: - If not supplied, a name is generated

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            activity_props = stepfunctions.ActivityProps(
                activity_name="activityName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b22b644ed0224ed8911beae00f4c015272b0b6846f925702d315e05b17bfc26e)
            check_type(argname="argument activity_name", value=activity_name, expected_type=type_hints["activity_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if activity_name is not None:
            self._values["activity_name"] = activity_name

    @builtins.property
    def activity_name(self) -> typing.Optional[builtins.str]:
        '''The name for this activity.

        :default: - If not supplied, a name is generated
        '''
        result = self._values.get("activity_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActivityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.AfterwardsOptions",
    jsii_struct_bases=[],
    name_mapping={
        "include_error_handlers": "includeErrorHandlers",
        "include_otherwise": "includeOtherwise",
    },
)
class AfterwardsOptions:
    def __init__(
        self,
        *,
        include_error_handlers: typing.Optional[builtins.bool] = None,
        include_otherwise: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for selecting the choice paths.

        :param include_error_handlers: Whether to include error handling states. If this is true, all states which are error handlers (added through 'onError') and states reachable via error handlers will be included as well. Default: false
        :param include_otherwise: Whether to include the default/otherwise transition for the current Choice state. If this is true and the current Choice does not have a default outgoing transition, one will be added included when .next() is called on the chain. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            afterwards_options = stepfunctions.AfterwardsOptions(
                include_error_handlers=False,
                include_otherwise=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4085645c0aa11ea16f29fe0328307d94fbc700a6b908a2c9d2b3209bc2f7af6)
            check_type(argname="argument include_error_handlers", value=include_error_handlers, expected_type=type_hints["include_error_handlers"])
            check_type(argname="argument include_otherwise", value=include_otherwise, expected_type=type_hints["include_otherwise"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if include_error_handlers is not None:
            self._values["include_error_handlers"] = include_error_handlers
        if include_otherwise is not None:
            self._values["include_otherwise"] = include_otherwise

    @builtins.property
    def include_error_handlers(self) -> typing.Optional[builtins.bool]:
        '''Whether to include error handling states.

        If this is true, all states which are error handlers (added through 'onError')
        and states reachable via error handlers will be included as well.

        :default: false
        '''
        result = self._values.get("include_error_handlers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def include_otherwise(self) -> typing.Optional[builtins.bool]:
        '''Whether to include the default/otherwise transition for the current Choice state.

        If this is true and the current Choice does not have a default outgoing
        transition, one will be added included when .next() is called on the chain.

        :default: false
        '''
        result = self._values.get("include_otherwise")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AfterwardsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.CatchProps",
    jsii_struct_bases=[],
    name_mapping={"errors": "errors", "result_path": "resultPath"},
)
class CatchProps:
    def __init__(
        self,
        *,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        result_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Error handler details.

        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value JsonPath.DISCARD, which will cause the error data to be discarded. Default: $

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            catch_props = stepfunctions.CatchProps(
                errors=["errors"],
                result_path="resultPath"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4b30052ea4266ae7ac11a0c2eaab9f31db04561d9040ab8175bd34b849414a0)
            check_type(argname="argument errors", value=errors, expected_type=type_hints["errors"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if errors is not None:
            self._values["errors"] = errors
        if result_path is not None:
            self._values["result_path"] = result_path

    @builtins.property
    def errors(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Errors to recover from by going to the given state.

        A list of error strings to retry, which can be either predefined errors
        (for example Errors.NoChoiceMatched) or a self-defined error.

        :default: All errors
        '''
        result = self._values.get("errors")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the error data.

        May also be the special value JsonPath.DISCARD, which will cause the error
        data to be discarded.

        :default: $
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CatchProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnActivity(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.CfnActivity",
):
    '''An activity is a task that you write in any programming language and host on any machine that has access to AWS Step Functions .

    Activities must poll Step Functions using the ``GetActivityTask`` API action and respond using ``SendTask*`` API actions. This function lets Step Functions know the existence of your activity and returns an identifier for use in a state machine and when polling from the activity.

    For information about creating an activity, see `Creating an Activity State Machine <https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-creating-activity-state-machine.html>`_ in the *AWS Step Functions Developer Guide* and `CreateActivity <https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateActivity.html>`_ in the *AWS Step Functions API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html
    :cloudformationResource: AWS::StepFunctions::Activity
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        cfn_activity = stepfunctions.CfnActivity(self, "MyCfnActivity",
            name="name",
        
            # the properties below are optional
            tags=[stepfunctions.CfnActivity.TagsEntryProperty(
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
        tags: typing.Optional[typing.Sequence[typing.Union["CfnActivity.TagsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the activity. A name must *not* contain: - white space - brackets ``< > { } [ ]`` - wildcard characters ``? *`` - special characters ``" # % \\ ^ | ~ `` $ & , ; : /` - control characters ( ``U+0000-001F`` , ``U+007F-009F`` ) To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.
        :param tags: The list of tags to add to a resource. Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9cac9ccbc74858ea58acc13770fdeee7b204562b53992182f500d45a5f816a2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnActivityProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3118727103487fc9862cb103a2c8a7c466265683e88e012835325059d1d7e0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__370d3cef66c2bfc06cc862207a47ec2707fa300961f0129ab6f3c2edf4a02cb2)
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
        '''Returns the ARN of the resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the activity. For example:.

        ``{ "Fn::GetAtt": ["MyActivity", "Name"] }``

        Returns a value similar to the following:

        ``myActivity``

        For more information about using ``Fn::GetAtt`` , see `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
        '''The name of the activity.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8395bdf4e76b8a41673d28377cd1001ff25935aca9798745ebef40fe06572120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["CfnActivity.TagsEntryProperty"]]:
        '''The list of tags to add to a resource.'''
        return typing.cast(typing.Optional[typing.List["CfnActivity.TagsEntryProperty"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["CfnActivity.TagsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c963f19dfa2bfb12cf0d22b5bf287aec4f47a000b16928a2dd660ae295dcde65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnActivity.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The ``TagsEntry`` property specifies *tags* to identify an activity.

            :param key: The ``key`` for a key-value pair in a tag entry.
            :param value: The ``value`` for a key-value pair in a tag entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                tags_entry_property = stepfunctions.CfnActivity.TagsEntryProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5e620d5be50cdb836aed85b2b5bbc76573db0139cccc1fa49f54e926f1e4cbc7)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The ``key`` for a key-value pair in a tag entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The ``value`` for a key-value pair in a tag entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-activity-tagsentry.html#cfn-stepfunctions-activity-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.CfnActivityProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnActivityProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnActivity.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnActivity``.

        :param name: The name of the activity. A name must *not* contain: - white space - brackets ``< > { } [ ]`` - wildcard characters ``? *`` - special characters ``" # % \\ ^ | ~ `` $ & , ; : /` - control characters ( ``U+0000-001F`` , ``U+007F-009F`` ) To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.
        :param tags: The list of tags to add to a resource. Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            cfn_activity_props = stepfunctions.CfnActivityProps(
                name="name",
            
                # the properties below are optional
                tags=[stepfunctions.CfnActivity.TagsEntryProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84792b5435bbf43a453a6bf0f4d6e6d61a7c86759e3f95b4d4af4d4e56f641c4)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the activity.

        A name must *not* contain:

        - white space
        - brackets ``< > { } [ ]``
        - wildcard characters ``? *``
        - special characters ``" # % \\ ^ | ~ `` $ & , ; : /`
        - control characters ( ``U+0000-001F`` , ``U+007F-009F`` )

        To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnActivity.TagsEntryProperty]]:
        '''The list of tags to add to a resource.

        Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html#cfn-stepfunctions-activity-tags
        :: ` .
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnActivity.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnActivityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStateMachine(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachine",
):
    '''Provisions a state machine.

    A state machine consists of a collection of states that can do work ( ``Task`` states), determine to which states to transition next ( ``Choice`` states), stop an execution with an error ( ``Fail`` states), and so on. State machines are specified using a JSON-based, structured language.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html
    :cloudformationResource: AWS::StepFunctions::StateMachine
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # definition: Any
        
        cfn_state_machine = stepfunctions.CfnStateMachine(self, "MyCfnStateMachine",
            role_arn="roleArn",
        
            # the properties below are optional
            definition=definition,
            definition_s3_location=stepfunctions.CfnStateMachine.S3LocationProperty(
                bucket="bucket",
                key="key",
        
                # the properties below are optional
                version="version"
            ),
            definition_string="definitionString",
            definition_substitutions={
                "definition_substitutions_key": "definitionSubstitutions"
            },
            logging_configuration=stepfunctions.CfnStateMachine.LoggingConfigurationProperty(
                destinations=[stepfunctions.CfnStateMachine.LogDestinationProperty(
                    cloud_watch_logs_log_group=stepfunctions.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                        log_group_arn="logGroupArn"
                    )
                )],
                include_execution_data=False,
                level="level"
            ),
            state_machine_name="stateMachineName",
            state_machine_type="stateMachineType",
            tags=[stepfunctions.CfnStateMachine.TagsEntryProperty(
                key="key",
                value="value"
            )],
            tracing_configuration=stepfunctions.CfnStateMachine.TracingConfigurationProperty(
                enabled=False
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role_arn: builtins.str,
        definition: typing.Any = None,
        definition_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_string: typing.Optional[builtins.str] = None,
        definition_substitutions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        state_machine_name: typing.Optional[builtins.str] = None,
        state_machine_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnStateMachine.TagsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tracing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.TracingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
        :param definition: The Amazon States Language definition of the state machine. The state machine definition must be in JSON or YAML, and the format of the object must match the format of your CloudFormation template file. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`_ .
        :param definition_s3_location: The name of the S3 bucket where the state machine definition is stored. The state machine definition must be a JSON or YAML file.
        :param definition_string: The Amazon States Language definition of the state machine. The state machine definition must be in JSON. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`_ .
        :param definition_substitutions: A map (string to string) that specifies the mappings for placeholder variables in the state machine definition. This enables the customer to inject values obtained at runtime, for example from intrinsic functions, in the state machine definition. Variables can be template parameter names, resource logical IDs, resource attributes, or a variable in a key-value map. Substitutions must follow the syntax: ``${key_name}`` or ``${variable_1,variable_2,...}`` .
        :param logging_configuration: Defines what execution history events are logged and where they are logged. .. epigraph:: By default, the ``level`` is set to ``OFF`` . For more information see `Log Levels <https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html>`_ in the AWS Step Functions User Guide.
        :param state_machine_name: The name of the state machine. A name must *not* contain: - white space - brackets ``< > { } [ ]`` - wildcard characters ``? *`` - special characters ``" # % \\ ^ | ~ `` $ & , ; : /` - control characters ( ``U+0000-001F`` , ``U+007F-009F`` ) .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param state_machine_type: Determines whether a ``STANDARD`` or ``EXPRESS`` state machine is created. The default is ``STANDARD`` . You cannot update the ``type`` of a state machine once it has been created. For more information on ``STANDARD`` and ``EXPRESS`` workflows, see `Standard Versus Express Workflows <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html>`_ in the AWS Step Functions Developer Guide.
        :param tags: The list of tags to add to a resource. Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + -
        :param tracing_configuration: Selects whether or not the state machine's AWS X-Ray tracing is enabled.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b19fff9309f98c9776cf416019a5217333b4d6f0f81e27e2256a87f931153d0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStateMachineProps(
            role_arn=role_arn,
            definition=definition,
            definition_s3_location=definition_s3_location,
            definition_string=definition_string,
            definition_substitutions=definition_substitutions,
            logging_configuration=logging_configuration,
            state_machine_name=state_machine_name,
            state_machine_type=state_machine_type,
            tags=tags,
            tracing_configuration=tracing_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07dab719dc25dde0e0ebd681e886c29dd992fd69300c5b97592744ca66975549)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d81dc102aa24fdc5c42fa4ed2ff7c70c77beb876a92e54f87c158489800243ef)
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
        '''Returns the ARN of the resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the state machine. For example:.

        ``{ "Fn::GetAtt": ["MyStateMachine", "Name"] }``

        Returns the name of your state machine:

        ``HelloWorld-StateMachine``

        If you did not specify the name it will be similar to the following:

        ``MyStateMachine-1234abcdefgh``

        For more information about using ``Fn::GetAtt`` , see `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ .

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrStateMachineRevisionId")
    def attr_state_machine_revision_id(self) -> builtins.str:
        '''Identifier for a state machine revision, which is an immutable, read-only snapshot of a state machine’s definition and configuration.

        :cloudformationAttribute: StateMachineRevisionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateMachineRevisionId"))

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
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role to use for this state machine.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3004fba1e9c0225151457c38edd4c7effc7d187628b86416f39849b982f49a1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Any:
        '''The Amazon States Language definition of the state machine.'''
        return typing.cast(typing.Any, jsii.get(self, "definition"))

    @definition.setter
    def definition(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f82f2a7642ea2ac7bdf170a2733a41594fd40eb07f7e540d495f22c6fa06b147)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="definitionS3Location")
    def definition_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.S3LocationProperty"]]:
        '''The name of the S3 bucket where the state machine definition is stored.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.S3LocationProperty"]], jsii.get(self, "definitionS3Location"))

    @definition_s3_location.setter
    def definition_s3_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c6f22451e8abd968219b59f11a227c9451d5cd7cb1ff91b3bd91c4ab25bd6da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="definitionString")
    def definition_string(self) -> typing.Optional[builtins.str]:
        '''The Amazon States Language definition of the state machine.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "definitionString"))

    @definition_string.setter
    def definition_string(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c930aec966c75b589ce56dba8aee211d61eeb6c41d99c5c84ab2df4b703b35d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionString", value)

    @builtins.property
    @jsii.member(jsii_name="definitionSubstitutions")
    def definition_substitutions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''A map (string to string) that specifies the mappings for placeholder variables in the state machine definition.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "definitionSubstitutions"))

    @definition_substitutions.setter
    def definition_substitutions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e05fa36d2c9116cb2c90b1560cd6e7bc08699fa552a7e75ce5775a927ad53415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionSubstitutions", value)

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LoggingConfigurationProperty"]]:
        '''Defines what execution history events are logged and where they are logged.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LoggingConfigurationProperty"]], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f4c64119545b342b25a9aba40a7ac8de878e2ca38859e38a10004112309301)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachineName")
    def state_machine_name(self) -> typing.Optional[builtins.str]:
        '''The name of the state machine.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateMachineName"))

    @state_machine_name.setter
    def state_machine_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1c0751a8a3952639ad0b17cb78032a0bad0e3a1e983836e5c861a8129c0c542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachineName", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachineType")
    def state_machine_type(self) -> typing.Optional[builtins.str]:
        '''Determines whether a ``STANDARD`` or ``EXPRESS`` state machine is created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateMachineType"))

    @state_machine_type.setter
    def state_machine_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aef9754ddbe205b0e3cda858acb6182a9a911881b2f81e68f20b454cc9d738e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachineType", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(
        self,
    ) -> typing.Optional[typing.List["CfnStateMachine.TagsEntryProperty"]]:
        '''The list of tags to add to a resource.'''
        return typing.cast(typing.Optional[typing.List["CfnStateMachine.TagsEntryProperty"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["CfnStateMachine.TagsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142d2d5d8871bd122c48cc77fb02230c828841e8672a11480c58d07a743ec8d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="tracingConfiguration")
    def tracing_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.TracingConfigurationProperty"]]:
        '''Selects whether or not the state machine's AWS X-Ray tracing is enabled.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.TracingConfigurationProperty"]], jsii.get(self, "tracingConfiguration"))

    @tracing_configuration.setter
    def tracing_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.TracingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7975c26bdc928c8d9fd66a2493df6fc6818b885815e25f63844e956d275c1d01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tracingConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachine.CloudWatchLogsLogGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class CloudWatchLogsLogGroupProperty:
        def __init__(
            self,
            *,
            log_group_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a CloudWatch log group.

            .. epigraph::

               For more information see `Standard Versus Express Workflows <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html>`_ in the AWS Step Functions Developer Guide.

            :param log_group_arn: The ARN of the the CloudWatch log group to which you want your logs emitted to. The ARN must end with ``:*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                cloud_watch_logs_log_group_property = stepfunctions.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd590e91d2c1399d369226ca3fcbd6666d564980b08611a4b5f952ef3e6b9644)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_arn is not None:
                self._values["log_group_arn"] = log_group_arn

        @builtins.property
        def log_group_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the the CloudWatch log group to which you want your logs emitted to.

            The ARN must end with ``:*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-cloudwatchlogsloggroup.html#cfn-stepfunctions-statemachine-cloudwatchlogsloggroup-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsLogGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachine.LogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_logs_log_group": "cloudWatchLogsLogGroup"},
    )
    class LogDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_log_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.CloudWatchLogsLogGroupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines a destination for ``LoggingConfiguration`` .

            .. epigraph::

               For more information on logging with ``EXPRESS`` workflows, see `Logging Express Workflows Using CloudWatch Logs <https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html>`_ .

            :param cloud_watch_logs_log_group: An object describing a CloudWatch log group. For more information, see `AWS::Logs::LogGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html>`_ in the AWS CloudFormation User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                log_destination_property = stepfunctions.CfnStateMachine.LogDestinationProperty(
                    cloud_watch_logs_log_group=stepfunctions.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                        log_group_arn="logGroupArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a5d8a3abcdb82fe13dbd692519b118f763c5de9bf0de6025642f4d45a207ab1)
                check_type(argname="argument cloud_watch_logs_log_group", value=cloud_watch_logs_log_group, expected_type=type_hints["cloud_watch_logs_log_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs_log_group is not None:
                self._values["cloud_watch_logs_log_group"] = cloud_watch_logs_log_group

        @builtins.property
        def cloud_watch_logs_log_group(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.CloudWatchLogsLogGroupProperty"]]:
            '''An object describing a CloudWatch log group.

            For more information, see `AWS::Logs::LogGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html>`_ in the AWS CloudFormation User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-logdestination.html#cfn-stepfunctions-statemachine-logdestination-cloudwatchlogsloggroup
            '''
            result = self._values.get("cloud_watch_logs_log_group")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.CloudWatchLogsLogGroupProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachine.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destinations": "destinations",
            "include_execution_data": "includeExecutionData",
            "level": "level",
        },
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.LogDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            include_execution_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines what execution history events are logged and where they are logged.

            Step Functions provides the log levels — ``OFF`` , ``ALL`` , ``ERROR`` , and ``FATAL`` . No event types log when set to ``OFF`` and all event types do when set to ``ALL`` .
            .. epigraph::

               By default, the ``level`` is set to ``OFF`` . For more information see `Log Levels <https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html>`_ in the AWS Step Functions User Guide.

            :param destinations: An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to ``OFF`` .
            :param include_execution_data: Determines whether execution data is included in your log. When set to ``false`` , data is excluded.
            :param level: Defines which category of execution history events are logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                logging_configuration_property = stepfunctions.CfnStateMachine.LoggingConfigurationProperty(
                    destinations=[stepfunctions.CfnStateMachine.LogDestinationProperty(
                        cloud_watch_logs_log_group=stepfunctions.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                            log_group_arn="logGroupArn"
                        )
                    )],
                    include_execution_data=False,
                    level="level"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24eee9bdacbb65e43216bb9ddfa4cfe3e27e892eb228ca21be7cd0565deb825a)
                check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
                check_type(argname="argument include_execution_data", value=include_execution_data, expected_type=type_hints["include_execution_data"])
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destinations is not None:
                self._values["destinations"] = destinations
            if include_execution_data is not None:
                self._values["include_execution_data"] = include_execution_data
            if level is not None:
                self._values["level"] = level

        @builtins.property
        def destinations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LogDestinationProperty"]]]]:
            '''An array of objects that describes where your execution history events will be logged.

            Limited to size 1. Required, if your log level is not set to ``OFF`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-destinations
            '''
            result = self._values.get("destinations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LogDestinationProperty"]]]], result)

        @builtins.property
        def include_execution_data(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Determines whether execution data is included in your log.

            When set to ``false`` , data is excluded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-includeexecutiondata
            '''
            result = self._values.get("include_execution_data")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def level(self) -> typing.Optional[builtins.str]:
            '''Defines which category of execution history events are logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-loggingconfiguration.html#cfn-stepfunctions-statemachine-loggingconfiguration-level
            '''
            result = self._values.get("level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachine.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key", "version": "version"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the S3 bucket location where a state machine definition is stored.

            The state machine definition must be a JSON or YAML file.

            :param bucket: The name of the S3 bucket where the state machine definition JSON or YAML file is stored.
            :param key: The name of the state machine definition file (Amazon S3 object name).
            :param version: For versioning-enabled buckets, a specific version of the state machine definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                s3_location_property = stepfunctions.CfnStateMachine.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                
                    # the properties below are optional
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24b148e6a91176407ca02fb5dd7411cf96ebdd5cdccdafa24b702f5578115e1d)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the S3 bucket where the state machine definition JSON or YAML file is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the state machine definition file (Amazon S3 object name).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''For versioning-enabled buckets, a specific version of the state machine definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-s3location.html#cfn-stepfunctions-statemachine-s3location-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachine.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The ``TagsEntry`` property specifies *tags* to identify a state machine.

            :param key: The ``key`` for a key-value pair in a tag entry.
            :param value: The ``value`` for a key-value pair in a tag entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                tags_entry_property = stepfunctions.CfnStateMachine.TagsEntryProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cfb83dface8660c95e6064ed3571632ddfd56b66cf9838d2dff4920c79c635e1)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The ``key`` for a key-value pair in a tag entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The ``value`` for a key-value pair in a tag entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tagsentry.html#cfn-stepfunctions-statemachine-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachine.TracingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class TracingConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Selects whether or not the state machine's AWS X-Ray tracing is enabled.

            To configure your state machine to send trace data to X-Ray, set ``Enabled`` to ``true`` .

            :param enabled: When set to ``true`` , X-Ray tracing is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                tracing_configuration_property = stepfunctions.CfnStateMachine.TracingConfigurationProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bbdafebe888490672c9f37361d4a6ddfd497f384ba2c643a0138dcf36eaf947d)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , X-Ray tracing is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachine-tracingconfiguration.html#cfn-stepfunctions-statemachine-tracingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TracingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnStateMachineAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachineAlias",
):
    '''Represents a state machine `alias <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html>`_ . An alias routes traffic to one or two versions of the same state machine.

    You can create up to 100 aliases for each state machine.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html
    :cloudformationResource: AWS::StepFunctions::StateMachineAlias
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        cfn_state_machine_alias = stepfunctions.CfnStateMachineAlias(self, "MyCfnStateMachineAlias",
            deployment_preference=stepfunctions.CfnStateMachineAlias.DeploymentPreferenceProperty(
                state_machine_version_arn="stateMachineVersionArn",
                type="type",
        
                # the properties below are optional
                alarms=["alarms"],
                interval=123,
                percentage=123
            ),
            description="description",
            name="name",
            routing_configuration=[stepfunctions.CfnStateMachineAlias.RoutingConfigurationVersionProperty(
                state_machine_version_arn="stateMachineVersionArn",
                weight=123
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        deployment_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachineAlias.DeploymentPreferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        routing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachineAlias.RoutingConfigurationVersionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param deployment_preference: The settings that enable gradual state machine deployments. These settings include `Alarms <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-alarms>`_ , `Interval <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-interval>`_ , `Percentage <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-percentage>`_ , `StateMachineVersionArn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-statemachineversionarn>`_ , and `Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-type>`_ . CloudFormation automatically shifts traffic from the version an alias currently points to, to a new state machine version that you specify. .. epigraph:: ``RoutingConfiguration`` and ``DeploymentPreference`` are mutually exclusive properties. You must define only one of these properties. Based on the type of deployment you want to perform, you can specify one of the following settings: - ``LINEAR`` - Shifts traffic to the new version in equal increments with an equal number of minutes between each increment. For example, if you specify the increment percent as ``20`` with an interval of ``600`` minutes, this deployment increases traffic by 20 percent every 600 minutes until the new version receives 100 percent of the traffic. This deployment immediately rolls back the new version if any Amazon CloudWatch alarms are triggered. - ``ALL_AT_ONCE`` - Shifts 100 percent of traffic to the new version immediately. CloudFormation monitors the new version and rolls it back automatically to the previous version if any CloudWatch alarms are triggered. - ``CANARY`` - Shifts traffic in two increments. In the first increment, a small percentage of traffic, for example, 10 percent is shifted to the new version. In the second increment, before a specified time interval in seconds gets over, the remaining traffic is shifted to the new version. The shift to the new version for the remaining traffic takes place only if no CloudWatch alarms are triggered during the specified time interval.
        :param description: An optional description of the state machine alias.
        :param name: The name of the state machine alias. If you don't provide a name, it uses an automatically generated name based on the logical ID.
        :param routing_configuration: The routing configuration of an alias. Routing configuration splits `StartExecution <https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html>`_ requests between one or two versions of the same state machine. Use ``RoutingConfiguration`` if you want to explicitly set the alias `weights <https://docs.aws.amazon.com/step-functions/latest/apireference/API_RoutingConfigurationListItem.html#StepFunctions-Type-RoutingConfigurationListItem-weight>`_ . Weight is the percentage of traffic you want to route to a state machine version. .. epigraph:: ``RoutingConfiguration`` and ``DeploymentPreference`` are mutually exclusive properties. You must define only one of these properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85744ef2fdff2d756e7a5ede3f88cb39b6c23cf8c88315a30006ec164aeda913)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStateMachineAliasProps(
            deployment_preference=deployment_preference,
            description=description,
            name=name,
            routing_configuration=routing_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39d3b5bbdb19199dd6c855f5e5c36c80442ad9f5bcfc52471013324e8a03057e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0631e2f126759615f5f8c79f47da93a2503e50646d811e8d62ca6adb72cc9d67)
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
        '''Returns the ARN of the state machine alias.

        For example, ``arn:aws:states:us-east-1:123456789012:stateMachine:myStateMachine:PROD`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="deploymentPreference")
    def deployment_preference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachineAlias.DeploymentPreferenceProperty"]]:
        '''The settings that enable gradual state machine deployments.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachineAlias.DeploymentPreferenceProperty"]], jsii.get(self, "deploymentPreference"))

    @deployment_preference.setter
    def deployment_preference(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachineAlias.DeploymentPreferenceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__291c291374c3a7bdc720916a40ec17c8994233f17b521e36f88493f1dfea6abe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentPreference", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the state machine alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c4a9670d54e1fd8d9f71a40d8fe51ff4c20b8266100071f23c2fcd11c913f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the state machine alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af65681afd264c6830e6a2a7499c40b1a1c1cd59a8a9d0c2b4f69d4df6f9f358)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="routingConfiguration")
    def routing_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStateMachineAlias.RoutingConfigurationVersionProperty"]]]]:
        '''The routing configuration of an alias.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStateMachineAlias.RoutingConfigurationVersionProperty"]]]], jsii.get(self, "routingConfiguration"))

    @routing_configuration.setter
    def routing_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStateMachineAlias.RoutingConfigurationVersionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91c36ec8b9a1fe59c6e03fb3ba3b15d8849aa3ea74c639879915303e21486168)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachineAlias.DeploymentPreferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "state_machine_version_arn": "stateMachineVersionArn",
            "type": "type",
            "alarms": "alarms",
            "interval": "interval",
            "percentage": "percentage",
        },
    )
    class DeploymentPreferenceProperty:
        def __init__(
            self,
            *,
            state_machine_version_arn: builtins.str,
            type: builtins.str,
            alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
            interval: typing.Optional[jsii.Number] = None,
            percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Enables gradual state machine deployments.

            CloudFormation automatically shifts traffic from the version the alias currently points to, to a new state machine version that you specify.

            :param state_machine_version_arn: The Amazon Resource Name (ARN) of the ```AWS::StepFunctions::StateMachineVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html>`_ resource that will be the final version to which the alias points to when the traffic shifting is complete. While performing gradual deployments, you can only provide a single state machine version ARN. To explicitly set version weights in a CloudFormation template, use ``RoutingConfiguration`` instead.
            :param type: The type of deployment you want to perform. You can specify one of the following types:. - ``LINEAR`` - Shifts traffic to the new version in equal increments with an equal number of minutes between each increment. For example, if you specify the increment percent as ``20`` with an interval of ``600`` minutes, this deployment increases traffic by 20 percent every 600 minutes until the new version receives 100 percent of the traffic. This deployment immediately rolls back the new version if any CloudWatch alarms are triggered. - ``ALL_AT_ONCE`` - Shifts 100 percent of traffic to the new version immediately. CloudFormation monitors the new version and rolls it back automatically to the previous version if any CloudWatch alarms are triggered. - ``CANARY`` - Shifts traffic in two increments. In the first increment, a small percentage of traffic, for example, 10 percent is shifted to the new version. In the second increment, before a specified time interval in seconds gets over, the remaining traffic is shifted to the new version. The shift to the new version for the remaining traffic takes place only if no CloudWatch alarms are triggered during the specified time interval.
            :param alarms: A list of Amazon CloudWatch alarms to be monitored during the deployment. The deployment fails and rolls back if any of these alarms go into the ``ALARM`` state.
            :param interval: The time in minutes between each traffic shifting increment.
            :param percentage: The percentage of traffic to shift to the new version in each increment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                deployment_preference_property = stepfunctions.CfnStateMachineAlias.DeploymentPreferenceProperty(
                    state_machine_version_arn="stateMachineVersionArn",
                    type="type",
                
                    # the properties below are optional
                    alarms=["alarms"],
                    interval=123,
                    percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8bf8e2b40097e36c0d014ffb281643658dd6d26279ce8e06bb1e9ce944fffb43)
                check_type(argname="argument state_machine_version_arn", value=state_machine_version_arn, expected_type=type_hints["state_machine_version_arn"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "state_machine_version_arn": state_machine_version_arn,
                "type": type,
            }
            if alarms is not None:
                self._values["alarms"] = alarms
            if interval is not None:
                self._values["interval"] = interval
            if percentage is not None:
                self._values["percentage"] = percentage

        @builtins.property
        def state_machine_version_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the ```AWS::StepFunctions::StateMachineVersion`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html>`_ resource that will be the final version to which the alias points to when the traffic shifting is complete.

            While performing gradual deployments, you can only provide a single state machine version ARN. To explicitly set version weights in a CloudFormation template, use ``RoutingConfiguration`` instead.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-statemachineversionarn
            '''
            result = self._values.get("state_machine_version_arn")
            assert result is not None, "Required property 'state_machine_version_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of deployment you want to perform. You can specify one of the following types:.

            - ``LINEAR`` - Shifts traffic to the new version in equal increments with an equal number of minutes between each increment.

            For example, if you specify the increment percent as ``20`` with an interval of ``600`` minutes, this deployment increases traffic by 20 percent every 600 minutes until the new version receives 100 percent of the traffic. This deployment immediately rolls back the new version if any CloudWatch alarms are triggered.

            - ``ALL_AT_ONCE`` - Shifts 100 percent of traffic to the new version immediately. CloudFormation monitors the new version and rolls it back automatically to the previous version if any CloudWatch alarms are triggered.
            - ``CANARY`` - Shifts traffic in two increments.

            In the first increment, a small percentage of traffic, for example, 10 percent is shifted to the new version. In the second increment, before a specified time interval in seconds gets over, the remaining traffic is shifted to the new version. The shift to the new version for the remaining traffic takes place only if no CloudWatch alarms are triggered during the specified time interval.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def alarms(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of Amazon CloudWatch alarms to be monitored during the deployment.

            The deployment fails and rolls back if any of these alarms go into the ``ALARM`` state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-alarms
            '''
            result = self._values.get("alarms")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''The time in minutes between each traffic shifting increment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def percentage(self) -> typing.Optional[jsii.Number]:
            '''The percentage of traffic to shift to the new version in each increment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-percentage
            '''
            result = self._values.get("percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentPreferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachineAlias.RoutingConfigurationVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "state_machine_version_arn": "stateMachineVersionArn",
            "weight": "weight",
        },
    )
    class RoutingConfigurationVersionProperty:
        def __init__(
            self,
            *,
            state_machine_version_arn: builtins.str,
            weight: jsii.Number,
        ) -> None:
            '''The state machine version to which you want to route the execution traffic.

            :param state_machine_version_arn: The Amazon Resource Name (ARN) that identifies one or two state machine versions defined in the routing configuration. If you specify the ARN of a second version, it must belong to the same state machine as the first version.
            :param weight: The percentage of traffic you want to route to the state machine version. The sum of the weights in the routing configuration must be equal to 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-routingconfigurationversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_stepfunctions as stepfunctions
                
                routing_configuration_version_property = stepfunctions.CfnStateMachineAlias.RoutingConfigurationVersionProperty(
                    state_machine_version_arn="stateMachineVersionArn",
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a688434f1bb6e3dfc9e2ccdd19ed95c105316293de60df8e4fe097b12705a50b)
                check_type(argname="argument state_machine_version_arn", value=state_machine_version_arn, expected_type=type_hints["state_machine_version_arn"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "state_machine_version_arn": state_machine_version_arn,
                "weight": weight,
            }

        @builtins.property
        def state_machine_version_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) that identifies one or two state machine versions defined in the routing configuration.

            If you specify the ARN of a second version, it must belong to the same state machine as the first version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-routingconfigurationversion.html#cfn-stepfunctions-statemachinealias-routingconfigurationversion-statemachineversionarn
            '''
            result = self._values.get("state_machine_version_arn")
            assert result is not None, "Required property 'state_machine_version_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def weight(self) -> jsii.Number:
            '''The percentage of traffic you want to route to the state machine version.

            The sum of the weights in the routing configuration must be equal to 100.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-routingconfigurationversion.html#cfn-stepfunctions-statemachinealias-routingconfigurationversion-weight
            '''
            result = self._values.get("weight")
            assert result is not None, "Required property 'weight' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoutingConfigurationVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachineAliasProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_preference": "deploymentPreference",
        "description": "description",
        "name": "name",
        "routing_configuration": "routingConfiguration",
    },
)
class CfnStateMachineAliasProps:
    def __init__(
        self,
        *,
        deployment_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachineAlias.DeploymentPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        routing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachineAlias.RoutingConfigurationVersionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStateMachineAlias``.

        :param deployment_preference: The settings that enable gradual state machine deployments. These settings include `Alarms <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-alarms>`_ , `Interval <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-interval>`_ , `Percentage <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-percentage>`_ , `StateMachineVersionArn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-statemachineversionarn>`_ , and `Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-type>`_ . CloudFormation automatically shifts traffic from the version an alias currently points to, to a new state machine version that you specify. .. epigraph:: ``RoutingConfiguration`` and ``DeploymentPreference`` are mutually exclusive properties. You must define only one of these properties. Based on the type of deployment you want to perform, you can specify one of the following settings: - ``LINEAR`` - Shifts traffic to the new version in equal increments with an equal number of minutes between each increment. For example, if you specify the increment percent as ``20`` with an interval of ``600`` minutes, this deployment increases traffic by 20 percent every 600 minutes until the new version receives 100 percent of the traffic. This deployment immediately rolls back the new version if any Amazon CloudWatch alarms are triggered. - ``ALL_AT_ONCE`` - Shifts 100 percent of traffic to the new version immediately. CloudFormation monitors the new version and rolls it back automatically to the previous version if any CloudWatch alarms are triggered. - ``CANARY`` - Shifts traffic in two increments. In the first increment, a small percentage of traffic, for example, 10 percent is shifted to the new version. In the second increment, before a specified time interval in seconds gets over, the remaining traffic is shifted to the new version. The shift to the new version for the remaining traffic takes place only if no CloudWatch alarms are triggered during the specified time interval.
        :param description: An optional description of the state machine alias.
        :param name: The name of the state machine alias. If you don't provide a name, it uses an automatically generated name based on the logical ID.
        :param routing_configuration: The routing configuration of an alias. Routing configuration splits `StartExecution <https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html>`_ requests between one or two versions of the same state machine. Use ``RoutingConfiguration`` if you want to explicitly set the alias `weights <https://docs.aws.amazon.com/step-functions/latest/apireference/API_RoutingConfigurationListItem.html#StepFunctions-Type-RoutingConfigurationListItem-weight>`_ . Weight is the percentage of traffic you want to route to a state machine version. .. epigraph:: ``RoutingConfiguration`` and ``DeploymentPreference`` are mutually exclusive properties. You must define only one of these properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            cfn_state_machine_alias_props = stepfunctions.CfnStateMachineAliasProps(
                deployment_preference=stepfunctions.CfnStateMachineAlias.DeploymentPreferenceProperty(
                    state_machine_version_arn="stateMachineVersionArn",
                    type="type",
            
                    # the properties below are optional
                    alarms=["alarms"],
                    interval=123,
                    percentage=123
                ),
                description="description",
                name="name",
                routing_configuration=[stepfunctions.CfnStateMachineAlias.RoutingConfigurationVersionProperty(
                    state_machine_version_arn="stateMachineVersionArn",
                    weight=123
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d59745dc4c655a3bf10278f9b74e39163a7b157ca93bafdd0e7939d5c39662)
            check_type(argname="argument deployment_preference", value=deployment_preference, expected_type=type_hints["deployment_preference"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument routing_configuration", value=routing_configuration, expected_type=type_hints["routing_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_preference is not None:
            self._values["deployment_preference"] = deployment_preference
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if routing_configuration is not None:
            self._values["routing_configuration"] = routing_configuration

    @builtins.property
    def deployment_preference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachineAlias.DeploymentPreferenceProperty]]:
        '''The settings that enable gradual state machine deployments.

        These settings include `Alarms <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-alarms>`_ , `Interval <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-interval>`_ , `Percentage <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-percentage>`_ , `StateMachineVersionArn <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-statemachineversionarn>`_ , and `Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stepfunctions-statemachinealias-deploymentpreference.html#cfn-stepfunctions-statemachinealias-deploymentpreference-type>`_ .

        CloudFormation automatically shifts traffic from the version an alias currently points to, to a new state machine version that you specify.
        .. epigraph::

           ``RoutingConfiguration`` and ``DeploymentPreference`` are mutually exclusive properties. You must define only one of these properties.

        Based on the type of deployment you want to perform, you can specify one of the following settings:

        - ``LINEAR`` - Shifts traffic to the new version in equal increments with an equal number of minutes between each increment.

        For example, if you specify the increment percent as ``20`` with an interval of ``600`` minutes, this deployment increases traffic by 20 percent every 600 minutes until the new version receives 100 percent of the traffic. This deployment immediately rolls back the new version if any Amazon CloudWatch alarms are triggered.

        - ``ALL_AT_ONCE`` - Shifts 100 percent of traffic to the new version immediately. CloudFormation monitors the new version and rolls it back automatically to the previous version if any CloudWatch alarms are triggered.
        - ``CANARY`` - Shifts traffic in two increments.

        In the first increment, a small percentage of traffic, for example, 10 percent is shifted to the new version. In the second increment, before a specified time interval in seconds gets over, the remaining traffic is shifted to the new version. The shift to the new version for the remaining traffic takes place only if no CloudWatch alarms are triggered during the specified time interval.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html#cfn-stepfunctions-statemachinealias-deploymentpreference
        '''
        result = self._values.get("deployment_preference")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachineAlias.DeploymentPreferenceProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the state machine alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html#cfn-stepfunctions-statemachinealias-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the state machine alias.

        If you don't provide a name, it uses an automatically generated name based on the logical ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html#cfn-stepfunctions-statemachinealias-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routing_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStateMachineAlias.RoutingConfigurationVersionProperty]]]]:
        '''The routing configuration of an alias.

        Routing configuration splits `StartExecution <https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html>`_ requests between one or two versions of the same state machine.

        Use ``RoutingConfiguration`` if you want to explicitly set the alias `weights <https://docs.aws.amazon.com/step-functions/latest/apireference/API_RoutingConfigurationListItem.html#StepFunctions-Type-RoutingConfigurationListItem-weight>`_ . Weight is the percentage of traffic you want to route to a state machine version.
        .. epigraph::

           ``RoutingConfiguration`` and ``DeploymentPreference`` are mutually exclusive properties. You must define only one of these properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachinealias.html#cfn-stepfunctions-statemachinealias-routingconfiguration
        '''
        result = self._values.get("routing_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStateMachineAlias.RoutingConfigurationVersionProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStateMachineAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachineProps",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "definition": "definition",
        "definition_s3_location": "definitionS3Location",
        "definition_string": "definitionString",
        "definition_substitutions": "definitionSubstitutions",
        "logging_configuration": "loggingConfiguration",
        "state_machine_name": "stateMachineName",
        "state_machine_type": "stateMachineType",
        "tags": "tags",
        "tracing_configuration": "tracingConfiguration",
    },
)
class CfnStateMachineProps:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        definition: typing.Any = None,
        definition_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_string: typing.Optional[builtins.str] = None,
        definition_substitutions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        state_machine_name: typing.Optional[builtins.str] = None,
        state_machine_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnStateMachine.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tracing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.TracingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStateMachine``.

        :param role_arn: The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
        :param definition: The Amazon States Language definition of the state machine. The state machine definition must be in JSON or YAML, and the format of the object must match the format of your CloudFormation template file. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`_ .
        :param definition_s3_location: The name of the S3 bucket where the state machine definition is stored. The state machine definition must be a JSON or YAML file.
        :param definition_string: The Amazon States Language definition of the state machine. The state machine definition must be in JSON. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`_ .
        :param definition_substitutions: A map (string to string) that specifies the mappings for placeholder variables in the state machine definition. This enables the customer to inject values obtained at runtime, for example from intrinsic functions, in the state machine definition. Variables can be template parameter names, resource logical IDs, resource attributes, or a variable in a key-value map. Substitutions must follow the syntax: ``${key_name}`` or ``${variable_1,variable_2,...}`` .
        :param logging_configuration: Defines what execution history events are logged and where they are logged. .. epigraph:: By default, the ``level`` is set to ``OFF`` . For more information see `Log Levels <https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html>`_ in the AWS Step Functions User Guide.
        :param state_machine_name: The name of the state machine. A name must *not* contain: - white space - brackets ``< > { } [ ]`` - wildcard characters ``? *`` - special characters ``" # % \\ ^ | ~ `` $ & , ; : /` - control characters ( ``U+0000-001F`` , ``U+007F-009F`` ) .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param state_machine_type: Determines whether a ``STANDARD`` or ``EXPRESS`` state machine is created. The default is ``STANDARD`` . You cannot update the ``type`` of a state machine once it has been created. For more information on ``STANDARD`` and ``EXPRESS`` workflows, see `Standard Versus Express Workflows <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html>`_ in the AWS Step Functions Developer Guide.
        :param tags: The list of tags to add to a resource. Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + -
        :param tracing_configuration: Selects whether or not the state machine's AWS X-Ray tracing is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # definition: Any
            
            cfn_state_machine_props = stepfunctions.CfnStateMachineProps(
                role_arn="roleArn",
            
                # the properties below are optional
                definition=definition,
                definition_s3_location=stepfunctions.CfnStateMachine.S3LocationProperty(
                    bucket="bucket",
                    key="key",
            
                    # the properties below are optional
                    version="version"
                ),
                definition_string="definitionString",
                definition_substitutions={
                    "definition_substitutions_key": "definitionSubstitutions"
                },
                logging_configuration=stepfunctions.CfnStateMachine.LoggingConfigurationProperty(
                    destinations=[stepfunctions.CfnStateMachine.LogDestinationProperty(
                        cloud_watch_logs_log_group=stepfunctions.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                            log_group_arn="logGroupArn"
                        )
                    )],
                    include_execution_data=False,
                    level="level"
                ),
                state_machine_name="stateMachineName",
                state_machine_type="stateMachineType",
                tags=[stepfunctions.CfnStateMachine.TagsEntryProperty(
                    key="key",
                    value="value"
                )],
                tracing_configuration=stepfunctions.CfnStateMachine.TracingConfigurationProperty(
                    enabled=False
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf4d4e83bd396b6667f5c30b66226d7e76f61626aea9c4ec1355f6e6a3631abd)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument definition_s3_location", value=definition_s3_location, expected_type=type_hints["definition_s3_location"])
            check_type(argname="argument definition_string", value=definition_string, expected_type=type_hints["definition_string"])
            check_type(argname="argument definition_substitutions", value=definition_substitutions, expected_type=type_hints["definition_substitutions"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
            check_type(argname="argument state_machine_type", value=state_machine_type, expected_type=type_hints["state_machine_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tracing_configuration", value=tracing_configuration, expected_type=type_hints["tracing_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if definition is not None:
            self._values["definition"] = definition
        if definition_s3_location is not None:
            self._values["definition_s3_location"] = definition_s3_location
        if definition_string is not None:
            self._values["definition_string"] = definition_string
        if definition_substitutions is not None:
            self._values["definition_substitutions"] = definition_substitutions
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if state_machine_name is not None:
            self._values["state_machine_name"] = state_machine_name
        if state_machine_type is not None:
            self._values["state_machine_type"] = state_machine_type
        if tags is not None:
            self._values["tags"] = tags
        if tracing_configuration is not None:
            self._values["tracing_configuration"] = tracing_configuration

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role to use for this state machine.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def definition(self) -> typing.Any:
        '''The Amazon States Language definition of the state machine.

        The state machine definition must be in JSON or YAML, and the format of the object must match the format of your CloudFormation template file. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definition
        '''
        result = self._values.get("definition")
        return typing.cast(typing.Any, result)

    @builtins.property
    def definition_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.S3LocationProperty]]:
        '''The name of the S3 bucket where the state machine definition is stored.

        The state machine definition must be a JSON or YAML file.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitions3location
        '''
        result = self._values.get("definition_s3_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.S3LocationProperty]], result)

    @builtins.property
    def definition_string(self) -> typing.Optional[builtins.str]:
        '''The Amazon States Language definition of the state machine.

        The state machine definition must be in JSON. See `Amazon States Language <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring
        '''
        result = self._values.get("definition_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def definition_substitutions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''A map (string to string) that specifies the mappings for placeholder variables in the state machine definition.

        This enables the customer to inject values obtained at runtime, for example from intrinsic functions, in the state machine definition. Variables can be template parameter names, resource logical IDs, resource attributes, or a variable in a key-value map.

        Substitutions must follow the syntax: ``${key_name}`` or ``${variable_1,variable_2,...}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionsubstitutions
        '''
        result = self._values.get("definition_substitutions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.LoggingConfigurationProperty]]:
        '''Defines what execution history events are logged and where they are logged.

        .. epigraph::

           By default, the ``level`` is set to ``OFF`` . For more information see `Log Levels <https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html>`_ in the AWS Step Functions User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.LoggingConfigurationProperty]], result)

    @builtins.property
    def state_machine_name(self) -> typing.Optional[builtins.str]:
        '''The name of the state machine.

        A name must *not* contain:

        - white space
        - brackets ``< > { } [ ]``
        - wildcard characters ``? *``
        - special characters ``" # % \\ ^ | ~ `` $ & , ; : /`
        - control characters ( ``U+0000-001F`` , ``U+007F-009F`` )

        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename
        '''
        result = self._values.get("state_machine_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_machine_type(self) -> typing.Optional[builtins.str]:
        '''Determines whether a ``STANDARD`` or ``EXPRESS`` state machine is created.

        The default is ``STANDARD`` . You cannot update the ``type`` of a state machine once it has been created. For more information on ``STANDARD`` and ``EXPRESS`` workflows, see `Standard Versus Express Workflows <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html>`_ in the AWS Step Functions Developer Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinetype
        '''
        result = self._values.get("state_machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnStateMachine.TagsEntryProperty]]:
        '''The list of tags to add to a resource.

        Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags
        :: ` .
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnStateMachine.TagsEntryProperty]], result)

    @builtins.property
    def tracing_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.TracingConfigurationProperty]]:
        '''Selects whether or not the state machine's AWS X-Ray tracing is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tracingconfiguration
        '''
        result = self._values.get("tracing_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.TracingConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStateMachineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStateMachineVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachineVersion",
):
    '''Represents a state machine `version <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html>`_ . A published version uses the latest state machine `*revision* <https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html>`_ . A revision is an immutable, read-only snapshot of a state machine’s definition and configuration.

    You can publish up to 1000 versions for each state machine.
    .. epigraph::

       Before you delete a version, make sure that version's ARN isn't being referenced in any long-running workflows or application code outside of the stack.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html
    :cloudformationResource: AWS::StepFunctions::StateMachineVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        cfn_state_machine_version = stepfunctions.CfnStateMachineVersion(self, "MyCfnStateMachineVersion",
            state_machine_arn="stateMachineArn",
        
            # the properties below are optional
            description="description",
            state_machine_revision_id="stateMachineRevisionId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        state_machine_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state_machine_revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param state_machine_arn: The Amazon Resource Name (ARN) of the state machine.
        :param description: An optional description of the state machine version.
        :param state_machine_revision_id: Identifier for a state machine revision, which is an immutable, read-only snapshot of a state machine’s definition and configuration. Only publish the state machine version if the current state machine's revision ID matches the specified ID. Use this option to avoid publishing a version if the state machine has changed since you last updated it. To specify the initial state machine revision, set the value as ``INITIAL`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b19ebd913b3792b5cf85d382b7166b1f3325d9d4c4d36e3487276014cbb29edc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStateMachineVersionProps(
            state_machine_arn=state_machine_arn,
            description=description,
            state_machine_revision_id=state_machine_revision_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5464561cedf359263d5e05f1d444de28a7d75d5ce4347840115515f065a5201)
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
            type_hints = typing.get_type_hints(_typecheckingstub__593f2bbe562bc9f9cee66f866efeb6b4662511cc706d0e7292314d744f609afb)
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
        '''Returns the ARN of the state machine version.

        For example, ``arn:aws:states:us-east-1:123456789012:stateMachine:myStateMachine:1`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="stateMachineArn")
    def state_machine_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the state machine.'''
        return typing.cast(builtins.str, jsii.get(self, "stateMachineArn"))

    @state_machine_arn.setter
    def state_machine_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b5bffae2ab6951189d8934aa88a458856f9a4d6623a0832d0295941754bf70d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachineArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the state machine version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8425cdd1ce7e33098a65ff2357b57674f96a520fc7d3cc63794e265253928cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachineRevisionId")
    def state_machine_revision_id(self) -> typing.Optional[builtins.str]:
        '''Identifier for a state machine revision, which is an immutable, read-only snapshot of a state machine’s definition and configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateMachineRevisionId"))

    @state_machine_revision_id.setter
    def state_machine_revision_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a80351896d09cb747491b59d0460387f46b6f51704f091b54c4fecf9f3f4bac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachineRevisionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.CfnStateMachineVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "state_machine_arn": "stateMachineArn",
        "description": "description",
        "state_machine_revision_id": "stateMachineRevisionId",
    },
)
class CfnStateMachineVersionProps:
    def __init__(
        self,
        *,
        state_machine_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state_machine_revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnStateMachineVersion``.

        :param state_machine_arn: The Amazon Resource Name (ARN) of the state machine.
        :param description: An optional description of the state machine version.
        :param state_machine_revision_id: Identifier for a state machine revision, which is an immutable, read-only snapshot of a state machine’s definition and configuration. Only publish the state machine version if the current state machine's revision ID matches the specified ID. Use this option to avoid publishing a version if the state machine has changed since you last updated it. To specify the initial state machine revision, set the value as ``INITIAL`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            cfn_state_machine_version_props = stepfunctions.CfnStateMachineVersionProps(
                state_machine_arn="stateMachineArn",
            
                # the properties below are optional
                description="description",
                state_machine_revision_id="stateMachineRevisionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a26dd5401b86d66727994521c663b875a629d09b7d66d7dc260fb560b6d9642)
            check_type(argname="argument state_machine_arn", value=state_machine_arn, expected_type=type_hints["state_machine_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument state_machine_revision_id", value=state_machine_revision_id, expected_type=type_hints["state_machine_revision_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "state_machine_arn": state_machine_arn,
        }
        if description is not None:
            self._values["description"] = description
        if state_machine_revision_id is not None:
            self._values["state_machine_revision_id"] = state_machine_revision_id

    @builtins.property
    def state_machine_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the state machine.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html#cfn-stepfunctions-statemachineversion-statemachinearn
        '''
        result = self._values.get("state_machine_arn")
        assert result is not None, "Required property 'state_machine_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the state machine version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html#cfn-stepfunctions-statemachineversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_machine_revision_id(self) -> typing.Optional[builtins.str]:
        '''Identifier for a state machine revision, which is an immutable, read-only snapshot of a state machine’s definition and configuration.

        Only publish the state machine version if the current state machine's revision ID matches the specified ID. Use this option to avoid publishing a version if the state machine has changed since you last updated it.

        To specify the initial state machine revision, set the value as ``INITIAL`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html#cfn-stepfunctions-statemachineversion-statemachinerevisionid
        '''
        result = self._values.get("state_machine_revision_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStateMachineVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.ChoiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "output_path": "outputPath",
        "state_name": "stateName",
    },
)
class ChoiceProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a Choice state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name

        :exampleMetadata: infused

        Example::

            choice = sfn.Choice(self, "What color is it?",
                comment="color comment"
            )
            handle_blue_item = sfn.Pass(self, "HandleBlueItem")
            handle_other_item_color = sfn.Pass(self, "HanldeOtherItemColor")
            choice.when(sfn.Condition.string_equals("$.color", "BLUE"), handle_blue_item,
                comment="blue item comment"
            )
            choice.otherwise(handle_other_item_color)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a926bb3a79f5cf3706dd32093c49a75fa6045aeefbff3e1b4943eb654489e685)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if state_name is not None:
            self._values["state_name"] = state_name

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChoiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.ChoiceTransitionOptions",
    jsii_struct_bases=[],
    name_mapping={"comment": "comment"},
)
class ChoiceTransitionOptions:
    def __init__(self, *, comment: typing.Optional[builtins.str] = None) -> None:
        '''Options for Choice Transition.

        :param comment: An optional description for the choice transition. Default: No comment

        :exampleMetadata: infused

        Example::

            choice = sfn.Choice(self, "What color is it?",
                comment="color comment"
            )
            handle_blue_item = sfn.Pass(self, "HandleBlueItem")
            handle_other_item_color = sfn.Pass(self, "HanldeOtherItemColor")
            choice.when(sfn.Condition.string_equals("$.color", "BLUE"), handle_blue_item,
                comment="blue item comment"
            )
            choice.otherwise(handle_other_item_color)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__254c8670f15896e504e7f2c5398c9717ddc003fe66835e546b52b1693c004add)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for the choice transition.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChoiceTransitionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Condition(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Condition",
):
    '''A Condition for use in a Choice state branch.

    :exampleMetadata: infused

    Example::

        map = sfn.Map(self, "Map State",
            max_concurrency=1,
            items_path=sfn.JsonPath.string_at("$.inputForMap"),
            item_selector={
                "item": sfn.JsonPath.string_at("$.Map.Item.Value")
            },
            result_path="$.mapOutput"
        )
        
        # The Map iterator can contain a IChainable, which can be an individual or multiple steps chained together.
        # Below example is with a Choice and Pass step
        choice = sfn.Choice(self, "Choice")
        condition1 = sfn.Condition.string_equals("$.item.status", "SUCCESS")
        step1 = sfn.Pass(self, "Step1")
        step2 = sfn.Pass(self, "Step2")
        finish = sfn.Pass(self, "Finish")
        
        definition = choice.when(condition1, step1).otherwise(step2).afterwards().next(finish)
        
        map.item_processor(definition)
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="and")
    @builtins.classmethod
    def and_(cls, *conditions: "Condition") -> "Condition":
        '''Combine two or more conditions with a logical AND.

        :param conditions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71eb0d2598d910c950378149f21b99ac6c39c861109d3ab21b603c6dd4a39f67)
            check_type(argname="argument conditions", value=conditions, expected_type=typing.Tuple[type_hints["conditions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("Condition", jsii.sinvoke(cls, "and", [*conditions]))

    @jsii.member(jsii_name="booleanEquals")
    @builtins.classmethod
    def boolean_equals(
        cls,
        variable: builtins.str,
        value: builtins.bool,
    ) -> "Condition":
        '''Matches if a boolean field has the given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b9bc889cdd24c404551cfb0d6925ab10c64ddca33272041a3c7d8db3e9025c7)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "booleanEquals", [variable, value]))

    @jsii.member(jsii_name="booleanEqualsJsonPath")
    @builtins.classmethod
    def boolean_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a boolean field equals to a value at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1db786980e3e6eb95ef1359718a8087981a167450763e1b1af4cccde32d8df67)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "booleanEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="isBoolean")
    @builtins.classmethod
    def is_boolean(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is boolean.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4044239d0ab330627f79630a789a88d7b43ad67590db42e02374bb20c513dda1)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isBoolean", [variable]))

    @jsii.member(jsii_name="isNotBoolean")
    @builtins.classmethod
    def is_not_boolean(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is not boolean.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d8d8efc940c58d80b1c03cc3a965aec81d82a73fd35d57efb6446acd9501e9c)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isNotBoolean", [variable]))

    @jsii.member(jsii_name="isNotNull")
    @builtins.classmethod
    def is_not_null(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is not null.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a9314e2710309f34934fbe6b184bffa9367a1d71ac9f79627e6c79845fc04a5)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isNotNull", [variable]))

    @jsii.member(jsii_name="isNotNumeric")
    @builtins.classmethod
    def is_not_numeric(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is not numeric.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18fa5c934c072dc5c01e61c786a81241c2a66991b9f365ba7656fee9bebb6bfb)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isNotNumeric", [variable]))

    @jsii.member(jsii_name="isNotPresent")
    @builtins.classmethod
    def is_not_present(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is not present.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af8d78236cfc082603b9981a5287c2ac458428d58eba55f05b44995b4210acfd)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isNotPresent", [variable]))

    @jsii.member(jsii_name="isNotString")
    @builtins.classmethod
    def is_not_string(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is not a string.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__343e7cf6c4a403ce9824b8a1b7dfa9fca52c0c03cd770a44c56f803c37338bf6)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isNotString", [variable]))

    @jsii.member(jsii_name="isNotTimestamp")
    @builtins.classmethod
    def is_not_timestamp(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is not a timestamp.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7250986a16f9bb8be78a9686c2ae7dce3fef5bb1c5b8b256fbcdb015c259919e)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isNotTimestamp", [variable]))

    @jsii.member(jsii_name="isNull")
    @builtins.classmethod
    def is_null(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is Null.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f79eb1053d2162c6a58e2c2b7f0557b73ad5660d50e70b80b385adb03087993)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isNull", [variable]))

    @jsii.member(jsii_name="isNumeric")
    @builtins.classmethod
    def is_numeric(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is numeric.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__561ba17c1b749efc2328847c14b1814d33920f4ab0fb079d257f56c929ca03a4)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isNumeric", [variable]))

    @jsii.member(jsii_name="isPresent")
    @builtins.classmethod
    def is_present(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is present.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__392be928fa30637320c733f4d7810aff4b79cb72e727ae2838ba58c1b919f493)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isPresent", [variable]))

    @jsii.member(jsii_name="isString")
    @builtins.classmethod
    def is_string(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is a string.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__badeb8cc1a4243c359dbfd4d33b9074f5f4d3646b5823a9c49c9fe26330592e6)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isString", [variable]))

    @jsii.member(jsii_name="isTimestamp")
    @builtins.classmethod
    def is_timestamp(cls, variable: builtins.str) -> "Condition":
        '''Matches if variable is a timestamp.

        :param variable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__361a2b8f339e790bd76aa839dfda488de2cc072d8a449e5a81b855b62eb59876)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        return typing.cast("Condition", jsii.sinvoke(cls, "isTimestamp", [variable]))

    @jsii.member(jsii_name="not")
    @builtins.classmethod
    def not_(cls, condition: "Condition") -> "Condition":
        '''Negate a condition.

        :param condition: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5acebcb4f135ed0cc9e840cb1cbaee78dd705f7b775d6b5cbe9eb4d18557941c)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
        return typing.cast("Condition", jsii.sinvoke(cls, "not", [condition]))

    @jsii.member(jsii_name="numberEquals")
    @builtins.classmethod
    def number_equals(cls, variable: builtins.str, value: jsii.Number) -> "Condition":
        '''Matches if a numeric field has the given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc2870430bc517ffa4c051bbeec0e433e96a52f7cded7c34363a0655bc8e8283)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberEquals", [variable, value]))

    @jsii.member(jsii_name="numberEqualsJsonPath")
    @builtins.classmethod
    def number_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a numeric field has the value in a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fbfe1d112b80de4f820cf91187f730fef81616ca2bd204372e64505b28b46c1)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="numberGreaterThan")
    @builtins.classmethod
    def number_greater_than(
        cls,
        variable: builtins.str,
        value: jsii.Number,
    ) -> "Condition":
        '''Matches if a numeric field is greater than the given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6d064c6f5ca8f0d29f98983b27295433d8fb18943cb0e8fb8588b430462566)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberGreaterThan", [variable, value]))

    @jsii.member(jsii_name="numberGreaterThanEquals")
    @builtins.classmethod
    def number_greater_than_equals(
        cls,
        variable: builtins.str,
        value: jsii.Number,
    ) -> "Condition":
        '''Matches if a numeric field is greater than or equal to the given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93f18ca4cac21cd9ca7599acbcaa3e51e34cd4c898c63ae7f85784f73b530f91)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberGreaterThanEquals", [variable, value]))

    @jsii.member(jsii_name="numberGreaterThanEqualsJsonPath")
    @builtins.classmethod
    def number_greater_than_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a numeric field is greater than or equal to the value at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6afb217f2f63404a040a45130eaa97bbe2d52ecc9c1d35a1c979bb3071894c0)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberGreaterThanEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="numberGreaterThanJsonPath")
    @builtins.classmethod
    def number_greater_than_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a numeric field is greater than the value at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a0df062863035ddc6506fe6962d7a1fc4d5a4b5e8529bc8d06dab3f53e38337)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberGreaterThanJsonPath", [variable, value]))

    @jsii.member(jsii_name="numberLessThan")
    @builtins.classmethod
    def number_less_than(
        cls,
        variable: builtins.str,
        value: jsii.Number,
    ) -> "Condition":
        '''Matches if a numeric field is less than the given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85df632e1bb32eaa6062ef02209f69b58d10a8dfa8cade99ef9532416279b42d)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberLessThan", [variable, value]))

    @jsii.member(jsii_name="numberLessThanEquals")
    @builtins.classmethod
    def number_less_than_equals(
        cls,
        variable: builtins.str,
        value: jsii.Number,
    ) -> "Condition":
        '''Matches if a numeric field is less than or equal to the given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab2dcbd2780b62793d8418faad84b7d828dd3f4f566b3e6ae53c3877bbd61227)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberLessThanEquals", [variable, value]))

    @jsii.member(jsii_name="numberLessThanEqualsJsonPath")
    @builtins.classmethod
    def number_less_than_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a numeric field is less than or equal to the numeric value at given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5a63d516352eb231b883e8e64d9639a572564facf5dea9a3c5198a9e22876c4)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberLessThanEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="numberLessThanJsonPath")
    @builtins.classmethod
    def number_less_than_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a numeric field is less than the value at the given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__599066fbf144c3ed0066b2f899bba8d423c4bb2dc9e2b874dbaa5ebf457e11df)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "numberLessThanJsonPath", [variable, value]))

    @jsii.member(jsii_name="or")
    @builtins.classmethod
    def or_(cls, *conditions: "Condition") -> "Condition":
        '''Combine two or more conditions with a logical OR.

        :param conditions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ebfca9e6b416b95d0c13f84b582d58628d0adebff6b077140c28ffa89cd681)
            check_type(argname="argument conditions", value=conditions, expected_type=typing.Tuple[type_hints["conditions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("Condition", jsii.sinvoke(cls, "or", [*conditions]))

    @jsii.member(jsii_name="stringEquals")
    @builtins.classmethod
    def string_equals(cls, variable: builtins.str, value: builtins.str) -> "Condition":
        '''Matches if a string field has the given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5e3bcb339531b64d38b5c4df6ca6651eaefce4132a0e157a06bf0ff0f92483)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringEquals", [variable, value]))

    @jsii.member(jsii_name="stringEqualsJsonPath")
    @builtins.classmethod
    def string_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field equals to a value at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78f169f014f9ae3df9f49252e02dead74ee520bb53ba38a05a3952b041b3e46e)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="stringGreaterThan")
    @builtins.classmethod
    def string_greater_than(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field sorts after a given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa269f3363724cd30c519d1c6741e4614000bba9e0d027da1ece94705be1180f)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringGreaterThan", [variable, value]))

    @jsii.member(jsii_name="stringGreaterThanEquals")
    @builtins.classmethod
    def string_greater_than_equals(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field sorts after or equal to a given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f68add250a89ba6ac56739d0a7f86bc8888c9863e1ddfb9955559b87fdd7d19)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringGreaterThanEquals", [variable, value]))

    @jsii.member(jsii_name="stringGreaterThanEqualsJsonPath")
    @builtins.classmethod
    def string_greater_than_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field sorts after or equal to value at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860e3ec79ef3c5b3b8a6b4959dcd94eaa8b6d982c515f4ec6305a18800737c02)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringGreaterThanEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="stringGreaterThanJsonPath")
    @builtins.classmethod
    def string_greater_than_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field sorts after a value at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0790ed513991abfda140a8c53d563ee6788dc73fe0008ceef63ea895a638ba7a)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringGreaterThanJsonPath", [variable, value]))

    @jsii.member(jsii_name="stringLessThan")
    @builtins.classmethod
    def string_less_than(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field sorts before a given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef009e1d0aeb56bc81745234de63e9ff0769c94902c109c64463af7cfe55b98c)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringLessThan", [variable, value]))

    @jsii.member(jsii_name="stringLessThanEquals")
    @builtins.classmethod
    def string_less_than_equals(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field sorts equal to or before a given value.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d90066748658a5be8982e167d4dd1de780d5a8b558e1fdf6ea75bc89e3a3cc9)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringLessThanEquals", [variable, value]))

    @jsii.member(jsii_name="stringLessThanEqualsJsonPath")
    @builtins.classmethod
    def string_less_than_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field sorts equal to or before a given mapping.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145b1a589a61e4fa1b0e930fb96671f16374fd9fdc4f63f3685a84951f9113cd)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringLessThanEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="stringLessThanJsonPath")
    @builtins.classmethod
    def string_less_than_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a string field sorts before a given value at a particular mapping.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d13f1a89d702d97299b808ac45fc1a8f5d3115c0f7f540e1e40bad59affb2fd)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringLessThanJsonPath", [variable, value]))

    @jsii.member(jsii_name="stringMatches")
    @builtins.classmethod
    def string_matches(cls, variable: builtins.str, value: builtins.str) -> "Condition":
        '''Matches if a field matches a string pattern that can contain a wild card (*) e.g: log-*.txt or *LATEST*. No other characters other than "*" have any special meaning - * can be escaped: \\*.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de73e811b3b1426b79947865d10e188cd9a19a7803f6f2310a8d94ff46ee056f)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "stringMatches", [variable, value]))

    @jsii.member(jsii_name="timestampEquals")
    @builtins.classmethod
    def timestamp_equals(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is the same time as the given timestamp.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c124b18e00eb90c97548b3ee174d109e9086ee3f576c7c21dea0c626b172ca)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampEquals", [variable, value]))

    @jsii.member(jsii_name="timestampEqualsJsonPath")
    @builtins.classmethod
    def timestamp_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is the same time as the timestamp at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9391c794c3ff6ae9ee1ab30da37a340d85e5e712386072e80559b30234fd7263)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="timestampGreaterThan")
    @builtins.classmethod
    def timestamp_greater_than(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is after the given timestamp.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86c020130869b22990c221979ed64ee6dc804120a40a7e5ba4388cf82a89f7f7)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampGreaterThan", [variable, value]))

    @jsii.member(jsii_name="timestampGreaterThanEquals")
    @builtins.classmethod
    def timestamp_greater_than_equals(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is after or equal to the given timestamp.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae72825e4f0dba8d57cf583d4b9da4aa4228292ee1bc145787d5bae8bdd13c9c)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampGreaterThanEquals", [variable, value]))

    @jsii.member(jsii_name="timestampGreaterThanEqualsJsonPath")
    @builtins.classmethod
    def timestamp_greater_than_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is after or equal to the timestamp at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1374c2638911f124c361c2f692e26a6c983ad283eb5675881a3005262018962)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampGreaterThanEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="timestampGreaterThanJsonPath")
    @builtins.classmethod
    def timestamp_greater_than_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is after the timestamp at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5567199e7723f4a83859c8e45186b8afe013d15927c9e560684990deaf97d212)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampGreaterThanJsonPath", [variable, value]))

    @jsii.member(jsii_name="timestampLessThan")
    @builtins.classmethod
    def timestamp_less_than(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is before the given timestamp.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd9508b8a46d6979f811f9f642e6dba0f1b1ec212fffb60d21dd98ae3b0cb1b0)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampLessThan", [variable, value]))

    @jsii.member(jsii_name="timestampLessThanEquals")
    @builtins.classmethod
    def timestamp_less_than_equals(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is before or equal to the given timestamp.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__459421befc35cebd0bbdf1d1d350af4f3fb47bd1d5e7d03db51ddcfb96fb1eff)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampLessThanEquals", [variable, value]))

    @jsii.member(jsii_name="timestampLessThanEqualsJsonPath")
    @builtins.classmethod
    def timestamp_less_than_equals_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is before or equal to the timestamp at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e734a1f85e798bc59d4fc4f1aaf3c7a28bd4808ec5f926179da1a6a1ae53857c)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampLessThanEqualsJsonPath", [variable, value]))

    @jsii.member(jsii_name="timestampLessThanJsonPath")
    @builtins.classmethod
    def timestamp_less_than_json_path(
        cls,
        variable: builtins.str,
        value: builtins.str,
    ) -> "Condition":
        '''Matches if a timestamp field is before the timestamp at a given mapping path.

        :param variable: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25cbb60f1773ec82d0235bd53fcbf222ee9038bc1b1039e8ad3e48e0445c9b77)
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Condition", jsii.sinvoke(cls, "timestampLessThanJsonPath", [variable, value]))

    @jsii.member(jsii_name="renderCondition")
    @abc.abstractmethod
    def render_condition(self) -> typing.Any:
        '''Render Amazon States Language JSON for the condition.'''
        ...


class _ConditionProxy(Condition):
    @jsii.member(jsii_name="renderCondition")
    def render_condition(self) -> typing.Any:
        '''Render Amazon States Language JSON for the condition.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderCondition", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Condition).__jsii_proxy_class__ = lambda : _ConditionProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.Credentials",
    jsii_struct_bases=[],
    name_mapping={"role": "role"},
)
class Credentials:
    def __init__(self, *, role: "TaskRole") -> None:
        '''Specifies a target role assumed by the State Machine's execution role for invoking the task's resource.

        :param role: The role to be assumed for executing the Task.

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html#task-state-fields
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            
            # submit_lambda: lambda.Function
            # iam_role: iam.Role
            
            
            # use a fixed role for all task invocations
            role = sfn.TaskRole.from_role(iam_role)
            # or use a json expression to resolve the role at runtime based on task inputs
            # const role = sfn.TaskRole.fromRoleArnJsonPath('$.RoleArn');
            
            submit_job = tasks.LambdaInvoke(self, "Submit Job",
                lambda_function=submit_lambda,
                output_path="$.Payload",
                # use credentials
                credentials=sfn.Credentials(role=role)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75c7ba87106a955eb0c1dd29b26afbdb125c2950c829f9cfb85b266f527c14df)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
        }

    @builtins.property
    def role(self) -> "TaskRole":
        '''The role to be assumed for executing the Task.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast("TaskRole", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Credentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.CsvHeaderLocation")
class CsvHeaderLocation(enum.Enum):
    '''CSV header location options.'''

    FIRST_ROW = "FIRST_ROW"
    '''Headers will be read from first row of CSV file.'''
    GIVEN = "GIVEN"
    '''Headers are provided in CSVHeaders property.'''


class CsvHeaders(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.CsvHeaders",
):
    '''Configuration for CSV header options for a CSV Item Reader.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        csv_headers = stepfunctions.CsvHeaders.use(["headers"])
    '''

    @jsii.member(jsii_name="use")
    @builtins.classmethod
    def use(cls, headers: typing.Sequence[builtins.str]) -> "CsvHeaders":
        '''Configures S3CsvItemReader to use the headers provided in the ``headers`` parameter.

        :param headers: - List of headers.

        :return: - CsvHeaders
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bca5f165d56905bd06f4a1c77bab648cc802c173242fb36fc4310aaebc86dc6)
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
        return typing.cast("CsvHeaders", jsii.sinvoke(cls, "use", [headers]))

    @jsii.member(jsii_name="useFirstRow")
    @builtins.classmethod
    def use_first_row(cls) -> "CsvHeaders":
        '''Configures S3CsvItemReader to read headers from the first row of the CSV file.

        :return: - CsvHeaders
        '''
        return typing.cast("CsvHeaders", jsii.sinvoke(cls, "useFirstRow", []))

    @builtins.property
    @jsii.member(jsii_name="headerLocation")
    def header_location(self) -> CsvHeaderLocation:
        '''Location of headers in CSV file.'''
        return typing.cast(CsvHeaderLocation, jsii.get(self, "headerLocation"))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of headers if ``headerLocation`` is ``GIVEN``.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headers"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.CustomStateProps",
    jsii_struct_bases=[],
    name_mapping={"state_json": "stateJson"},
)
class CustomStateProps:
    def __init__(self, *, state_json: typing.Mapping[builtins.str, typing.Any]) -> None:
        '''Properties for defining a custom state definition.

        :param state_json: Amazon States Language (JSON-based) definition of the state.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_dynamodb as dynamodb
            
            
            # create a table
            table = dynamodb.Table(self, "montable",
                partition_key=dynamodb.Attribute(
                    name="id",
                    type=dynamodb.AttributeType.STRING
                )
            )
            
            final_status = sfn.Pass(self, "final step")
            
            # States language JSON to put an item into DynamoDB
            # snippet generated from https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-code-snippet.html#tutorial-code-snippet-1
            state_json = {
                "Type": "Task",
                "Resource": "arn:aws:states:::dynamodb:putItem",
                "Parameters": {
                    "TableName": table.table_name,
                    "Item": {
                        "id": {
                            "S": "MyEntry"
                        }
                    }
                },
                "ResultPath": null
            }
            
            # custom state which represents a task to insert data into DynamoDB
            custom = sfn.CustomState(self, "my custom task",
                state_json=state_json
            )
            
            # catch errors with addCatch
            error_handler = sfn.Pass(self, "handle failure")
            custom.add_catch(error_handler)
            
            # retry the task if something goes wrong
            custom.add_retry(
                errors=[sfn.Errors.ALL],
                interval=Duration.seconds(10),
                max_attempts=5
            )
            
            chain = sfn.Chain.start(custom).next(final_status)
            
            sm = sfn.StateMachine(self, "StateMachine",
                definition_body=sfn.DefinitionBody.from_chainable(chain),
                timeout=Duration.seconds(30),
                comment="a super cool state machine"
            )
            
            # don't forget permissions. You need to assign them
            table.grant_write_data(sm)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde0868841af19410dad218c5615177bdc4ee1633d65f2618ef7750dfcf857d6)
            check_type(argname="argument state_json", value=state_json, expected_type=type_hints["state_json"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "state_json": state_json,
        }

    @builtins.property
    def state_json(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''Amazon States Language (JSON-based) definition of the state.

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html
        '''
        result = self._values.get("state_json")
        assert result is not None, "Required property 'state_json' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomStateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DefinitionBody(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_stepfunctions.DefinitionBody",
):
    '''
    :exampleMetadata: infused

    Example::

        state_machine = stepfunctions.StateMachine(self, "SM",
            definition_body=stepfunctions.DefinitionBody.from_chainable(stepfunctions.Wait(self, "Hello", time=stepfunctions.WaitTime.duration(Duration.seconds(10))))
        )
        
        iot.TopicRule(self, "TopicRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
            actions=[
                actions.StepFunctionsStateMachineAction(state_machine)
            ]
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromChainable")
    @builtins.classmethod
    def from_chainable(cls, chainable: "IChainable") -> "DefinitionBody":
        '''
        :param chainable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c2a13855ce583fafff8ce021d579ed3a8ce8c50b9af46c8d337814412dd2ef)
            check_type(argname="argument chainable", value=chainable, expected_type=type_hints["chainable"])
        return typing.cast("DefinitionBody", jsii.sinvoke(cls, "fromChainable", [chainable]))

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(
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
    ) -> "DefinitionBody":
        '''
        :param path: -
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e34fabd0367a0519a35d86d419baa37e6fe26ad05457e96b236a55bb8c0cc1e)
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

        return typing.cast("DefinitionBody", jsii.sinvoke(cls, "fromFile", [path, options]))

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(cls, definition: builtins.str) -> "DefinitionBody":
        '''
        :param definition: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9105593602193f6c430b59ac16525785e4183211394cf7f4a2cc2ba6b2354e01)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
        return typing.cast("DefinitionBody", jsii.sinvoke(cls, "fromString", [definition]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        sfn_principal: _IPrincipal_539bb2fd,
        sfn_props: typing.Union["StateMachineProps", typing.Dict[builtins.str, typing.Any]],
        graph: typing.Optional["StateGraph"] = None,
    ) -> "DefinitionConfig":
        '''
        :param scope: -
        :param sfn_principal: -
        :param sfn_props: -
        :param graph: -
        '''
        ...


class _DefinitionBodyProxy(DefinitionBody):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        sfn_principal: _IPrincipal_539bb2fd,
        sfn_props: typing.Union["StateMachineProps", typing.Dict[builtins.str, typing.Any]],
        graph: typing.Optional["StateGraph"] = None,
    ) -> "DefinitionConfig":
        '''
        :param scope: -
        :param sfn_principal: -
        :param sfn_props: -
        :param graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__982308674c1f12c5d781609eb6924d004d05afbe7d720d0e8a36fb8d432cf97c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument sfn_principal", value=sfn_principal, expected_type=type_hints["sfn_principal"])
            check_type(argname="argument sfn_props", value=sfn_props, expected_type=type_hints["sfn_props"])
            check_type(argname="argument graph", value=graph, expected_type=type_hints["graph"])
        return typing.cast("DefinitionConfig", jsii.invoke(self, "bind", [scope, sfn_principal, sfn_props, graph]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DefinitionBody).__jsii_proxy_class__ = lambda : _DefinitionBodyProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.DefinitionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "definition": "definition",
        "definition_s3_location": "definitionS3Location",
        "definition_string": "definitionString",
    },
)
class DefinitionConfig:
    def __init__(
        self,
        *,
        definition: typing.Any = None,
        definition_s3_location: typing.Optional[typing.Union[CfnStateMachine.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        definition_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Partial object from the StateMachine L1 construct properties containing definition information.

        :param definition: 
        :param definition_s3_location: 
        :param definition_string: 

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # definition: Any
            
            definition_config = stepfunctions.DefinitionConfig(
                definition=definition,
                definition_s3_location=stepfunctions.CfnStateMachine.S3LocationProperty(
                    bucket="bucket",
                    key="key",
            
                    # the properties below are optional
                    version="version"
                ),
                definition_string="definitionString"
            )
        '''
        if isinstance(definition_s3_location, dict):
            definition_s3_location = CfnStateMachine.S3LocationProperty(**definition_s3_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0110b36a0362589a48107daf28e3afe725be68dbbc869656e5a397d958ab43dd)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument definition_s3_location", value=definition_s3_location, expected_type=type_hints["definition_s3_location"])
            check_type(argname="argument definition_string", value=definition_string, expected_type=type_hints["definition_string"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if definition is not None:
            self._values["definition"] = definition
        if definition_s3_location is not None:
            self._values["definition_s3_location"] = definition_s3_location
        if definition_string is not None:
            self._values["definition_string"] = definition_string

    @builtins.property
    def definition(self) -> typing.Any:
        result = self._values.get("definition")
        return typing.cast(typing.Any, result)

    @builtins.property
    def definition_s3_location(
        self,
    ) -> typing.Optional[CfnStateMachine.S3LocationProperty]:
        result = self._values.get("definition_s3_location")
        return typing.cast(typing.Optional[CfnStateMachine.S3LocationProperty], result)

    @builtins.property
    def definition_string(self) -> typing.Optional[builtins.str]:
        result = self._values.get("definition_string")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefinitionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Errors(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_stepfunctions.Errors"):
    '''Predefined error strings Error names in Amazon States Language - https://states-language.net/spec.html#appendix-a Error handling in Step Functions - https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_dynamodb as dynamodb
        
        
        # create a table
        table = dynamodb.Table(self, "montable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        final_status = sfn.Pass(self, "final step")
        
        # States language JSON to put an item into DynamoDB
        # snippet generated from https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-code-snippet.html#tutorial-code-snippet-1
        state_json = {
            "Type": "Task",
            "Resource": "arn:aws:states:::dynamodb:putItem",
            "Parameters": {
                "TableName": table.table_name,
                "Item": {
                    "id": {
                        "S": "MyEntry"
                    }
                }
            },
            "ResultPath": null
        }
        
        # custom state which represents a task to insert data into DynamoDB
        custom = sfn.CustomState(self, "my custom task",
            state_json=state_json
        )
        
        # catch errors with addCatch
        error_handler = sfn.Pass(self, "handle failure")
        custom.add_catch(error_handler)
        
        # retry the task if something goes wrong
        custom.add_retry(
            errors=[sfn.Errors.ALL],
            interval=Duration.seconds(10),
            max_attempts=5
        )
        
        chain = sfn.Chain.start(custom).next(final_status)
        
        sm = sfn.StateMachine(self, "StateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(chain),
            timeout=Duration.seconds(30),
            comment="a super cool state machine"
        )
        
        # don't forget permissions. You need to assign them
        table.grant_write_data(sm)
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALL")
    def ALL(cls) -> builtins.str:
        '''Matches any Error.'''
        return typing.cast(builtins.str, jsii.sget(cls, "ALL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BRANCH_FAILED")
    def BRANCH_FAILED(cls) -> builtins.str:
        '''A branch of a Parallel state failed.'''
        return typing.cast(builtins.str, jsii.sget(cls, "BRANCH_FAILED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEARTBEAT_TIMEOUT")
    def HEARTBEAT_TIMEOUT(cls) -> builtins.str:
        '''A Task State failed to heartbeat for a time longer than the “HeartbeatSeconds” value.'''
        return typing.cast(builtins.str, jsii.sget(cls, "HEARTBEAT_TIMEOUT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NO_CHOICE_MATCHED")
    def NO_CHOICE_MATCHED(cls) -> builtins.str:
        '''A Choice state failed to find a match for the condition field extracted from its input.'''
        return typing.cast(builtins.str, jsii.sget(cls, "NO_CHOICE_MATCHED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PARAMETER_PATH_FAILURE")
    def PARAMETER_PATH_FAILURE(cls) -> builtins.str:
        '''Within a state’s “Parameters” field, the attempt to replace a field whose name ends in “.$” using a Path failed.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PARAMETER_PATH_FAILURE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PERMISSIONS")
    def PERMISSIONS(cls) -> builtins.str:
        '''A Task State failed because it had insufficient privileges to execute the specified code.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PERMISSIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESULT_PATH_MATCH_FAILURE")
    def RESULT_PATH_MATCH_FAILURE(cls) -> builtins.str:
        '''A Task State’s “ResultPath” field cannot be applied to the input the state received.'''
        return typing.cast(builtins.str, jsii.sget(cls, "RESULT_PATH_MATCH_FAILURE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TASKS_FAILED")
    def TASKS_FAILED(cls) -> builtins.str:
        '''A Task State failed during the execution.'''
        return typing.cast(builtins.str, jsii.sget(cls, "TASKS_FAILED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TIMEOUT")
    def TIMEOUT(cls) -> builtins.str:
        '''A Task State either ran longer than the “TimeoutSeconds” value, or failed to heartbeat for a time longer than the “HeartbeatSeconds” value.'''
        return typing.cast(builtins.str, jsii.sget(cls, "TIMEOUT"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.FailProps",
    jsii_struct_bases=[],
    name_mapping={
        "cause": "cause",
        "cause_path": "causePath",
        "comment": "comment",
        "error": "error",
        "error_path": "errorPath",
        "state_name": "stateName",
    },
)
class FailProps:
    def __init__(
        self,
        *,
        cause: typing.Optional[builtins.str] = None,
        cause_path: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        error: typing.Optional[builtins.str] = None,
        error_path: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a Fail state.

        :param cause: A description for the cause of the failure. Default: - No description
        :param cause_path: JsonPath expression to select part of the state to be the cause to this state. You can also use an intrinsic function that returns a string to specify this property. The allowed functions include States.Format, States.JsonToString, States.ArrayGetItem, States.Base64Encode, States.Base64Decode, States.Hash, and States.UUID. Default: - No cause path
        :param comment: An optional description for this state. Default: - No comment
        :param error: Error code used to represent this failure. Default: - No error code
        :param error_path: JsonPath expression to select part of the state to be the error to this state. You can also use an intrinsic function that returns a string to specify this property. The allowed functions include States.Format, States.JsonToString, States.ArrayGetItem, States.Base64Encode, States.Base64Decode, States.Hash, and States.UUID. Default: - No error path
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name

        :exampleMetadata: infused

        Example::

            fail = sfn.Fail(self, "Fail",
                error_path=sfn.JsonPath.format("error: {}.", sfn.JsonPath.string_at("$.someError")),
                cause_path="States.Format('cause: {}.', $.someCause)"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e34991edae92aa24b2bb75c9df693e2185f13c40aaf16ee220fc07ef991eaa7c)
            check_type(argname="argument cause", value=cause, expected_type=type_hints["cause"])
            check_type(argname="argument cause_path", value=cause_path, expected_type=type_hints["cause_path"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument error", value=error, expected_type=type_hints["error"])
            check_type(argname="argument error_path", value=error_path, expected_type=type_hints["error_path"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cause is not None:
            self._values["cause"] = cause
        if cause_path is not None:
            self._values["cause_path"] = cause_path
        if comment is not None:
            self._values["comment"] = comment
        if error is not None:
            self._values["error"] = error
        if error_path is not None:
            self._values["error_path"] = error_path
        if state_name is not None:
            self._values["state_name"] = state_name

    @builtins.property
    def cause(self) -> typing.Optional[builtins.str]:
        '''A description for the cause of the failure.

        :default: - No description
        '''
        result = self._values.get("cause")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cause_path(self) -> typing.Optional[builtins.str]:
        '''JsonPath expression to select part of the state to be the cause to this state.

        You can also use an intrinsic function that returns a string to specify this property.
        The allowed functions include States.Format, States.JsonToString, States.ArrayGetItem, States.Base64Encode, States.Base64Decode, States.Hash, and States.UUID.

        :default: - No cause path
        '''
        result = self._values.get("cause_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error(self) -> typing.Optional[builtins.str]:
        '''Error code used to represent this failure.

        :default: - No error code
        '''
        result = self._values.get("error")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_path(self) -> typing.Optional[builtins.str]:
        '''JsonPath expression to select part of the state to be the error to this state.

        You can also use an intrinsic function that returns a string to specify this property.
        The allowed functions include States.Format, States.JsonToString, States.ArrayGetItem, States.Base64Encode, States.Base64Decode, States.Hash, and States.UUID.

        :default: - No error path
        '''
        result = self._values.get("error_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FailProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FieldUtils(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.FieldUtils",
):
    '''Helper functions to work with structures containing fields.'''

    @jsii.member(jsii_name="containsTaskToken")
    @builtins.classmethod
    def contains_task_token(
        cls,
        obj: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> builtins.bool:
        '''Returns whether the given task structure contains the TaskToken field anywhere.

        The field is considered included if the field itself or one of its containing
        fields occurs anywhere in the payload.

        :param obj: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66d8682b1b0f9fb3dcb908bf3abca8eac95fe74d771082e1734661a049f7b124)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "containsTaskToken", [obj]))

    @jsii.member(jsii_name="findReferencedPaths")
    @builtins.classmethod
    def find_referenced_paths(
        cls,
        obj: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> typing.List[builtins.str]:
        '''Return all JSON paths used in the given structure.

        :param obj: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c06b5d6a012a295ccc553ab17a70060cd3e1e30e5c31aa452a942673082b25ee)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "findReferencedPaths", [obj]))

    @jsii.member(jsii_name="renderObject")
    @builtins.classmethod
    def render_object(
        cls,
        obj: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Render a JSON structure containing fields to the right StepFunctions structure.

        :param obj: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d3d657b8055d48ebc198eb4602747aafd8a12d895196df4b25610da111bc38b)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.sinvoke(cls, "renderObject", [obj]))


class FileDefinitionBody(
    DefinitionBody,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.FileDefinitionBody",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # chainable: stepfunctions.IChainable
        
        file_definition_body = stepfunctions.FileDefinitionBody.from_chainable(chainable)
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
        :param path: -
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
            type_hints = typing.get_type_hints(_typecheckingstub__526ef9213812e76ec99bd530d4fbea7cc137d220b92525fe763d6d315362734f)
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
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        _sfn_principal: _IPrincipal_539bb2fd,
        _sfn_props: typing.Union["StateMachineProps", typing.Dict[builtins.str, typing.Any]],
        _graph: typing.Optional["StateGraph"] = None,
    ) -> DefinitionConfig:
        '''
        :param scope: -
        :param _sfn_principal: -
        :param _sfn_props: -
        :param _graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__552303f8ba754bf57e2991b15cb67699f0b3be1720aaa2082c7f9e7c858151e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument _sfn_principal", value=_sfn_principal, expected_type=type_hints["_sfn_principal"])
            check_type(argname="argument _sfn_props", value=_sfn_props, expected_type=type_hints["_sfn_props"])
            check_type(argname="argument _graph", value=_graph, expected_type=type_hints["_graph"])
        return typing.cast(DefinitionConfig, jsii.invoke(self, "bind", [scope, _sfn_principal, _sfn_props, _graph]))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.FindStateOptions",
    jsii_struct_bases=[],
    name_mapping={"include_error_handlers": "includeErrorHandlers"},
)
class FindStateOptions:
    def __init__(
        self,
        *,
        include_error_handlers: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for finding reachable states.

        :param include_error_handlers: Whether or not to follow error-handling transitions. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            find_state_options = stepfunctions.FindStateOptions(
                include_error_handlers=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ff50e720afaefc7918f464dff492d9f8f0c7249476cc81f87395388b3a9c7e2)
            check_type(argname="argument include_error_handlers", value=include_error_handlers, expected_type=type_hints["include_error_handlers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if include_error_handlers is not None:
            self._values["include_error_handlers"] = include_error_handlers

    @builtins.property
    def include_error_handlers(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to follow error-handling transitions.

        :default: false
        '''
        result = self._values.get("include_error_handlers")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FindStateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_stepfunctions.IActivity")
class IActivity(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a Step Functions Activity https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html.'''

    @builtins.property
    @jsii.member(jsii_name="activityArn")
    def activity_arn(self) -> builtins.str:
        '''The ARN of the activity.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="activityName")
    def activity_name(self) -> builtins.str:
        '''The name of the activity.

        :attribute: true
        '''
        ...


class _IActivityProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a Step Functions Activity https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_stepfunctions.IActivity"

    @builtins.property
    @jsii.member(jsii_name="activityArn")
    def activity_arn(self) -> builtins.str:
        '''The ARN of the activity.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "activityArn"))

    @builtins.property
    @jsii.member(jsii_name="activityName")
    def activity_name(self) -> builtins.str:
        '''The name of the activity.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "activityName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IActivity).__jsii_proxy_class__ = lambda : _IActivityProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_stepfunctions.IChainable")
class IChainable(typing_extensions.Protocol):
    '''Interface for objects that can be used in a Chain.'''

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        '''The chainable end state(s) of this chainable.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Descriptive identifier for this chainable.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        '''The start state of this chainable.'''
        ...


class _IChainableProxy:
    '''Interface for objects that can be used in a Chain.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_stepfunctions.IChainable"

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List["INextable"]:
        '''The chainable end state(s) of this chainable.'''
        return typing.cast(typing.List["INextable"], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Descriptive identifier for this chainable.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        '''The start state of this chainable.'''
        return typing.cast("State", jsii.get(self, "startState"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChainable).__jsii_proxy_class__ = lambda : _IChainableProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_stepfunctions.IItemReader")
class IItemReader(typing_extensions.Protocol):
    '''Base interface for Item Reader configurations.'''

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing objects to iterate over or a file with a list to iterate over.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        '''The Amazon S3 API action that Step Functions must invoke depending on the specified dataset.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="maxItems")
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        ...

    @jsii.member(jsii_name="providePolicyStatements")
    def provide_policy_statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''Compile policy statements to provide relevent permissions to the state machine.'''
        ...

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Render the ItemReader as JSON object.'''
        ...


class _IItemReaderProxy:
    '''Base interface for Item Reader configurations.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_stepfunctions.IItemReader"

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing objects to iterate over or a file with a list to iterate over.'''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        '''The Amazon S3 API action that Step Functions must invoke depending on the specified dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="maxItems")
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxItems"))

    @jsii.member(jsii_name="providePolicyStatements")
    def provide_policy_statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''Compile policy statements to provide relevent permissions to the state machine.'''
        return typing.cast(typing.List[_PolicyStatement_0fe33853], jsii.invoke(self, "providePolicyStatements", []))

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Render the ItemReader as JSON object.'''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IItemReader).__jsii_proxy_class__ = lambda : _IItemReaderProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_stepfunctions.INextable")
class INextable(typing_extensions.Protocol):
    '''Interface for states that can have 'next' states.'''

    @jsii.member(jsii_name="next")
    def next(self, state: IChainable) -> "Chain":
        '''Go to the indicated state after this state.

        :param state: -

        :return: The chain of states built up
        '''
        ...


class _INextableProxy:
    '''Interface for states that can have 'next' states.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_stepfunctions.INextable"

    @jsii.member(jsii_name="next")
    def next(self, state: IChainable) -> "Chain":
        '''Go to the indicated state after this state.

        :param state: -

        :return: The chain of states built up
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dbb71ff45be8e3c94fd024ed10a51f986e7e089ef33bfae17adc18a574bf024)
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        return typing.cast("Chain", jsii.invoke(self, "next", [state]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INextable).__jsii_proxy_class__ = lambda : _INextableProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_stepfunctions.IStateMachine")
class IStateMachine(
    _IResource_c80c4260,
    _IGrantable_71c4f5de,
    typing_extensions.Protocol,
):
    '''A State Machine.'''

    @builtins.property
    @jsii.member(jsii_name="stateMachineArn")
    def state_machine_arn(self) -> builtins.str:
        '''The ARN of the state machine.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        identity: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity custom permissions.

        :param identity: The principal.
        :param actions: The list of desired actions.
        '''
        ...

    @jsii.member(jsii_name="grantExecution")
    def grant_execution(
        self,
        identity: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions for all executions of a state machine.

        :param identity: The principal.
        :param actions: The list of desired actions.
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity read permissions for this state machine.

        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantStartExecution")
    def grant_start_execution(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to start an execution of this state machine.

        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantStartSyncExecution")
    def grant_start_sync_execution(
        self,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to start a synchronous execution of this state machine.

        :param identity: The principal.
        '''
        ...

    @jsii.member(jsii_name="grantTaskResponse")
    def grant_task_response(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity read permissions for this state machine.

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
        '''Return the given named metric for this State Machine's executions.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricAborted")
    def metric_aborted(
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
        '''Metric for the number of executions that were aborted.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(
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
        '''Metric for the number of executions that failed.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricStarted")
    def metric_started(
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
        '''Metric for the number of executions that were started.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricSucceeded")
    def metric_succeeded(
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
        '''Metric for the number of executions that succeeded.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricThrottled")
    def metric_throttled(
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
        '''Metric for the number of executions that were throttled.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricTime")
    def metric_time(
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
        '''Metric for the interval, in milliseconds, between the time the execution starts and the time it closes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricTimedOut")
    def metric_timed_out(
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
        '''Metric for the number of executions that timed out.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        ...


class _IStateMachineProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_IGrantable_71c4f5de), # type: ignore[misc]
):
    '''A State Machine.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_stepfunctions.IStateMachine"

    @builtins.property
    @jsii.member(jsii_name="stateMachineArn")
    def state_machine_arn(self) -> builtins.str:
        '''The ARN of the state machine.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "stateMachineArn"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        identity: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity custom permissions.

        :param identity: The principal.
        :param actions: The list of desired actions.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__330377705d17e346007692578b485457a023c38351a46c6e22975a8a2b8192ae)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [identity, *actions]))

    @jsii.member(jsii_name="grantExecution")
    def grant_execution(
        self,
        identity: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions for all executions of a state machine.

        :param identity: The principal.
        :param actions: The list of desired actions.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31bd3fa2600dc4d3bf5687e9b4e868f708b68f607efbd2cfa7fb5f71fba15756)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantExecution", [identity, *actions]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity read permissions for this state machine.

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67aefd85a78dbc72556e294ed43f407d7fe2e40185f6dcefcda2b91bce4a9e6c)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [identity]))

    @jsii.member(jsii_name="grantStartExecution")
    def grant_start_execution(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to start an execution of this state machine.

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b84edd8c4dd517d793cea8632f963ea68ac72a33187299a17ff7549b1e1dc14d)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantStartExecution", [identity]))

    @jsii.member(jsii_name="grantStartSyncExecution")
    def grant_start_sync_execution(
        self,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to start a synchronous execution of this state machine.

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92ed05a6f0e60c0385d1fe8dff7aa6ee6308b0dbdec64f6f70f98b5d1fdf23ed)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantStartSyncExecution", [identity]))

    @jsii.member(jsii_name="grantTaskResponse")
    def grant_task_response(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity read permissions for this state machine.

        :param identity: The principal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789a3eccb8c002cee01668ce309a302eced31df5999f98457203940330528ab4)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantTaskResponse", [identity]))

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
        '''Return the given named metric for this State Machine's executions.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cab371f4587948afe28a72a9dde908f44a64ec26dee050808f7b1236c4c7da9)
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

    @jsii.member(jsii_name="metricAborted")
    def metric_aborted(
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
        '''Metric for the number of executions that were aborted.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricAborted", [props]))

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(
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
        '''Metric for the number of executions that failed.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFailed", [props]))

    @jsii.member(jsii_name="metricStarted")
    def metric_started(
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
        '''Metric for the number of executions that were started.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricStarted", [props]))

    @jsii.member(jsii_name="metricSucceeded")
    def metric_succeeded(
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
        '''Metric for the number of executions that succeeded.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSucceeded", [props]))

    @jsii.member(jsii_name="metricThrottled")
    def metric_throttled(
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
        '''Metric for the number of executions that were throttled.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricThrottled", [props]))

    @jsii.member(jsii_name="metricTime")
    def metric_time(
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
        '''Metric for the interval, in milliseconds, between the time the execution starts and the time it closes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTime", [props]))

    @jsii.member(jsii_name="metricTimedOut")
    def metric_timed_out(
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
        '''Metric for the number of executions that timed out.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTimedOut", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStateMachine).__jsii_proxy_class__ = lambda : _IStateMachineProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.InputType")
class InputType(enum.Enum):
    '''The type of task input.'''

    TEXT = "TEXT"
    '''Use a literal string This might be a JSON-encoded object, or just text.

    valid JSON text: standalone, quote-delimited strings; objects; arrays; numbers; Boolean values; and null.

    example: ``literal string``
    example: {"json": "encoded"}
    '''
    OBJECT = "OBJECT"
    '''Use an object which may contain Data and Context fields as object values, if desired.

    example:
    {
    literal: 'literal',
    SomeInput: sfn.JsonPath.stringAt('$.someField')
    }

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-contextobject.html
    '''


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.IntegrationPattern")
class IntegrationPattern(enum.Enum):
    '''AWS Step Functions integrates with services directly in the Amazon States Language.

    You can control these AWS services using service integration patterns:

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_codebuild as codebuild
        
        
        project = codebuild.Project(self, "Project",
            project_name="MyTestProject",
            build_spec=codebuild.BuildSpec.from_object_to_yaml({
                "version": 0.2,
                "batch": {
                    "build-list": [{
                        "identifier": "id",
                        "buildspec": "version: 0.2\nphases:\n  build:\n    commands:\n      - echo \"Hello, from small!\""
                    }
                    ]
                }
            })
        )
        project.enable_batch_builds()
        
        task = tasks.CodeBuildStartBuildBatch(self, "buildBatchTask",
            project=project,
            integration_pattern=sfn.IntegrationPattern.REQUEST_RESPONSE,
            environment_variables_override={
                "test": codebuild.BuildEnvironmentVariable(
                    type=codebuild.BuildEnvironmentVariableType.PLAINTEXT,
                    value="testValue"
                )
            }
        )
    '''

    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    '''Step Functions will wait for an HTTP response and then progress to the next state.

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-default
    '''
    RUN_JOB = "RUN_JOB"
    '''Step Functions can wait for a request to complete before progressing to the next state.

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync
    '''
    WAIT_FOR_TASK_TOKEN = "WAIT_FOR_TASK_TOKEN"
    '''Callback tasks provide a way to pause a workflow until a task token is returned.

    You must set a task token when using the callback pattern

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token
    '''


class ItemBatcher(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.ItemBatcher",
):
    '''Configuration for processing a group of items in a single child workflow execution.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # batch_input: Any
        
        item_batcher = stepfunctions.ItemBatcher(
            batch_input=batch_input,
            max_input_bytes_per_batch=123,
            max_input_bytes_per_batch_path="maxInputBytesPerBatchPath",
            max_items_per_batch=123,
            max_items_per_batch_path="maxItemsPerBatchPath"
        )
    '''

    def __init__(
        self,
        *,
        batch_input: typing.Optional[typing.Mapping[typing.Any, typing.Any]] = None,
        max_input_bytes_per_batch: typing.Optional[jsii.Number] = None,
        max_input_bytes_per_batch_path: typing.Optional[builtins.str] = None,
        max_items_per_batch: typing.Optional[jsii.Number] = None,
        max_items_per_batch_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param batch_input: BatchInput. Fixed JSON input to include in each batch passed to each child workflow execution Default: - No batchInput
        :param max_input_bytes_per_batch: MaxInputBytesPerBatch. Specifies the maximum number of bytes that each child workflow execution processes, as static number Default: - uses value of ``maxInputBytesPerBatchPath`` as the max size per batch, no limits on the batch size under the 256KB limit if that property was also not provided
        :param max_input_bytes_per_batch_path: MaxInputBytesPerBatchPath. Specifies the maximum number of bytes that each child workflow execution processes, as JsonPath Default: - uses value of ``maxInputBytesPerBatch`` as the max size per batch, no limits on the batch size under the 256KB limit if that property was also not provided
        :param max_items_per_batch: MaxItemsPerBatch. Specifies the maximum number of items that each child workflow execution processes, as static number Default: - uses value of ``maxItemsPerBatchPath`` as the max items per batch, no limits on the number of items in a batch under the 256KB limit if that property was also not provided
        :param max_items_per_batch_path: MaxItemsPerBatchPath. Specifies the maximum number of items that each child workflow execution processes, as JsonPath Default: - uses value of ``maxItemsPerBatch`` as the max items per batch, no limits on the number of items in a batch under the 256KB limit if that property was also not provided
        '''
        props = ItemBatcherProps(
            batch_input=batch_input,
            max_input_bytes_per_batch=max_input_bytes_per_batch,
            max_input_bytes_per_batch_path=max_input_bytes_per_batch_path,
            max_items_per_batch=max_items_per_batch,
            max_items_per_batch_path=max_items_per_batch_path,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Render ItemBatcher in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @jsii.member(jsii_name="validateItemBatcher")
    def validate_item_batcher(self) -> typing.List[builtins.str]:
        '''Validate this ItemBatcher.'''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateItemBatcher", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.ItemBatcherProps",
    jsii_struct_bases=[],
    name_mapping={
        "batch_input": "batchInput",
        "max_input_bytes_per_batch": "maxInputBytesPerBatch",
        "max_input_bytes_per_batch_path": "maxInputBytesPerBatchPath",
        "max_items_per_batch": "maxItemsPerBatch",
        "max_items_per_batch_path": "maxItemsPerBatchPath",
    },
)
class ItemBatcherProps:
    def __init__(
        self,
        *,
        batch_input: typing.Optional[typing.Mapping[typing.Any, typing.Any]] = None,
        max_input_bytes_per_batch: typing.Optional[jsii.Number] = None,
        max_input_bytes_per_batch_path: typing.Optional[builtins.str] = None,
        max_items_per_batch: typing.Optional[jsii.Number] = None,
        max_items_per_batch_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Interface for ItemBatcher configuration properties.

        :param batch_input: BatchInput. Fixed JSON input to include in each batch passed to each child workflow execution Default: - No batchInput
        :param max_input_bytes_per_batch: MaxInputBytesPerBatch. Specifies the maximum number of bytes that each child workflow execution processes, as static number Default: - uses value of ``maxInputBytesPerBatchPath`` as the max size per batch, no limits on the batch size under the 256KB limit if that property was also not provided
        :param max_input_bytes_per_batch_path: MaxInputBytesPerBatchPath. Specifies the maximum number of bytes that each child workflow execution processes, as JsonPath Default: - uses value of ``maxInputBytesPerBatch`` as the max size per batch, no limits on the batch size under the 256KB limit if that property was also not provided
        :param max_items_per_batch: MaxItemsPerBatch. Specifies the maximum number of items that each child workflow execution processes, as static number Default: - uses value of ``maxItemsPerBatchPath`` as the max items per batch, no limits on the number of items in a batch under the 256KB limit if that property was also not provided
        :param max_items_per_batch_path: MaxItemsPerBatchPath. Specifies the maximum number of items that each child workflow execution processes, as JsonPath Default: - uses value of ``maxItemsPerBatch`` as the max items per batch, no limits on the number of items in a batch under the 256KB limit if that property was also not provided

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # batch_input: Any
            
            item_batcher_props = stepfunctions.ItemBatcherProps(
                batch_input=batch_input,
                max_input_bytes_per_batch=123,
                max_input_bytes_per_batch_path="maxInputBytesPerBatchPath",
                max_items_per_batch=123,
                max_items_per_batch_path="maxItemsPerBatchPath"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28b90617c58a85778754752511df05551643031e0ec1d9e5687a61beda24688f)
            check_type(argname="argument batch_input", value=batch_input, expected_type=type_hints["batch_input"])
            check_type(argname="argument max_input_bytes_per_batch", value=max_input_bytes_per_batch, expected_type=type_hints["max_input_bytes_per_batch"])
            check_type(argname="argument max_input_bytes_per_batch_path", value=max_input_bytes_per_batch_path, expected_type=type_hints["max_input_bytes_per_batch_path"])
            check_type(argname="argument max_items_per_batch", value=max_items_per_batch, expected_type=type_hints["max_items_per_batch"])
            check_type(argname="argument max_items_per_batch_path", value=max_items_per_batch_path, expected_type=type_hints["max_items_per_batch_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if batch_input is not None:
            self._values["batch_input"] = batch_input
        if max_input_bytes_per_batch is not None:
            self._values["max_input_bytes_per_batch"] = max_input_bytes_per_batch
        if max_input_bytes_per_batch_path is not None:
            self._values["max_input_bytes_per_batch_path"] = max_input_bytes_per_batch_path
        if max_items_per_batch is not None:
            self._values["max_items_per_batch"] = max_items_per_batch
        if max_items_per_batch_path is not None:
            self._values["max_items_per_batch_path"] = max_items_per_batch_path

    @builtins.property
    def batch_input(self) -> typing.Optional[typing.Mapping[typing.Any, typing.Any]]:
        '''BatchInput.

        Fixed JSON input to include in each batch passed to each child workflow execution

        :default: - No batchInput
        '''
        result = self._values.get("batch_input")
        return typing.cast(typing.Optional[typing.Mapping[typing.Any, typing.Any]], result)

    @builtins.property
    def max_input_bytes_per_batch(self) -> typing.Optional[jsii.Number]:
        '''MaxInputBytesPerBatch.

        Specifies the maximum number of bytes that each child workflow execution processes, as static number

        :default:

        - uses value of ``maxInputBytesPerBatchPath`` as the max size per batch,
        no limits on the batch size under the 256KB limit if that property was also not provided
        '''
        result = self._values.get("max_input_bytes_per_batch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_input_bytes_per_batch_path(self) -> typing.Optional[builtins.str]:
        '''MaxInputBytesPerBatchPath.

        Specifies the maximum number of bytes that each child workflow execution processes, as JsonPath

        :default:

        - uses value of ``maxInputBytesPerBatch`` as the max size per batch,
        no limits on the batch size under the 256KB limit if that property was also not provided
        '''
        result = self._values.get("max_input_bytes_per_batch_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_items_per_batch(self) -> typing.Optional[jsii.Number]:
        '''MaxItemsPerBatch.

        Specifies the maximum number of items that each child workflow execution processes, as static number

        :default:

        - uses value of ``maxItemsPerBatchPath`` as the max items per batch,
        no limits on the number of items in a batch under the 256KB limit if that property was also not provided
        '''
        result = self._values.get("max_items_per_batch")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_items_per_batch_path(self) -> typing.Optional[builtins.str]:
        '''MaxItemsPerBatchPath.

        Specifies the maximum number of items that each child workflow execution processes, as JsonPath

        :default:

        - uses value of ``maxItemsPerBatch`` as the max items per batch,
        no limits on the number of items in a batch under the 256KB limit if that property was also not provided
        '''
        result = self._values.get("max_items_per_batch_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ItemBatcherProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.ItemReaderProps",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "max_items": "maxItems"},
)
class ItemReaderProps:
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        max_items: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Base interface for Item Reader configuration properties.

        :param bucket: S3 Bucket containing objects to iterate over or a file with a list to iterate over.
        :param max_items: Limits the number of items passed to the Distributed Map state. Default: - Distributed Map state will iterate over all items provided by the ItemReader

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3 as s3
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # bucket: s3.Bucket
            
            item_reader_props = stepfunctions.ItemReaderProps(
                bucket=bucket,
            
                # the properties below are optional
                max_items=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8df53cde2f82ea6228f0c9a5a5ba0a4dd36c18fba9835f9f3150547f7cee754)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument max_items", value=max_items, expected_type=type_hints["max_items"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if max_items is not None:
            self._values["max_items"] = max_items

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing objects to iterate over or a file with a list to iterate over.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        result = self._values.get("max_items")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ItemReaderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.JitterType")
class JitterType(enum.Enum):
    '''Values allowed in the retrier JitterStrategy field.

    :exampleMetadata: infused

    Example::

        parallel = sfn.Parallel(self, "Do the work in parallel")
        
        # Add branches to be executed in parallel
        ship_item = sfn.Pass(self, "ShipItem")
        send_invoice = sfn.Pass(self, "SendInvoice")
        restock = sfn.Pass(self, "Restock")
        parallel.branch(ship_item)
        parallel.branch(send_invoice)
        parallel.branch(restock)
        
        # Retry the whole workflow if something goes wrong with exponential backoff
        parallel.add_retry(
            max_attempts=1,
            max_delay=Duration.seconds(5),
            jitter_strategy=sfn.JitterType.FULL
        )
        
        # How to recover from errors
        send_failure_notification = sfn.Pass(self, "SendFailureNotification")
        parallel.add_catch(send_failure_notification)
        
        # What to do in case everything succeeded
        close_order = sfn.Pass(self, "CloseOrder")
        parallel.next(close_order)
    '''

    FULL = "FULL"
    '''Calculates the delay to be a random number between 0 and the computed backoff for the given retry attempt count.'''
    NONE = "NONE"
    '''Calculates the delay to be the computed backoff for the given retry attempt count (equivalent to if Jitter was not declared - i.e. the default value).'''


class JsonPath(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.JsonPath",
):
    '''Extract a field from the State Machine data or context that gets passed around between states.

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-paths.html
    :exampleMetadata: infused

    Example::

        submit_job_activity = sfn.Activity(self, "SubmitJob")
        
        tasks.StepFunctionsInvokeActivity(self, "Submit Job",
            activity=submit_job_activity,
            parameters={
                "comment": "Selecting what I care about.",
                "MyDetails": {
                    "size": sfn.JsonPath.string_at("$.product.details.size"),
                    "exists": sfn.JsonPath.string_at("$.product.availability"),
                    "StaticValue": "foo"
                }
            }
        )
    '''

    @jsii.member(jsii_name="array")
    @builtins.classmethod
    def array(cls, *values: builtins.str) -> builtins.str:
        '''Make an intrinsic States.Array expression.

        Combine any number of string literals or JsonPath expressions into an array.

        Use this function if the value of an array element directly has to come
        from a JSON Path expression (either the State object or the Context object).

        If the array contains object literals whose values come from a JSON path
        expression, you do not need to use this function.

        :param values: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f608b3fd4b201a0a1482b5f0a70098cf3a3bd7d163d2b909a61815f6ff4a6737)
            check_type(argname="argument values", value=values, expected_type=typing.Tuple[type_hints["values"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(builtins.str, jsii.sinvoke(cls, "array", [*values]))

    @jsii.member(jsii_name="arrayContains")
    @builtins.classmethod
    def array_contains(cls, array: typing.Any, value: typing.Any) -> builtins.str:
        '''Make an intrinsic States.ArrayContains expression.

        Use this function to determine if a specific value is present in an array. For example, you can use this function to detect if there was an error in a Map state iteration.

        :param array: -
        :param value: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088de6efa9a8b3d08870747fd80f1047204d1f99fcd9d2020876d01e904b961c)
            check_type(argname="argument array", value=array, expected_type=type_hints["array"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arrayContains", [array, value]))

    @jsii.member(jsii_name="arrayGetItem")
    @builtins.classmethod
    def array_get_item(cls, array: typing.Any, index: jsii.Number) -> builtins.str:
        '''Make an intrinsic States.ArrayGetItem expression.

        Use this function to get a specified index's value in an array.

        :param array: -
        :param index: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b6413ab81aefe0cb4d39cdffb2973b82823f6583665642e33f7d2e736ed49b5)
            check_type(argname="argument array", value=array, expected_type=type_hints["array"])
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arrayGetItem", [array, index]))

    @jsii.member(jsii_name="arrayLength")
    @builtins.classmethod
    def array_length(cls, array: typing.Any) -> builtins.str:
        '''Make an intrinsic States.ArrayLength expression.

        Use this function to get the length of an array.

        :param array: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__066df6cc20da873d2b1d90282c5ae886a4849b38a02d69dc36feae9c5490efe1)
            check_type(argname="argument array", value=array, expected_type=type_hints["array"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arrayLength", [array]))

    @jsii.member(jsii_name="arrayPartition")
    @builtins.classmethod
    def array_partition(
        cls,
        array: typing.Any,
        chunk_size: jsii.Number,
    ) -> builtins.str:
        '''Make an intrinsic States.ArrayPartition expression.

        Use this function to partition a large array. You can also use this intrinsic to slice the data and then send the payload in smaller chunks.

        :param array: -
        :param chunk_size: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc77862b0de7c7c02295791475860476ecdd7e6e12d7c6bba98efbeb931e86e1)
            check_type(argname="argument array", value=array, expected_type=type_hints["array"])
            check_type(argname="argument chunk_size", value=chunk_size, expected_type=type_hints["chunk_size"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arrayPartition", [array, chunk_size]))

    @jsii.member(jsii_name="arrayRange")
    @builtins.classmethod
    def array_range(
        cls,
        start: jsii.Number,
        end: jsii.Number,
        step: jsii.Number,
    ) -> builtins.str:
        '''Make an intrinsic States.ArrayRange expression.

        Use this function to create a new array containing a specific range of elements. The new array can contain up to 1000 elements.

        :param start: -
        :param end: -
        :param step: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66dc96e3ef5fe23ddc3268294a3758d98b1d5702ff86e2397d4b92453e45945c)
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument step", value=step, expected_type=type_hints["step"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arrayRange", [start, end, step]))

    @jsii.member(jsii_name="arrayUnique")
    @builtins.classmethod
    def array_unique(cls, array: typing.Any) -> builtins.str:
        '''Make an intrinsic States.ArrayUnique expression.

        Use this function to get the length of an array.
        Use this function to remove duplicate values from an array and returns an array containing only unique elements. This function takes an array, which can be unsorted, as its sole argument.

        :param array: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f7421e7bfe112627dadb759031678f094b4a6dc3c7ffb052c42413214015be)
            check_type(argname="argument array", value=array, expected_type=type_hints["array"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arrayUnique", [array]))

    @jsii.member(jsii_name="base64Decode")
    @builtins.classmethod
    def base64_decode(cls, base64: builtins.str) -> builtins.str:
        '''Make an intrinsic States.Base64Decode expression.

        Use this function to decode data based on MIME Base64 decoding scheme. You can use this function to pass data to other AWS services without using a Lambda function.

        :param base64: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e71d2c009521adfc2f539cfa65b95ae6f95e8c5f294620fc0b60c41a3234d22a)
            check_type(argname="argument base64", value=base64, expected_type=type_hints["base64"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "base64Decode", [base64]))

    @jsii.member(jsii_name="base64Encode")
    @builtins.classmethod
    def base64_encode(cls, input: builtins.str) -> builtins.str:
        '''Make an intrinsic States.Base64Encode expression.

        Use this function to encode data based on MIME Base64 encoding scheme. You can use this function to pass data to other AWS services without using an AWS Lambda function.

        :param input: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa34b328214814976f329340e3b2ff58e0c4bfec265b32b49a35f48c4428a7b0)
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "base64Encode", [input]))

    @jsii.member(jsii_name="format")
    @builtins.classmethod
    def format(cls, format_string: builtins.str, *values: builtins.str) -> builtins.str:
        '''Make an intrinsic States.Format expression.

        This can be used to embed JSON Path variables inside a format string.

        For example::

           sfn.JsonPath.format("Hello, my name is {}.", sfn.JsonPath.string_at("$.name"))

        :param format_string: -
        :param values: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a65ae0ed7034cb9b7372f57ae44f6a74ad07f3a7e0613da2f76f53c592a3df50)
            check_type(argname="argument format_string", value=format_string, expected_type=type_hints["format_string"])
            check_type(argname="argument values", value=values, expected_type=typing.Tuple[type_hints["values"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(builtins.str, jsii.sinvoke(cls, "format", [format_string, *values]))

    @jsii.member(jsii_name="hash")
    @builtins.classmethod
    def hash(cls, data: typing.Any, algorithm: builtins.str) -> builtins.str:
        '''Make an intrinsic States.Hash expression.

        Use this function to calculate the hash value of a given input. You can use this function to pass data to other AWS services without using a Lambda function.

        :param data: -
        :param algorithm: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5172eedb2a8508c195d9860a659889436742614328a885cc829ec82bbb6edab0)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "hash", [data, algorithm]))

    @jsii.member(jsii_name="isEncodedJsonPath")
    @builtins.classmethod
    def is_encoded_json_path(cls, value: builtins.str) -> builtins.bool:
        '''Determines if the indicated string is an encoded JSON path.

        :param value: string to be evaluated.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf495c28eeb68a82510bf46f764aafbb98e9152a5a58c61ac08b70497e448fc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isEncodedJsonPath", [value]))

    @jsii.member(jsii_name="jsonMerge")
    @builtins.classmethod
    def json_merge(cls, value1: typing.Any, value2: typing.Any) -> builtins.str:
        '''Make an intrinsic States.JsonMerge expression.

        Use this function to merge two JSON objects into a single object.

        :param value1: -
        :param value2: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e03a4f189712c0723816ff3f337f7563d3175582971c8fba095186f3644a1832)
            check_type(argname="argument value1", value=value1, expected_type=type_hints["value1"])
            check_type(argname="argument value2", value=value2, expected_type=type_hints["value2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "jsonMerge", [value1, value2]))

    @jsii.member(jsii_name="jsonToString")
    @builtins.classmethod
    def json_to_string(cls, value: typing.Any) -> builtins.str:
        '''Make an intrinsic States.JsonToString expression.

        During the execution of the Step Functions state machine, encode the
        given object into a JSON string.

        For example::

           sfn.JsonPath.json_to_string(sfn.JsonPath.object_at("$.someObject"))

        :param value: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6436aab05f387323f9cb74a6b784dd4c768239125631c909c725501e7bf7fd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "jsonToString", [value]))

    @jsii.member(jsii_name="listAt")
    @builtins.classmethod
    def list_at(cls, path: builtins.str) -> typing.List[builtins.str]:
        '''Instead of using a literal string list, get the value from a JSON path.

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__791d54d72cca605dac6e53897a875a0836bef45df8935a30c09d1adb81bce886)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "listAt", [path]))

    @jsii.member(jsii_name="mathAdd")
    @builtins.classmethod
    def math_add(cls, num1: jsii.Number, num2: jsii.Number) -> builtins.str:
        '''Make an intrinsic States.MathAdd expression.

        Use this function to return the sum of two numbers. For example, you can use this function to increment values inside a loop without invoking a Lambda function.

        :param num1: -
        :param num2: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de44de70b3f9d451f756efc0fe38516dbc6d81f7af66a3acd65cacf20d4e0224)
            check_type(argname="argument num1", value=num1, expected_type=type_hints["num1"])
            check_type(argname="argument num2", value=num2, expected_type=type_hints["num2"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "mathAdd", [num1, num2]))

    @jsii.member(jsii_name="mathRandom")
    @builtins.classmethod
    def math_random(cls, start: jsii.Number, end: jsii.Number) -> builtins.str:
        '''Make an intrinsic States.MathRandom expression.

        Use this function to return a random number between the specified start and end number. For example, you can use this function to distribute a specific task between two or more resources.

        :param start: -
        :param end: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d94e6703ef6e05edfee1f44b8f0522b8c9af9b8b61a177fe7416fbde4c0a9385)
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "mathRandom", [start, end]))

    @jsii.member(jsii_name="numberAt")
    @builtins.classmethod
    def number_at(cls, path: builtins.str) -> jsii.Number:
        '''Instead of using a literal number, get the value from a JSON path.

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff382ceecb543f17e967c677aca2b4a8ce5745808e77f81d86c5f16e859b6888)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "numberAt", [path]))

    @jsii.member(jsii_name="objectAt")
    @builtins.classmethod
    def object_at(cls, path: builtins.str) -> _IResolvable_da3f097b:
        '''Reference a complete (complex) object in a JSON path location.

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7664cbc5a31ad0f20576e6a4f0186b6bc4c3f582ca1f2a5e05e6947613b85107)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(_IResolvable_da3f097b, jsii.sinvoke(cls, "objectAt", [path]))

    @jsii.member(jsii_name="stringAt")
    @builtins.classmethod
    def string_at(cls, path: builtins.str) -> builtins.str:
        '''Instead of using a literal string, get the value from a JSON path.

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72ee75a1ba7f71927b8abcece4a47abab805af4517b1944222291ca6751c1d17)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "stringAt", [path]))

    @jsii.member(jsii_name="stringSplit")
    @builtins.classmethod
    def string_split(
        cls,
        input_string: builtins.str,
        splitter: builtins.str,
    ) -> builtins.str:
        '''Make an intrinsic States.StringSplit expression.

        Use this function to split a string into an array of values. This function takes two arguments.The first argument is a string and the second argument is the delimiting character that the function will use to divide the string.

        :param input_string: -
        :param splitter: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41f25b1cfc6bdbcf6a60207ed8a5687faef8e1cf0a749fc6aed7aa5a806f40e4)
            check_type(argname="argument input_string", value=input_string, expected_type=type_hints["input_string"])
            check_type(argname="argument splitter", value=splitter, expected_type=type_hints["splitter"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "stringSplit", [input_string, splitter]))

    @jsii.member(jsii_name="stringToJson")
    @builtins.classmethod
    def string_to_json(cls, json_string: builtins.str) -> _IResolvable_da3f097b:
        '''Make an intrinsic States.StringToJson expression.

        During the execution of the Step Functions state machine, parse the given
        argument as JSON into its object form.

        For example::

           sfn.JsonPath.string_to_json(sfn.JsonPath.string_at("$.someJsonBody"))

        :param json_string: -

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad3c4072377fc7d5595082ca2f09f08e9f4d6f6919262abf3916a57efba60e27)
            check_type(argname="argument json_string", value=json_string, expected_type=type_hints["json_string"])
        return typing.cast(_IResolvable_da3f097b, jsii.sinvoke(cls, "stringToJson", [json_string]))

    @jsii.member(jsii_name="uuid")
    @builtins.classmethod
    def uuid(cls) -> builtins.str:
        '''Make an intrinsic States.UUID expression.

        Use this function to return a version 4 universally unique identifier (v4 UUID) generated using random numbers. For example, you can use this function to call other AWS services or resources that need a UUID parameter or insert items in a DynamoDB table.

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-intrinsic-functions.html
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "uuid", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DISCARD")
    def DISCARD(cls) -> builtins.str:
        '''Special string value to discard state input, output or result.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DISCARD"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="entireContext")
    def entire_context(cls) -> builtins.str:
        '''Use the entire context data structure.

        Will be an object at invocation time, but is represented in the CDK
        application as a string.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "entireContext"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="entirePayload")
    def entire_payload(cls) -> builtins.str:
        '''Use the entire data structure.

        Will be an object at invocation time, but is represented in the CDK
        application as a string.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "entirePayload"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="executionId")
    def execution_id(cls) -> builtins.str:
        '''Return the Execution Id field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "executionId"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="executionInput")
    def execution_input(cls) -> builtins.str:
        '''Return the Execution Input field from the context object.

        - Will be an object at invocation time, but is represented in the CDK
          application as a string.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "executionInput"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="executionName")
    def execution_name(cls) -> builtins.str:
        '''Return the Execution Name field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "executionName"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(cls) -> builtins.str:
        '''Return the Execution RoleArn field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "executionRoleArn"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="executionStartTime")
    def execution_start_time(cls) -> builtins.str:
        '''Return the Execution StartTime field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "executionStartTime"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="stateEnteredTime")
    def state_entered_time(cls) -> builtins.str:
        '''Return the State EnteredTime field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "stateEnteredTime"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="stateMachineId")
    def state_machine_id(cls) -> builtins.str:
        '''Return the StateMachine Id field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "stateMachineId"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="stateMachineName")
    def state_machine_name(cls) -> builtins.str:
        '''Return the StateMachine Name field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "stateMachineName"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="stateName")
    def state_name(cls) -> builtins.str:
        '''Return the State Name field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "stateName"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="stateRetryCount")
    def state_retry_count(cls) -> builtins.str:
        '''Return the State RetryCount field from the context object.'''
        return typing.cast(builtins.str, jsii.sget(cls, "stateRetryCount"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="taskToken")
    def task_token(cls) -> builtins.str:
        '''Return the Task Token field from the context object.

        External actions will need this token to report step completion
        back to StepFunctions using the ``SendTaskSuccess`` or ``SendTaskFailure``
        calls.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "taskToken"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.LogLevel")
class LogLevel(enum.Enum):
    '''Defines which category of execution history events are logged.

    :default: ERROR

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        
        
        log_group = logs.LogGroup(self, "MyLogGroup")
        
        definition = sfn.Chain.start(sfn.Pass(self, "Pass"))
        
        sfn.StateMachine(self, "MyStateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(definition),
            logs=sfn.LogOptions(
                destination=log_group,
                level=sfn.LogLevel.ALL
            )
        )
    '''

    OFF = "OFF"
    '''No Logging.'''
    ALL = "ALL"
    '''Log everything.'''
    ERROR = "ERROR"
    '''Log all errors.'''
    FATAL = "FATAL"
    '''Log fatal errors.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.LogOptions",
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
        destination: _ILogGroup_3c4fa718,
        include_execution_data: typing.Optional[builtins.bool] = None,
        level: typing.Optional[LogLevel] = None,
    ) -> None:
        '''Defines what execution history events are logged and where they are logged.

        :param destination: The log group where the execution history events will be logged.
        :param include_execution_data: Determines whether execution data is included in your log. Default: false
        :param level: Defines which category of execution history events are logged. Default: ERROR

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_logs as logs
            
            
            log_group = logs.LogGroup(self, "MyLogGroup")
            
            definition = sfn.Chain.start(sfn.Pass(self, "Pass"))
            
            sfn.StateMachine(self, "MyStateMachine",
                definition_body=sfn.DefinitionBody.from_chainable(definition),
                logs=sfn.LogOptions(
                    destination=log_group,
                    level=sfn.LogLevel.ALL
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b27a348000a6495796817f9fd3b73934a015750ac2d2e09e165c45b4d2d5772)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument include_execution_data", value=include_execution_data, expected_type=type_hints["include_execution_data"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }
        if include_execution_data is not None:
            self._values["include_execution_data"] = include_execution_data
        if level is not None:
            self._values["level"] = level

    @builtins.property
    def destination(self) -> _ILogGroup_3c4fa718:
        '''The log group where the execution history events will be logged.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(_ILogGroup_3c4fa718, result)

    @builtins.property
    def include_execution_data(self) -> typing.Optional[builtins.bool]:
        '''Determines whether execution data is included in your log.

        :default: false
        '''
        result = self._values.get("include_execution_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def level(self) -> typing.Optional[LogLevel]:
        '''Defines which category of execution history events are logged.

        :default: ERROR
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[LogLevel], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.MapBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "item_selector": "itemSelector",
        "items_path": "itemsPath",
        "max_concurrency": "maxConcurrency",
        "max_concurrency_path": "maxConcurrencyPath",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "state_name": "stateName",
    },
)
class MapBaseProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        items_path: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_concurrency_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a Map state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param item_selector: The JSON that you want to override your default iteration input (mutually exclusive with ``parameters``). Default: $
        :param items_path: JSONPath expression to select the array to iterate over. Default: $
        :param max_concurrency: MaxConcurrency. An upper bound on the number of iterations you want running at once. Default: - full concurrency
        :param max_concurrency_path: MaxConcurrencyPath. A JsonPath that specifies the maximum concurrency dynamically from the state input. Default: - full concurrency
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # item_selector: Any
            # result_selector: Any
            
            map_base_props = stepfunctions.MapBaseProps(
                comment="comment",
                input_path="inputPath",
                item_selector={
                    "item_selector_key": item_selector
                },
                items_path="itemsPath",
                max_concurrency=123,
                max_concurrency_path="maxConcurrencyPath",
                output_path="outputPath",
                result_path="resultPath",
                result_selector={
                    "result_selector_key": result_selector
                },
                state_name="stateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__123fd5cef3e54859ea847c1cc590a95cd39ecae394611b5e8add5b44b8354ab6)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument item_selector", value=item_selector, expected_type=type_hints["item_selector"])
            check_type(argname="argument items_path", value=items_path, expected_type=type_hints["items_path"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_concurrency_path", value=max_concurrency_path, expected_type=type_hints["max_concurrency_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if item_selector is not None:
            self._values["item_selector"] = item_selector
        if items_path is not None:
            self._values["items_path"] = items_path
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_concurrency_path is not None:
            self._values["max_concurrency_path"] = max_concurrency_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if state_name is not None:
            self._values["state_name"] = state_name

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def item_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that you want to override your default iteration input (mutually exclusive  with ``parameters``).

        :default: $

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-itemselector.html
        '''
        result = self._values.get("item_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def items_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select the array to iterate over.

        :default: $
        '''
        result = self._values.get("items_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[jsii.Number]:
        '''MaxConcurrency.

        An upper bound on the number of iterations you want running at once.

        :default: - full concurrency

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-asl-use-map-state-inline.html#map-state-inline-additional-fields
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrency_path(self) -> typing.Optional[builtins.str]:
        '''MaxConcurrencyPath.

        A JsonPath that specifies the maximum concurrency dynamically from the state input.

        :default: - full concurrency

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-asl-use-map-state-inline.html#map-state-inline-additional-fields
        '''
        result = self._values.get("max_concurrency_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: $
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MapBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.MapProps",
    jsii_struct_bases=[MapBaseProps],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "item_selector": "itemSelector",
        "items_path": "itemsPath",
        "max_concurrency": "maxConcurrency",
        "max_concurrency_path": "maxConcurrencyPath",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "state_name": "stateName",
        "parameters": "parameters",
    },
)
class MapProps(MapBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        items_path: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_concurrency_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''Properties for defining a Map state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param item_selector: The JSON that you want to override your default iteration input (mutually exclusive with ``parameters``). Default: $
        :param items_path: JSONPath expression to select the array to iterate over. Default: $
        :param max_concurrency: MaxConcurrency. An upper bound on the number of iterations you want running at once. Default: - full concurrency
        :param max_concurrency_path: MaxConcurrencyPath. A JsonPath that specifies the maximum concurrency dynamically from the state input. Default: - full concurrency
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        :param parameters: (deprecated) The JSON that you want to override your default iteration input (mutually exclusive with ``itemSelector``). Default: $

        :exampleMetadata: infused

        Example::

            map = sfn.Map(self, "Map State",
                max_concurrency=1,
                items_path=sfn.JsonPath.string_at("$.inputForMap"),
                item_selector={
                    "item": sfn.JsonPath.string_at("$.Map.Item.Value")
                },
                result_path="$.mapOutput"
            )
            
            # The Map iterator can contain a IChainable, which can be an individual or multiple steps chained together.
            # Below example is with a Choice and Pass step
            choice = sfn.Choice(self, "Choice")
            condition1 = sfn.Condition.string_equals("$.item.status", "SUCCESS")
            step1 = sfn.Pass(self, "Step1")
            step2 = sfn.Pass(self, "Step2")
            finish = sfn.Pass(self, "Finish")
            
            definition = choice.when(condition1, step1).otherwise(step2).afterwards().next(finish)
            
            map.item_processor(definition)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__841961f24272e2df479ccf3f591259c5dbc7bf471c2a6e11c7c7d61bf0e153ec)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument item_selector", value=item_selector, expected_type=type_hints["item_selector"])
            check_type(argname="argument items_path", value=items_path, expected_type=type_hints["items_path"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_concurrency_path", value=max_concurrency_path, expected_type=type_hints["max_concurrency_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if item_selector is not None:
            self._values["item_selector"] = item_selector
        if items_path is not None:
            self._values["items_path"] = items_path
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_concurrency_path is not None:
            self._values["max_concurrency_path"] = max_concurrency_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if state_name is not None:
            self._values["state_name"] = state_name
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def item_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that you want to override your default iteration input (mutually exclusive  with ``parameters``).

        :default: $

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-itemselector.html
        '''
        result = self._values.get("item_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def items_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select the array to iterate over.

        :default: $
        '''
        result = self._values.get("items_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[jsii.Number]:
        '''MaxConcurrency.

        An upper bound on the number of iterations you want running at once.

        :default: - full concurrency

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-asl-use-map-state-inline.html#map-state-inline-additional-fields
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrency_path(self) -> typing.Optional[builtins.str]:
        '''MaxConcurrencyPath.

        A JsonPath that specifies the maximum concurrency dynamically from the state input.

        :default: - full concurrency

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-asl-use-map-state-inline.html#map-state-inline-additional-fields
        '''
        result = self._values.get("max_concurrency_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: $
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(deprecated) The JSON that you want to override your default iteration input (mutually exclusive  with ``itemSelector``).

        :default: $

        :deprecated:

        Step Functions has deprecated the ``parameters`` field in favor of
        the new ``itemSelector`` field

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-itemselector.html
        :stability: deprecated
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MapProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.ParallelProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "state_name": "stateName",
    },
)
class ParallelProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a Parallel state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # result_selector: Any
            
            parallel_props = stepfunctions.ParallelProps(
                comment="comment",
                input_path="inputPath",
                output_path="outputPath",
                result_path="resultPath",
                result_selector={
                    "result_selector_key": result_selector
                },
                state_name="stateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a04fcca9cbcddc34201ab96bfd6e4be7793eed6937bb07ccd5c1a2dc45a6484)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if state_name is not None:
            self._values["state_name"] = state_name

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: $
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParallelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.PassProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "output_path": "outputPath",
        "parameters": "parameters",
        "result": "result",
        "result_path": "resultPath",
        "state_name": "stateName",
    },
)
class PassProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        result: typing.Optional["Result"] = None,
        result_path: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a Pass state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param parameters: Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input. Default: No parameters
        :param result: If given, treat as the result of this operation. Can be used to inject or replace the current execution state. Default: No injected result
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name

        :exampleMetadata: infused

        Example::

            # Makes the current JSON state { ..., "subObject": { "hello": "world" } }
            pass = sfn.Pass(self, "Add Hello World",
                result=sfn.Result.from_object({"hello": "world"}),
                result_path="$.subObject"
            )
            
            # Set the next state
            next_state = sfn.Pass(self, "NextState")
            pass.next(next_state)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d80da5dbca7702d56f2a0dd67c4a5a72e182c08bcd852d74ea0fa21442f048)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument result", value=result, expected_type=type_hints["result"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if parameters is not None:
            self._values["parameters"] = parameters
        if result is not None:
            self._values["result"] = result
        if result_path is not None:
            self._values["result_path"] = result_path
        if state_name is not None:
            self._values["state_name"] = state_name

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input.

        :default: No parameters

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def result(self) -> typing.Optional["Result"]:
        '''If given, treat as the result of this operation.

        Can be used to inject or replace the current execution state.

        :default: No injected result
        '''
        result = self._values.get("result")
        return typing.cast(typing.Optional["Result"], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: $
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PassProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.ProcessorConfig",
    jsii_struct_bases=[],
    name_mapping={"execution_type": "executionType", "mode": "mode"},
)
class ProcessorConfig:
    def __init__(
        self,
        *,
        execution_type: typing.Optional["ProcessorType"] = None,
        mode: typing.Optional["ProcessorMode"] = None,
    ) -> None:
        '''Specifies the configuration for the processor Map state.

        :param execution_type: Specifies the execution type for the Map workflow. You must provide this field if you specified ``DISTRIBUTED`` for the ``mode`` sub-field. Default: - no execution type
        :param mode: Specifies the execution mode for the Map workflow. Default: - ProcessorMode.INLINE

        :exampleMetadata: infused

        Example::

            map = sfn.Map(self, "Map State",
                max_concurrency=1,
                items_path=sfn.JsonPath.string_at("$.inputForMap"),
                item_selector={
                    "item": sfn.JsonPath.string_at("$.Map.Item.Value")
                },
                result_path="$.mapOutput"
            )
            
            map.item_processor(sfn.Pass(self, "Pass State"),
                mode=sfn.ProcessorMode.DISTRIBUTED,
                execution_type=sfn.ProcessorType.STANDARD
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31ff219914b0d650a3cc1eb8631c77a0fd4affa44a5d994dc200757166b4959)
            check_type(argname="argument execution_type", value=execution_type, expected_type=type_hints["execution_type"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if execution_type is not None:
            self._values["execution_type"] = execution_type
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def execution_type(self) -> typing.Optional["ProcessorType"]:
        '''Specifies the execution type for the Map workflow.

        You must provide this field if you specified ``DISTRIBUTED`` for the ``mode`` sub-field.

        :default: - no execution type
        '''
        result = self._values.get("execution_type")
        return typing.cast(typing.Optional["ProcessorType"], result)

    @builtins.property
    def mode(self) -> typing.Optional["ProcessorMode"]:
        '''Specifies the execution mode for the Map workflow.

        :default: - ProcessorMode.INLINE
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["ProcessorMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProcessorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.ProcessorMode")
class ProcessorMode(enum.Enum):
    '''Mode of the Map workflow.

    :exampleMetadata: infused

    Example::

        map = sfn.Map(self, "Map State",
            max_concurrency=1,
            items_path=sfn.JsonPath.string_at("$.inputForMap"),
            item_selector={
                "item": sfn.JsonPath.string_at("$.Map.Item.Value")
            },
            result_path="$.mapOutput"
        )
        
        map.item_processor(sfn.Pass(self, "Pass State"),
            mode=sfn.ProcessorMode.DISTRIBUTED,
            execution_type=sfn.ProcessorType.STANDARD
        )
    '''

    INLINE = "INLINE"
    '''Inline Map mode.'''
    DISTRIBUTED = "DISTRIBUTED"
    '''Distributed Map mode.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.ProcessorType")
class ProcessorType(enum.Enum):
    '''Execution type for the Map workflow.

    :exampleMetadata: infused

    Example::

        map = sfn.Map(self, "Map State",
            max_concurrency=1,
            items_path=sfn.JsonPath.string_at("$.inputForMap"),
            item_selector={
                "item": sfn.JsonPath.string_at("$.Map.Item.Value")
            },
            result_path="$.mapOutput"
        )
        
        map.item_processor(sfn.Pass(self, "Pass State"),
            mode=sfn.ProcessorMode.DISTRIBUTED,
            execution_type=sfn.ProcessorType.STANDARD
        )
    '''

    STANDARD = "STANDARD"
    '''Standard execution type.'''
    EXPRESS = "EXPRESS"
    '''Express execution type.'''


class Result(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_stepfunctions.Result"):
    '''The result of a Pass operation.

    :exampleMetadata: infused

    Example::

        # Makes the current JSON state { ..., "subObject": { "hello": "world" } }
        pass = sfn.Pass(self, "Add Hello World",
            result=sfn.Result.from_object({"hello": "world"}),
            result_path="$.subObject"
        )
        
        # Set the next state
        next_state = sfn.Pass(self, "NextState")
        pass.next(next_state)
    '''

    def __init__(self, value: typing.Any) -> None:
        '''
        :param value: result of the Pass operation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03617b4630db9dcdb093cf33053ff1c356d21c05e74b38ea8811464bc3fd24b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.create(self.__class__, self, [value])

    @jsii.member(jsii_name="fromArray")
    @builtins.classmethod
    def from_array(cls, value: typing.Sequence[typing.Any]) -> "Result":
        '''The result of the operation is an array.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c5d4ed5a0f4e741ccf9d2e3ddfe01fd92fa69cd2f3bd2f4aaf2bfacf3c04823)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Result", jsii.sinvoke(cls, "fromArray", [value]))

    @jsii.member(jsii_name="fromBoolean")
    @builtins.classmethod
    def from_boolean(cls, value: builtins.bool) -> "Result":
        '''The result of the operation is a boolean.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b54f9e8f1a575aea261b9615223628a454b88112ac3018e8bdfd096921aad1c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Result", jsii.sinvoke(cls, "fromBoolean", [value]))

    @jsii.member(jsii_name="fromNumber")
    @builtins.classmethod
    def from_number(cls, value: jsii.Number) -> "Result":
        '''The result of the operation is a number.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2893d7f002c7ba8fef05ee75544a163571341072dfac17ef5901e8bb26f2f4e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Result", jsii.sinvoke(cls, "fromNumber", [value]))

    @jsii.member(jsii_name="fromObject")
    @builtins.classmethod
    def from_object(cls, value: typing.Mapping[builtins.str, typing.Any]) -> "Result":
        '''The result of the operation is an object.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db43a330458ab9fb395b00b0376ac06a03666ab606b8c9ddea25971d2ce0719f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Result", jsii.sinvoke(cls, "fromObject", [value]))

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(cls, value: builtins.str) -> "Result":
        '''The result of the operation is a string.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3615b36aa1e6d0193c5cb37ecfb6f1833c1503331f692609e2775414220fc42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Result", jsii.sinvoke(cls, "fromString", [value]))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''result of the Pass operation.'''
        return typing.cast(typing.Any, jsii.get(self, "value"))


class ResultWriter(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.ResultWriter",
):
    '''Configuration for writing Distributed Map state results to S3.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        
        
        # create a bucket
        bucket = s3.Bucket(self, "Bucket")
        
        distributed_map = sfn.DistributedMap(self, "Distributed Map State",
            item_reader=sfn.S3JsonItemReader(
                bucket=bucket,
                key="my-key.json"
            ),
            result_writer=sfn.ResultWriter(
                bucket=bucket,
                prefix="my-prefix"
            )
        )
        distributed_map.item_processor(sfn.Pass(self, "Pass State"))
    '''

    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: S3 Bucket in which to save Map Run results.
        :param prefix: S3 prefix in which to save Map Run results. Default: - No prefix
        '''
        props = ResultWriterProps(bucket=bucket, prefix=prefix)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="providePolicyStatements")
    def provide_policy_statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''Compile policy statements to provide relevent permissions to the state machine.'''
        return typing.cast(typing.List[_PolicyStatement_0fe33853], jsii.invoke(self, "providePolicyStatements", []))

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Render ResultWriter in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket in which to save Map Run results.'''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> typing.Optional[builtins.str]:
        '''S3 prefix in which to save Map Run results.

        :default: - No prefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefix"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.ResultWriterProps",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "prefix": "prefix"},
)
class ResultWriterProps:
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Interface for Result Writer configuration properties.

        :param bucket: S3 Bucket in which to save Map Run results.
        :param prefix: S3 prefix in which to save Map Run results. Default: - No prefix

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            
            
            # create a bucket
            bucket = s3.Bucket(self, "Bucket")
            
            distributed_map = sfn.DistributedMap(self, "Distributed Map State",
                item_reader=sfn.S3JsonItemReader(
                    bucket=bucket,
                    key="my-key.json"
                ),
                result_writer=sfn.ResultWriter(
                    bucket=bucket,
                    prefix="my-prefix"
                )
            )
            distributed_map.item_processor(sfn.Pass(self, "Pass State"))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e7633dd729e9dd58a8e472e766fe10b0748d68a61f3d07bfec9cc5b8b4721f)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket in which to save Map Run results.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''S3 prefix in which to save Map Run results.

        :default: - No prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResultWriterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.RetryProps",
    jsii_struct_bases=[],
    name_mapping={
        "backoff_rate": "backoffRate",
        "errors": "errors",
        "interval": "interval",
        "jitter_strategy": "jitterStrategy",
        "max_attempts": "maxAttempts",
        "max_delay": "maxDelay",
    },
)
class RetryProps:
    def __init__(
        self,
        *,
        backoff_rate: typing.Optional[jsii.Number] = None,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        interval: typing.Optional[_Duration_4839e8c3] = None,
        jitter_strategy: typing.Optional[JitterType] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        max_delay: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Retry details.

        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param jitter_strategy: Introduces a randomization over the retry interval. Default: - No jitter strategy
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3
        :param max_delay: Maximum limit on retry interval growth during exponential backoff. Default: - No max delay

        :exampleMetadata: infused

        Example::

            parallel = sfn.Parallel(self, "Do the work in parallel")
            
            # Add branches to be executed in parallel
            ship_item = sfn.Pass(self, "ShipItem")
            send_invoice = sfn.Pass(self, "SendInvoice")
            restock = sfn.Pass(self, "Restock")
            parallel.branch(ship_item)
            parallel.branch(send_invoice)
            parallel.branch(restock)
            
            # Retry the whole workflow if something goes wrong with exponential backoff
            parallel.add_retry(
                max_attempts=1,
                max_delay=Duration.seconds(5),
                jitter_strategy=sfn.JitterType.FULL
            )
            
            # How to recover from errors
            send_failure_notification = sfn.Pass(self, "SendFailureNotification")
            parallel.add_catch(send_failure_notification)
            
            # What to do in case everything succeeded
            close_order = sfn.Pass(self, "CloseOrder")
            parallel.next(close_order)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__984afa5a2055f0c35fc8c3cf6882093d3a32a8b56c725bd4e3c643f693f59d40)
            check_type(argname="argument backoff_rate", value=backoff_rate, expected_type=type_hints["backoff_rate"])
            check_type(argname="argument errors", value=errors, expected_type=type_hints["errors"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument jitter_strategy", value=jitter_strategy, expected_type=type_hints["jitter_strategy"])
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument max_delay", value=max_delay, expected_type=type_hints["max_delay"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backoff_rate is not None:
            self._values["backoff_rate"] = backoff_rate
        if errors is not None:
            self._values["errors"] = errors
        if interval is not None:
            self._values["interval"] = interval
        if jitter_strategy is not None:
            self._values["jitter_strategy"] = jitter_strategy
        if max_attempts is not None:
            self._values["max_attempts"] = max_attempts
        if max_delay is not None:
            self._values["max_delay"] = max_delay

    @builtins.property
    def backoff_rate(self) -> typing.Optional[jsii.Number]:
        '''Multiplication for how much longer the wait interval gets on every retry.

        :default: 2
        '''
        result = self._values.get("backoff_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def errors(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Errors to retry.

        A list of error strings to retry, which can be either predefined errors
        (for example Errors.NoChoiceMatched) or a self-defined error.

        :default: All errors
        '''
        result = self._values.get("errors")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''How many seconds to wait initially before retrying.

        :default: Duration.seconds(1)
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def jitter_strategy(self) -> typing.Optional[JitterType]:
        '''Introduces a randomization over the retry interval.

        :default: - No jitter strategy
        '''
        result = self._values.get("jitter_strategy")
        return typing.cast(typing.Optional[JitterType], result)

    @builtins.property
    def max_attempts(self) -> typing.Optional[jsii.Number]:
        '''How many times to retry this particular error.

        May be 0 to disable retry for specific errors (in case you have
        a catch-all retry policy).

        :default: 3
        '''
        result = self._values.get("max_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_delay(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Maximum limit on retry interval growth during exponential backoff.

        :default: - No max delay
        '''
        result = self._values.get("max_delay")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RetryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IItemReader)
class S3CsvItemReader(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.S3CsvItemReader",
):
    '''Item Reader configuration for iterating over items in a CSV file stored in S3.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3 as s3
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # bucket: s3.Bucket
        # csv_headers: stepfunctions.CsvHeaders
        
        s3_csv_item_reader = stepfunctions.S3CsvItemReader(
            bucket=bucket,
            key="key",
        
            # the properties below are optional
            csv_headers=csv_headers,
            max_items=123
        )
    '''

    def __init__(
        self,
        *,
        csv_headers: typing.Optional[CsvHeaders] = None,
        key: builtins.str,
        bucket: _IBucket_42e086fd,
        max_items: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param csv_headers: CSV file header configuration. Default: - CsvHeaders with CsvHeadersLocation.FIRST_ROW
        :param key: Key of file stored in S3 bucket containing an array to iterate over.
        :param bucket: S3 Bucket containing objects to iterate over or a file with a list to iterate over.
        :param max_items: Limits the number of items passed to the Distributed Map state. Default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        props = S3CsvItemReaderProps(
            csv_headers=csv_headers, key=key, bucket=bucket, max_items=max_items
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="providePolicyStatements")
    def provide_policy_statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''Compile policy statements to provide relevent permissions to the state machine.'''
        return typing.cast(typing.List[_PolicyStatement_0fe33853], jsii.invoke(self, "providePolicyStatements", []))

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Renders the ItemReader configuration as JSON object.'''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing a file with a list to iterate over.'''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="csvHeaders")
    def csv_headers(self) -> CsvHeaders:
        '''CSV headers configuration.'''
        return typing.cast(CsvHeaders, jsii.get(self, "csvHeaders"))

    @builtins.property
    @jsii.member(jsii_name="inputType")
    def _input_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputType"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        '''S3 key of a file with a list to iterate over.'''
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        '''ARN for the ``getObject`` method of the S3 API This API method is used to iterate all objects in the S3 bucket/prefix.'''
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="maxItems")
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - No maxItems
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxItems"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.S3FileItemReaderProps",
    jsii_struct_bases=[ItemReaderProps],
    name_mapping={"bucket": "bucket", "max_items": "maxItems", "key": "key"},
)
class S3FileItemReaderProps(ItemReaderProps):
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        max_items: typing.Optional[jsii.Number] = None,
        key: builtins.str,
    ) -> None:
        '''Base interface for Item Reader configuration properties the iterate over entries in a S3 file.

        :param bucket: S3 Bucket containing objects to iterate over or a file with a list to iterate over.
        :param max_items: Limits the number of items passed to the Distributed Map state. Default: - Distributed Map state will iterate over all items provided by the ItemReader
        :param key: Key of file stored in S3 bucket containing an array to iterate over.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            
            
            # create a bucket
            bucket = s3.Bucket(self, "Bucket")
            
            distributed_map = sfn.DistributedMap(self, "Distributed Map State",
                item_reader=sfn.S3JsonItemReader(
                    bucket=bucket,
                    key="my-key.json"
                ),
                result_writer=sfn.ResultWriter(
                    bucket=bucket,
                    prefix="my-prefix"
                )
            )
            distributed_map.item_processor(sfn.Pass(self, "Pass State"))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc17fd96c577f0b5f18e9d0043337043a5db7cf7c35fdc1b09e959cf7f58221c)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument max_items", value=max_items, expected_type=type_hints["max_items"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }
        if max_items is not None:
            self._values["max_items"] = max_items

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing objects to iterate over or a file with a list to iterate over.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        result = self._values.get("max_items")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Key of file stored in S3 bucket containing an array to iterate over.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3FileItemReaderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IItemReader)
class S3JsonItemReader(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.S3JsonItemReader",
):
    '''Item Reader configuration for iterating over items in a JSON array stored in a S3 file.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        
        
        # create a bucket
        bucket = s3.Bucket(self, "Bucket")
        
        distributed_map = sfn.DistributedMap(self, "Distributed Map State",
            item_reader=sfn.S3JsonItemReader(
                bucket=bucket,
                key="my-key.json"
            ),
            result_writer=sfn.ResultWriter(
                bucket=bucket,
                prefix="my-prefix"
            )
        )
        distributed_map.item_processor(sfn.Pass(self, "Pass State"))
    '''

    def __init__(
        self,
        *,
        key: builtins.str,
        bucket: _IBucket_42e086fd,
        max_items: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param key: Key of file stored in S3 bucket containing an array to iterate over.
        :param bucket: S3 Bucket containing objects to iterate over or a file with a list to iterate over.
        :param max_items: Limits the number of items passed to the Distributed Map state. Default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        props = S3FileItemReaderProps(key=key, bucket=bucket, max_items=max_items)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="providePolicyStatements")
    def provide_policy_statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''Compile policy statements to provide relevent permissions to the state machine.'''
        return typing.cast(typing.List[_PolicyStatement_0fe33853], jsii.invoke(self, "providePolicyStatements", []))

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Renders the ItemReader configuration as JSON object.

        :return: - JSON object
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing a file with a list to iterate over.'''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="inputType")
    def _input_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputType"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        '''S3 key of a file with a list to iterate over.'''
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        '''ARN for the ``getObject`` method of the S3 API This API method is used to iterate all objects in the S3 bucket/prefix.'''
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="maxItems")
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - No maxItems
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxItems"))


@jsii.implements(IItemReader)
class S3ManifestItemReader(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.S3ManifestItemReader",
):
    '''Item Reader configuration for iterating over items in a S3 inventory manifest file stored in S3.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3 as s3
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # bucket: s3.Bucket
        
        s3_manifest_item_reader = stepfunctions.S3ManifestItemReader(
            bucket=bucket,
            key="key",
        
            # the properties below are optional
            max_items=123
        )
    '''

    def __init__(
        self,
        *,
        key: builtins.str,
        bucket: _IBucket_42e086fd,
        max_items: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param key: Key of file stored in S3 bucket containing an array to iterate over.
        :param bucket: S3 Bucket containing objects to iterate over or a file with a list to iterate over.
        :param max_items: Limits the number of items passed to the Distributed Map state. Default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        props = S3FileItemReaderProps(key=key, bucket=bucket, max_items=max_items)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="providePolicyStatements")
    def provide_policy_statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''Compile policy statements to provide relevent permissions to the state machine.'''
        return typing.cast(typing.List[_PolicyStatement_0fe33853], jsii.invoke(self, "providePolicyStatements", []))

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Renders the ItemReader configuration as JSON object.

        :return: - JSON object
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing a file with a list to iterate over.'''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="inputType")
    def _input_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputType"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        '''S3 key of a file with a list to iterate over.'''
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        '''ARN for the ``getObject`` method of the S3 API This API method is used to iterate all objects in the S3 bucket/prefix.'''
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="maxItems")
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - No maxItems
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxItems"))


@jsii.implements(IItemReader)
class S3ObjectsItemReader(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.S3ObjectsItemReader",
):
    '''Item Reader configuration for iterating over objects in an S3 bucket.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3 as s3
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # bucket: s3.Bucket
        
        s3_objects_item_reader = stepfunctions.S3ObjectsItemReader(
            bucket=bucket,
        
            # the properties below are optional
            max_items=123,
            prefix="prefix"
        )
    '''

    def __init__(
        self,
        *,
        prefix: typing.Optional[builtins.str] = None,
        bucket: _IBucket_42e086fd,
        max_items: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param prefix: S3 prefix used to limit objects to iterate over. Default: - No prefix
        :param bucket: S3 Bucket containing objects to iterate over or a file with a list to iterate over.
        :param max_items: Limits the number of items passed to the Distributed Map state. Default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        props = S3ObjectsItemReaderProps(
            prefix=prefix, bucket=bucket, max_items=max_items
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="providePolicyStatements")
    def provide_policy_statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''Compile policy statements to provide relevent permissions to the state machine.'''
        return typing.cast(typing.List[_PolicyStatement_0fe33853], jsii.invoke(self, "providePolicyStatements", []))

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Renders the ItemReader configuration as JSON object.

        :return: - JSON object
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing objects to iterate over.'''
        return typing.cast(_IBucket_42e086fd, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        '''ARN for the ``listObjectsV2`` method of the S3 API This API method is used to iterate all objects in the S3 bucket/prefix.'''
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="maxItems")
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxItems"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> typing.Optional[builtins.str]:
        '''S3 prefix used to limit objects to iterate over.

        :default: - No prefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefix"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.S3ObjectsItemReaderProps",
    jsii_struct_bases=[ItemReaderProps],
    name_mapping={"bucket": "bucket", "max_items": "maxItems", "prefix": "prefix"},
)
class S3ObjectsItemReaderProps(ItemReaderProps):
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        max_items: typing.Optional[jsii.Number] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for configuring an Item Reader that iterates over objects in an S3 bucket.

        :param bucket: S3 Bucket containing objects to iterate over or a file with a list to iterate over.
        :param max_items: Limits the number of items passed to the Distributed Map state. Default: - Distributed Map state will iterate over all items provided by the ItemReader
        :param prefix: S3 prefix used to limit objects to iterate over. Default: - No prefix

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3 as s3
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # bucket: s3.Bucket
            
            s3_objects_item_reader_props = stepfunctions.S3ObjectsItemReaderProps(
                bucket=bucket,
            
                # the properties below are optional
                max_items=123,
                prefix="prefix"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0839027a57f578b6a339286602923b0024b1f5e10dc2fb3ce8ac185f643a3bbc)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument max_items", value=max_items, expected_type=type_hints["max_items"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if max_items is not None:
            self._values["max_items"] = max_items
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing objects to iterate over or a file with a list to iterate over.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        result = self._values.get("max_items")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''S3 prefix used to limit objects to iterate over.

        :default: - No prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ObjectsItemReaderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.ServiceIntegrationPattern")
class ServiceIntegrationPattern(enum.Enum):
    '''Three ways to call an integrated service: Request Response, Run a Job and Wait for a Callback with Task Token.

    :default: FIRE_AND_FORGET

    :see:

    https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html

    Here, they are named as FIRE_AND_FORGET, SYNC and WAIT_FOR_TASK_TOKEN respectfully.
    '''

    FIRE_AND_FORGET = "FIRE_AND_FORGET"
    '''Call a service and progress to the next state immediately after the API call completes.'''
    SYNC = "SYNC"
    '''Call a service and wait for a job to complete.'''
    WAIT_FOR_TASK_TOKEN = "WAIT_FOR_TASK_TOKEN"
    '''Call a service with a task token and wait until that token is returned by SendTaskSuccess/SendTaskFailure with payload.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.SingleStateOptions",
    jsii_struct_bases=[ParallelProps],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "state_name": "stateName",
        "prefix_states": "prefixStates",
        "state_id": "stateId",
    },
)
class SingleStateOptions(ParallelProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
        prefix_states: typing.Optional[builtins.str] = None,
        state_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for creating a single state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        :param prefix_states: String to prefix all stateIds in the state machine with. Default: stateId
        :param state_id: ID of newly created containing state. Default: Construct ID of the StateMachineFragment

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # result_selector: Any
            
            single_state_options = stepfunctions.SingleStateOptions(
                comment="comment",
                input_path="inputPath",
                output_path="outputPath",
                prefix_states="prefixStates",
                result_path="resultPath",
                result_selector={
                    "result_selector_key": result_selector
                },
                state_id="stateId",
                state_name="stateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bfe6c744bf72f7e27c754b7de24b3cc1c8ee511680b9a61ee46fc118dd6a5c9)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
            check_type(argname="argument prefix_states", value=prefix_states, expected_type=type_hints["prefix_states"])
            check_type(argname="argument state_id", value=state_id, expected_type=type_hints["state_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if state_name is not None:
            self._values["state_name"] = state_name
        if prefix_states is not None:
            self._values["prefix_states"] = prefix_states
        if state_id is not None:
            self._values["state_id"] = state_id

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: $
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix_states(self) -> typing.Optional[builtins.str]:
        '''String to prefix all stateIds in the state machine with.

        :default: stateId
        '''
        result = self._values.get("prefix_states")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_id(self) -> typing.Optional[builtins.str]:
        '''ID of newly created containing state.

        :default: Construct ID of the StateMachineFragment
        '''
        result = self._values.get("state_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SingleStateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IChainable)
class State(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_stepfunctions.State",
):
    '''Base class for all other state classes.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param comment: A comment describing this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param parameters: Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input. Default: No parameters
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__095d7fa7ac65d852ef7641274fbdf11368859faad0abca011b7a488dead935f0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StateProps(
            comment=comment,
            input_path=input_path,
            output_path=output_path,
            parameters=parameters,
            result_path=result_path,
            result_selector=result_selector,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="filterNextables")
    @builtins.classmethod
    def filter_nextables(
        cls,
        states: typing.Sequence["State"],
    ) -> typing.List[INextable]:
        '''Return only the states that allow chaining from an array of states.

        :param states: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8285bd9e997c66a751e5455febad37743a69532169b26fb46600526e58ae970)
            check_type(argname="argument states", value=states, expected_type=type_hints["states"])
        return typing.cast(typing.List[INextable], jsii.sinvoke(cls, "filterNextables", [states]))

    @jsii.member(jsii_name="findReachableEndStates")
    @builtins.classmethod
    def find_reachable_end_states(
        cls,
        start: "State",
        *,
        include_error_handlers: typing.Optional[builtins.bool] = None,
    ) -> typing.List["State"]:
        '''Find the set of end states states reachable through transitions from the given start state.

        :param start: -
        :param include_error_handlers: Whether or not to follow error-handling transitions. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4622deb77b2918e678ad2d3a555fc84d4bb73d0ef35db3e8c844460b9bedd41c)
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        options = FindStateOptions(include_error_handlers=include_error_handlers)

        return typing.cast(typing.List["State"], jsii.sinvoke(cls, "findReachableEndStates", [start, options]))

    @jsii.member(jsii_name="findReachableStates")
    @builtins.classmethod
    def find_reachable_states(
        cls,
        start: "State",
        *,
        include_error_handlers: typing.Optional[builtins.bool] = None,
    ) -> typing.List["State"]:
        '''Find the set of states reachable through transitions from the given start state.

        This does not retrieve states from within sub-graphs, such as states within a Parallel state's branch.

        :param start: -
        :param include_error_handlers: Whether or not to follow error-handling transitions. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cec53ebef4ca820e7a85aa44b21deceeca71c230ec6ec855e5c5d6bb4880bdc0)
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        options = FindStateOptions(include_error_handlers=include_error_handlers)

        return typing.cast(typing.List["State"], jsii.sinvoke(cls, "findReachableStates", [start, options]))

    @jsii.member(jsii_name="prefixStates")
    @builtins.classmethod
    def prefix_states(
        cls,
        root: _constructs_77d1e7e8.IConstruct,
        prefix: builtins.str,
    ) -> None:
        '''Add a prefix to the stateId of all States found in a construct tree.

        :param root: -
        :param prefix: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b73e6298c3658224e6c25d0abee853dc2cbd5ed77d4f935e724af3c0f2f36d9e)
            check_type(argname="argument root", value=root, expected_type=type_hints["root"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        return typing.cast(None, jsii.sinvoke(cls, "prefixStates", [root, prefix]))

    @jsii.member(jsii_name="addBranch")
    def _add_branch(self, branch: "StateGraph") -> None:
        '''Add a parallel branch to this state.

        :param branch: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9f89078424459b1c694d56e01d3910a25c8af32756935aaace102680b9010a8)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
        return typing.cast(None, jsii.invoke(self, "addBranch", [branch]))

    @jsii.member(jsii_name="addChoice")
    def _add_choice(
        self,
        condition: Condition,
        next: "State",
        *,
        comment: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Add a choice branch to this state.

        :param condition: -
        :param next: -
        :param comment: An optional description for the choice transition. Default: No comment
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df2c90f3de37dcdaf38ae6a3e70460c7cdfd78a154847df351088cd8a3b22960)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        options = ChoiceTransitionOptions(comment=comment)

        return typing.cast(None, jsii.invoke(self, "addChoice", [condition, next, options]))

    @jsii.member(jsii_name="addItemProcessor")
    def _add_item_processor(
        self,
        processor: "StateGraph",
        *,
        execution_type: typing.Optional[ProcessorType] = None,
        mode: typing.Optional[ProcessorMode] = None,
    ) -> None:
        '''Add a item processor to this state.

        :param processor: -
        :param execution_type: Specifies the execution type for the Map workflow. You must provide this field if you specified ``DISTRIBUTED`` for the ``mode`` sub-field. Default: - no execution type
        :param mode: Specifies the execution mode for the Map workflow. Default: - ProcessorMode.INLINE
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5de90784fdeaa0fa9de5d18b85a161ebed718ee0e26df2989a66073001fcb12d)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        config = ProcessorConfig(execution_type=execution_type, mode=mode)

        return typing.cast(None, jsii.invoke(self, "addItemProcessor", [processor, config]))

    @jsii.member(jsii_name="addIterator")
    def _add_iterator(self, iteration: "StateGraph") -> None:
        '''Add a map iterator to this state.

        :param iteration: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5562e3f75801d7a93e7b5728bae35a75af70b818bb2fc8dcd8e5aa13d0766eb9)
            check_type(argname="argument iteration", value=iteration, expected_type=type_hints["iteration"])
        return typing.cast(None, jsii.invoke(self, "addIterator", [iteration]))

    @jsii.member(jsii_name="addPrefix")
    def add_prefix(self, x: builtins.str) -> None:
        '''Add a prefix to the stateId of this state.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7b71fffe032923dbb5cba43a418faf869357c809484ea9fcd9d26ceea47259a)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(None, jsii.invoke(self, "addPrefix", [x]))

    @jsii.member(jsii_name="bindToGraph")
    def bind_to_graph(self, graph: "StateGraph") -> None:
        '''Register this state as part of the given graph.

        Don't call this. It will be called automatically when you work
        with states normally.

        :param graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bdaefb727b4b60b3bebb8ea3b5db4a529cd533e6f827f21ccc0ff1822343254)
            check_type(argname="argument graph", value=graph, expected_type=type_hints["graph"])
        return typing.cast(None, jsii.invoke(self, "bindToGraph", [graph]))

    @jsii.member(jsii_name="makeDefault")
    def _make_default(self, def_: "State") -> None:
        '''Make the indicated state the default choice transition of this state.

        :param def_: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee3ac76d6f92e799c65c47a04ad37a5bd88574a09db9de401595f330f3a126de)
            check_type(argname="argument def_", value=def_, expected_type=type_hints["def_"])
        return typing.cast(None, jsii.invoke(self, "makeDefault", [def_]))

    @jsii.member(jsii_name="makeNext")
    def _make_next(self, next: "State") -> None:
        '''Make the indicated state the default transition of this state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a69a1ac363b05a6ca439baf3f08831b411887d784118ecc98566dca2d8872de)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast(None, jsii.invoke(self, "makeNext", [next]))

    @jsii.member(jsii_name="renderBranches")
    def _render_branches(self) -> typing.Any:
        '''Render parallel branches in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderBranches", []))

    @jsii.member(jsii_name="renderChoices")
    def _render_choices(self) -> typing.Any:
        '''Render the choices in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderChoices", []))

    @jsii.member(jsii_name="renderInputOutput")
    def _render_input_output(self) -> typing.Any:
        '''Render InputPath/Parameters/OutputPath in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderInputOutput", []))

    @jsii.member(jsii_name="renderItemProcessor")
    def _render_item_processor(self) -> typing.Any:
        '''Render ItemProcessor in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderItemProcessor", []))

    @jsii.member(jsii_name="renderIterator")
    def _render_iterator(self) -> typing.Any:
        '''Render map iterator in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderIterator", []))

    @jsii.member(jsii_name="renderNextEnd")
    def _render_next_end(self) -> typing.Any:
        '''Render the default next state in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderNextEnd", []))

    @jsii.member(jsii_name="renderResultSelector")
    def _render_result_selector(self) -> typing.Any:
        '''Render ResultSelector in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderResultSelector", []))

    @jsii.member(jsii_name="renderRetryCatch")
    def _render_retry_catch(self) -> typing.Any:
        '''Render error recovery options in ASL JSON format.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderRetryCatch", []))

    @jsii.member(jsii_name="toStateJson")
    @abc.abstractmethod
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Render the state as JSON.'''
        ...

    @jsii.member(jsii_name="validateState")
    def _validate_state(self) -> typing.List[builtins.str]:
        '''Allows the state to validate itself.'''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateState", []))

    @jsii.member(jsii_name="whenBoundToGraph")
    def _when_bound_to_graph(self, graph: "StateGraph") -> None:
        '''Called whenever this state is bound to a graph.

        Can be overridden by subclasses.

        :param graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acfe4853db045f97378bdb44b521dcb1b8b46261f09a3786e2e5519eef4bf29d)
            check_type(argname="argument graph", value=graph, expected_type=type_hints["graph"])
        return typing.cast(None, jsii.invoke(self, "whenBoundToGraph", [graph]))

    @builtins.property
    @jsii.member(jsii_name="branches")
    def _branches(self) -> typing.List["StateGraph"]:
        return typing.cast(typing.List["StateGraph"], jsii.get(self, "branches"))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    @abc.abstractmethod
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Descriptive identifier for this chainable.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> "State":
        '''First state of this Chainable.'''
        return typing.cast("State", jsii.get(self, "startState"))

    @builtins.property
    @jsii.member(jsii_name="stateId")
    def state_id(self) -> builtins.str:
        '''Tokenized string that evaluates to the state's ID.'''
        return typing.cast(builtins.str, jsii.get(self, "stateId"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def _comment(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comment"))

    @builtins.property
    @jsii.member(jsii_name="inputPath")
    def _input_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputPath"))

    @builtins.property
    @jsii.member(jsii_name="outputPath")
    def _output_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputPath"))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def _parameters(self) -> typing.Optional[typing.Mapping[typing.Any, typing.Any]]:
        return typing.cast(typing.Optional[typing.Mapping[typing.Any, typing.Any]], jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="resultPath")
    def _result_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resultPath"))

    @builtins.property
    @jsii.member(jsii_name="resultSelector")
    def _result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[typing.Any, typing.Any]]:
        return typing.cast(typing.Optional[typing.Mapping[typing.Any, typing.Any]], jsii.get(self, "resultSelector"))

    @builtins.property
    @jsii.member(jsii_name="stateName")
    def _state_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateName"))

    @builtins.property
    @jsii.member(jsii_name="defaultChoice")
    def _default_choice(self) -> typing.Optional["State"]:
        return typing.cast(typing.Optional["State"], jsii.get(self, "defaultChoice"))

    @_default_choice.setter
    def _default_choice(self, value: typing.Optional["State"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa9d14a638bb5fe2be1b697c5d2a93e5cb602c30d93b1a5ca1eece88b36b1df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultChoice", value)

    @builtins.property
    @jsii.member(jsii_name="iteration")
    def _iteration(self) -> typing.Optional["StateGraph"]:
        return typing.cast(typing.Optional["StateGraph"], jsii.get(self, "iteration"))

    @_iteration.setter
    def _iteration(self, value: typing.Optional["StateGraph"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe26ac05d39997cba9f0b774e8732e0d7e33aa2715be53c5d2b6746630255f5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iteration", value)

    @builtins.property
    @jsii.member(jsii_name="processor")
    def _processor(self) -> typing.Optional["StateGraph"]:
        return typing.cast(typing.Optional["StateGraph"], jsii.get(self, "processor"))

    @_processor.setter
    def _processor(self, value: typing.Optional["StateGraph"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18c6226d92e32b97a3bd2c7822b52c85358b3bd9174c0fcf373dcb3292508540)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "processor", value)

    @builtins.property
    @jsii.member(jsii_name="processorConfig")
    def _processor_config(self) -> typing.Optional[ProcessorConfig]:
        return typing.cast(typing.Optional[ProcessorConfig], jsii.get(self, "processorConfig"))

    @_processor_config.setter
    def _processor_config(self, value: typing.Optional[ProcessorConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2064eb72a766ce7c2f9e0be9e43dd6ea46736ba5dd83721de5468681035dcb9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "processorConfig", value)

    @builtins.property
    @jsii.member(jsii_name="processorMode")
    def _processor_mode(self) -> typing.Optional[ProcessorMode]:
        return typing.cast(typing.Optional[ProcessorMode], jsii.get(self, "processorMode"))

    @_processor_mode.setter
    def _processor_mode(self, value: typing.Optional[ProcessorMode]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2607af153540f000865a3d1354fc0086931cc826a2328eb0ae249231c9c35ef2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "processorMode", value)


class _StateProxy(State):
    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Render the state as JSON.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, State).__jsii_proxy_class__ = lambda : _StateProxy


class StateGraph(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.StateGraph",
):
    '''A collection of connected states.

    A StateGraph is used to keep track of all states that are connected (have
    transitions between them). It does not include the substatemachines in
    a Parallel's branches: those are their own StateGraphs, but the graphs
    themselves have a hierarchical relationship as well.

    By assigning states to a definitive StateGraph, we verify that no state
    machines are constructed. In particular:

    - Every state object can only ever be in 1 StateGraph, and not inadvertently
      be used in two graphs.
    - Every stateId must be unique across all states in the entire state
      machine.

    All policy statements in all states in all substatemachines are bubbled so
    that the top-level StateMachine instantiation can read them all and add
    them to the IAM Role.

    You do not need to instantiate this class; it is used internally.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # state: stepfunctions.State
        
        state_graph = stepfunctions.StateGraph(state, "graphDescription")
    '''

    def __init__(self, start_state: State, graph_description: builtins.str) -> None:
        '''
        :param start_state: state that gets executed when the state machine is launched.
        :param graph_description: description of the state machine.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45cc793b7e63b62353e75a13b1efe7e1c03416eb034851d41ac5b855a86cc475)
            check_type(argname="argument start_state", value=start_state, expected_type=type_hints["start_state"])
            check_type(argname="argument graph_description", value=graph_description, expected_type=type_hints["graph_description"])
        jsii.create(self.__class__, self, [start_state, graph_description])

    @jsii.member(jsii_name="bind")
    def bind(self, state_machine: "StateMachine") -> None:
        '''Binds this StateGraph to the StateMachine it defines and updates state machine permissions.

        :param state_machine: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c41fc2afd076bb5952af77d1651e7e739c7d0276024e5796a2d444fd4ba8db)
            check_type(argname="argument state_machine", value=state_machine, expected_type=type_hints["state_machine"])
        return typing.cast(None, jsii.invoke(self, "bind", [state_machine]))

    @jsii.member(jsii_name="registerPolicyStatement")
    def register_policy_statement(self, statement: _PolicyStatement_0fe33853) -> None:
        '''Register a Policy Statement used by states in this graph.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d649f93a2503f72395d055e758cb6b2340de6c8f77bdd56474547120392e535)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "registerPolicyStatement", [statement]))

    @jsii.member(jsii_name="registerState")
    def register_state(self, state: State) -> None:
        '''Register a state as part of this graph.

        Called by State.bindToGraph().

        :param state: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04cf5f7930ddcda9609e5560874ab06f26b4161423a2c9f15da86279c7ea7818)
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        return typing.cast(None, jsii.invoke(self, "registerState", [state]))

    @jsii.member(jsii_name="registerSuperGraph")
    def register_super_graph(self, graph: "StateGraph") -> None:
        '''Register this graph as a child of the given graph.

        Resource changes will be bubbled up to the given graph.

        :param graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a7cc2af53307fbb64a215cec870e4cea5ecf0b33bda74fef438d746903abbc4)
            check_type(argname="argument graph", value=graph, expected_type=type_hints["graph"])
        return typing.cast(None, jsii.invoke(self, "registerSuperGraph", [graph]))

    @jsii.member(jsii_name="toGraphJson")
    def to_graph_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language JSON for this graph.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toGraphJson", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Return a string description of this graph.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="policyStatements")
    def policy_statements(self) -> typing.List[_PolicyStatement_0fe33853]:
        '''The accumulated policy statements.'''
        return typing.cast(typing.List[_PolicyStatement_0fe33853], jsii.get(self, "policyStatements"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> State:
        '''state that gets executed when the state machine is launched.'''
        return typing.cast(State, jsii.get(self, "startState"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Set a timeout to render into the graph JSON.

        Read/write. Only makes sense on the top-level graph, subgraphs
        do not support this feature.

        :default: No timeout
        '''
        return typing.cast(typing.Optional[_Duration_4839e8c3], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: typing.Optional[_Duration_4839e8c3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d70fd99dfd053938f6857187678eff1538a49411584203816fe1ee6e2e95a57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)


@jsii.implements(IStateMachine)
class StateMachine(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.StateMachine",
):
    '''Define a StepFunctions State Machine.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_stepfunctions as stepfunctions
        
        
        pipeline = codepipeline.Pipeline(self, "MyPipeline")
        input_artifact = codepipeline.Artifact()
        start_state = stepfunctions.Pass(self, "StartState")
        simple_state_machine = stepfunctions.StateMachine(self, "SimpleStateMachine",
            definition=start_state
        )
        step_function_action = codepipeline_actions.StepFunctionInvokeAction(
            action_name="Invoke",
            state_machine=simple_state_machine,
            state_machine_input=codepipeline_actions.StateMachineInput.file_path(input_artifact.at_path("assets/input.json"))
        )
        pipeline.add_stage(
            stage_name="StepFunctions",
            actions=[step_function_action]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        definition: typing.Optional[IChainable] = None,
        definition_body: typing.Optional[DefinitionBody] = None,
        definition_substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        logs: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        state_machine_name: typing.Optional[builtins.str] = None,
        state_machine_type: typing.Optional["StateMachineType"] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        tracing_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param comment: Comment that describes this state machine. Default: - No comment
        :param definition: (deprecated) Definition for this state machine.
        :param definition_body: Definition for this state machine.
        :param definition_substitutions: substitutions for the definition body as a key-value map.
        :param logs: Defines what execution history events are logged and where they are logged. Default: No logging
        :param removal_policy: The removal policy to apply to state machine. Default: RemovalPolicy.DESTROY
        :param role: The execution role for the state machine service. Default: A role is automatically created
        :param state_machine_name: A name for the state machine. Default: A name is automatically generated
        :param state_machine_type: Type of the state machine. Default: StateMachineType.STANDARD
        :param timeout: Maximum run time for this state machine. Default: No timeout
        :param tracing_enabled: Specifies whether Amazon X-Ray tracing is enabled for this state machine. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efdfc02291401a50a1d945e5208e9becb9828352fec32bc109ccebafc162614e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StateMachineProps(
            comment=comment,
            definition=definition,
            definition_body=definition_body,
            definition_substitutions=definition_substitutions,
            logs=logs,
            removal_policy=removal_policy,
            role=role,
            state_machine_name=state_machine_name,
            state_machine_type=state_machine_type,
            timeout=timeout,
            tracing_enabled=tracing_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromStateMachineArn")
    @builtins.classmethod
    def from_state_machine_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        state_machine_arn: builtins.str,
    ) -> IStateMachine:
        '''Import a state machine.

        :param scope: -
        :param id: -
        :param state_machine_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dec1adbbe53b54bdacbe2c45386b0970883e6a6ea92d2dd5187b13837238802)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument state_machine_arn", value=state_machine_arn, expected_type=type_hints["state_machine_arn"])
        return typing.cast(IStateMachine, jsii.sinvoke(cls, "fromStateMachineArn", [scope, id, state_machine_arn]))

    @jsii.member(jsii_name="fromStateMachineName")
    @builtins.classmethod
    def from_state_machine_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        state_machine_name: builtins.str,
    ) -> IStateMachine:
        '''Import a state machine via resource name.

        :param scope: -
        :param id: -
        :param state_machine_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9d3d7898b3441749750d918233ae686af49db0c0bf54d9e123f31c4307ae53a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
        return typing.cast(IStateMachine, jsii.sinvoke(cls, "fromStateMachineName", [scope, id, state_machine_name]))

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''Add the given statement to the role's policy.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9722a5396d55198fc0f7899f6cd72adb62c73fdbba082f415df383e5176a389a)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToRolePolicy", [statement]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        identity: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity custom permissions.

        :param identity: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a379c65b3abf8422a7281124e586179178f0b3549b77f94825bb37365de34c5)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [identity, *actions]))

    @jsii.member(jsii_name="grantExecution")
    def grant_execution(
        self,
        identity: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions on all executions of the state machine.

        :param identity: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__403096ab0bc513019435d412939f8df18641c1b52bfba18e821c391fa4b9024d)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantExecution", [identity, *actions]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to read results from state machine.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de328dbf28de2be4ba9b61ea81bce4e6d383ec0968b0e914acb7378b694c7b96)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [identity]))

    @jsii.member(jsii_name="grantStartExecution")
    def grant_start_execution(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to start an execution of this state machine.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efa2d941a46220f1692542e8c26652619270873ffe07f55fc9aa7a063799ed08)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantStartExecution", [identity]))

    @jsii.member(jsii_name="grantStartSyncExecution")
    def grant_start_sync_execution(
        self,
        identity: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions to start a synchronous execution of this state machine.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1fc6bb22c960bfd2ca38ccc6a9922c3aadc1289dcf5bed18e2559bd0700d32e)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantStartSyncExecution", [identity]))

    @jsii.member(jsii_name="grantTaskResponse")
    def grant_task_response(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the given identity task response permissions on a state machine.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b16d8608f524913e06d7166d119ec903318d80b6015288e92a06223a03e95a)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantTaskResponse", [identity]))

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
        '''Return the given named metric for this State Machine's executions.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e00f442fc4f33cd6bcc931ba95c9117d241aef41be5171c27548e74d91fcd9be)
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

    @jsii.member(jsii_name="metricAborted")
    def metric_aborted(
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
        '''Metric for the number of executions that were aborted.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricAborted", [props]))

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(
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
        '''Metric for the number of executions that failed.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFailed", [props]))

    @jsii.member(jsii_name="metricStarted")
    def metric_started(
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
        '''Metric for the number of executions that were started.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricStarted", [props]))

    @jsii.member(jsii_name="metricSucceeded")
    def metric_succeeded(
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
        '''Metric for the number of executions that succeeded.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSucceeded", [props]))

    @jsii.member(jsii_name="metricThrottled")
    def metric_throttled(
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
        '''Metric for the number of executions that were throttled.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricThrottled", [props]))

    @jsii.member(jsii_name="metricTime")
    def metric_time(
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
        '''Metric for the interval, in milliseconds, between the time the execution starts and the time it closes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTime", [props]))

    @jsii.member(jsii_name="metricTimedOut")
    def metric_timed_out(
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
        '''Metric for the number of executions that timed out.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTimedOut", [props]))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_539bb2fd:
        '''The principal this state machine is running as.'''
        return typing.cast(_IPrincipal_539bb2fd, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _IRole_235f5d8e:
        '''Execution role of this state machine.'''
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="stateMachineArn")
    def state_machine_arn(self) -> builtins.str:
        '''The ARN of the state machine.'''
        return typing.cast(builtins.str, jsii.get(self, "stateMachineArn"))

    @builtins.property
    @jsii.member(jsii_name="stateMachineName")
    def state_machine_name(self) -> builtins.str:
        '''The name of the state machine.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "stateMachineName"))

    @builtins.property
    @jsii.member(jsii_name="stateMachineRevisionId")
    def state_machine_revision_id(self) -> builtins.str:
        '''Identifier for the state machine revision, which is an immutable, read-only snapshot of a state machine’s definition and configuration.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "stateMachineRevisionId"))

    @builtins.property
    @jsii.member(jsii_name="stateMachineType")
    def state_machine_type(self) -> "StateMachineType":
        '''Type of the state machine.

        :attribute: true
        '''
        return typing.cast("StateMachineType", jsii.get(self, "stateMachineType"))


@jsii.implements(IChainable)
class StateMachineFragment(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_stepfunctions.StateMachineFragment",
):
    '''Base class for reusable state machine fragments.

    :exampleMetadata: nofixture infused

    Example::

        from aws_cdk import Stack
        from constructs import Construct
        import aws_cdk.aws_stepfunctions as sfn
        
        class MyJob(sfn.StateMachineFragment):
        
            def __init__(self, parent, id, *, jobFlavor):
                super().__init__(parent, id)
        
                choice = sfn.Choice(self, "Choice").when(sfn.Condition.string_equals("$.branch", "left"), sfn.Pass(self, "Left Branch")).when(sfn.Condition.string_equals("$.branch", "right"), sfn.Pass(self, "Right Branch"))
        
                # ...
        
                self.start_state = choice
                self.end_states = choice.afterwards().end_states
        
        class MyStack(Stack):
            def __init__(self, scope, id):
                super().__init__(scope, id)
                # Do 3 different variants of MyJob in parallel
                parallel = sfn.Parallel(self, "All jobs").branch(MyJob(self, "Quick", job_flavor="quick").prefix_states()).branch(MyJob(self, "Medium", job_flavor="medium").prefix_states()).branch(MyJob(self, "Slow", job_flavor="slow").prefix_states())
        
                sfn.StateMachine(self, "MyStateMachine",
                    definition_body=sfn.DefinitionBody.from_chainable(parallel)
                )
    '''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''Creates a new construct node.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings. If the ID includes a path separator (``/``), then it will be replaced by double dash ``--``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c5c1191e0b1af51b303ad19000be8e5c4e97e8491eb40cd68c462fa7e42f03)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @jsii.member(jsii_name="next")
    def next(self, next: IChainable) -> "Chain":
        '''Continue normal execution with the given state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c75eaddac3409d6cdf5dd627e25e2ee4bb9a37cb569d80a08e1847684c226d7)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast("Chain", jsii.invoke(self, "next", [next]))

    @jsii.member(jsii_name="prefixStates")
    def prefix_states(
        self,
        prefix: typing.Optional[builtins.str] = None,
    ) -> "StateMachineFragment":
        '''Prefix the IDs of all states in this state machine fragment.

        Use this to avoid multiple copies of the state machine all having the
        same state IDs.

        :param prefix: The prefix to add. Will use construct ID by default.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18974d4c0fc7d5b60c0b12888f566840996e0be64f94ae03e6639ebccff3409b)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        return typing.cast("StateMachineFragment", jsii.invoke(self, "prefixStates", [prefix]))

    @jsii.member(jsii_name="toSingleState")
    def to_single_state(
        self,
        *,
        prefix_states: typing.Optional[builtins.str] = None,
        state_id: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> "Parallel":
        '''Wrap all states in this state machine fragment up into a single state.

        This can be used to add retry or error handling onto this state
        machine fragment.

        Be aware that this changes the result of the inner state machine
        to be an array with the result of the state machine in it. Adjust
        your paths accordingly. For example, change 'outputPath' to
        '$[0]'.

        :param prefix_states: String to prefix all stateIds in the state machine with. Default: stateId
        :param state_id: ID of newly created containing state. Default: Construct ID of the StateMachineFragment
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        options = SingleStateOptions(
            prefix_states=prefix_states,
            state_id=state_id,
            comment=comment,
            input_path=input_path,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            state_name=state_name,
        )

        return typing.cast("Parallel", jsii.invoke(self, "toSingleState", [options]))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    @abc.abstractmethod
    def end_states(self) -> typing.List[INextable]:
        '''The states to chain onto if this fragment is used.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Descriptive identifier for this chainable.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    @abc.abstractmethod
    def start_state(self) -> State:
        '''The start state of this state machine fragment.'''
        ...


class _StateMachineFragmentProxy(StateMachineFragment):
    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''The states to chain onto if this fragment is used.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> State:
        '''The start state of this state machine fragment.'''
        return typing.cast(State, jsii.get(self, "startState"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, StateMachineFragment).__jsii_proxy_class__ = lambda : _StateMachineFragmentProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.StateMachineProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "definition": "definition",
        "definition_body": "definitionBody",
        "definition_substitutions": "definitionSubstitutions",
        "logs": "logs",
        "removal_policy": "removalPolicy",
        "role": "role",
        "state_machine_name": "stateMachineName",
        "state_machine_type": "stateMachineType",
        "timeout": "timeout",
        "tracing_enabled": "tracingEnabled",
    },
)
class StateMachineProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        definition: typing.Optional[IChainable] = None,
        definition_body: typing.Optional[DefinitionBody] = None,
        definition_substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        logs: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        state_machine_name: typing.Optional[builtins.str] = None,
        state_machine_type: typing.Optional["StateMachineType"] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
        tracing_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for defining a State Machine.

        :param comment: Comment that describes this state machine. Default: - No comment
        :param definition: (deprecated) Definition for this state machine.
        :param definition_body: Definition for this state machine.
        :param definition_substitutions: substitutions for the definition body as a key-value map.
        :param logs: Defines what execution history events are logged and where they are logged. Default: No logging
        :param removal_policy: The removal policy to apply to state machine. Default: RemovalPolicy.DESTROY
        :param role: The execution role for the state machine service. Default: A role is automatically created
        :param state_machine_name: A name for the state machine. Default: A name is automatically generated
        :param state_machine_type: Type of the state machine. Default: StateMachineType.STANDARD
        :param timeout: Maximum run time for this state machine. Default: No timeout
        :param tracing_enabled: Specifies whether Amazon X-Ray tracing is enabled for this state machine. Default: false

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_stepfunctions as stepfunctions
            
            
            pipeline = codepipeline.Pipeline(self, "MyPipeline")
            input_artifact = codepipeline.Artifact()
            start_state = stepfunctions.Pass(self, "StartState")
            simple_state_machine = stepfunctions.StateMachine(self, "SimpleStateMachine",
                definition=start_state
            )
            step_function_action = codepipeline_actions.StepFunctionInvokeAction(
                action_name="Invoke",
                state_machine=simple_state_machine,
                state_machine_input=codepipeline_actions.StateMachineInput.file_path(input_artifact.at_path("assets/input.json"))
            )
            pipeline.add_stage(
                stage_name="StepFunctions",
                actions=[step_function_action]
            )
        '''
        if isinstance(logs, dict):
            logs = LogOptions(**logs)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24d23b501c893898901860f31ff1a0a0fa81eb89f06a7acf3eef4f15e46022f6)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument definition_body", value=definition_body, expected_type=type_hints["definition_body"])
            check_type(argname="argument definition_substitutions", value=definition_substitutions, expected_type=type_hints["definition_substitutions"])
            check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
            check_type(argname="argument state_machine_type", value=state_machine_type, expected_type=type_hints["state_machine_type"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tracing_enabled", value=tracing_enabled, expected_type=type_hints["tracing_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if definition is not None:
            self._values["definition"] = definition
        if definition_body is not None:
            self._values["definition_body"] = definition_body
        if definition_substitutions is not None:
            self._values["definition_substitutions"] = definition_substitutions
        if logs is not None:
            self._values["logs"] = logs
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if role is not None:
            self._values["role"] = role
        if state_machine_name is not None:
            self._values["state_machine_name"] = state_machine_name
        if state_machine_type is not None:
            self._values["state_machine_type"] = state_machine_type
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing_enabled is not None:
            self._values["tracing_enabled"] = tracing_enabled

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Comment that describes this state machine.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def definition(self) -> typing.Optional[IChainable]:
        '''(deprecated) Definition for this state machine.

        :deprecated: use definitionBody: DefinitionBody.fromChainable()

        :stability: deprecated
        '''
        result = self._values.get("definition")
        return typing.cast(typing.Optional[IChainable], result)

    @builtins.property
    def definition_body(self) -> typing.Optional[DefinitionBody]:
        '''Definition for this state machine.'''
        result = self._values.get("definition_body")
        return typing.cast(typing.Optional[DefinitionBody], result)

    @builtins.property
    def definition_substitutions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''substitutions for the definition body as a key-value map.'''
        result = self._values.get("definition_substitutions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def logs(self) -> typing.Optional[LogOptions]:
        '''Defines what execution history events are logged and where they are logged.

        :default: No logging
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional[LogOptions], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The removal policy to apply to state machine.

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The execution role for the state machine service.

        :default: A role is automatically created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def state_machine_name(self) -> typing.Optional[builtins.str]:
        '''A name for the state machine.

        :default: A name is automatically generated
        '''
        result = self._values.get("state_machine_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_machine_type(self) -> typing.Optional["StateMachineType"]:
        '''Type of the state machine.

        :default: StateMachineType.STANDARD
        '''
        result = self._values.get("state_machine_type")
        return typing.cast(typing.Optional["StateMachineType"], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Maximum run time for this state machine.

        :default: No timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def tracing_enabled(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether Amazon X-Ray tracing is enabled for this state machine.

        :default: false
        '''
        result = self._values.get("tracing_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StateMachineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_stepfunctions.StateMachineType")
class StateMachineType(enum.Enum):
    '''Two types of state machines are available in AWS Step Functions: EXPRESS AND STANDARD.

    :default: STANDARD

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html
    :exampleMetadata: infused

    Example::

        state_machine_definition = stepfunctions.Pass(self, "PassState")
        
        state_machine = stepfunctions.StateMachine(self, "StateMachine",
            definition=state_machine_definition,
            state_machine_type=stepfunctions.StateMachineType.EXPRESS
        )
        
        apigateway.StepFunctionsRestApi(self, "StepFunctionsRestApi",
            deploy=True,
            state_machine=state_machine
        )
    '''

    EXPRESS = "EXPRESS"
    '''Express Workflows are ideal for high-volume, event processing workloads.'''
    STANDARD = "STANDARD"
    '''Standard Workflows are ideal for long-running, durable, and auditable workflows.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.StateProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "output_path": "outputPath",
        "parameters": "parameters",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "state_name": "stateName",
    },
)
class StateProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties shared by all states.

        :param comment: A comment describing this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param parameters: Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input. Default: No parameters
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # parameters: Any
            # result_selector: Any
            
            state_props = stepfunctions.StateProps(
                comment="comment",
                input_path="inputPath",
                output_path="outputPath",
                parameters={
                    "parameters_key": parameters
                },
                result_path="resultPath",
                result_selector={
                    "result_selector_key": result_selector
                },
                state_name="stateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b03d550137d1f7258c191a636f4e39f4e3ecdc83ecee214790010cc1584599d)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if parameters is not None:
            self._values["parameters"] = parameters
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if state_name is not None:
            self._values["state_name"] = state_name

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment describing this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input.

        :default: No parameters

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: $
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StateTransitionMetric(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.StateTransitionMetric",
):
    '''Metrics on the rate limiting performed on state machine execution.

    These rate limits are shared across all state machines.

    :exampleMetadata: infused

    Example::

        cloudwatch.Alarm(self, "ThrottledAlarm",
            metric=sfn.StateTransitionMetric.metric_throttled_events(),
            threshold=10,
            evaluation_periods=2
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="metric")
    @builtins.classmethod
    def metric(
        cls,
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
        '''Return the given named metric for the service's state transition metrics.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d556c15cb7d46dea75f4d4d5be455df4181351677d04c896b3cece7c2f4164)
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricConsumedCapacity")
    @builtins.classmethod
    def metric_consumed_capacity(
        cls,
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
        '''Metric for the number of available state transitions per second.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricConsumedCapacity", [props]))

    @jsii.member(jsii_name="metricProvisionedBucketSize")
    @builtins.classmethod
    def metric_provisioned_bucket_size(
        cls,
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
        '''Metric for the number of available state transitions.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricProvisionedBucketSize", [props]))

    @jsii.member(jsii_name="metricProvisionedRefillRate")
    @builtins.classmethod
    def metric_provisioned_refill_rate(
        cls,
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
        '''Metric for the provisioned steady-state execution rate.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricProvisionedRefillRate", [props]))

    @jsii.member(jsii_name="metricThrottledEvents")
    @builtins.classmethod
    def metric_throttled_events(
        cls,
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
        '''Metric for the number of throttled state transitions.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricThrottledEvents", [props]))


class StringDefinitionBody(
    DefinitionBody,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.StringDefinitionBody",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # chainable: stepfunctions.IChainable
        
        string_definition_body = stepfunctions.StringDefinitionBody.from_chainable(chainable)
    '''

    def __init__(self, body: builtins.str) -> None:
        '''
        :param body: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5817d6d61140231e4bd01c29102ec205d9d1d0f848af6dd3aa28a11467c52a)
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
        jsii.create(self.__class__, self, [body])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _sfn_principal: _IPrincipal_539bb2fd,
        _sfn_props: typing.Union[StateMachineProps, typing.Dict[builtins.str, typing.Any]],
        _graph: typing.Optional[StateGraph] = None,
    ) -> DefinitionConfig:
        '''
        :param _scope: -
        :param _sfn_principal: -
        :param _sfn_props: -
        :param _graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aae45f38855ad466a878a7d83ebc926e1b656c12480ab66d4c642079849950e1)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _sfn_principal", value=_sfn_principal, expected_type=type_hints["_sfn_principal"])
            check_type(argname="argument _sfn_props", value=_sfn_props, expected_type=type_hints["_sfn_props"])
            check_type(argname="argument _graph", value=_graph, expected_type=type_hints["_graph"])
        return typing.cast(DefinitionConfig, jsii.invoke(self, "bind", [_scope, _sfn_principal, _sfn_props, _graph]))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))


class Succeed(
    State,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Succeed",
):
    '''Define a Succeed state in the state machine.

    Reaching a Succeed state terminates the state execution in success.

    :exampleMetadata: infused

    Example::

        success = sfn.Succeed(self, "We did it!")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e35ef3ad1b65975090819e8b098b2b754472124db44d9bf100117c9f3c97b861)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SucceedProps(
            comment=comment,
            input_path=input_path,
            output_path=output_path,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.SucceedProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "output_path": "outputPath",
        "state_name": "stateName",
    },
)
class SucceedProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a Succeed state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            succeed_props = stepfunctions.SucceedProps(
                comment="comment",
                input_path="inputPath",
                output_path="outputPath",
                state_name="stateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bcb322679d9a165f0c2d8e6c39b61e6673747fb3e4fb30298aed922536d5e7d)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if state_name is not None:
            self._values["state_name"] = state_name

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SucceedProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TaskInput(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.TaskInput",
):
    '''Type union for task classes that accept multiple types of payload.

    :exampleMetadata: infused

    Example::

        # fn: lambda.Function
        
        tasks.LambdaInvoke(self, "Invoke with callback",
            lambda_function=fn,
            integration_pattern=sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
            payload=sfn.TaskInput.from_object({
                "token": sfn.JsonPath.task_token,
                "input": sfn.JsonPath.string_at("$.someField")
            })
        )
    '''

    @jsii.member(jsii_name="fromJsonPathAt")
    @builtins.classmethod
    def from_json_path_at(cls, path: builtins.str) -> "TaskInput":
        '''Use a part of the execution data or task context as task input.

        Use this when you want to use a subobject or string from
        the current state machine execution or the current task context
        as complete payload to a task.

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a16bc413eb726c46f5b831021734efa77e701554386db73af23b8f97b5efcfab)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast("TaskInput", jsii.sinvoke(cls, "fromJsonPathAt", [path]))

    @jsii.member(jsii_name="fromObject")
    @builtins.classmethod
    def from_object(cls, obj: typing.Mapping[builtins.str, typing.Any]) -> "TaskInput":
        '''Use an object as task input.

        This object may contain JSON path fields as object values, if desired.

        Use ``sfn.JsonPath.DISCARD`` in place of ``null`` for languages that do not support ``null`` (i.e. Python).

        :param obj: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44f51b46946413e542cf081c0a3cecd65b415e2e9f64f9e57d989a11ff927db7)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast("TaskInput", jsii.sinvoke(cls, "fromObject", [obj]))

    @jsii.member(jsii_name="fromText")
    @builtins.classmethod
    def from_text(cls, text: builtins.str) -> "TaskInput":
        '''Use a literal string as task input.

        This might be a JSON-encoded object, or just a text.

        :param text: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4460ece474b7c5793d096111af286d4137cfc1cfc5ca165e37c695701d7c5af7)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        return typing.cast("TaskInput", jsii.sinvoke(cls, "fromText", [text]))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> InputType:
        '''type of task input.'''
        return typing.cast(InputType, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''payload for the corresponding input type.

        It can be a JSON-encoded object, context, data, etc.
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.TaskMetricsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "metric_dimensions": "metricDimensions",
        "metric_prefix_plural": "metricPrefixPlural",
        "metric_prefix_singular": "metricPrefixSingular",
    },
)
class TaskMetricsConfig:
    def __init__(
        self,
        *,
        metric_dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        metric_prefix_plural: typing.Optional[builtins.str] = None,
        metric_prefix_singular: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Task Metrics.

        :param metric_dimensions: The dimensions to attach to metrics. Default: - No metrics
        :param metric_prefix_plural: Prefix for plural metric names of activity actions. Default: - No such metrics
        :param metric_prefix_singular: Prefix for singular metric names of activity actions. Default: - No such metrics

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # metric_dimensions: Any
            
            task_metrics_config = stepfunctions.TaskMetricsConfig(
                metric_dimensions={
                    "metric_dimensions_key": metric_dimensions
                },
                metric_prefix_plural="metricPrefixPlural",
                metric_prefix_singular="metricPrefixSingular"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b853c8cb66c2f5d1054d5d4bf9d98efca35d979661a5be38eaf7dd6e44cef4cc)
            check_type(argname="argument metric_dimensions", value=metric_dimensions, expected_type=type_hints["metric_dimensions"])
            check_type(argname="argument metric_prefix_plural", value=metric_prefix_plural, expected_type=type_hints["metric_prefix_plural"])
            check_type(argname="argument metric_prefix_singular", value=metric_prefix_singular, expected_type=type_hints["metric_prefix_singular"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metric_dimensions is not None:
            self._values["metric_dimensions"] = metric_dimensions
        if metric_prefix_plural is not None:
            self._values["metric_prefix_plural"] = metric_prefix_plural
        if metric_prefix_singular is not None:
            self._values["metric_prefix_singular"] = metric_prefix_singular

    @builtins.property
    def metric_dimensions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The dimensions to attach to metrics.

        :default: - No metrics
        '''
        result = self._values.get("metric_dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def metric_prefix_plural(self) -> typing.Optional[builtins.str]:
        '''Prefix for plural metric names of activity actions.

        :default: - No such metrics
        '''
        result = self._values.get("metric_prefix_plural")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_prefix_singular(self) -> typing.Optional[builtins.str]:
        '''Prefix for singular metric names of activity actions.

        :default: - No such metrics
        '''
        result = self._values.get("metric_prefix_singular")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskMetricsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TaskRole(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_stepfunctions.TaskRole",
):
    '''Role to be assumed by the State Machine's execution role for invoking a task's resource.

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html#task-state-fields
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        
        # submit_lambda: lambda.Function
        # iam_role: iam.Role
        
        
        # use a fixed role for all task invocations
        role = sfn.TaskRole.from_role(iam_role)
        # or use a json expression to resolve the role at runtime based on task inputs
        # const role = sfn.TaskRole.fromRoleArnJsonPath('$.RoleArn');
        
        submit_job = tasks.LambdaInvoke(self, "Submit Job",
            lambda_function=submit_lambda,
            output_path="$.Payload",
            # use credentials
            credentials=sfn.Credentials(role=role)
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromRole")
    @builtins.classmethod
    def from_role(cls, role: _IRole_235f5d8e) -> "TaskRole":
        '''Construct a task role based on the provided IAM Role.

        :param role: IAM Role.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bddea2e373d15cc4e0247b91d3bca3f413aeb2470100f4983965f64d4e53db0)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast("TaskRole", jsii.sinvoke(cls, "fromRole", [role]))

    @jsii.member(jsii_name="fromRoleArnJsonPath")
    @builtins.classmethod
    def from_role_arn_json_path(cls, expression: builtins.str) -> "TaskRole":
        '''Construct a task role retrieved from task inputs using a json expression.

        :param expression: json expression to roleArn.

        Example::

            sfn.TaskRole.from_role_arn_json_path("$.RoleArn")
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f0576900770ad89340628b613309cb0873d7789836eb9f1f1a5eb5eea3129f9)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        return typing.cast("TaskRole", jsii.sinvoke(cls, "fromRoleArnJsonPath", [expression]))

    @builtins.property
    @jsii.member(jsii_name="resource")
    @abc.abstractmethod
    def resource(self) -> builtins.str:
        '''Retrieves the resource for use in IAM Policies for this TaskRole.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    @abc.abstractmethod
    def role_arn(self) -> builtins.str:
        '''Retrieves the roleArn for this TaskRole.'''
        ...


class _TaskRoleProxy(TaskRole):
    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        '''Retrieves the resource for use in IAM Policies for this TaskRole.'''
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''Retrieves the roleArn for this TaskRole.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, TaskRole).__jsii_proxy_class__ = lambda : _TaskRoleProxy


@jsii.implements(INextable)
class TaskStateBase(
    State,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_stepfunctions.TaskStateBase",
):
    '''Define a Task state in the state machine.

    Reaching a Task state causes some work to be executed, represented by the
    Task's resource property. Task constructs represent a generic Amazon
    States Language Task.

    For some resource types, more specific subclasses of Task may be available
    which are more convenient to use.
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union[Credentials, typing.Dict[builtins.str, typing.Any]]] = None,
        heartbeat: typing.Optional[_Duration_4839e8c3] = None,
        heartbeat_timeout: typing.Optional["Timeout"] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
        task_timeout: typing.Optional["Timeout"] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param comment: An optional description for this state. Default: - No comment
        :param credentials: Credentials for an IAM Role that the State Machine assumes for executing the task. This enables cross-account resource invocations. Default: - None (Task is executed using the State Machine's execution role)
        :param heartbeat: (deprecated) Timeout for the heartbeat. Default: - None
        :param heartbeat_timeout: Timeout for the heartbeat. [disable-awslint:duration-prop-type] is needed because all props interface in aws-stepfunctions-tasks extend this interface Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns. Depending on the AWS Service, the Service Integration Pattern availability will vary. Default: - ``IntegrationPattern.REQUEST_RESPONSE`` for most tasks. ``IntegrationPattern.RUN_JOB`` for the following exceptions: ``BatchSubmitJob``, ``EmrAddStep``, ``EmrCreateCluster``, ``EmrTerminationCluster``, and ``EmrContainersStartJobRun``.
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        :param task_timeout: Timeout for the task. [disable-awslint:duration-prop-type] is needed because all props interface in aws-stepfunctions-tasks extend this interface Default: - None
        :param timeout: (deprecated) Timeout for the task. Default: - None
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8030332c4c85b7a6f12c27dd03b5ae36fd9b38ad46888955d3d5325978e42311)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TaskStateBaseProps(
            comment=comment,
            credentials=credentials,
            heartbeat=heartbeat,
            heartbeat_timeout=heartbeat_timeout,
            input_path=input_path,
            integration_pattern=integration_pattern,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            state_name=state_name,
            task_timeout=task_timeout,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addCatch")
    def add_catch(
        self,
        handler: IChainable,
        *,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        result_path: typing.Optional[builtins.str] = None,
    ) -> "TaskStateBase":
        '''Add a recovery handler for this state.

        When a particular error occurs, execution will continue at the error
        handler instead of failing the state machine execution.

        :param handler: -
        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value JsonPath.DISCARD, which will cause the error data to be discarded. Default: $
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__661e0a128e151fbb1312f41cea74fbc148d98cfa524d7238bc6d0994bff443e4)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = CatchProps(errors=errors, result_path=result_path)

        return typing.cast("TaskStateBase", jsii.invoke(self, "addCatch", [handler, props]))

    @jsii.member(jsii_name="addRetry")
    def add_retry(
        self,
        *,
        backoff_rate: typing.Optional[jsii.Number] = None,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        interval: typing.Optional[_Duration_4839e8c3] = None,
        jitter_strategy: typing.Optional[JitterType] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        max_delay: typing.Optional[_Duration_4839e8c3] = None,
    ) -> "TaskStateBase":
        '''Add retry configuration for this state.

        This controls if and how the execution will be retried if a particular
        error occurs.

        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param jitter_strategy: Introduces a randomization over the retry interval. Default: - No jitter strategy
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3
        :param max_delay: Maximum limit on retry interval growth during exponential backoff. Default: - No max delay
        '''
        props = RetryProps(
            backoff_rate=backoff_rate,
            errors=errors,
            interval=interval,
            jitter_strategy=jitter_strategy,
            max_attempts=max_attempts,
            max_delay=max_delay,
        )

        return typing.cast("TaskStateBase", jsii.invoke(self, "addRetry", [props]))

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
        '''Return the given named metric for this Task.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e107390a3e2550b832e771f6471431f1576a6bdab08445ca9d4fef451ab0888)
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

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(
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
        '''Metric for the number of times this activity fails.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFailed", [props]))

    @jsii.member(jsii_name="metricHeartbeatTimedOut")
    def metric_heartbeat_timed_out(
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
        '''Metric for the number of times the heartbeat times out for this activity.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricHeartbeatTimedOut", [props]))

    @jsii.member(jsii_name="metricRunTime")
    def metric_run_time(
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
        '''The interval, in milliseconds, between the time the Task starts and the time it closes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricRunTime", [props]))

    @jsii.member(jsii_name="metricScheduled")
    def metric_scheduled(
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
        '''Metric for the number of times this activity is scheduled.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricScheduled", [props]))

    @jsii.member(jsii_name="metricScheduleTime")
    def metric_schedule_time(
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
        '''The interval, in milliseconds, for which the activity stays in the schedule state.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricScheduleTime", [props]))

    @jsii.member(jsii_name="metricStarted")
    def metric_started(
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
        '''Metric for the number of times this activity is started.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricStarted", [props]))

    @jsii.member(jsii_name="metricSucceeded")
    def metric_succeeded(
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
        '''Metric for the number of times this activity succeeds.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSucceeded", [props]))

    @jsii.member(jsii_name="metricTime")
    def metric_time(
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
        '''The interval, in milliseconds, between the time the activity is scheduled and the time it closes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTime", [props]))

    @jsii.member(jsii_name="metricTimedOut")
    def metric_timed_out(
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
        '''Metric for the number of times this activity times out.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTimedOut", [props]))

    @jsii.member(jsii_name="next")
    def next(self, next: IChainable) -> "Chain":
        '''Continue normal execution with the given state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec5d5503bc58bc8692d34bfb6d62f6cd19c7cbd72d15cfc1e421a14b3a77eeb4)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast("Chain", jsii.invoke(self, "next", [next]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @jsii.member(jsii_name="whenBoundToGraph")
    def _when_bound_to_graph(self, graph: StateGraph) -> None:
        '''Called whenever this state is bound to a graph.

        Can be overridden by subclasses.

        :param graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3476e23aff91128cb42df4fe5996139f3397e205600e914f57e1d211d4569d6)
            check_type(argname="argument graph", value=graph, expected_type=type_hints["graph"])
        return typing.cast(None, jsii.invoke(self, "whenBoundToGraph", [graph]))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    @abc.abstractmethod
    def _task_metrics(self) -> typing.Optional[TaskMetricsConfig]:
        ...

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    @abc.abstractmethod
    def _task_policies(self) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        ...


class _TaskStateBaseProxy(
    TaskStateBase,
    jsii.proxy_for(State), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="taskMetrics")
    def _task_metrics(self) -> typing.Optional[TaskMetricsConfig]:
        return typing.cast(typing.Optional[TaskMetricsConfig], jsii.get(self, "taskMetrics"))

    @builtins.property
    @jsii.member(jsii_name="taskPolicies")
    def _task_policies(self) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], jsii.get(self, "taskPolicies"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, TaskStateBase).__jsii_proxy_class__ = lambda : _TaskStateBaseProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.TaskStateBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "credentials": "credentials",
        "heartbeat": "heartbeat",
        "heartbeat_timeout": "heartbeatTimeout",
        "input_path": "inputPath",
        "integration_pattern": "integrationPattern",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "state_name": "stateName",
        "task_timeout": "taskTimeout",
        "timeout": "timeout",
    },
)
class TaskStateBaseProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union[Credentials, typing.Dict[builtins.str, typing.Any]]] = None,
        heartbeat: typing.Optional[_Duration_4839e8c3] = None,
        heartbeat_timeout: typing.Optional["Timeout"] = None,
        input_path: typing.Optional[builtins.str] = None,
        integration_pattern: typing.Optional[IntegrationPattern] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
        task_timeout: typing.Optional["Timeout"] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Props that are common to all tasks.

        :param comment: An optional description for this state. Default: - No comment
        :param credentials: Credentials for an IAM Role that the State Machine assumes for executing the task. This enables cross-account resource invocations. Default: - None (Task is executed using the State Machine's execution role)
        :param heartbeat: (deprecated) Timeout for the heartbeat. Default: - None
        :param heartbeat_timeout: Timeout for the heartbeat. [disable-awslint:duration-prop-type] is needed because all props interface in aws-stepfunctions-tasks extend this interface Default: - None
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: - The entire task input (JSON path '$')
        :param integration_pattern: AWS Step Functions integrates with services directly in the Amazon States Language. You can control these AWS services using service integration patterns. Depending on the AWS Service, the Service Integration Pattern availability will vary. Default: - ``IntegrationPattern.REQUEST_RESPONSE`` for most tasks. ``IntegrationPattern.RUN_JOB`` for the following exceptions: ``BatchSubmitJob``, ``EmrAddStep``, ``EmrCreateCluster``, ``EmrTerminationCluster``, and ``EmrContainersStartJobRun``.
        :param output_path: JSONPath expression to select select a portion of the state output to pass to the next state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: - The entire JSON node determined by the state input, the task result, and resultPath is passed to the next state (JSON path '$')
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: - Replaces the entire input with the result (JSON path '$')
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        :param task_timeout: Timeout for the task. [disable-awslint:duration-prop-type] is needed because all props interface in aws-stepfunctions-tasks extend this interface Default: - None
        :param timeout: (deprecated) Timeout for the task. Default: - None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # result_selector: Any
            # task_role: stepfunctions.TaskRole
            # timeout: stepfunctions.Timeout
            
            task_state_base_props = stepfunctions.TaskStateBaseProps(
                comment="comment",
                credentials=stepfunctions.Credentials(
                    role=task_role
                ),
                heartbeat=cdk.Duration.minutes(30),
                heartbeat_timeout=timeout,
                input_path="inputPath",
                integration_pattern=stepfunctions.IntegrationPattern.REQUEST_RESPONSE,
                output_path="outputPath",
                result_path="resultPath",
                result_selector={
                    "result_selector_key": result_selector
                },
                state_name="stateName",
                task_timeout=timeout,
                timeout=cdk.Duration.minutes(30)
            )
        '''
        if isinstance(credentials, dict):
            credentials = Credentials(**credentials)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__487ae196f9ce32bf6886dc0cf55352b7b5f5a24cc25636bf22f525ed68b9944b)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument heartbeat", value=heartbeat, expected_type=type_hints["heartbeat"])
            check_type(argname="argument heartbeat_timeout", value=heartbeat_timeout, expected_type=type_hints["heartbeat_timeout"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument integration_pattern", value=integration_pattern, expected_type=type_hints["integration_pattern"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
            check_type(argname="argument task_timeout", value=task_timeout, expected_type=type_hints["task_timeout"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if credentials is not None:
            self._values["credentials"] = credentials
        if heartbeat is not None:
            self._values["heartbeat"] = heartbeat
        if heartbeat_timeout is not None:
            self._values["heartbeat_timeout"] = heartbeat_timeout
        if input_path is not None:
            self._values["input_path"] = input_path
        if integration_pattern is not None:
            self._values["integration_pattern"] = integration_pattern
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if state_name is not None:
            self._values["state_name"] = state_name
        if task_timeout is not None:
            self._values["task_timeout"] = task_timeout
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: - No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(self) -> typing.Optional[Credentials]:
        '''Credentials for an IAM Role that the State Machine assumes for executing the task.

        This enables cross-account resource invocations.

        :default: - None (Task is executed using the State Machine's execution role)

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-access-cross-acct-resources.html
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[Credentials], result)

    @builtins.property
    def heartbeat(self) -> typing.Optional[_Duration_4839e8c3]:
        '''(deprecated) Timeout for the heartbeat.

        :default: - None

        :deprecated: use ``heartbeatTimeout``

        :stability: deprecated
        '''
        result = self._values.get("heartbeat")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def heartbeat_timeout(self) -> typing.Optional["Timeout"]:
        '''Timeout for the heartbeat.

        [disable-awslint:duration-prop-type] is needed because all props interface in
        aws-stepfunctions-tasks extend this interface

        :default: - None
        '''
        result = self._values.get("heartbeat_timeout")
        return typing.cast(typing.Optional["Timeout"], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: - The entire task input (JSON path '$')
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_pattern(self) -> typing.Optional[IntegrationPattern]:
        '''AWS Step Functions integrates with services directly in the Amazon States Language.

        You can control these AWS services using service integration patterns.

        Depending on the AWS Service, the Service Integration Pattern availability will vary.

        :default:

        - ``IntegrationPattern.REQUEST_RESPONSE`` for most tasks.
        ``IntegrationPattern.RUN_JOB`` for the following exceptions:
        ``BatchSubmitJob``, ``EmrAddStep``, ``EmrCreateCluster``, ``EmrTerminationCluster``, and ``EmrContainersStartJobRun``.

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/connect-supported-services.html
        '''
        result = self._values.get("integration_pattern")
        return typing.cast(typing.Optional[IntegrationPattern], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select select a portion of the state output to pass to the next state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default:

        - The entire JSON node determined by the state input, the task result,
        and resultPath is passed to the next state (JSON path '$')
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: - Replaces the entire input with the result (JSON path '$')
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def task_timeout(self) -> typing.Optional["Timeout"]:
        '''Timeout for the task.

        [disable-awslint:duration-prop-type] is needed because all props interface in
        aws-stepfunctions-tasks extend this interface

        :default: - None
        '''
        result = self._values.get("task_timeout")
        return typing.cast(typing.Optional["Timeout"], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''(deprecated) Timeout for the task.

        :default: - None

        :deprecated: use ``taskTimeout``

        :stability: deprecated
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskStateBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Timeout(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Timeout",
):
    '''Timeout for a task or heartbeat.

    :exampleMetadata: infused

    Example::

        tasks.GlueStartJobRun(self, "Task",
            glue_job_name="my-glue-job",
            arguments=sfn.TaskInput.from_object({
                "key": "value"
            }),
            task_timeout=sfn.Timeout.duration(Duration.minutes(30)),
            notify_delay_after=Duration.minutes(5)
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="at")
    @builtins.classmethod
    def at(cls, path: builtins.str) -> "Timeout":
        '''Use a dynamic timeout specified by a path in the state input.

        The path must select a field whose value is a positive integer.

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede5a9c52734b5209acc0043a69f8b4333ea0d0bf32a48bb028d1695fc6077b9)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast("Timeout", jsii.sinvoke(cls, "at", [path]))

    @jsii.member(jsii_name="duration")
    @builtins.classmethod
    def duration(cls, duration: _Duration_4839e8c3) -> "Timeout":
        '''Use a duration as timeout.

        :param duration: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a04d027f66b61507aa552be04c2ce9593fc80d23f348ffb16cd24bef17942c5)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
        return typing.cast("Timeout", jsii.sinvoke(cls, "duration", [duration]))

    @builtins.property
    @jsii.member(jsii_name="path")
    @abc.abstractmethod
    def path(self) -> typing.Optional[builtins.str]:
        '''Path for this timeout.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="seconds")
    @abc.abstractmethod
    def seconds(self) -> typing.Optional[jsii.Number]:
        '''Seconds for this timeout.'''
        ...


class _TimeoutProxy(Timeout):
    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> typing.Optional[builtins.str]:
        '''Path for this timeout.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> typing.Optional[jsii.Number]:
        '''Seconds for this timeout.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "seconds"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Timeout).__jsii_proxy_class__ = lambda : _TimeoutProxy


@jsii.implements(INextable)
class Wait(
    State,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Wait",
):
    '''Define a Wait state in the state machine.

    A Wait state can be used to delay execution of the state machine for a while.

    :exampleMetadata: infused

    Example::

        convert_to_seconds = tasks.EvaluateExpression(self, "Convert to seconds",
            expression="$.waitMilliseconds / 1000",
            result_path="$.waitSeconds"
        )
        
        create_message = tasks.EvaluateExpression(self, "Create message",
            # Note: this is a string inside a string.
            expression="`Now waiting ${$.waitSeconds} seconds...`",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            result_path="$.message"
        )
        
        publish_message = tasks.SnsPublish(self, "Publish message",
            topic=sns.Topic(self, "cool-topic"),
            message=sfn.TaskInput.from_json_path_at("$.message"),
            result_path="$.sns"
        )
        
        wait = sfn.Wait(self, "Wait",
            time=sfn.WaitTime.seconds_path("$.waitSeconds")
        )
        
        sfn.StateMachine(self, "StateMachine",
            definition=convert_to_seconds.next(create_message).next(publish_message).next(wait)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        time: "WaitTime",
        comment: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param time: Wait duration.
        :param comment: An optional description for this state. Default: No comment
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6a8ce927e9d411d4263a43306a0e94bd7a5d563bd35e990ab82dbb660c79604)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = WaitProps(time=time, comment=comment, state_name=state_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="next")
    def next(self, next: IChainable) -> "Chain":
        '''Continue normal execution with the given state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae1afef777a31475bd858e03eee2febe97f62b64e27252472e23b8636248fb2)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast("Chain", jsii.invoke(self, "next", [next]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.WaitProps",
    jsii_struct_bases=[],
    name_mapping={"time": "time", "comment": "comment", "state_name": "stateName"},
)
class WaitProps:
    def __init__(
        self,
        *,
        time: "WaitTime",
        comment: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a Wait state.

        :param time: Wait duration.
        :param comment: An optional description for this state. Default: No comment
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name

        :exampleMetadata: infused

        Example::

            convert_to_seconds = tasks.EvaluateExpression(self, "Convert to seconds",
                expression="$.waitMilliseconds / 1000",
                result_path="$.waitSeconds"
            )
            
            create_message = tasks.EvaluateExpression(self, "Create message",
                # Note: this is a string inside a string.
                expression="`Now waiting ${$.waitSeconds} seconds...`",
                runtime=lambda_.Runtime.NODEJS_LATEST,
                result_path="$.message"
            )
            
            publish_message = tasks.SnsPublish(self, "Publish message",
                topic=sns.Topic(self, "cool-topic"),
                message=sfn.TaskInput.from_json_path_at("$.message"),
                result_path="$.sns"
            )
            
            wait = sfn.Wait(self, "Wait",
                time=sfn.WaitTime.seconds_path("$.waitSeconds")
            )
            
            sfn.StateMachine(self, "StateMachine",
                definition=convert_to_seconds.next(create_message).next(publish_message).next(wait)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534eb46b5e3f50b25dea609490a5fd97e2e7f56c6eeed5ea19d37b6997865461)
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "time": time,
        }
        if comment is not None:
            self._values["comment"] = comment
        if state_name is not None:
            self._values["state_name"] = state_name

    @builtins.property
    def time(self) -> "WaitTime":
        '''Wait duration.'''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast("WaitTime", result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WaitProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WaitTime(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.WaitTime",
):
    '''Represents the Wait state which delays a state machine from continuing for a specified time.

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-wait-state.html
    :exampleMetadata: infused

    Example::

        convert_to_seconds = tasks.EvaluateExpression(self, "Convert to seconds",
            expression="$.waitMilliseconds / 1000",
            result_path="$.waitSeconds"
        )
        
        create_message = tasks.EvaluateExpression(self, "Create message",
            # Note: this is a string inside a string.
            expression="`Now waiting ${$.waitSeconds} seconds...`",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            result_path="$.message"
        )
        
        publish_message = tasks.SnsPublish(self, "Publish message",
            topic=sns.Topic(self, "cool-topic"),
            message=sfn.TaskInput.from_json_path_at("$.message"),
            result_path="$.sns"
        )
        
        wait = sfn.Wait(self, "Wait",
            time=sfn.WaitTime.seconds_path("$.waitSeconds")
        )
        
        sfn.StateMachine(self, "StateMachine",
            definition=convert_to_seconds.next(create_message).next(publish_message).next(wait)
        )
    '''

    @jsii.member(jsii_name="duration")
    @builtins.classmethod
    def duration(cls, duration: _Duration_4839e8c3) -> "WaitTime":
        '''Wait a fixed amount of time.

        :param duration: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a809799722bcdc0c6cece03ff859948273709f66e461d30e317ffbd0ab85aca2)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
        return typing.cast("WaitTime", jsii.sinvoke(cls, "duration", [duration]))

    @jsii.member(jsii_name="secondsPath")
    @builtins.classmethod
    def seconds_path(cls, path: builtins.str) -> "WaitTime":
        '''Wait for a number of seconds stored in the state object.

        Example value: ``$.waitSeconds``

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbd7acf00a5586f287932ed2fd2b8aea94218c4e4ed6ce940a9b4f871ce7f4ce)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast("WaitTime", jsii.sinvoke(cls, "secondsPath", [path]))

    @jsii.member(jsii_name="timestamp")
    @builtins.classmethod
    def timestamp(cls, timestamp: builtins.str) -> "WaitTime":
        '''Wait until the given ISO8601 timestamp.

        Example value: ``2016-03-14T01:59:00Z``

        :param timestamp: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74e6bb97aa64089395900b447ec0f2759ffee7f85b56e84eeaded8aa5dc0a3b2)
            check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
        return typing.cast("WaitTime", jsii.sinvoke(cls, "timestamp", [timestamp]))

    @jsii.member(jsii_name="timestampPath")
    @builtins.classmethod
    def timestamp_path(cls, path: builtins.str) -> "WaitTime":
        '''Wait until a timestamp found in the state object.

        Example value: ``$.waitTimestamp``

        :param path: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d88e6966e5553a37e050d3139be3d625237f07f7a3a9c23fa5bb2232f8c50be0)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast("WaitTime", jsii.sinvoke(cls, "timestampPath", [path]))


@jsii.implements(IActivity)
class Activity(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Activity",
):
    '''Define a new Step Functions Activity.

    :exampleMetadata: infused

    Example::

        activity = sfn.Activity(self, "Activity")
        
        role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )
        
        activity.grant(role, "states:SendTaskSuccess")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        activity_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param activity_name: The name for this activity. Default: - If not supplied, a name is generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9e3c9e855deb3c2b532345b0d2587dc14ad685d296794311bbf280ab9f6b10d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ActivityProps(activity_name=activity_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromActivityArn")
    @builtins.classmethod
    def from_activity_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        activity_arn: builtins.str,
    ) -> IActivity:
        '''Construct an Activity from an existing Activity ARN.

        :param scope: -
        :param id: -
        :param activity_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23b5f89f13e4afd1f578e47dbd171c4eb80f5231c5844de3057b40bd4e21f11)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument activity_arn", value=activity_arn, expected_type=type_hints["activity_arn"])
        return typing.cast(IActivity, jsii.sinvoke(cls, "fromActivityArn", [scope, id, activity_arn]))

    @jsii.member(jsii_name="fromActivityName")
    @builtins.classmethod
    def from_activity_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        activity_name: builtins.str,
    ) -> IActivity:
        '''Construct an Activity from an existing Activity Name.

        :param scope: -
        :param id: -
        :param activity_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8ac7cbf2053f3b4870981fbfd4f3dd21553e4a66f1c2462b2aa64dfa477566)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument activity_name", value=activity_name, expected_type=type_hints["activity_name"])
        return typing.cast(IActivity, jsii.sinvoke(cls, "fromActivityName", [scope, id, activity_name]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        identity: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the given identity permissions on this Activity.

        :param identity: The principal.
        :param actions: The list of desired actions.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d112510c9f361d871db6717bbfc59060fea12f921f3593ef09bffe88a48574)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [identity, *actions]))

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
        '''Return the given named metric for this Activity.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f960b5875dcb81c7f4b6e91c03015375df2e5c6bb3da84f476bf59c2baaba3e)
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

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(
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
        '''Metric for the number of times this activity fails.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFailed", [props]))

    @jsii.member(jsii_name="metricHeartbeatTimedOut")
    def metric_heartbeat_timed_out(
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
        '''Metric for the number of times the heartbeat times out for this activity.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricHeartbeatTimedOut", [props]))

    @jsii.member(jsii_name="metricRunTime")
    def metric_run_time(
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
        '''The interval, in milliseconds, between the time the activity starts and the time it closes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricRunTime", [props]))

    @jsii.member(jsii_name="metricScheduled")
    def metric_scheduled(
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
        '''Metric for the number of times this activity is scheduled.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricScheduled", [props]))

    @jsii.member(jsii_name="metricScheduleTime")
    def metric_schedule_time(
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
        '''The interval, in milliseconds, for which the activity stays in the schedule state.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricScheduleTime", [props]))

    @jsii.member(jsii_name="metricStarted")
    def metric_started(
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
        '''Metric for the number of times this activity is started.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricStarted", [props]))

    @jsii.member(jsii_name="metricSucceeded")
    def metric_succeeded(
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
        '''Metric for the number of times this activity succeeds.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSucceeded", [props]))

    @jsii.member(jsii_name="metricTime")
    def metric_time(
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
        '''The interval, in milliseconds, between the time the activity is scheduled and the time it closes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: average over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTime", [props]))

    @jsii.member(jsii_name="metricTimedOut")
    def metric_timed_out(
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
        '''Metric for the number of times this activity times out.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTimedOut", [props]))

    @builtins.property
    @jsii.member(jsii_name="activityArn")
    def activity_arn(self) -> builtins.str:
        '''The ARN of the activity.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "activityArn"))

    @builtins.property
    @jsii.member(jsii_name="activityName")
    def activity_name(self) -> builtins.str:
        '''The name of the activity.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "activityName"))


@jsii.implements(IChainable)
class Chain(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_stepfunctions.Chain"):
    '''A collection of states to chain onto.

    A Chain has a start and zero or more chainable ends. If there are
    zero ends, calling next() on the Chain will fail.

    :exampleMetadata: infused

    Example::

        map = sfn.Map(self, "Map State",
            max_concurrency=1,
            items_path=sfn.JsonPath.string_at("$.inputForMap"),
            item_selector={
                "item": sfn.JsonPath.string_at("$.Map.Item.Value")
            },
            result_path="$.mapOutput"
        )
        
        # The Map iterator can contain a IChainable, which can be an individual or multiple steps chained together.
        # Below example is with a Choice and Pass step
        choice = sfn.Choice(self, "Choice")
        condition1 = sfn.Condition.string_equals("$.item.status", "SUCCESS")
        step1 = sfn.Pass(self, "Step1")
        step2 = sfn.Pass(self, "Step2")
        finish = sfn.Pass(self, "Finish")
        
        definition = choice.when(condition1, step1).otherwise(step2).afterwards().next(finish)
        
        map.item_processor(definition)
    '''

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(
        cls,
        start_state: State,
        end_states: typing.Sequence[INextable],
        last_added: IChainable,
    ) -> "Chain":
        '''Make a Chain with specific start and end states, and a last-added Chainable.

        :param start_state: -
        :param end_states: -
        :param last_added: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26a438e6d1ba5d4cefba34fbd2fbe2750e8c479b9d8629bb5a75c0c294b63f1a)
            check_type(argname="argument start_state", value=start_state, expected_type=type_hints["start_state"])
            check_type(argname="argument end_states", value=end_states, expected_type=type_hints["end_states"])
            check_type(argname="argument last_added", value=last_added, expected_type=type_hints["last_added"])
        return typing.cast("Chain", jsii.sinvoke(cls, "custom", [start_state, end_states, last_added]))

    @jsii.member(jsii_name="sequence")
    @builtins.classmethod
    def sequence(cls, start: IChainable, next: IChainable) -> "Chain":
        '''Make a Chain with the start from one chain and the ends from another.

        :param start: -
        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c955028ecc98936f323c8550ebfcb4aeef25333244714448c6f9471f6ee0ad4f)
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast("Chain", jsii.sinvoke(cls, "sequence", [start, next]))

    @jsii.member(jsii_name="start")
    @builtins.classmethod
    def start(cls, state: IChainable) -> "Chain":
        '''Begin a new Chain from one chainable.

        :param state: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee2c65d541581403b83500bc7df204a5106888551ba6bd48d4870081c4fd4cc5)
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        return typing.cast("Chain", jsii.sinvoke(cls, "start", [state]))

    @jsii.member(jsii_name="next")
    def next(self, next: IChainable) -> "Chain":
        '''Continue normal execution with the given state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd744fb658532d41afa54a85d0b054476b1228d7172fa8e1c494c14f2fa7d5f)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast("Chain", jsii.invoke(self, "next", [next]))

    @jsii.member(jsii_name="toSingleState")
    def to_single_state(
        self,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> "Parallel":
        '''Return a single state that encompasses all states in the chain.

        This can be used to add error handling to a sequence of states.

        Be aware that this changes the result of the inner state machine
        to be an array with the result of the state machine in it. Adjust
        your paths accordingly. For example, change 'outputPath' to
        '$[0]'.

        :param id: -
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__468194d7b14012a289ab0c26efcba49fbd09832b9f87d79467e6334c81f8495e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ParallelProps(
            comment=comment,
            input_path=input_path,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            state_name=state_name,
        )

        return typing.cast("Parallel", jsii.invoke(self, "toSingleState", [id, props]))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''The chainable end state(s) of this chain.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Identify this Chain.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="startState")
    def start_state(self) -> State:
        '''The start state of this chain.'''
        return typing.cast(State, jsii.get(self, "startState"))


class ChainDefinitionBody(
    DefinitionBody,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.ChainDefinitionBody",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_stepfunctions as stepfunctions
        
        # chainable: stepfunctions.IChainable
        
        chain_definition_body = stepfunctions.ChainDefinitionBody.from_chainable(chainable)
    '''

    def __init__(self, chainable: IChainable) -> None:
        '''
        :param chainable: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd08795a00486d8e3c10949ac36b6c93109ecc1bb3a98a3e10990fe66c603599)
            check_type(argname="argument chainable", value=chainable, expected_type=type_hints["chainable"])
        jsii.create(self.__class__, self, [chainable])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        _sfn_principal: _IPrincipal_539bb2fd,
        sfn_props: typing.Union[StateMachineProps, typing.Dict[builtins.str, typing.Any]],
        graph: typing.Optional[StateGraph] = None,
    ) -> DefinitionConfig:
        '''
        :param scope: -
        :param _sfn_principal: -
        :param sfn_props: -
        :param graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e36acb57c00ddfc834d6027c29b11bab26d8b33890707c567bc4f7804a9786f2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument _sfn_principal", value=_sfn_principal, expected_type=type_hints["_sfn_principal"])
            check_type(argname="argument sfn_props", value=sfn_props, expected_type=type_hints["sfn_props"])
            check_type(argname="argument graph", value=graph, expected_type=type_hints["graph"])
        return typing.cast(DefinitionConfig, jsii.invoke(self, "bind", [scope, _sfn_principal, sfn_props, graph]))

    @builtins.property
    @jsii.member(jsii_name="chainable")
    def chainable(self) -> IChainable:
        return typing.cast(IChainable, jsii.get(self, "chainable"))


class Choice(
    State,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Choice",
):
    '''Define a Choice in the state machine.

    A choice state can be used to make decisions based on the execution
    state.

    :exampleMetadata: infused

    Example::

        map = sfn.Map(self, "Map State",
            max_concurrency=1,
            items_path=sfn.JsonPath.string_at("$.inputForMap"),
            item_selector={
                "item": sfn.JsonPath.string_at("$.Map.Item.Value")
            },
            result_path="$.mapOutput"
        )
        
        # The Map iterator can contain a IChainable, which can be an individual or multiple steps chained together.
        # Below example is with a Choice and Pass step
        choice = sfn.Choice(self, "Choice")
        condition1 = sfn.Condition.string_equals("$.item.status", "SUCCESS")
        step1 = sfn.Pass(self, "Step1")
        step2 = sfn.Pass(self, "Step2")
        finish = sfn.Pass(self, "Finish")
        
        definition = choice.when(condition1, step1).otherwise(step2).afterwards().next(finish)
        
        map.item_processor(definition)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29c27d2454927afdcf01784360c45c98368486d465f54265c1199aa70baaae72)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ChoiceProps(
            comment=comment,
            input_path=input_path,
            output_path=output_path,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="afterwards")
    def afterwards(
        self,
        *,
        include_error_handlers: typing.Optional[builtins.bool] = None,
        include_otherwise: typing.Optional[builtins.bool] = None,
    ) -> Chain:
        '''Return a Chain that contains all reachable end states from this Choice.

        Use this to combine all possible choice paths back.

        :param include_error_handlers: Whether to include error handling states. If this is true, all states which are error handlers (added through 'onError') and states reachable via error handlers will be included as well. Default: false
        :param include_otherwise: Whether to include the default/otherwise transition for the current Choice state. If this is true and the current Choice does not have a default outgoing transition, one will be added included when .next() is called on the chain. Default: false
        '''
        options = AfterwardsOptions(
            include_error_handlers=include_error_handlers,
            include_otherwise=include_otherwise,
        )

        return typing.cast(Chain, jsii.invoke(self, "afterwards", [options]))

    @jsii.member(jsii_name="otherwise")
    def otherwise(self, def_: IChainable) -> "Choice":
        '''If none of the given conditions match, continue execution with the given state.

        If no conditions match and no otherwise() has been given, an execution
        error will be raised.

        :param def_: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58e659f8b3dba6c37e918b57bca058880f69e9f4da0a230edb80f223a37fbc82)
            check_type(argname="argument def_", value=def_, expected_type=type_hints["def_"])
        return typing.cast("Choice", jsii.invoke(self, "otherwise", [def_]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @jsii.member(jsii_name="when")
    def when(
        self,
        condition: Condition,
        next: IChainable,
        *,
        comment: typing.Optional[builtins.str] = None,
    ) -> "Choice":
        '''If the given condition matches, continue execution with the given state.

        :param condition: -
        :param next: -
        :param comment: An optional description for the choice transition. Default: No comment
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5351e3ee5e1f4b5b58ec322e57749fdd65cdc8bb76443318ef63b4eedc5cb0b)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        options = ChoiceTransitionOptions(comment=comment)

        return typing.cast("Choice", jsii.invoke(self, "when", [condition, next, options]))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))


@jsii.implements(IChainable, INextable)
class CustomState(
    State,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.CustomState",
):
    '''State defined by supplying Amazon States Language (ASL) in the state machine.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_dynamodb as dynamodb
        
        
        # create a table
        table = dynamodb.Table(self, "montable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        final_status = sfn.Pass(self, "final step")
        
        # States language JSON to put an item into DynamoDB
        # snippet generated from https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-code-snippet.html#tutorial-code-snippet-1
        state_json = {
            "Type": "Task",
            "Resource": "arn:aws:states:::dynamodb:putItem",
            "Parameters": {
                "TableName": table.table_name,
                "Item": {
                    "id": {
                        "S": "MyEntry"
                    }
                }
            },
            "ResultPath": null
        }
        
        # custom state which represents a task to insert data into DynamoDB
        custom = sfn.CustomState(self, "my custom task",
            state_json=state_json
        )
        
        # catch errors with addCatch
        error_handler = sfn.Pass(self, "handle failure")
        custom.add_catch(error_handler)
        
        # retry the task if something goes wrong
        custom.add_retry(
            errors=[sfn.Errors.ALL],
            interval=Duration.seconds(10),
            max_attempts=5
        )
        
        chain = sfn.Chain.start(custom).next(final_status)
        
        sm = sfn.StateMachine(self, "StateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(chain),
            timeout=Duration.seconds(30),
            comment="a super cool state machine"
        )
        
        # don't forget permissions. You need to assign them
        table.grant_write_data(sm)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        state_json: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param state_json: Amazon States Language (JSON-based) definition of the state.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab8400575bd03faff673b28e1d5b185298520835ed4e6586fba73ccac57c6f0e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CustomStateProps(state_json=state_json)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addCatch")
    def add_catch(
        self,
        handler: IChainable,
        *,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        result_path: typing.Optional[builtins.str] = None,
    ) -> "CustomState":
        '''Add a recovery handler for this state.

        When a particular error occurs, execution will continue at the error
        handler instead of failing the state machine execution.

        :param handler: -
        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value JsonPath.DISCARD, which will cause the error data to be discarded. Default: $
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af51c0590f129eeca0846aafaf90162dc24f8f5c4a9df58d88432f4facb4ff08)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = CatchProps(errors=errors, result_path=result_path)

        return typing.cast("CustomState", jsii.invoke(self, "addCatch", [handler, props]))

    @jsii.member(jsii_name="addRetry")
    def add_retry(
        self,
        *,
        backoff_rate: typing.Optional[jsii.Number] = None,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        interval: typing.Optional[_Duration_4839e8c3] = None,
        jitter_strategy: typing.Optional[JitterType] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        max_delay: typing.Optional[_Duration_4839e8c3] = None,
    ) -> "CustomState":
        '''Add retry configuration for this state.

        This controls if and how the execution will be retried if a particular
        error occurs.

        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param jitter_strategy: Introduces a randomization over the retry interval. Default: - No jitter strategy
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3
        :param max_delay: Maximum limit on retry interval growth during exponential backoff. Default: - No max delay
        '''
        props = RetryProps(
            backoff_rate=backoff_rate,
            errors=errors,
            interval=interval,
            jitter_strategy=jitter_strategy,
            max_attempts=max_attempts,
            max_delay=max_delay,
        )

        return typing.cast("CustomState", jsii.invoke(self, "addRetry", [props]))

    @jsii.member(jsii_name="next")
    def next(self, next: IChainable) -> Chain:
        '''Continue normal execution with the given state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c55cf19adb97a87b3d9f8561497d58ec4f0dc221883c0d757f4bec5f4690cadd)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast(Chain, jsii.invoke(self, "next", [next]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Returns the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.DistributedMapProps",
    jsii_struct_bases=[MapBaseProps],
    name_mapping={
        "comment": "comment",
        "input_path": "inputPath",
        "item_selector": "itemSelector",
        "items_path": "itemsPath",
        "max_concurrency": "maxConcurrency",
        "max_concurrency_path": "maxConcurrencyPath",
        "output_path": "outputPath",
        "result_path": "resultPath",
        "result_selector": "resultSelector",
        "state_name": "stateName",
        "item_batcher": "itemBatcher",
        "item_reader": "itemReader",
        "label": "label",
        "map_execution_type": "mapExecutionType",
        "result_writer": "resultWriter",
        "tolerated_failure_count": "toleratedFailureCount",
        "tolerated_failure_count_path": "toleratedFailureCountPath",
        "tolerated_failure_percentage": "toleratedFailurePercentage",
        "tolerated_failure_percentage_path": "toleratedFailurePercentagePath",
    },
)
class DistributedMapProps(MapBaseProps):
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        items_path: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_concurrency_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
        item_batcher: typing.Optional[ItemBatcher] = None,
        item_reader: typing.Optional[IItemReader] = None,
        label: typing.Optional[builtins.str] = None,
        map_execution_type: typing.Optional[StateMachineType] = None,
        result_writer: typing.Optional[ResultWriter] = None,
        tolerated_failure_count: typing.Optional[jsii.Number] = None,
        tolerated_failure_count_path: typing.Optional[builtins.str] = None,
        tolerated_failure_percentage: typing.Optional[jsii.Number] = None,
        tolerated_failure_percentage_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for configuring a Distribute Map state.

        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param item_selector: The JSON that you want to override your default iteration input (mutually exclusive with ``parameters``). Default: $
        :param items_path: JSONPath expression to select the array to iterate over. Default: $
        :param max_concurrency: MaxConcurrency. An upper bound on the number of iterations you want running at once. Default: - full concurrency
        :param max_concurrency_path: MaxConcurrencyPath. A JsonPath that specifies the maximum concurrency dynamically from the state input. Default: - full concurrency
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        :param item_batcher: Specifies to process a group of items in a single child workflow execution. Default: - No itemBatcher
        :param item_reader: ItemReader. Configuration for where to read items dataset in S3 to iterate Default: - No itemReader
        :param label: Label. Unique name for the Distributed Map state added to each Map Run Default: - No label
        :param map_execution_type: MapExecutionType. The execution type of the distributed map state Default: StateMachineType.STANDARD
        :param result_writer: Configuration for S3 location in which to save Map Run results. Default: - No resultWriter
        :param tolerated_failure_count: ToleratedFailureCount. Number of failed items to tolerate in a Map Run, as static number Default: - No toleratedFailureCount
        :param tolerated_failure_count_path: ToleratedFailureCountPath. Number of failed items to tolerate in a Map Run, as JsonPath Default: - No toleratedFailureCountPath
        :param tolerated_failure_percentage: ToleratedFailurePercentage. Percentage of failed items to tolerate in a Map Run, as static number Default: - No toleratedFailurePercentage
        :param tolerated_failure_percentage_path: ToleratedFailurePercentagePath. Percentage of failed items to tolerate in a Map Run, as JsonPath Default: - No toleratedFailurePercentagePath

        :exampleMetadata: infused

        Example::

            distributed_map = sfn.DistributedMap(self, "Distributed Map State",
                max_concurrency=1,
                items_path=sfn.JsonPath.string_at("$.inputForMap")
            )
            distributed_map.item_processor(sfn.Pass(self, "Pass State"))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e484af477b46c0e70f635ed9610c7183f70c2184fd7a48f091a5477df9ee3d5d)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            check_type(argname="argument item_selector", value=item_selector, expected_type=type_hints["item_selector"])
            check_type(argname="argument items_path", value=items_path, expected_type=type_hints["items_path"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_concurrency_path", value=max_concurrency_path, expected_type=type_hints["max_concurrency_path"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
            check_type(argname="argument result_path", value=result_path, expected_type=type_hints["result_path"])
            check_type(argname="argument result_selector", value=result_selector, expected_type=type_hints["result_selector"])
            check_type(argname="argument state_name", value=state_name, expected_type=type_hints["state_name"])
            check_type(argname="argument item_batcher", value=item_batcher, expected_type=type_hints["item_batcher"])
            check_type(argname="argument item_reader", value=item_reader, expected_type=type_hints["item_reader"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument map_execution_type", value=map_execution_type, expected_type=type_hints["map_execution_type"])
            check_type(argname="argument result_writer", value=result_writer, expected_type=type_hints["result_writer"])
            check_type(argname="argument tolerated_failure_count", value=tolerated_failure_count, expected_type=type_hints["tolerated_failure_count"])
            check_type(argname="argument tolerated_failure_count_path", value=tolerated_failure_count_path, expected_type=type_hints["tolerated_failure_count_path"])
            check_type(argname="argument tolerated_failure_percentage", value=tolerated_failure_percentage, expected_type=type_hints["tolerated_failure_percentage"])
            check_type(argname="argument tolerated_failure_percentage_path", value=tolerated_failure_percentage_path, expected_type=type_hints["tolerated_failure_percentage_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if input_path is not None:
            self._values["input_path"] = input_path
        if item_selector is not None:
            self._values["item_selector"] = item_selector
        if items_path is not None:
            self._values["items_path"] = items_path
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_concurrency_path is not None:
            self._values["max_concurrency_path"] = max_concurrency_path
        if output_path is not None:
            self._values["output_path"] = output_path
        if result_path is not None:
            self._values["result_path"] = result_path
        if result_selector is not None:
            self._values["result_selector"] = result_selector
        if state_name is not None:
            self._values["state_name"] = state_name
        if item_batcher is not None:
            self._values["item_batcher"] = item_batcher
        if item_reader is not None:
            self._values["item_reader"] = item_reader
        if label is not None:
            self._values["label"] = label
        if map_execution_type is not None:
            self._values["map_execution_type"] = map_execution_type
        if result_writer is not None:
            self._values["result_writer"] = result_writer
        if tolerated_failure_count is not None:
            self._values["tolerated_failure_count"] = tolerated_failure_count
        if tolerated_failure_count_path is not None:
            self._values["tolerated_failure_count_path"] = tolerated_failure_count_path
        if tolerated_failure_percentage is not None:
            self._values["tolerated_failure_percentage"] = tolerated_failure_percentage
        if tolerated_failure_percentage_path is not None:
            self._values["tolerated_failure_percentage_path"] = tolerated_failure_percentage_path

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''An optional description for this state.

        :default: No comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the input to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        input to be the empty object {}.

        :default: $
        '''
        result = self._values.get("input_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def item_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that you want to override your default iteration input (mutually exclusive  with ``parameters``).

        :default: $

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-itemselector.html
        '''
        result = self._values.get("item_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def items_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select the array to iterate over.

        :default: $
        '''
        result = self._values.get("items_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[jsii.Number]:
        '''MaxConcurrency.

        An upper bound on the number of iterations you want running at once.

        :default: - full concurrency

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-asl-use-map-state-inline.html#map-state-inline-additional-fields
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_concurrency_path(self) -> typing.Optional[builtins.str]:
        '''MaxConcurrencyPath.

        A JsonPath that specifies the maximum concurrency dynamically from the state input.

        :default: - full concurrency

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-asl-use-map-state-inline.html#map-state-inline-additional-fields
        '''
        result = self._values.get("max_concurrency_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to select part of the state to be the output to this state.

        May also be the special value JsonPath.DISCARD, which will cause the effective
        output to be the empty object {}.

        :default: $
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_path(self) -> typing.Optional[builtins.str]:
        '''JSONPath expression to indicate where to inject the state's output.

        May also be the special value JsonPath.DISCARD, which will cause the state's
        input to become its output.

        :default: $
        '''
        result = self._values.get("result_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def result_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The JSON that will replace the state's raw result and become the effective result before ResultPath is applied.

        You can use ResultSelector to create a payload with values that are static
        or selected from the state's raw result.

        :default: - None

        :see: https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector
        '''
        result = self._values.get("result_selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def state_name(self) -> typing.Optional[builtins.str]:
        '''Optional name for this state.

        :default: - The construct ID will be used as state name
        '''
        result = self._values.get("state_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def item_batcher(self) -> typing.Optional[ItemBatcher]:
        '''Specifies to process a group of items in a single child workflow execution.

        :default: - No itemBatcher
        '''
        result = self._values.get("item_batcher")
        return typing.cast(typing.Optional[ItemBatcher], result)

    @builtins.property
    def item_reader(self) -> typing.Optional[IItemReader]:
        '''ItemReader.

        Configuration for where to read items dataset in S3 to iterate

        :default: - No itemReader
        '''
        result = self._values.get("item_reader")
        return typing.cast(typing.Optional[IItemReader], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Label.

        Unique name for the Distributed Map state added to each Map Run

        :default: - No label
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def map_execution_type(self) -> typing.Optional[StateMachineType]:
        '''MapExecutionType.

        The execution type of the distributed map state

        :default: StateMachineType.STANDARD
        '''
        result = self._values.get("map_execution_type")
        return typing.cast(typing.Optional[StateMachineType], result)

    @builtins.property
    def result_writer(self) -> typing.Optional[ResultWriter]:
        '''Configuration for S3 location in which to save Map Run results.

        :default: - No resultWriter
        '''
        result = self._values.get("result_writer")
        return typing.cast(typing.Optional[ResultWriter], result)

    @builtins.property
    def tolerated_failure_count(self) -> typing.Optional[jsii.Number]:
        '''ToleratedFailureCount.

        Number of failed items to tolerate in a Map Run, as static number

        :default: - No toleratedFailureCount
        '''
        result = self._values.get("tolerated_failure_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tolerated_failure_count_path(self) -> typing.Optional[builtins.str]:
        '''ToleratedFailureCountPath.

        Number of failed items to tolerate in a Map Run, as JsonPath

        :default: - No toleratedFailureCountPath
        '''
        result = self._values.get("tolerated_failure_count_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tolerated_failure_percentage(self) -> typing.Optional[jsii.Number]:
        '''ToleratedFailurePercentage.

        Percentage of failed items to tolerate in a Map Run, as static number

        :default: - No toleratedFailurePercentage
        '''
        result = self._values.get("tolerated_failure_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tolerated_failure_percentage_path(self) -> typing.Optional[builtins.str]:
        '''ToleratedFailurePercentagePath.

        Percentage of failed items to tolerate in a Map Run, as JsonPath

        :default: - No toleratedFailurePercentagePath
        '''
        result = self._values.get("tolerated_failure_percentage_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributedMapProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Fail(
    State,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Fail",
):
    '''Define a Fail state in the state machine.

    Reaching a Fail state terminates the state execution in failure.

    :exampleMetadata: infused

    Example::

        fail = sfn.Fail(self, "Fail",
            error_path=sfn.JsonPath.format("error: {}.", sfn.JsonPath.string_at("$.someError")),
            cause_path="States.Format('cause: {}.', $.someCause)"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cause: typing.Optional[builtins.str] = None,
        cause_path: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        error: typing.Optional[builtins.str] = None,
        error_path: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param cause: A description for the cause of the failure. Default: - No description
        :param cause_path: JsonPath expression to select part of the state to be the cause to this state. You can also use an intrinsic function that returns a string to specify this property. The allowed functions include States.Format, States.JsonToString, States.ArrayGetItem, States.Base64Encode, States.Base64Decode, States.Hash, and States.UUID. Default: - No cause path
        :param comment: An optional description for this state. Default: - No comment
        :param error: Error code used to represent this failure. Default: - No error code
        :param error_path: JsonPath expression to select part of the state to be the error to this state. You can also use an intrinsic function that returns a string to specify this property. The allowed functions include States.Format, States.JsonToString, States.ArrayGetItem, States.Base64Encode, States.Base64Decode, States.Hash, and States.UUID. Default: - No error path
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c583b760e906e99018014914554eafc9ccbd2b3420c0edbf5013a7649fb8c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = FailProps(
            cause=cause,
            cause_path=cause_path,
            comment=comment,
            error=error,
            error_path=error_path,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @jsii.member(jsii_name="validateState")
    def _validate_state(self) -> typing.List[builtins.str]:
        '''Validate this state.'''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateState", []))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))


@jsii.implements(INextable)
class MapBase(
    State,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_stepfunctions.MapBase",
):
    '''Define a Map state in the state machine.

    A ``Map`` state can be used to run a set of steps for each element of an input array.
    A Map state will execute the same steps for multiple entries of an array in the state input.

    While the Parallel state executes multiple branches of steps using the same input, a Map state
    will execute the same steps for multiple entries of an array in the state input.

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-map-state.html
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        items_path: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_concurrency_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param item_selector: The JSON that you want to override your default iteration input (mutually exclusive with ``parameters``). Default: $
        :param items_path: JSONPath expression to select the array to iterate over. Default: $
        :param max_concurrency: MaxConcurrency. An upper bound on the number of iterations you want running at once. Default: - full concurrency
        :param max_concurrency_path: MaxConcurrencyPath. A JsonPath that specifies the maximum concurrency dynamically from the state input. Default: - full concurrency
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d25d492eb753f17d954200a30dfae328a6f5710335312d1b5ffe0113a9ded82)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MapBaseProps(
            comment=comment,
            input_path=input_path,
            item_selector=item_selector,
            items_path=items_path,
            max_concurrency=max_concurrency,
            max_concurrency_path=max_concurrency_path,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="next")
    def next(self, next: IChainable) -> Chain:
        '''Continue normal execution with the given state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bfdae9c7d12de08b43f94e8bc33eaeef588cdf2a814eb233b86a9976943ed7b)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast(Chain, jsii.invoke(self, "next", [next]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @jsii.member(jsii_name="validateState")
    def _validate_state(self) -> typing.List[builtins.str]:
        '''Validate this state.'''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateState", []))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))

    @builtins.property
    @jsii.member(jsii_name="itemSelector")
    def _item_selector(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "itemSelector"))

    @builtins.property
    @jsii.member(jsii_name="itemsPath")
    def _items_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "itemsPath"))


class _MapBaseProxy(
    MapBase,
    jsii.proxy_for(State), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, MapBase).__jsii_proxy_class__ = lambda : _MapBaseProxy


@jsii.implements(INextable)
class Parallel(
    State,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Parallel",
):
    '''Define a Parallel state in the state machine.

    A Parallel state can be used to run one or more state machines at the same
    time.

    The Result of a Parallel state is an array of the results of its substatemachines.

    :exampleMetadata: nofixture infused

    Example::

        from aws_cdk import Stack
        from constructs import Construct
        import aws_cdk.aws_stepfunctions as sfn
        
        class MyJob(sfn.StateMachineFragment):
        
            def __init__(self, parent, id, *, jobFlavor):
                super().__init__(parent, id)
        
                choice = sfn.Choice(self, "Choice").when(sfn.Condition.string_equals("$.branch", "left"), sfn.Pass(self, "Left Branch")).when(sfn.Condition.string_equals("$.branch", "right"), sfn.Pass(self, "Right Branch"))
        
                # ...
        
                self.start_state = choice
                self.end_states = choice.afterwards().end_states
        
        class MyStack(Stack):
            def __init__(self, scope, id):
                super().__init__(scope, id)
                # Do 3 different variants of MyJob in parallel
                parallel = sfn.Parallel(self, "All jobs").branch(MyJob(self, "Quick", job_flavor="quick").prefix_states()).branch(MyJob(self, "Medium", job_flavor="medium").prefix_states()).branch(MyJob(self, "Slow", job_flavor="slow").prefix_states())
        
                sfn.StateMachine(self, "MyStateMachine",
                    definition_body=sfn.DefinitionBody.from_chainable(parallel)
                )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94610eed4635a69c6d4a92818527e6ecdf15561092c488fb6caa8d8ec9778a22)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ParallelProps(
            comment=comment,
            input_path=input_path,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addCatch")
    def add_catch(
        self,
        handler: IChainable,
        *,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        result_path: typing.Optional[builtins.str] = None,
    ) -> "Parallel":
        '''Add a recovery handler for this state.

        When a particular error occurs, execution will continue at the error
        handler instead of failing the state machine execution.

        :param handler: -
        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value JsonPath.DISCARD, which will cause the error data to be discarded. Default: $
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__182be923de45451a3be4a0e5bda7642ee82b8bfb46a7fd13f9cdc8084f23f9bb)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = CatchProps(errors=errors, result_path=result_path)

        return typing.cast("Parallel", jsii.invoke(self, "addCatch", [handler, props]))

    @jsii.member(jsii_name="addRetry")
    def add_retry(
        self,
        *,
        backoff_rate: typing.Optional[jsii.Number] = None,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        interval: typing.Optional[_Duration_4839e8c3] = None,
        jitter_strategy: typing.Optional[JitterType] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        max_delay: typing.Optional[_Duration_4839e8c3] = None,
    ) -> "Parallel":
        '''Add retry configuration for this state.

        This controls if and how the execution will be retried if a particular
        error occurs.

        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param jitter_strategy: Introduces a randomization over the retry interval. Default: - No jitter strategy
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3
        :param max_delay: Maximum limit on retry interval growth during exponential backoff. Default: - No max delay
        '''
        props = RetryProps(
            backoff_rate=backoff_rate,
            errors=errors,
            interval=interval,
            jitter_strategy=jitter_strategy,
            max_attempts=max_attempts,
            max_delay=max_delay,
        )

        return typing.cast("Parallel", jsii.invoke(self, "addRetry", [props]))

    @jsii.member(jsii_name="bindToGraph")
    def bind_to_graph(self, graph: StateGraph) -> None:
        '''Overwrites State.bindToGraph. Adds branches to the Parallel state here so that any necessary prefixes are appended first.

        :param graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f51369cf1df8050a9193691c532125259fc7c9e4293a269130e56f7600e8e869)
            check_type(argname="argument graph", value=graph, expected_type=type_hints["graph"])
        return typing.cast(None, jsii.invoke(self, "bindToGraph", [graph]))

    @jsii.member(jsii_name="branch")
    def branch(self, *branches: IChainable) -> "Parallel":
        '''Define one or more branches to run in parallel.

        :param branches: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__697633cbf62e47597c9fdc7d002c0aee2b85afe1b449f1d0ce4917552cf01271)
            check_type(argname="argument branches", value=branches, expected_type=typing.Tuple[type_hints["branches"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("Parallel", jsii.invoke(self, "branch", [*branches]))

    @jsii.member(jsii_name="next")
    def next(self, next: IChainable) -> Chain:
        '''Continue normal execution with the given state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf2f89f1d526659416028630d3a07331a2f13a5067fd5e45f41dd46895179826)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast(Chain, jsii.invoke(self, "next", [next]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @jsii.member(jsii_name="validateState")
    def _validate_state(self) -> typing.List[builtins.str]:
        '''Validate this state.'''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateState", []))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))


@jsii.implements(INextable)
class Pass(
    State,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Pass",
):
    '''Define a Pass in the state machine.

    A Pass state can be used to transform the current execution's state.

    :exampleMetadata: infused

    Example::

        choice = sfn.Choice(self, "Did it work?")
        
        # Add conditions with .when()
        success_state = sfn.Pass(self, "SuccessState")
        failure_state = sfn.Pass(self, "FailureState")
        choice.when(sfn.Condition.string_equals("$.status", "SUCCESS"), success_state)
        choice.when(sfn.Condition.number_greater_than("$.attempts", 5), failure_state)
        
        # Use .otherwise() to indicate what should be done if none of the conditions match
        try_again_state = sfn.Pass(self, "TryAgainState")
        choice.otherwise(try_again_state)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        result: typing.Optional[Result] = None,
        result_path: typing.Optional[builtins.str] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param parameters: Parameters pass a collection of key-value pairs, either static values or JSONPath expressions that select from the input. Default: No parameters
        :param result: If given, treat as the result of this operation. Can be used to inject or replace the current execution state. Default: No injected result
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d42bf3e652e85f6ec94972b87e3cd78f4420b89e56b719dae3323e4b9c485f2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PassProps(
            comment=comment,
            input_path=input_path,
            output_path=output_path,
            parameters=parameters,
            result=result,
            result_path=result_path,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="next")
    def next(self, next: IChainable) -> Chain:
        '''Continue normal execution with the given state.

        :param next: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4f3a4b985638e018cf9da160ea401084953cf6a22e9ff97cb9b82310d664a55)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
        return typing.cast(Chain, jsii.invoke(self, "next", [next]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @builtins.property
    @jsii.member(jsii_name="endStates")
    def end_states(self) -> typing.List[INextable]:
        '''Continuable states of this Chainable.'''
        return typing.cast(typing.List[INextable], jsii.get(self, "endStates"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_stepfunctions.S3CsvItemReaderProps",
    jsii_struct_bases=[S3FileItemReaderProps],
    name_mapping={
        "bucket": "bucket",
        "max_items": "maxItems",
        "key": "key",
        "csv_headers": "csvHeaders",
    },
)
class S3CsvItemReaderProps(S3FileItemReaderProps):
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        max_items: typing.Optional[jsii.Number] = None,
        key: builtins.str,
        csv_headers: typing.Optional[CsvHeaders] = None,
    ) -> None:
        '''Properties for configuring an Item Reader that iterates over items in a CSV file in S3.

        :param bucket: S3 Bucket containing objects to iterate over or a file with a list to iterate over.
        :param max_items: Limits the number of items passed to the Distributed Map state. Default: - Distributed Map state will iterate over all items provided by the ItemReader
        :param key: Key of file stored in S3 bucket containing an array to iterate over.
        :param csv_headers: CSV file header configuration. Default: - CsvHeaders with CsvHeadersLocation.FIRST_ROW

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3 as s3
            from aws_cdk import aws_stepfunctions as stepfunctions
            
            # bucket: s3.Bucket
            # csv_headers: stepfunctions.CsvHeaders
            
            s3_csv_item_reader_props = stepfunctions.S3CsvItemReaderProps(
                bucket=bucket,
                key="key",
            
                # the properties below are optional
                csv_headers=csv_headers,
                max_items=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd148cd8282abe643b20452cf3c099e0d66560a90ddb7ec54f83740859fe615d)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument max_items", value=max_items, expected_type=type_hints["max_items"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument csv_headers", value=csv_headers, expected_type=type_hints["csv_headers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "key": key,
        }
        if max_items is not None:
            self._values["max_items"] = max_items
        if csv_headers is not None:
            self._values["csv_headers"] = csv_headers

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''S3 Bucket containing objects to iterate over or a file with a list to iterate over.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def max_items(self) -> typing.Optional[jsii.Number]:
        '''Limits the number of items passed to the Distributed Map state.

        :default: - Distributed Map state will iterate over all items provided by the ItemReader
        '''
        result = self._values.get("max_items")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Key of file stored in S3 bucket containing an array to iterate over.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def csv_headers(self) -> typing.Optional[CsvHeaders]:
        '''CSV file header configuration.

        :default: - CsvHeaders with CsvHeadersLocation.FIRST_ROW
        '''
        result = self._values.get("csv_headers")
        return typing.cast(typing.Optional[CsvHeaders], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3CsvItemReaderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(INextable)
class DistributedMap(
    MapBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.DistributedMap",
):
    '''Define a Distributed Mode Map state in the state machine.

    A ``Map`` state can be used to run a set of steps for each element of an input array.
    A Map state will execute the same steps for multiple entries of an array in the state input.

    While the Parallel state executes multiple branches of steps using the same input, a Map state
    will execute the same steps for multiple entries of an array in the state input.

    A ``Map`` state in ``Distributed`` mode will execute a child workflow for each iteration of the Map state.
    This serves to increase concurrency and allows for larger workloads to be run in a single state machine.

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-asl-use-map-state-distributed.html
    :exampleMetadata: infused

    Example::

        distributed_map = sfn.DistributedMap(self, "Distributed Map State",
            max_concurrency=1,
            items_path=sfn.JsonPath.string_at("$.inputForMap")
        )
        distributed_map.item_processor(sfn.Pass(self, "Pass State"))
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        item_batcher: typing.Optional[ItemBatcher] = None,
        item_reader: typing.Optional[IItemReader] = None,
        label: typing.Optional[builtins.str] = None,
        map_execution_type: typing.Optional[StateMachineType] = None,
        result_writer: typing.Optional[ResultWriter] = None,
        tolerated_failure_count: typing.Optional[jsii.Number] = None,
        tolerated_failure_count_path: typing.Optional[builtins.str] = None,
        tolerated_failure_percentage: typing.Optional[jsii.Number] = None,
        tolerated_failure_percentage_path: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        items_path: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_concurrency_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param item_batcher: Specifies to process a group of items in a single child workflow execution. Default: - No itemBatcher
        :param item_reader: ItemReader. Configuration for where to read items dataset in S3 to iterate Default: - No itemReader
        :param label: Label. Unique name for the Distributed Map state added to each Map Run Default: - No label
        :param map_execution_type: MapExecutionType. The execution type of the distributed map state Default: StateMachineType.STANDARD
        :param result_writer: Configuration for S3 location in which to save Map Run results. Default: - No resultWriter
        :param tolerated_failure_count: ToleratedFailureCount. Number of failed items to tolerate in a Map Run, as static number Default: - No toleratedFailureCount
        :param tolerated_failure_count_path: ToleratedFailureCountPath. Number of failed items to tolerate in a Map Run, as JsonPath Default: - No toleratedFailureCountPath
        :param tolerated_failure_percentage: ToleratedFailurePercentage. Percentage of failed items to tolerate in a Map Run, as static number Default: - No toleratedFailurePercentage
        :param tolerated_failure_percentage_path: ToleratedFailurePercentagePath. Percentage of failed items to tolerate in a Map Run, as JsonPath Default: - No toleratedFailurePercentagePath
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param item_selector: The JSON that you want to override your default iteration input (mutually exclusive with ``parameters``). Default: $
        :param items_path: JSONPath expression to select the array to iterate over. Default: $
        :param max_concurrency: MaxConcurrency. An upper bound on the number of iterations you want running at once. Default: - full concurrency
        :param max_concurrency_path: MaxConcurrencyPath. A JsonPath that specifies the maximum concurrency dynamically from the state input. Default: - full concurrency
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f7d4222fc9728237ee261157ec268cfd8f396c371bc6402ec7a1a4ea42917d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DistributedMapProps(
            item_batcher=item_batcher,
            item_reader=item_reader,
            label=label,
            map_execution_type=map_execution_type,
            result_writer=result_writer,
            tolerated_failure_count=tolerated_failure_count,
            tolerated_failure_count_path=tolerated_failure_count_path,
            tolerated_failure_percentage=tolerated_failure_percentage,
            tolerated_failure_percentage_path=tolerated_failure_percentage_path,
            comment=comment,
            input_path=input_path,
            item_selector=item_selector,
            items_path=items_path,
            max_concurrency=max_concurrency,
            max_concurrency_path=max_concurrency_path,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isDistributedMap")
    @builtins.classmethod
    def is_distributed_map(cls, x: typing.Any) -> builtins.bool:
        '''Return whether the given object is a DistributedMap.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31933264cd976eda9b915ac15b88658cd66607d4305ac5503092b27ee9650f4)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isDistributedMap", [x]))

    @jsii.member(jsii_name="addCatch")
    def add_catch(
        self,
        handler: IChainable,
        *,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        result_path: typing.Optional[builtins.str] = None,
    ) -> "DistributedMap":
        '''Add a recovery handler for this state.

        When a particular error occurs, execution will continue at the error
        handler instead of failing the state machine execution.

        :param handler: -
        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value JsonPath.DISCARD, which will cause the error data to be discarded. Default: $
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b96420299a828b17719584b98a81fc0affc397b69e90092f29e7d9afb2d48324)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = CatchProps(errors=errors, result_path=result_path)

        return typing.cast("DistributedMap", jsii.invoke(self, "addCatch", [handler, props]))

    @jsii.member(jsii_name="addRetry")
    def add_retry(
        self,
        *,
        backoff_rate: typing.Optional[jsii.Number] = None,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        interval: typing.Optional[_Duration_4839e8c3] = None,
        jitter_strategy: typing.Optional[JitterType] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        max_delay: typing.Optional[_Duration_4839e8c3] = None,
    ) -> "DistributedMap":
        '''Add retry configuration for this state.

        This controls if and how the execution will be retried if a particular
        error occurs.

        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param jitter_strategy: Introduces a randomization over the retry interval. Default: - No jitter strategy
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3
        :param max_delay: Maximum limit on retry interval growth during exponential backoff. Default: - No max delay
        '''
        props = RetryProps(
            backoff_rate=backoff_rate,
            errors=errors,
            interval=interval,
            jitter_strategy=jitter_strategy,
            max_attempts=max_attempts,
            max_delay=max_delay,
        )

        return typing.cast("DistributedMap", jsii.invoke(self, "addRetry", [props]))

    @jsii.member(jsii_name="itemProcessor")
    def item_processor(
        self,
        processor: IChainable,
        *,
        execution_type: typing.Optional[ProcessorType] = None,
        mode: typing.Optional[ProcessorMode] = None,
    ) -> "DistributedMap":
        '''Define item processor in a Distributed Map.

        A Distributed Map must have a non-empty item processor

        :param processor: -
        :param execution_type: Specifies the execution type for the Map workflow. You must provide this field if you specified ``DISTRIBUTED`` for the ``mode`` sub-field. Default: - no execution type
        :param mode: Specifies the execution mode for the Map workflow. Default: - ProcessorMode.INLINE
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f10278e982625ca06b2d3266813a2418de02709637602f80e07445047d125579)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        config = ProcessorConfig(execution_type=execution_type, mode=mode)

        return typing.cast("DistributedMap", jsii.invoke(self, "itemProcessor", [processor, config]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @jsii.member(jsii_name="validateState")
    def _validate_state(self) -> typing.List[builtins.str]:
        '''Validate this state.'''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateState", []))

    @jsii.member(jsii_name="whenBoundToGraph")
    def _when_bound_to_graph(self, graph: StateGraph) -> None:
        '''Called whenever this state is bound to a graph.

        Can be overridden by subclasses.

        :param graph: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e505be41bf00ad65952efb21c612874ac8a42269a7a70f2a1c0ee866dbb902c0)
            check_type(argname="argument graph", value=graph, expected_type=type_hints["graph"])
        return typing.cast(None, jsii.invoke(self, "whenBoundToGraph", [graph]))


@jsii.implements(INextable)
class Map(
    MapBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_stepfunctions.Map",
):
    '''Define a Map state in the state machine.

    A ``Map`` state can be used to run a set of steps for each element of an input array.
    A Map state will execute the same steps for multiple entries of an array in the state input.

    While the Parallel state executes multiple branches of steps using the same input, a Map state
    will execute the same steps for multiple entries of an array in the state input.

    :see: https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-map-state.html
    :exampleMetadata: infused

    Example::

        map = sfn.Map(self, "Map State",
            max_concurrency=1,
            items_path=sfn.JsonPath.string_at("$.inputForMap"),
            item_selector={
                "item": sfn.JsonPath.string_at("$.Map.Item.Value")
            },
            result_path="$.mapOutput"
        )
        
        # The Map iterator can contain a IChainable, which can be an individual or multiple steps chained together.
        # Below example is with a Choice and Pass step
        choice = sfn.Choice(self, "Choice")
        condition1 = sfn.Condition.string_equals("$.item.status", "SUCCESS")
        step1 = sfn.Pass(self, "Step1")
        step2 = sfn.Pass(self, "Step2")
        finish = sfn.Pass(self, "Finish")
        
        definition = choice.when(condition1, step1).otherwise(step2).afterwards().next(finish)
        
        map.item_processor(definition)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        comment: typing.Optional[builtins.str] = None,
        input_path: typing.Optional[builtins.str] = None,
        item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        items_path: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_concurrency_path: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
        result_path: typing.Optional[builtins.str] = None,
        result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        state_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: Descriptive identifier for this chainable.
        :param parameters: (deprecated) The JSON that you want to override your default iteration input (mutually exclusive with ``itemSelector``). Default: $
        :param comment: An optional description for this state. Default: No comment
        :param input_path: JSONPath expression to select part of the state to be the input to this state. May also be the special value JsonPath.DISCARD, which will cause the effective input to be the empty object {}. Default: $
        :param item_selector: The JSON that you want to override your default iteration input (mutually exclusive with ``parameters``). Default: $
        :param items_path: JSONPath expression to select the array to iterate over. Default: $
        :param max_concurrency: MaxConcurrency. An upper bound on the number of iterations you want running at once. Default: - full concurrency
        :param max_concurrency_path: MaxConcurrencyPath. A JsonPath that specifies the maximum concurrency dynamically from the state input. Default: - full concurrency
        :param output_path: JSONPath expression to select part of the state to be the output to this state. May also be the special value JsonPath.DISCARD, which will cause the effective output to be the empty object {}. Default: $
        :param result_path: JSONPath expression to indicate where to inject the state's output. May also be the special value JsonPath.DISCARD, which will cause the state's input to become its output. Default: $
        :param result_selector: The JSON that will replace the state's raw result and become the effective result before ResultPath is applied. You can use ResultSelector to create a payload with values that are static or selected from the state's raw result. Default: - None
        :param state_name: Optional name for this state. Default: - The construct ID will be used as state name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78d28fbd908923a38f00f8f82b2387552ae3a53fe5d860d66d336f49ba4c36c1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MapProps(
            parameters=parameters,
            comment=comment,
            input_path=input_path,
            item_selector=item_selector,
            items_path=items_path,
            max_concurrency=max_concurrency,
            max_concurrency_path=max_concurrency_path,
            output_path=output_path,
            result_path=result_path,
            result_selector=result_selector,
            state_name=state_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addCatch")
    def add_catch(
        self,
        handler: IChainable,
        *,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        result_path: typing.Optional[builtins.str] = None,
    ) -> "Map":
        '''Add a recovery handler for this state.

        When a particular error occurs, execution will continue at the error
        handler instead of failing the state machine execution.

        :param handler: -
        :param errors: Errors to recover from by going to the given state. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param result_path: JSONPath expression to indicate where to inject the error data. May also be the special value JsonPath.DISCARD, which will cause the error data to be discarded. Default: $
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__477e230f69a651e6927594095a0d2d681abd0858db9b79de5caf573bda0f7eb6)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = CatchProps(errors=errors, result_path=result_path)

        return typing.cast("Map", jsii.invoke(self, "addCatch", [handler, props]))

    @jsii.member(jsii_name="addRetry")
    def add_retry(
        self,
        *,
        backoff_rate: typing.Optional[jsii.Number] = None,
        errors: typing.Optional[typing.Sequence[builtins.str]] = None,
        interval: typing.Optional[_Duration_4839e8c3] = None,
        jitter_strategy: typing.Optional[JitterType] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        max_delay: typing.Optional[_Duration_4839e8c3] = None,
    ) -> "Map":
        '''Add retry configuration for this state.

        This controls if and how the execution will be retried if a particular
        error occurs.

        :param backoff_rate: Multiplication for how much longer the wait interval gets on every retry. Default: 2
        :param errors: Errors to retry. A list of error strings to retry, which can be either predefined errors (for example Errors.NoChoiceMatched) or a self-defined error. Default: All errors
        :param interval: How many seconds to wait initially before retrying. Default: Duration.seconds(1)
        :param jitter_strategy: Introduces a randomization over the retry interval. Default: - No jitter strategy
        :param max_attempts: How many times to retry this particular error. May be 0 to disable retry for specific errors (in case you have a catch-all retry policy). Default: 3
        :param max_delay: Maximum limit on retry interval growth during exponential backoff. Default: - No max delay
        '''
        props = RetryProps(
            backoff_rate=backoff_rate,
            errors=errors,
            interval=interval,
            jitter_strategy=jitter_strategy,
            max_attempts=max_attempts,
            max_delay=max_delay,
        )

        return typing.cast("Map", jsii.invoke(self, "addRetry", [props]))

    @jsii.member(jsii_name="itemProcessor")
    def item_processor(
        self,
        processor: IChainable,
        *,
        execution_type: typing.Optional[ProcessorType] = None,
        mode: typing.Optional[ProcessorMode] = None,
    ) -> "Map":
        '''Define item processor in Map.

        A Map must either have a non-empty iterator or a non-empty item processor (mutually exclusive  with ``iterator``).

        :param processor: -
        :param execution_type: Specifies the execution type for the Map workflow. You must provide this field if you specified ``DISTRIBUTED`` for the ``mode`` sub-field. Default: - no execution type
        :param mode: Specifies the execution mode for the Map workflow. Default: - ProcessorMode.INLINE
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57880144217f818052832dac038a8875120f8ef30f1d286864bba6785bb1afd5)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        config = ProcessorConfig(execution_type=execution_type, mode=mode)

        return typing.cast("Map", jsii.invoke(self, "itemProcessor", [processor, config]))

    @jsii.member(jsii_name="iterator")
    def iterator(self, iterator: IChainable) -> "Map":
        '''(deprecated) Define iterator state machine in Map.

        A Map must either have a non-empty iterator or a non-empty item processor (mutually exclusive  with ``itemProcessor``).

        :param iterator: -

        :deprecated: - use ``itemProcessor`` instead.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46bf9177a387f4dcf5be0d20783b744edaca8974e7384b16a446321cc3bc65aa)
            check_type(argname="argument iterator", value=iterator, expected_type=type_hints["iterator"])
        return typing.cast("Map", jsii.invoke(self, "iterator", [iterator]))

    @jsii.member(jsii_name="toStateJson")
    def to_state_json(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''Return the Amazon States Language object for this state.'''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.invoke(self, "toStateJson", []))

    @jsii.member(jsii_name="validateState")
    def _validate_state(self) -> typing.List[builtins.str]:
        '''Validate this state.'''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validateState", []))


__all__ = [
    "Activity",
    "ActivityProps",
    "AfterwardsOptions",
    "CatchProps",
    "CfnActivity",
    "CfnActivityProps",
    "CfnStateMachine",
    "CfnStateMachineAlias",
    "CfnStateMachineAliasProps",
    "CfnStateMachineProps",
    "CfnStateMachineVersion",
    "CfnStateMachineVersionProps",
    "Chain",
    "ChainDefinitionBody",
    "Choice",
    "ChoiceProps",
    "ChoiceTransitionOptions",
    "Condition",
    "Credentials",
    "CsvHeaderLocation",
    "CsvHeaders",
    "CustomState",
    "CustomStateProps",
    "DefinitionBody",
    "DefinitionConfig",
    "DistributedMap",
    "DistributedMapProps",
    "Errors",
    "Fail",
    "FailProps",
    "FieldUtils",
    "FileDefinitionBody",
    "FindStateOptions",
    "IActivity",
    "IChainable",
    "IItemReader",
    "INextable",
    "IStateMachine",
    "InputType",
    "IntegrationPattern",
    "ItemBatcher",
    "ItemBatcherProps",
    "ItemReaderProps",
    "JitterType",
    "JsonPath",
    "LogLevel",
    "LogOptions",
    "Map",
    "MapBase",
    "MapBaseProps",
    "MapProps",
    "Parallel",
    "ParallelProps",
    "Pass",
    "PassProps",
    "ProcessorConfig",
    "ProcessorMode",
    "ProcessorType",
    "Result",
    "ResultWriter",
    "ResultWriterProps",
    "RetryProps",
    "S3CsvItemReader",
    "S3CsvItemReaderProps",
    "S3FileItemReaderProps",
    "S3JsonItemReader",
    "S3ManifestItemReader",
    "S3ObjectsItemReader",
    "S3ObjectsItemReaderProps",
    "ServiceIntegrationPattern",
    "SingleStateOptions",
    "State",
    "StateGraph",
    "StateMachine",
    "StateMachineFragment",
    "StateMachineProps",
    "StateMachineType",
    "StateProps",
    "StateTransitionMetric",
    "StringDefinitionBody",
    "Succeed",
    "SucceedProps",
    "TaskInput",
    "TaskMetricsConfig",
    "TaskRole",
    "TaskStateBase",
    "TaskStateBaseProps",
    "Timeout",
    "Wait",
    "WaitProps",
    "WaitTime",
]

publication.publish()

def _typecheckingstub__b22b644ed0224ed8911beae00f4c015272b0b6846f925702d315e05b17bfc26e(
    *,
    activity_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4085645c0aa11ea16f29fe0328307d94fbc700a6b908a2c9d2b3209bc2f7af6(
    *,
    include_error_handlers: typing.Optional[builtins.bool] = None,
    include_otherwise: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b30052ea4266ae7ac11a0c2eaab9f31db04561d9040ab8175bd34b849414a0(
    *,
    errors: typing.Optional[typing.Sequence[builtins.str]] = None,
    result_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9cac9ccbc74858ea58acc13770fdeee7b204562b53992182f500d45a5f816a2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnActivity.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3118727103487fc9862cb103a2c8a7c466265683e88e012835325059d1d7e0d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__370d3cef66c2bfc06cc862207a47ec2707fa300961f0129ab6f3c2edf4a02cb2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8395bdf4e76b8a41673d28377cd1001ff25935aca9798745ebef40fe06572120(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c963f19dfa2bfb12cf0d22b5bf287aec4f47a000b16928a2dd660ae295dcde65(
    value: typing.Optional[typing.List[CfnActivity.TagsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e620d5be50cdb836aed85b2b5bbc76573db0139cccc1fa49f54e926f1e4cbc7(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84792b5435bbf43a453a6bf0f4d6e6d61a7c86759e3f95b4d4af4d4e56f641c4(
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnActivity.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b19fff9309f98c9776cf416019a5217333b4d6f0f81e27e2256a87f931153d0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role_arn: builtins.str,
    definition: typing.Any = None,
    definition_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_string: typing.Optional[builtins.str] = None,
    definition_substitutions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state_machine_name: typing.Optional[builtins.str] = None,
    state_machine_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnStateMachine.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.TracingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07dab719dc25dde0e0ebd681e886c29dd992fd69300c5b97592744ca66975549(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d81dc102aa24fdc5c42fa4ed2ff7c70c77beb876a92e54f87c158489800243ef(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3004fba1e9c0225151457c38edd4c7effc7d187628b86416f39849b982f49a1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f82f2a7642ea2ac7bdf170a2733a41594fd40eb07f7e540d495f22c6fa06b147(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c6f22451e8abd968219b59f11a227c9451d5cd7cb1ff91b3bd91c4ab25bd6da(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c930aec966c75b589ce56dba8aee211d61eeb6c41d99c5c84ab2df4b703b35d3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e05fa36d2c9116cb2c90b1560cd6e7bc08699fa552a7e75ce5775a927ad53415(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f4c64119545b342b25a9aba40a7ac8de878e2ca38859e38a10004112309301(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.LoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c0751a8a3952639ad0b17cb78032a0bad0e3a1e983836e5c861a8129c0c542(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aef9754ddbe205b0e3cda858acb6182a9a911881b2f81e68f20b454cc9d738e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142d2d5d8871bd122c48cc77fb02230c828841e8672a11480c58d07a743ec8d0(
    value: typing.Optional[typing.List[CfnStateMachine.TagsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7975c26bdc928c8d9fd66a2493df6fc6818b885815e25f63844e956d275c1d01(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.TracingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd590e91d2c1399d369226ca3fcbd6666d564980b08611a4b5f952ef3e6b9644(
    *,
    log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a5d8a3abcdb82fe13dbd692519b118f763c5de9bf0de6025642f4d45a207ab1(
    *,
    cloud_watch_logs_log_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.CloudWatchLogsLogGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24eee9bdacbb65e43216bb9ddfa4cfe3e27e892eb228ca21be7cd0565deb825a(
    *,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.LogDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_execution_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24b148e6a91176407ca02fb5dd7411cf96ebdd5cdccdafa24b702f5578115e1d(
    *,
    bucket: builtins.str,
    key: builtins.str,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb83dface8660c95e6064ed3571632ddfd56b66cf9838d2dff4920c79c635e1(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbdafebe888490672c9f37361d4a6ddfd497f384ba2c643a0138dcf36eaf947d(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85744ef2fdff2d756e7a5ede3f88cb39b6c23cf8c88315a30006ec164aeda913(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deployment_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachineAlias.DeploymentPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    routing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachineAlias.RoutingConfigurationVersionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39d3b5bbdb19199dd6c855f5e5c36c80442ad9f5bcfc52471013324e8a03057e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0631e2f126759615f5f8c79f47da93a2503e50646d811e8d62ca6adb72cc9d67(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__291c291374c3a7bdc720916a40ec17c8994233f17b521e36f88493f1dfea6abe(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachineAlias.DeploymentPreferenceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c4a9670d54e1fd8d9f71a40d8fe51ff4c20b8266100071f23c2fcd11c913f4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af65681afd264c6830e6a2a7499c40b1a1c1cd59a8a9d0c2b4f69d4df6f9f358(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c36ec8b9a1fe59c6e03fb3ba3b15d8849aa3ea74c639879915303e21486168(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStateMachineAlias.RoutingConfigurationVersionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bf8e2b40097e36c0d014ffb281643658dd6d26279ce8e06bb1e9ce944fffb43(
    *,
    state_machine_version_arn: builtins.str,
    type: builtins.str,
    alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
    interval: typing.Optional[jsii.Number] = None,
    percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a688434f1bb6e3dfc9e2ccdd19ed95c105316293de60df8e4fe097b12705a50b(
    *,
    state_machine_version_arn: builtins.str,
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d59745dc4c655a3bf10278f9b74e39163a7b157ca93bafdd0e7939d5c39662(
    *,
    deployment_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachineAlias.DeploymentPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    routing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachineAlias.RoutingConfigurationVersionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf4d4e83bd396b6667f5c30b66226d7e76f61626aea9c4ec1355f6e6a3631abd(
    *,
    role_arn: builtins.str,
    definition: typing.Any = None,
    definition_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_string: typing.Optional[builtins.str] = None,
    definition_substitutions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state_machine_name: typing.Optional[builtins.str] = None,
    state_machine_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnStateMachine.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.TracingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b19ebd913b3792b5cf85d382b7166b1f3325d9d4c4d36e3487276014cbb29edc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    state_machine_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    state_machine_revision_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5464561cedf359263d5e05f1d444de28a7d75d5ce4347840115515f065a5201(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__593f2bbe562bc9f9cee66f866efeb6b4662511cc706d0e7292314d744f609afb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b5bffae2ab6951189d8934aa88a458856f9a4d6623a0832d0295941754bf70d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8425cdd1ce7e33098a65ff2357b57674f96a520fc7d3cc63794e265253928cf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a80351896d09cb747491b59d0460387f46b6f51704f091b54c4fecf9f3f4bac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a26dd5401b86d66727994521c663b875a629d09b7d66d7dc260fb560b6d9642(
    *,
    state_machine_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    state_machine_revision_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a926bb3a79f5cf3706dd32093c49a75fa6045aeefbff3e1b4943eb654489e685(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__254c8670f15896e504e7f2c5398c9717ddc003fe66835e546b52b1693c004add(
    *,
    comment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71eb0d2598d910c950378149f21b99ac6c39c861109d3ab21b603c6dd4a39f67(
    *conditions: Condition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b9bc889cdd24c404551cfb0d6925ab10c64ddca33272041a3c7d8db3e9025c7(
    variable: builtins.str,
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1db786980e3e6eb95ef1359718a8087981a167450763e1b1af4cccde32d8df67(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4044239d0ab330627f79630a789a88d7b43ad67590db42e02374bb20c513dda1(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8d8efc940c58d80b1c03cc3a965aec81d82a73fd35d57efb6446acd9501e9c(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a9314e2710309f34934fbe6b184bffa9367a1d71ac9f79627e6c79845fc04a5(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18fa5c934c072dc5c01e61c786a81241c2a66991b9f365ba7656fee9bebb6bfb(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8d78236cfc082603b9981a5287c2ac458428d58eba55f05b44995b4210acfd(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__343e7cf6c4a403ce9824b8a1b7dfa9fca52c0c03cd770a44c56f803c37338bf6(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7250986a16f9bb8be78a9686c2ae7dce3fef5bb1c5b8b256fbcdb015c259919e(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f79eb1053d2162c6a58e2c2b7f0557b73ad5660d50e70b80b385adb03087993(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__561ba17c1b749efc2328847c14b1814d33920f4ab0fb079d257f56c929ca03a4(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__392be928fa30637320c733f4d7810aff4b79cb72e727ae2838ba58c1b919f493(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__badeb8cc1a4243c359dbfd4d33b9074f5f4d3646b5823a9c49c9fe26330592e6(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__361a2b8f339e790bd76aa839dfda488de2cc072d8a449e5a81b855b62eb59876(
    variable: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5acebcb4f135ed0cc9e840cb1cbaee78dd705f7b775d6b5cbe9eb4d18557941c(
    condition: Condition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc2870430bc517ffa4c051bbeec0e433e96a52f7cded7c34363a0655bc8e8283(
    variable: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fbfe1d112b80de4f820cf91187f730fef81616ca2bd204372e64505b28b46c1(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6d064c6f5ca8f0d29f98983b27295433d8fb18943cb0e8fb8588b430462566(
    variable: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93f18ca4cac21cd9ca7599acbcaa3e51e34cd4c898c63ae7f85784f73b530f91(
    variable: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6afb217f2f63404a040a45130eaa97bbe2d52ecc9c1d35a1c979bb3071894c0(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0df062863035ddc6506fe6962d7a1fc4d5a4b5e8529bc8d06dab3f53e38337(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85df632e1bb32eaa6062ef02209f69b58d10a8dfa8cade99ef9532416279b42d(
    variable: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab2dcbd2780b62793d8418faad84b7d828dd3f4f566b3e6ae53c3877bbd61227(
    variable: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5a63d516352eb231b883e8e64d9639a572564facf5dea9a3c5198a9e22876c4(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599066fbf144c3ed0066b2f899bba8d423c4bb2dc9e2b874dbaa5ebf457e11df(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ebfca9e6b416b95d0c13f84b582d58628d0adebff6b077140c28ffa89cd681(
    *conditions: Condition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5e3bcb339531b64d38b5c4df6ca6651eaefce4132a0e157a06bf0ff0f92483(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78f169f014f9ae3df9f49252e02dead74ee520bb53ba38a05a3952b041b3e46e(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa269f3363724cd30c519d1c6741e4614000bba9e0d027da1ece94705be1180f(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f68add250a89ba6ac56739d0a7f86bc8888c9863e1ddfb9955559b87fdd7d19(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860e3ec79ef3c5b3b8a6b4959dcd94eaa8b6d982c515f4ec6305a18800737c02(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0790ed513991abfda140a8c53d563ee6788dc73fe0008ceef63ea895a638ba7a(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef009e1d0aeb56bc81745234de63e9ff0769c94902c109c64463af7cfe55b98c(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d90066748658a5be8982e167d4dd1de780d5a8b558e1fdf6ea75bc89e3a3cc9(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145b1a589a61e4fa1b0e930fb96671f16374fd9fdc4f63f3685a84951f9113cd(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d13f1a89d702d97299b808ac45fc1a8f5d3115c0f7f540e1e40bad59affb2fd(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de73e811b3b1426b79947865d10e188cd9a19a7803f6f2310a8d94ff46ee056f(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c124b18e00eb90c97548b3ee174d109e9086ee3f576c7c21dea0c626b172ca(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9391c794c3ff6ae9ee1ab30da37a340d85e5e712386072e80559b30234fd7263(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86c020130869b22990c221979ed64ee6dc804120a40a7e5ba4388cf82a89f7f7(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae72825e4f0dba8d57cf583d4b9da4aa4228292ee1bc145787d5bae8bdd13c9c(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1374c2638911f124c361c2f692e26a6c983ad283eb5675881a3005262018962(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5567199e7723f4a83859c8e45186b8afe013d15927c9e560684990deaf97d212(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd9508b8a46d6979f811f9f642e6dba0f1b1ec212fffb60d21dd98ae3b0cb1b0(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__459421befc35cebd0bbdf1d1d350af4f3fb47bd1d5e7d03db51ddcfb96fb1eff(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e734a1f85e798bc59d4fc4f1aaf3c7a28bd4808ec5f926179da1a6a1ae53857c(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25cbb60f1773ec82d0235bd53fcbf222ee9038bc1b1039e8ad3e48e0445c9b77(
    variable: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75c7ba87106a955eb0c1dd29b26afbdb125c2950c829f9cfb85b266f527c14df(
    *,
    role: TaskRole,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bca5f165d56905bd06f4a1c77bab648cc802c173242fb36fc4310aaebc86dc6(
    headers: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde0868841af19410dad218c5615177bdc4ee1633d65f2618ef7750dfcf857d6(
    *,
    state_json: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c2a13855ce583fafff8ce021d579ed3a8ce8c50b9af46c8d337814412dd2ef(
    chainable: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e34fabd0367a0519a35d86d419baa37e6fe26ad05457e96b236a55bb8c0cc1e(
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

def _typecheckingstub__9105593602193f6c430b59ac16525785e4183211394cf7f4a2cc2ba6b2354e01(
    definition: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__982308674c1f12c5d781609eb6924d004d05afbe7d720d0e8a36fb8d432cf97c(
    scope: _constructs_77d1e7e8.Construct,
    sfn_principal: _IPrincipal_539bb2fd,
    sfn_props: typing.Union[StateMachineProps, typing.Dict[builtins.str, typing.Any]],
    graph: typing.Optional[StateGraph] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0110b36a0362589a48107daf28e3afe725be68dbbc869656e5a397d958ab43dd(
    *,
    definition: typing.Any = None,
    definition_s3_location: typing.Optional[typing.Union[CfnStateMachine.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    definition_string: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e34991edae92aa24b2bb75c9df693e2185f13c40aaf16ee220fc07ef991eaa7c(
    *,
    cause: typing.Optional[builtins.str] = None,
    cause_path: typing.Optional[builtins.str] = None,
    comment: typing.Optional[builtins.str] = None,
    error: typing.Optional[builtins.str] = None,
    error_path: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66d8682b1b0f9fb3dcb908bf3abca8eac95fe74d771082e1734661a049f7b124(
    obj: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c06b5d6a012a295ccc553ab17a70060cd3e1e30e5c31aa452a942673082b25ee(
    obj: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d3d657b8055d48ebc198eb4602747aafd8a12d895196df4b25610da111bc38b(
    obj: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__526ef9213812e76ec99bd530d4fbea7cc137d220b92525fe763d6d315362734f(
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

def _typecheckingstub__552303f8ba754bf57e2991b15cb67699f0b3be1720aaa2082c7f9e7c858151e8(
    scope: _constructs_77d1e7e8.Construct,
    _sfn_principal: _IPrincipal_539bb2fd,
    _sfn_props: typing.Union[StateMachineProps, typing.Dict[builtins.str, typing.Any]],
    _graph: typing.Optional[StateGraph] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff50e720afaefc7918f464dff492d9f8f0c7249476cc81f87395388b3a9c7e2(
    *,
    include_error_handlers: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dbb71ff45be8e3c94fd024ed10a51f986e7e089ef33bfae17adc18a574bf024(
    state: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__330377705d17e346007692578b485457a023c38351a46c6e22975a8a2b8192ae(
    identity: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31bd3fa2600dc4d3bf5687e9b4e868f708b68f607efbd2cfa7fb5f71fba15756(
    identity: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67aefd85a78dbc72556e294ed43f407d7fe2e40185f6dcefcda2b91bce4a9e6c(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b84edd8c4dd517d793cea8632f963ea68ac72a33187299a17ff7549b1e1dc14d(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92ed05a6f0e60c0385d1fe8dff7aa6ee6308b0dbdec64f6f70f98b5d1fdf23ed(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789a3eccb8c002cee01668ce309a302eced31df5999f98457203940330528ab4(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cab371f4587948afe28a72a9dde908f44a64ec26dee050808f7b1236c4c7da9(
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

def _typecheckingstub__28b90617c58a85778754752511df05551643031e0ec1d9e5687a61beda24688f(
    *,
    batch_input: typing.Optional[typing.Mapping[typing.Any, typing.Any]] = None,
    max_input_bytes_per_batch: typing.Optional[jsii.Number] = None,
    max_input_bytes_per_batch_path: typing.Optional[builtins.str] = None,
    max_items_per_batch: typing.Optional[jsii.Number] = None,
    max_items_per_batch_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8df53cde2f82ea6228f0c9a5a5ba0a4dd36c18fba9835f9f3150547f7cee754(
    *,
    bucket: _IBucket_42e086fd,
    max_items: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f608b3fd4b201a0a1482b5f0a70098cf3a3bd7d163d2b909a61815f6ff4a6737(
    *values: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088de6efa9a8b3d08870747fd80f1047204d1f99fcd9d2020876d01e904b961c(
    array: typing.Any,
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b6413ab81aefe0cb4d39cdffb2973b82823f6583665642e33f7d2e736ed49b5(
    array: typing.Any,
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__066df6cc20da873d2b1d90282c5ae886a4849b38a02d69dc36feae9c5490efe1(
    array: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc77862b0de7c7c02295791475860476ecdd7e6e12d7c6bba98efbeb931e86e1(
    array: typing.Any,
    chunk_size: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dc96e3ef5fe23ddc3268294a3758d98b1d5702ff86e2397d4b92453e45945c(
    start: jsii.Number,
    end: jsii.Number,
    step: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f7421e7bfe112627dadb759031678f094b4a6dc3c7ffb052c42413214015be(
    array: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e71d2c009521adfc2f539cfa65b95ae6f95e8c5f294620fc0b60c41a3234d22a(
    base64: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa34b328214814976f329340e3b2ff58e0c4bfec265b32b49a35f48c4428a7b0(
    input: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a65ae0ed7034cb9b7372f57ae44f6a74ad07f3a7e0613da2f76f53c592a3df50(
    format_string: builtins.str,
    *values: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5172eedb2a8508c195d9860a659889436742614328a885cc829ec82bbb6edab0(
    data: typing.Any,
    algorithm: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf495c28eeb68a82510bf46f764aafbb98e9152a5a58c61ac08b70497e448fc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e03a4f189712c0723816ff3f337f7563d3175582971c8fba095186f3644a1832(
    value1: typing.Any,
    value2: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6436aab05f387323f9cb74a6b784dd4c768239125631c909c725501e7bf7fd0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__791d54d72cca605dac6e53897a875a0836bef45df8935a30c09d1adb81bce886(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de44de70b3f9d451f756efc0fe38516dbc6d81f7af66a3acd65cacf20d4e0224(
    num1: jsii.Number,
    num2: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94e6703ef6e05edfee1f44b8f0522b8c9af9b8b61a177fe7416fbde4c0a9385(
    start: jsii.Number,
    end: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff382ceecb543f17e967c677aca2b4a8ce5745808e77f81d86c5f16e859b6888(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7664cbc5a31ad0f20576e6a4f0186b6bc4c3f582ca1f2a5e05e6947613b85107(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72ee75a1ba7f71927b8abcece4a47abab805af4517b1944222291ca6751c1d17(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41f25b1cfc6bdbcf6a60207ed8a5687faef8e1cf0a749fc6aed7aa5a806f40e4(
    input_string: builtins.str,
    splitter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad3c4072377fc7d5595082ca2f09f08e9f4d6f6919262abf3916a57efba60e27(
    json_string: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b27a348000a6495796817f9fd3b73934a015750ac2d2e09e165c45b4d2d5772(
    *,
    destination: _ILogGroup_3c4fa718,
    include_execution_data: typing.Optional[builtins.bool] = None,
    level: typing.Optional[LogLevel] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__123fd5cef3e54859ea847c1cc590a95cd39ecae394611b5e8add5b44b8354ab6(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    items_path: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_concurrency_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__841961f24272e2df479ccf3f591259c5dbc7bf471c2a6e11c7c7d61bf0e153ec(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    items_path: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_concurrency_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a04fcca9cbcddc34201ab96bfd6e4be7793eed6937bb07ccd5c1a2dc45a6484(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d80da5dbca7702d56f2a0dd67c4a5a72e182c08bcd852d74ea0fa21442f048(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    result: typing.Optional[Result] = None,
    result_path: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31ff219914b0d650a3cc1eb8631c77a0fd4affa44a5d994dc200757166b4959(
    *,
    execution_type: typing.Optional[ProcessorType] = None,
    mode: typing.Optional[ProcessorMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03617b4630db9dcdb093cf33053ff1c356d21c05e74b38ea8811464bc3fd24b4(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5d4ed5a0f4e741ccf9d2e3ddfe01fd92fa69cd2f3bd2f4aaf2bfacf3c04823(
    value: typing.Sequence[typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54f9e8f1a575aea261b9615223628a454b88112ac3018e8bdfd096921aad1c1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2893d7f002c7ba8fef05ee75544a163571341072dfac17ef5901e8bb26f2f4e4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db43a330458ab9fb395b00b0376ac06a03666ab606b8c9ddea25971d2ce0719f(
    value: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3615b36aa1e6d0193c5cb37ecfb6f1833c1503331f692609e2775414220fc42e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e7633dd729e9dd58a8e472e766fe10b0748d68a61f3d07bfec9cc5b8b4721f(
    *,
    bucket: _IBucket_42e086fd,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__984afa5a2055f0c35fc8c3cf6882093d3a32a8b56c725bd4e3c643f693f59d40(
    *,
    backoff_rate: typing.Optional[jsii.Number] = None,
    errors: typing.Optional[typing.Sequence[builtins.str]] = None,
    interval: typing.Optional[_Duration_4839e8c3] = None,
    jitter_strategy: typing.Optional[JitterType] = None,
    max_attempts: typing.Optional[jsii.Number] = None,
    max_delay: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc17fd96c577f0b5f18e9d0043337043a5db7cf7c35fdc1b09e959cf7f58221c(
    *,
    bucket: _IBucket_42e086fd,
    max_items: typing.Optional[jsii.Number] = None,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0839027a57f578b6a339286602923b0024b1f5e10dc2fb3ce8ac185f643a3bbc(
    *,
    bucket: _IBucket_42e086fd,
    max_items: typing.Optional[jsii.Number] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bfe6c744bf72f7e27c754b7de24b3cc1c8ee511680b9a61ee46fc118dd6a5c9(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
    prefix_states: typing.Optional[builtins.str] = None,
    state_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__095d7fa7ac65d852ef7641274fbdf11368859faad0abca011b7a488dead935f0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8285bd9e997c66a751e5455febad37743a69532169b26fb46600526e58ae970(
    states: typing.Sequence[State],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4622deb77b2918e678ad2d3a555fc84d4bb73d0ef35db3e8c844460b9bedd41c(
    start: State,
    *,
    include_error_handlers: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cec53ebef4ca820e7a85aa44b21deceeca71c230ec6ec855e5c5d6bb4880bdc0(
    start: State,
    *,
    include_error_handlers: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b73e6298c3658224e6c25d0abee853dc2cbd5ed77d4f935e724af3c0f2f36d9e(
    root: _constructs_77d1e7e8.IConstruct,
    prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9f89078424459b1c694d56e01d3910a25c8af32756935aaace102680b9010a8(
    branch: StateGraph,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df2c90f3de37dcdaf38ae6a3e70460c7cdfd78a154847df351088cd8a3b22960(
    condition: Condition,
    next: State,
    *,
    comment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5de90784fdeaa0fa9de5d18b85a161ebed718ee0e26df2989a66073001fcb12d(
    processor: StateGraph,
    *,
    execution_type: typing.Optional[ProcessorType] = None,
    mode: typing.Optional[ProcessorMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5562e3f75801d7a93e7b5728bae35a75af70b818bb2fc8dcd8e5aa13d0766eb9(
    iteration: StateGraph,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b71fffe032923dbb5cba43a418faf869357c809484ea9fcd9d26ceea47259a(
    x: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bdaefb727b4b60b3bebb8ea3b5db4a529cd533e6f827f21ccc0ff1822343254(
    graph: StateGraph,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee3ac76d6f92e799c65c47a04ad37a5bd88574a09db9de401595f330f3a126de(
    def_: State,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a69a1ac363b05a6ca439baf3f08831b411887d784118ecc98566dca2d8872de(
    next: State,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acfe4853db045f97378bdb44b521dcb1b8b46261f09a3786e2e5519eef4bf29d(
    graph: StateGraph,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa9d14a638bb5fe2be1b697c5d2a93e5cb602c30d93b1a5ca1eece88b36b1df(
    value: typing.Optional[State],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe26ac05d39997cba9f0b774e8732e0d7e33aa2715be53c5d2b6746630255f5f(
    value: typing.Optional[StateGraph],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18c6226d92e32b97a3bd2c7822b52c85358b3bd9174c0fcf373dcb3292508540(
    value: typing.Optional[StateGraph],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2064eb72a766ce7c2f9e0be9e43dd6ea46736ba5dd83721de5468681035dcb9f(
    value: typing.Optional[ProcessorConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2607af153540f000865a3d1354fc0086931cc826a2328eb0ae249231c9c35ef2(
    value: typing.Optional[ProcessorMode],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45cc793b7e63b62353e75a13b1efe7e1c03416eb034851d41ac5b855a86cc475(
    start_state: State,
    graph_description: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c41fc2afd076bb5952af77d1651e7e739c7d0276024e5796a2d444fd4ba8db(
    state_machine: StateMachine,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d649f93a2503f72395d055e758cb6b2340de6c8f77bdd56474547120392e535(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04cf5f7930ddcda9609e5560874ab06f26b4161423a2c9f15da86279c7ea7818(
    state: State,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a7cc2af53307fbb64a215cec870e4cea5ecf0b33bda74fef438d746903abbc4(
    graph: StateGraph,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d70fd99dfd053938f6857187678eff1538a49411584203816fe1ee6e2e95a57(
    value: typing.Optional[_Duration_4839e8c3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efdfc02291401a50a1d945e5208e9becb9828352fec32bc109ccebafc162614e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    definition: typing.Optional[IChainable] = None,
    definition_body: typing.Optional[DefinitionBody] = None,
    definition_substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    logs: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    state_machine_name: typing.Optional[builtins.str] = None,
    state_machine_type: typing.Optional[StateMachineType] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    tracing_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dec1adbbe53b54bdacbe2c45386b0970883e6a6ea92d2dd5187b13837238802(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    state_machine_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9d3d7898b3441749750d918233ae686af49db0c0bf54d9e123f31c4307ae53a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    state_machine_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9722a5396d55198fc0f7899f6cd72adb62c73fdbba082f415df383e5176a389a(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a379c65b3abf8422a7281124e586179178f0b3549b77f94825bb37365de34c5(
    identity: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__403096ab0bc513019435d412939f8df18641c1b52bfba18e821c391fa4b9024d(
    identity: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de328dbf28de2be4ba9b61ea81bce4e6d383ec0968b0e914acb7378b694c7b96(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efa2d941a46220f1692542e8c26652619270873ffe07f55fc9aa7a063799ed08(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1fc6bb22c960bfd2ca38ccc6a9922c3aadc1289dcf5bed18e2559bd0700d32e(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b16d8608f524913e06d7166d119ec903318d80b6015288e92a06223a03e95a(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00f442fc4f33cd6bcc931ba95c9117d241aef41be5171c27548e74d91fcd9be(
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

def _typecheckingstub__b1c5c1191e0b1af51b303ad19000be8e5c4e97e8491eb40cd68c462fa7e42f03(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c75eaddac3409d6cdf5dd627e25e2ee4bb9a37cb569d80a08e1847684c226d7(
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18974d4c0fc7d5b60c0b12888f566840996e0be64f94ae03e6639ebccff3409b(
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d23b501c893898901860f31ff1a0a0fa81eb89f06a7acf3eef4f15e46022f6(
    *,
    comment: typing.Optional[builtins.str] = None,
    definition: typing.Optional[IChainable] = None,
    definition_body: typing.Optional[DefinitionBody] = None,
    definition_substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    logs: typing.Optional[typing.Union[LogOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    state_machine_name: typing.Optional[builtins.str] = None,
    state_machine_type: typing.Optional[StateMachineType] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
    tracing_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b03d550137d1f7258c191a636f4e39f4e3ecdc83ecee214790010cc1584599d(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d556c15cb7d46dea75f4d4d5be455df4181351677d04c896b3cece7c2f4164(
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

def _typecheckingstub__cb5817d6d61140231e4bd01c29102ec205d9d1d0f848af6dd3aa28a11467c52a(
    body: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae45f38855ad466a878a7d83ebc926e1b656c12480ab66d4c642079849950e1(
    _scope: _constructs_77d1e7e8.Construct,
    _sfn_principal: _IPrincipal_539bb2fd,
    _sfn_props: typing.Union[StateMachineProps, typing.Dict[builtins.str, typing.Any]],
    _graph: typing.Optional[StateGraph] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35ef3ad1b65975090819e8b098b2b754472124db44d9bf100117c9f3c97b861(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bcb322679d9a165f0c2d8e6c39b61e6673747fb3e4fb30298aed922536d5e7d(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16bc413eb726c46f5b831021734efa77e701554386db73af23b8f97b5efcfab(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f51b46946413e542cf081c0a3cecd65b415e2e9f64f9e57d989a11ff927db7(
    obj: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4460ece474b7c5793d096111af286d4137cfc1cfc5ca165e37c695701d7c5af7(
    text: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b853c8cb66c2f5d1054d5d4bf9d98efca35d979661a5be38eaf7dd6e44cef4cc(
    *,
    metric_dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    metric_prefix_plural: typing.Optional[builtins.str] = None,
    metric_prefix_singular: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bddea2e373d15cc4e0247b91d3bca3f413aeb2470100f4983965f64d4e53db0(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f0576900770ad89340628b613309cb0873d7789836eb9f1f1a5eb5eea3129f9(
    expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8030332c4c85b7a6f12c27dd03b5ae36fd9b38ad46888955d3d5325978e42311(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[Credentials, typing.Dict[builtins.str, typing.Any]]] = None,
    heartbeat: typing.Optional[_Duration_4839e8c3] = None,
    heartbeat_timeout: typing.Optional[Timeout] = None,
    input_path: typing.Optional[builtins.str] = None,
    integration_pattern: typing.Optional[IntegrationPattern] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
    task_timeout: typing.Optional[Timeout] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__661e0a128e151fbb1312f41cea74fbc148d98cfa524d7238bc6d0994bff443e4(
    handler: IChainable,
    *,
    errors: typing.Optional[typing.Sequence[builtins.str]] = None,
    result_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e107390a3e2550b832e771f6471431f1576a6bdab08445ca9d4fef451ab0888(
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

def _typecheckingstub__ec5d5503bc58bc8692d34bfb6d62f6cd19c7cbd72d15cfc1e421a14b3a77eeb4(
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3476e23aff91128cb42df4fe5996139f3397e205600e914f57e1d211d4569d6(
    graph: StateGraph,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__487ae196f9ce32bf6886dc0cf55352b7b5f5a24cc25636bf22f525ed68b9944b(
    *,
    comment: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[Credentials, typing.Dict[builtins.str, typing.Any]]] = None,
    heartbeat: typing.Optional[_Duration_4839e8c3] = None,
    heartbeat_timeout: typing.Optional[Timeout] = None,
    input_path: typing.Optional[builtins.str] = None,
    integration_pattern: typing.Optional[IntegrationPattern] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
    task_timeout: typing.Optional[Timeout] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ede5a9c52734b5209acc0043a69f8b4333ea0d0bf32a48bb028d1695fc6077b9(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a04d027f66b61507aa552be04c2ce9593fc80d23f348ffb16cd24bef17942c5(
    duration: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6a8ce927e9d411d4263a43306a0e94bd7a5d563bd35e990ab82dbb660c79604(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    time: WaitTime,
    comment: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae1afef777a31475bd858e03eee2febe97f62b64e27252472e23b8636248fb2(
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534eb46b5e3f50b25dea609490a5fd97e2e7f56c6eeed5ea19d37b6997865461(
    *,
    time: WaitTime,
    comment: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a809799722bcdc0c6cece03ff859948273709f66e461d30e317ffbd0ab85aca2(
    duration: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd7acf00a5586f287932ed2fd2b8aea94218c4e4ed6ce940a9b4f871ce7f4ce(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74e6bb97aa64089395900b447ec0f2759ffee7f85b56e84eeaded8aa5dc0a3b2(
    timestamp: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88e6966e5553a37e050d3139be3d625237f07f7a3a9c23fa5bb2232f8c50be0(
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e3c9e855deb3c2b532345b0d2587dc14ad685d296794311bbf280ab9f6b10d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    activity_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23b5f89f13e4afd1f578e47dbd171c4eb80f5231c5844de3057b40bd4e21f11(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    activity_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8ac7cbf2053f3b4870981fbfd4f3dd21553e4a66f1c2462b2aa64dfa477566(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    activity_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d112510c9f361d871db6717bbfc59060fea12f921f3593ef09bffe88a48574(
    identity: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f960b5875dcb81c7f4b6e91c03015375df2e5c6bb3da84f476bf59c2baaba3e(
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

def _typecheckingstub__26a438e6d1ba5d4cefba34fbd2fbe2750e8c479b9d8629bb5a75c0c294b63f1a(
    start_state: State,
    end_states: typing.Sequence[INextable],
    last_added: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c955028ecc98936f323c8550ebfcb4aeef25333244714448c6f9471f6ee0ad4f(
    start: IChainable,
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee2c65d541581403b83500bc7df204a5106888551ba6bd48d4870081c4fd4cc5(
    state: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd744fb658532d41afa54a85d0b054476b1228d7172fa8e1c494c14f2fa7d5f(
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__468194d7b14012a289ab0c26efcba49fbd09832b9f87d79467e6334c81f8495e(
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd08795a00486d8e3c10949ac36b6c93109ecc1bb3a98a3e10990fe66c603599(
    chainable: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e36acb57c00ddfc834d6027c29b11bab26d8b33890707c567bc4f7804a9786f2(
    scope: _constructs_77d1e7e8.Construct,
    _sfn_principal: _IPrincipal_539bb2fd,
    sfn_props: typing.Union[StateMachineProps, typing.Dict[builtins.str, typing.Any]],
    graph: typing.Optional[StateGraph] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c27d2454927afdcf01784360c45c98368486d465f54265c1199aa70baaae72(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58e659f8b3dba6c37e918b57bca058880f69e9f4da0a230edb80f223a37fbc82(
    def_: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5351e3ee5e1f4b5b58ec322e57749fdd65cdc8bb76443318ef63b4eedc5cb0b(
    condition: Condition,
    next: IChainable,
    *,
    comment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab8400575bd03faff673b28e1d5b185298520835ed4e6586fba73ccac57c6f0e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    state_json: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af51c0590f129eeca0846aafaf90162dc24f8f5c4a9df58d88432f4facb4ff08(
    handler: IChainable,
    *,
    errors: typing.Optional[typing.Sequence[builtins.str]] = None,
    result_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c55cf19adb97a87b3d9f8561497d58ec4f0dc221883c0d757f4bec5f4690cadd(
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e484af477b46c0e70f635ed9610c7183f70c2184fd7a48f091a5477df9ee3d5d(
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    items_path: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_concurrency_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
    item_batcher: typing.Optional[ItemBatcher] = None,
    item_reader: typing.Optional[IItemReader] = None,
    label: typing.Optional[builtins.str] = None,
    map_execution_type: typing.Optional[StateMachineType] = None,
    result_writer: typing.Optional[ResultWriter] = None,
    tolerated_failure_count: typing.Optional[jsii.Number] = None,
    tolerated_failure_count_path: typing.Optional[builtins.str] = None,
    tolerated_failure_percentage: typing.Optional[jsii.Number] = None,
    tolerated_failure_percentage_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c583b760e906e99018014914554eafc9ccbd2b3420c0edbf5013a7649fb8c0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cause: typing.Optional[builtins.str] = None,
    cause_path: typing.Optional[builtins.str] = None,
    comment: typing.Optional[builtins.str] = None,
    error: typing.Optional[builtins.str] = None,
    error_path: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d25d492eb753f17d954200a30dfae328a6f5710335312d1b5ffe0113a9ded82(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    items_path: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_concurrency_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bfdae9c7d12de08b43f94e8bc33eaeef588cdf2a814eb233b86a9976943ed7b(
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94610eed4635a69c6d4a92818527e6ecdf15561092c488fb6caa8d8ec9778a22(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__182be923de45451a3be4a0e5bda7642ee82b8bfb46a7fd13f9cdc8084f23f9bb(
    handler: IChainable,
    *,
    errors: typing.Optional[typing.Sequence[builtins.str]] = None,
    result_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f51369cf1df8050a9193691c532125259fc7c9e4293a269130e56f7600e8e869(
    graph: StateGraph,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697633cbf62e47597c9fdc7d002c0aee2b85afe1b449f1d0ce4917552cf01271(
    *branches: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf2f89f1d526659416028630d3a07331a2f13a5067fd5e45f41dd46895179826(
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d42bf3e652e85f6ec94972b87e3cd78f4420b89e56b719dae3323e4b9c485f2f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    result: typing.Optional[Result] = None,
    result_path: typing.Optional[builtins.str] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4f3a4b985638e018cf9da160ea401084953cf6a22e9ff97cb9b82310d664a55(
    next: IChainable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd148cd8282abe643b20452cf3c099e0d66560a90ddb7ec54f83740859fe615d(
    *,
    bucket: _IBucket_42e086fd,
    max_items: typing.Optional[jsii.Number] = None,
    key: builtins.str,
    csv_headers: typing.Optional[CsvHeaders] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f7d4222fc9728237ee261157ec268cfd8f396c371bc6402ec7a1a4ea42917d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    item_batcher: typing.Optional[ItemBatcher] = None,
    item_reader: typing.Optional[IItemReader] = None,
    label: typing.Optional[builtins.str] = None,
    map_execution_type: typing.Optional[StateMachineType] = None,
    result_writer: typing.Optional[ResultWriter] = None,
    tolerated_failure_count: typing.Optional[jsii.Number] = None,
    tolerated_failure_count_path: typing.Optional[builtins.str] = None,
    tolerated_failure_percentage: typing.Optional[jsii.Number] = None,
    tolerated_failure_percentage_path: typing.Optional[builtins.str] = None,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    items_path: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_concurrency_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31933264cd976eda9b915ac15b88658cd66607d4305ac5503092b27ee9650f4(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b96420299a828b17719584b98a81fc0affc397b69e90092f29e7d9afb2d48324(
    handler: IChainable,
    *,
    errors: typing.Optional[typing.Sequence[builtins.str]] = None,
    result_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f10278e982625ca06b2d3266813a2418de02709637602f80e07445047d125579(
    processor: IChainable,
    *,
    execution_type: typing.Optional[ProcessorType] = None,
    mode: typing.Optional[ProcessorMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e505be41bf00ad65952efb21c612874ac8a42269a7a70f2a1c0ee866dbb902c0(
    graph: StateGraph,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d28fbd908923a38f00f8f82b2387552ae3a53fe5d860d66d336f49ba4c36c1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    comment: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
    item_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    items_path: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_concurrency_path: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
    result_path: typing.Optional[builtins.str] = None,
    result_selector: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    state_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__477e230f69a651e6927594095a0d2d681abd0858db9b79de5caf573bda0f7eb6(
    handler: IChainable,
    *,
    errors: typing.Optional[typing.Sequence[builtins.str]] = None,
    result_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57880144217f818052832dac038a8875120f8ef30f1d286864bba6785bb1afd5(
    processor: IChainable,
    *,
    execution_type: typing.Optional[ProcessorType] = None,
    mode: typing.Optional[ProcessorMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46bf9177a387f4dcf5be0d20783b744edaca8974e7384b16a446321cc3bc65aa(
    iterator: IChainable,
) -> None:
    """Type checking stubs"""
    pass
