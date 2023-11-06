'''
# Assertions

If you're migrating from the old `@aws-cdk/assert` library, first use this migration guide to migrate from `@aws-cdk/assert` to `@aws-cdk/assertions` found in
[our GitHub repository](https://github.com/aws/aws-cdk/blob/v1-main/packages/@aws-cdk/assertions/MIGRATING.md). Then, you can migrate your application to AWS CDK v2 in order to use this library using [this guide](https://docs.aws.amazon.com/cdk/v2/guide/migrating-v2.html).

Functions for writing test asserting against CDK applications, with focus on CloudFormation templates.

The `Template` class includes a set of methods for writing assertions against CloudFormation templates. Use one of the `Template.fromXxx()` static methods to create an instance of this class.

To create `Template` from CDK stack, start off with:

```python
from aws_cdk import Stack
from aws_cdk.assertions import Template

stack = Stack()
# ...
template = Template.from_stack(stack)
```

Alternatively, assertions can be run on an existing CloudFormation template -

```python
template_json = "{ \"Resources\": ... }" # The CloudFormation template as JSON serialized string.
template = Template.from_string(template_json)
```

**Cyclical Resources Note**

If allowing cyclical references is desired, for example in the case of unprocessed Transform templates, supply TemplateParsingOptions and
set skipCyclicalDependenciesCheck to true. In all other cases, will fail on detecting cyclical dependencies.

## Full Template Match

The simplest assertion would be to assert that the template matches a given
template.

```python
template.template_matches({
    "Resources": {
        "BarLogicalId": {
            "Type": "Foo::Bar",
            "Properties": {
                "Baz": "Qux"
            }
        }
    }
})
```

By default, the `templateMatches()` API will use the an 'object-like' comparison,
which means that it will allow for the actual template to be a superset of the
given expectation. See [Special Matchers](#special-matchers) for details on how
to change this.

Snapshot testing is a common technique to store a snapshot of the output and
compare it during future changes. Since CloudFormation templates are human readable,
they are a good target for snapshot testing.

The `toJSON()` method on the `Template` can be used to produce a well formatted JSON
of the CloudFormation template that can be used as a snapshot.

See [Snapshot Testing in Jest](https://jestjs.io/docs/snapshot-testing) and [Snapshot
Testing in Java](https://json-snapshot.github.io/).

## Counting Resources

This module allows asserting the number of resources of a specific type found
in a template.

```python
template.resource_count_is("Foo::Bar", 2)
```

You can also count the number of resources of a specific type whose `Properties`
section contains the specified properties:

```python
template.resource_properties_count_is("Foo::Bar", {
    "Foo": "Bar",
    "Baz": 5,
    "Qux": ["Waldo", "Fred"]
}, 1)
```

## Resource Matching & Retrieval

Beyond resource counting, the module also allows asserting that a resource with
specific properties are present.

The following code asserts that the `Properties` section of a resource of type
`Foo::Bar` contains the specified properties -

```python
template.has_resource_properties("Foo::Bar", {
    "Lorem": "Ipsum",
    "Baz": 5,
    "Qux": ["Waldo", "Fred"]
})
```

You can also assert that the `Properties` section of all resources of type
`Foo::Bar` contains the specified properties -

```python
template.all_resources_properties("Foo::Bar", {
    "Lorem": "Ipsum",
    "Baz": 5,
    "Qux": ["Waldo", "Fred"]
})
```

Alternatively, if you would like to assert the entire resource definition, you
can use the `hasResource()` API.

```python
template.has_resource("Foo::Bar", {
    "Properties": {"Lorem": "Ipsum"},
    "DependsOn": ["Waldo", "Fred"]
})
```

You can also assert the definitions of all resources of a type using the
`allResources()` API.

```python
template.all_resources("Foo::Bar", {
    "Properties": {"Lorem": "Ipsum"},
    "DependsOn": ["Waldo", "Fred"]
})
```

Beyond assertions, the module provides APIs to retrieve matching resources.
The `findResources()` API is complementary to the `hasResource()` API, except,
instead of asserting its presence, it returns the set of matching resources.

By default, the `hasResource()` and `hasResourceProperties()` APIs perform deep
partial object matching. This behavior can be configured using matchers.
See subsequent section on [special matchers](#special-matchers).

## Output and Mapping sections

The module allows you to assert that the CloudFormation template contains an Output
that matches specific properties. The following code asserts that a template contains
an Output with a `logicalId` of `Foo` and the specified properties -

```python
expected = {
    "Value": "Bar",
    "Export": {"Name": "ExportBaz"}
}
template.has_output("Foo", expected)
```

If you want to match against all Outputs in the template, use `*` as the `logicalId`.

```python
template.has_output("*", {
    "Value": "Bar",
    "Export": {"Name": "ExportBaz"}
})
```

`findOutputs()` will return a set of outputs that match the `logicalId` and `props`,
and you can use the `'*'` special case as well.

```python
result = template.find_outputs("*", {"Value": "Fred"})
expect(result.Foo).to_equal({"Value": "Fred", "Description": "FooFred"})
expect(result.Bar).to_equal({"Value": "Fred", "Description": "BarFred"})
```

The APIs `hasMapping()`, `findMappings()`, `hasCondition()`, and `hasCondtions()` provide similar functionalities.

## Special Matchers

The expectation provided to the `hasXxx()`, `findXxx()` and `templateMatches()`
APIs, besides carrying literal values, as seen in the above examples, also accept
special matchers.

They are available as part of the `Match` class.

### Object Matchers

The `Match.objectLike()` API can be used to assert that the target is a superset
object of the provided pattern.
This API will perform a deep partial match on the target.
Deep partial matching is where objects are matched partially recursively. At each
level, the list of keys in the target is a subset of the provided pattern.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": {
#           "Wobble": "Flob",
#           "Bob": "Cat"
#         }
#       }
#     }
#   }
# }

# The following will NOT throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Fred": Match.object_like({
        "Wobble": "Flob"
    })
})

# The following will throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Fred": Match.object_like({
        "Brew": "Coffee"
    })
})
```

The `Match.objectEquals()` API can be used to assert a target as a deep exact
match.

### Presence and Absence

The `Match.absent()` matcher can be used to specify that a specific
value should not exist on the target. This can be used within `Match.objectLike()`
or outside of any matchers.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": {
#           "Wobble": "Flob",
#         }
#       }
#     }
#   }
# }

# The following will NOT throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Fred": Match.object_like({
        "Bob": Match.absent()
    })
})

# The following will throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Fred": Match.object_like({
        "Wobble": Match.absent()
    })
})
```

The `Match.anyValue()` matcher can be used to specify that a specific value should be found
at the location. This matcher will fail if when the target location has null-ish values
(i.e., `null` or `undefined`).

This matcher can be combined with any of the other matchers.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": {
#           "Wobble": ["Flob", "Flib"],
#         }
#       }
#     }
#   }
# }

# The following will NOT throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Fred": {
        "Wobble": [Match.any_value(), Match.any_value()]
    }
})

# The following will throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Fred": {
        "Wimble": Match.any_value()
    }
})
```

### Array Matchers

The `Match.arrayWith()` API can be used to assert that the target is equal to or a subset
of the provided pattern array.
This API will perform subset match on the target.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": ["Flob", "Cat"]
#       }
#     }
#   }
# }

# The following will NOT throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Fred": Match.array_with(["Flob"])
})

# The following will throw an assertion error
template.has_resource_properties("Foo::Bar", Match.object_like({
    "Fred": Match.array_with(["Wobble"])
}))
```

*Note:* The list of items in the pattern array should be in order as they appear in the
target array. Out of order will be recorded as a match failure.

Alternatively, the `Match.arrayEquals()` API can be used to assert that the target is
exactly equal to the pattern array.

### String Matchers

The `Match.stringLikeRegexp()` API can be used to assert that the target matches the
provided regular expression.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Template": "const includeHeaders = true;"
#       }
#     }
#   }
# }

# The following will NOT throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Template": Match.string_like_regexp("includeHeaders = (true|false)")
})

# The following will throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Template": Match.string_like_regexp("includeHeaders = null")
})
```

### Not Matcher

The not matcher inverts the search pattern and matches all patterns in the path that does
not match the pattern specified.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": ["Flob", "Cat"]
#       }
#     }
#   }
# }

# The following will NOT throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Fred": Match.not(["Flob"])
})

# The following will throw an assertion error
template.has_resource_properties("Foo::Bar", Match.object_like({
    "Fred": Match.not(["Flob", "Cat"])
}))
```

### Serialized JSON

Often, we find that some CloudFormation Resource types declare properties as a string,
but actually expect JSON serialized as a string.
For example, the [`BuildSpec` property of `AWS::CodeBuild::Project`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-buildspec),
the [`Definition` property of `AWS::StepFunctions::StateMachine`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definition),
to name a couple.

The `Match.serializedJson()` matcher allows deep matching within a stringified JSON.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Baz": "{ \"Fred\": [\"Waldo\", \"Willow\"] }"
#       }
#     }
#   }
# }

# The following will NOT throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Baz": Match.serialized_json({
        "Fred": Match.array_with(["Waldo"])
    })
})

# The following will throw an assertion error
template.has_resource_properties("Foo::Bar", {
    "Baz": Match.serialized_json({
        "Fred": ["Waldo", "Johnny"]
    })
})
```

## Capturing Values

The matcher APIs documented above allow capturing values in the matching entry
(Resource, Output, Mapping, etc.). The following code captures a string from a
matching resource.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": ["Flob", "Cat"],
#         "Waldo": ["Qix", "Qux"],
#       }
#     }
#   }
# }

fred_capture = Capture()
waldo_capture = Capture()
template.has_resource_properties("Foo::Bar", {
    "Fred": fred_capture,
    "Waldo": ["Qix", waldo_capture]
})

fred_capture.as_array() # returns ["Flob", "Cat"]
waldo_capture.as_string()
```

With captures, a nested pattern can also be specified, so that only targets
that match the nested pattern will be captured. This pattern can be literals or
further Matchers.

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar1": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": ["Flob", "Cat"],
#       }
#     }
#     "MyBar2": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": ["Qix", "Qux"],
#       }
#     }
#   }
# }

capture = Capture(Match.array_with(["Cat"]))
template.has_resource_properties("Foo::Bar", {
    "Fred": capture
})

capture.as_array()
```

When multiple resources match the given condition, each `Capture` defined in
the condition will capture all matching values. They can be paged through using
the `next()` API. The following example illustrates this -

```python
# Given a template -
# {
#   "Resources": {
#     "MyBar": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": "Flob",
#       }
#     },
#     "MyBaz": {
#       "Type": "Foo::Bar",
#       "Properties": {
#         "Fred": "Quib",
#       }
#     }
#   }
# }

fred_capture = Capture()
template.has_resource_properties("Foo::Bar", {
    "Fred": fred_capture
})

fred_capture.as_string() # returns "Flob"
fred_capture.next() # returns true
fred_capture.as_string()
```

## Asserting Annotations

In addition to template matching, we provide an API for annotation matching.
[Annotations](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.Annotations.html)
can be added via the [Aspects](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.Aspects.html)
API. You can learn more about Aspects [here](https://docs.aws.amazon.com/cdk/v2/guide/aspects.html).

Say you have a `MyAspect` and a `MyStack` that uses `MyAspect`:

```python
import aws_cdk as cdk
from constructs import Construct, IConstruct

@jsii.implements(cdk.IAspect)
class MyAspect:
    def visit(self, node):
        if node instanceof cdk.CfnResource && node.cfn_resource_type == "Foo::Bar":
            self.error(node, "we do not want a Foo::Bar resource")

    def error(self, node, message):
        cdk.Annotations.of(node).add_error(message)

class MyStack(cdk.Stack):
    def __init__(self, scope, id):
        super().__init__(scope, id)

        stack = cdk.Stack()
        cdk.CfnResource(stack, "Foo",
            type="Foo::Bar",
            properties={
                "Fred": "Thud"
            }
        )
        cdk.Aspects.of(stack).add(MyAspect())
```

We can then assert that the stack contains the expected Error:

```python
# import { Annotations } from '@aws-cdk/assertions';

Annotations.from_stack(stack).has_error("/Default/Foo", "we do not want a Foo::Bar resource")
```

Here are the available APIs for `Annotations`:

* `hasError()`, `hasNoError()`, and `findError()`
* `hasWarning()`, `hasNoWarning()`, and `findWarning()`
* `hasInfo()`, `hasNoInfo()`, and `findInfo()`

The corresponding `findXxx()` API is complementary to the `hasXxx()` API, except instead
of asserting its presence, it returns the set of matching messages.

In addition, this suite of APIs is compatible with `Matchers` for more fine-grained control.
For example, the following assertion works as well:

```python
Annotations.from_stack(stack).has_error("/Default/Foo",
    Match.string_like_regexp(".*Foo::Bar.*"))
```
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

from .. import Stack as _Stack_2866e57f
from ..cx_api import SynthesisMessage as _SynthesisMessage_b3ae3c62


class Annotations(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.assertions.Annotations",
):
    '''Suite of assertions that can be run on a CDK Stack.

    Focused on asserting annotations.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import assertions
        
        # stack: cdk.Stack
        
        annotations = assertions.Annotations.from_stack(stack)
    '''

    @jsii.member(jsii_name="fromStack")
    @builtins.classmethod
    def from_stack(cls, stack: _Stack_2866e57f) -> "Annotations":
        '''Base your assertions on the messages returned by a synthesized CDK ``Stack``.

        :param stack: the CDK Stack to run assertions on.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dffec3a2a7a1a9f1b88ff9e3533fd5895867e3261f050f0b21259953c59554f)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
        return typing.cast("Annotations", jsii.sinvoke(cls, "fromStack", [stack]))

    @jsii.member(jsii_name="findError")
    def find_error(
        self,
        construct_path: builtins.str,
        message: typing.Any,
    ) -> typing.List[_SynthesisMessage_b3ae3c62]:
        '''Get the set of matching errors of a given construct path and message.

        :param construct_path: the construct path to the error. Provide ``'*'`` to match all errors in the template.
        :param message: the error message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f6064e884b81060ed5691b5c77d99fe9171969d33e0f5c39db63629f9b14233)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(typing.List[_SynthesisMessage_b3ae3c62], jsii.invoke(self, "findError", [construct_path, message]))

    @jsii.member(jsii_name="findInfo")
    def find_info(
        self,
        construct_path: builtins.str,
        message: typing.Any,
    ) -> typing.List[_SynthesisMessage_b3ae3c62]:
        '''Get the set of matching infos of a given construct path and message.

        :param construct_path: the construct path to the info. Provide ``'*'`` to match all infos in the template.
        :param message: the info message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8194b87ea6257ea629eb3ca14994457d25764fa7dc4dc21a1ecebfb7392cf893)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(typing.List[_SynthesisMessage_b3ae3c62], jsii.invoke(self, "findInfo", [construct_path, message]))

    @jsii.member(jsii_name="findWarning")
    def find_warning(
        self,
        construct_path: builtins.str,
        message: typing.Any,
    ) -> typing.List[_SynthesisMessage_b3ae3c62]:
        '''Get the set of matching warning of a given construct path and message.

        :param construct_path: the construct path to the warning. Provide ``'*'`` to match all warnings in the template.
        :param message: the warning message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b9ed07482937b302b271f5ecd83ad83b12af81c8b5912069077f5465abc36a)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(typing.List[_SynthesisMessage_b3ae3c62], jsii.invoke(self, "findWarning", [construct_path, message]))

    @jsii.member(jsii_name="hasError")
    def has_error(self, construct_path: builtins.str, message: typing.Any) -> None:
        '''Assert that an error with the given message exists in the synthesized CDK ``Stack``.

        :param construct_path: the construct path to the error. Provide ``'*'`` to match all errors in the template.
        :param message: the error message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b7c83521585d4519a99991c56b91963a89741ac27b8a8914684737e203a2273)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(None, jsii.invoke(self, "hasError", [construct_path, message]))

    @jsii.member(jsii_name="hasInfo")
    def has_info(self, construct_path: builtins.str, message: typing.Any) -> None:
        '''Assert that an info with the given message exists in the synthesized CDK ``Stack``.

        :param construct_path: the construct path to the info. Provide ``'*'`` to match all info in the template.
        :param message: the info message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4474081f3d9b4d5d317af8608f249a04ddea10859b5496e931c243fbd7bbffa9)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(None, jsii.invoke(self, "hasInfo", [construct_path, message]))

    @jsii.member(jsii_name="hasNoError")
    def has_no_error(self, construct_path: builtins.str, message: typing.Any) -> None:
        '''Assert that an error with the given message does not exist in the synthesized CDK ``Stack``.

        :param construct_path: the construct path to the error. Provide ``'*'`` to match all errors in the template.
        :param message: the error message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca70d40be65a245d658fb88df040d0e83e8e632fdd5e2ee95dc766f1c438a795)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(None, jsii.invoke(self, "hasNoError", [construct_path, message]))

    @jsii.member(jsii_name="hasNoInfo")
    def has_no_info(self, construct_path: builtins.str, message: typing.Any) -> None:
        '''Assert that an info with the given message does not exist in the synthesized CDK ``Stack``.

        :param construct_path: the construct path to the info. Provide ``'*'`` to match all info in the template.
        :param message: the info message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c305e483a4c9a4cc2875c6b72244cf281efd6942b9742401ecc991a2aaa0fd2)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(None, jsii.invoke(self, "hasNoInfo", [construct_path, message]))

    @jsii.member(jsii_name="hasNoWarning")
    def has_no_warning(self, construct_path: builtins.str, message: typing.Any) -> None:
        '''Assert that an warning with the given message does not exist in the synthesized CDK ``Stack``.

        :param construct_path: the construct path to the warning. Provide ``'*'`` to match all warnings in the template.
        :param message: the warning message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a9a4d7658d222b5a854156cb3f9e2156ce1fca2f67a73459ffe8631f270eae)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(None, jsii.invoke(self, "hasNoWarning", [construct_path, message]))

    @jsii.member(jsii_name="hasWarning")
    def has_warning(self, construct_path: builtins.str, message: typing.Any) -> None:
        '''Assert that an warning with the given message exists in the synthesized CDK ``Stack``.

        :param construct_path: the construct path to the warning. Provide ``'*'`` to match all warnings in the template.
        :param message: the warning message as should be expected. This should be a string or Matcher object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef14b35c0df2f219e2c887dd18c1ee458e984bcbfa8b30a116ad13762f24a5ad)
            check_type(argname="argument construct_path", value=construct_path, expected_type=type_hints["construct_path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast(None, jsii.invoke(self, "hasWarning", [construct_path, message]))


class Match(metaclass=jsii.JSIIAbstractClass, jsii_type="aws-cdk-lib.assertions.Match"):
    '''Partial and special matching during template assertions.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="absent")
    @builtins.classmethod
    def absent(cls) -> "Matcher":
        '''Use this matcher in the place of a field's value, if the field must not be present.'''
        return typing.cast("Matcher", jsii.sinvoke(cls, "absent", []))

    @jsii.member(jsii_name="anyValue")
    @builtins.classmethod
    def any_value(cls) -> "Matcher":
        '''Matches any non-null value at the target.'''
        return typing.cast("Matcher", jsii.sinvoke(cls, "anyValue", []))

    @jsii.member(jsii_name="arrayEquals")
    @builtins.classmethod
    def array_equals(cls, pattern: typing.Sequence[typing.Any]) -> "Matcher":
        '''Matches the specified pattern with the array found in the same relative path of the target.

        The set of elements (or matchers) must match exactly and in order.

        :param pattern: the pattern to match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc2fc6b89509c8782c1d71064aba95c7f8ce8825fb3287ada62d9f7a7fcd3ca3)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        return typing.cast("Matcher", jsii.sinvoke(cls, "arrayEquals", [pattern]))

    @jsii.member(jsii_name="arrayWith")
    @builtins.classmethod
    def array_with(cls, pattern: typing.Sequence[typing.Any]) -> "Matcher":
        '''Matches the specified pattern with the array found in the same relative path of the target.

        The set of elements (or matchers) must be in the same order as would be found.

        :param pattern: the pattern to match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fafc2dce97140cefc00887659682f218b01db7c89e52b4430b2843868fb3589f)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        return typing.cast("Matcher", jsii.sinvoke(cls, "arrayWith", [pattern]))

    @jsii.member(jsii_name="exact")
    @builtins.classmethod
    def exact(cls, pattern: typing.Any) -> "Matcher":
        '''Deep exact matching of the specified pattern to the target.

        :param pattern: the pattern to match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd6b2bcc466f2428e69319f1508695c522a5e069b08ce97c06e72e3d2927aa57)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        return typing.cast("Matcher", jsii.sinvoke(cls, "exact", [pattern]))

    @jsii.member(jsii_name="not")
    @builtins.classmethod
    def not_(cls, pattern: typing.Any) -> "Matcher":
        '''Matches any target which does NOT follow the specified pattern.

        :param pattern: the pattern to NOT match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ac65d172037fe8d399409899d5d6843aaa87d02106d1021d4d528350f15adb)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        return typing.cast("Matcher", jsii.sinvoke(cls, "not", [pattern]))

    @jsii.member(jsii_name="objectEquals")
    @builtins.classmethod
    def object_equals(
        cls,
        pattern: typing.Mapping[builtins.str, typing.Any],
    ) -> "Matcher":
        '''Matches the specified pattern to an object found in the same relative path of the target.

        The keys and their values (or matchers) must match exactly with the target.

        :param pattern: the pattern to match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26dde9bd8eb2015c3779e6c829fa6c442206244c4003e11e435d3f73943b01ac)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        return typing.cast("Matcher", jsii.sinvoke(cls, "objectEquals", [pattern]))

    @jsii.member(jsii_name="objectLike")
    @builtins.classmethod
    def object_like(
        cls,
        pattern: typing.Mapping[builtins.str, typing.Any],
    ) -> "Matcher":
        '''Matches the specified pattern to an object found in the same relative path of the target.

        The keys and their values (or matchers) must be present in the target but the target can be a superset.

        :param pattern: the pattern to match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95fb0724e4fc6f68e1782f5f00503622e0a52a46523a159830c3f2092f1bb53c)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        return typing.cast("Matcher", jsii.sinvoke(cls, "objectLike", [pattern]))

    @jsii.member(jsii_name="serializedJson")
    @builtins.classmethod
    def serialized_json(cls, pattern: typing.Any) -> "Matcher":
        '''Matches any string-encoded JSON and applies the specified pattern after parsing it.

        :param pattern: the pattern to match after parsing the encoded JSON.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0764fac955478ef959c585f03fb2034993495f3f94a6cac7a567e56978cf4cee)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        return typing.cast("Matcher", jsii.sinvoke(cls, "serializedJson", [pattern]))

    @jsii.member(jsii_name="stringLikeRegexp")
    @builtins.classmethod
    def string_like_regexp(cls, pattern: builtins.str) -> "Matcher":
        '''Matches targets according to a regular expression.

        :param pattern: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98a9c300f7bb1df47fc43d6b03131a9b5739f02259f381da6d7e61074f71c366)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        return typing.cast("Matcher", jsii.sinvoke(cls, "stringLikeRegexp", [pattern]))


class _MatchProxy(Match):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Match).__jsii_proxy_class__ = lambda : _MatchProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.assertions.MatchCapture",
    jsii_struct_bases=[],
    name_mapping={"capture": "capture", "value": "value"},
)
class MatchCapture:
    def __init__(self, *, capture: "Capture", value: typing.Any) -> None:
        '''Information about a value captured during match.

        :param capture: The instance of Capture class to which this capture is associated with.
        :param value: The value that was captured.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import assertions
            
            # capture: assertions.Capture
            # value: Any
            
            match_capture = assertions.MatchCapture(
                capture=capture,
                value=value
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaff32ba4b1c664eb41260f4e77edb8a54d7961b3b19bd287bf22ead0930c217)
            check_type(argname="argument capture", value=capture, expected_type=type_hints["capture"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capture": capture,
            "value": value,
        }

    @builtins.property
    def capture(self) -> "Capture":
        '''The instance of Capture class to which this capture is associated with.'''
        result = self._values.get("capture")
        assert result is not None, "Required property 'capture' is missing"
        return typing.cast("Capture", result)

    @builtins.property
    def value(self) -> typing.Any:
        '''The value that was captured.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MatchCapture(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.assertions.MatchFailure",
    jsii_struct_bases=[],
    name_mapping={
        "matcher": "matcher",
        "message": "message",
        "path": "path",
        "cost": "cost",
    },
)
class MatchFailure:
    def __init__(
        self,
        *,
        matcher: "Matcher",
        message: builtins.str,
        path: typing.Sequence[builtins.str],
        cost: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Match failure details.

        :param matcher: The matcher that had the failure.
        :param message: Failure message.
        :param path: The relative path in the target where the failure occurred. If the failure occurred at root of the match tree, set the path to an empty list. If it occurs in the 5th index of an array nested within the 'foo' key of an object, set the path as ``['/foo', '[5]']``.
        :param cost: The cost of this particular mismatch. Default: 1

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import assertions
            
            # matcher: assertions.Matcher
            
            match_failure = assertions.MatchFailure(
                matcher=matcher,
                message="message",
                path=["path"],
            
                # the properties below are optional
                cost=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e753d803b4a02068cb2dfb45661621427e697484daa7ddc1b6a680a4595c89)
            check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument cost", value=cost, expected_type=type_hints["cost"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "matcher": matcher,
            "message": message,
            "path": path,
        }
        if cost is not None:
            self._values["cost"] = cost

    @builtins.property
    def matcher(self) -> "Matcher":
        '''The matcher that had the failure.'''
        result = self._values.get("matcher")
        assert result is not None, "Required property 'matcher' is missing"
        return typing.cast("Matcher", result)

    @builtins.property
    def message(self) -> builtins.str:
        '''Failure message.'''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.List[builtins.str]:
        '''The relative path in the target where the failure occurred.

        If the failure occurred at root of the match tree, set the path to an empty list.
        If it occurs in the 5th index of an array nested within the 'foo' key of an object,
        set the path as ``['/foo', '[5]']``.
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cost(self) -> typing.Optional[jsii.Number]:
        '''The cost of this particular mismatch.

        :default: 1
        '''
        result = self._values.get("cost")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MatchFailure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MatchResult(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.assertions.MatchResult",
):
    '''The result of ``Match.test()``.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import assertions
        
        # target: Any
        
        match_result = assertions.MatchResult(target)
    '''

    def __init__(self, target: typing.Any) -> None:
        '''
        :param target: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb5a29b76424d084bdc310c6b78a218fa7665792de6535b46e71143003dd6195)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        jsii.create(self.__class__, self, [target])

    @jsii.member(jsii_name="compose")
    def compose(self, id: builtins.str, inner: "MatchResult") -> "MatchResult":
        '''Compose the results of a previous match as a subtree.

        :param id: the id of the parent tree.
        :param inner: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5707d27d3d9ef8648d76144fef31bb7e8e203d4d97e24e6577be793184d6b06e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inner", value=inner, expected_type=type_hints["inner"])
        return typing.cast("MatchResult", jsii.invoke(self, "compose", [id, inner]))

    @jsii.member(jsii_name="finished")
    def finished(self) -> "MatchResult":
        '''Prepare the result to be analyzed.

        This API *must* be called prior to analyzing these results.
        '''
        return typing.cast("MatchResult", jsii.invoke(self, "finished", []))

    @jsii.member(jsii_name="hasFailed")
    def has_failed(self) -> builtins.bool:
        '''Does the result contain any failures.

        If not, the result is a success
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "hasFailed", []))

    @jsii.member(jsii_name="push")
    def push(
        self,
        matcher: "Matcher",
        path: typing.Sequence[builtins.str],
        message: builtins.str,
    ) -> "MatchResult":
        '''(deprecated) DEPRECATED.

        :param matcher: -
        :param path: -
        :param message: -

        :deprecated: use recordFailure()

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45bee7c8fb202d40364739632ae8bc933408a64dd4bc116fdba19be6d8af7683)
            check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        return typing.cast("MatchResult", jsii.invoke(self, "push", [matcher, path, message]))

    @jsii.member(jsii_name="recordCapture")
    def record_capture(self, *, capture: "Capture", value: typing.Any) -> None:
        '''Record a capture against in this match result.

        :param capture: The instance of Capture class to which this capture is associated with.
        :param value: The value that was captured.
        '''
        options = MatchCapture(capture=capture, value=value)

        return typing.cast(None, jsii.invoke(self, "recordCapture", [options]))

    @jsii.member(jsii_name="recordFailure")
    def record_failure(
        self,
        *,
        matcher: "Matcher",
        message: builtins.str,
        path: typing.Sequence[builtins.str],
        cost: typing.Optional[jsii.Number] = None,
    ) -> "MatchResult":
        '''Record a new failure into this result at a specific path.

        :param matcher: The matcher that had the failure.
        :param message: Failure message.
        :param path: The relative path in the target where the failure occurred. If the failure occurred at root of the match tree, set the path to an empty list. If it occurs in the 5th index of an array nested within the 'foo' key of an object, set the path as ``['/foo', '[5]']``.
        :param cost: The cost of this particular mismatch. Default: 1
        '''
        failure = MatchFailure(matcher=matcher, message=message, path=path, cost=cost)

        return typing.cast("MatchResult", jsii.invoke(self, "recordFailure", [failure]))

    @jsii.member(jsii_name="renderMismatch")
    def render_mismatch(self) -> builtins.str:
        '''Do a deep render of the match result, showing the structure mismatches in context.'''
        return typing.cast(builtins.str, jsii.invoke(self, "renderMismatch", []))

    @jsii.member(jsii_name="toHumanStrings")
    def to_human_strings(self) -> typing.List[builtins.str]:
        '''Render the failed match in a presentable way.

        Prefer using ``renderMismatch`` over this method. It is left for backwards
        compatibility for test suites that expect it, but ``renderMismatch()`` will
        produce better output.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "toHumanStrings", []))

    @builtins.property
    @jsii.member(jsii_name="failCost")
    def fail_cost(self) -> jsii.Number:
        '''The cost of the failures so far.'''
        return typing.cast(jsii.Number, jsii.get(self, "failCost"))

    @builtins.property
    @jsii.member(jsii_name="failCount")
    def fail_count(self) -> jsii.Number:
        '''The number of failures.'''
        return typing.cast(jsii.Number, jsii.get(self, "failCount"))

    @builtins.property
    @jsii.member(jsii_name="isSuccess")
    def is_success(self) -> builtins.bool:
        '''Whether the match is a success.'''
        return typing.cast(builtins.bool, jsii.get(self, "isSuccess"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> typing.Any:
        '''The target for which this result was generated.'''
        return typing.cast(typing.Any, jsii.get(self, "target"))


class Matcher(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.assertions.Matcher",
):
    '''Represents a matcher that can perform special data matching capabilities between a given pattern and a target.

    :exampleMetadata: infused

    Example::

        # Given a template -
        # {
        #   "Resources": {
        #     "MyBar": {
        #       "Type": "Foo::Bar",
        #       "Properties": {
        #         "Fred": ["Flob", "Cat"]
        #       }
        #     }
        #   }
        # }
        
        # The following will NOT throw an assertion error
        template.has_resource_properties("Foo::Bar", {
            "Fred": Match.array_with(["Flob"])
        })
        
        # The following will throw an assertion error
        template.has_resource_properties("Foo::Bar", Match.object_like({
            "Fred": Match.array_with(["Wobble"])
        }))
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="isMatcher")
    @builtins.classmethod
    def is_matcher(cls, x: typing.Any) -> builtins.bool:
        '''Check whether the provided object is a subtype of the ``IMatcher``.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34e173c6e90c1fe62d73014facdde86cc643902cca812a81d90683adef3cb82e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isMatcher", [x]))

    @jsii.member(jsii_name="test")
    @abc.abstractmethod
    def test(self, actual: typing.Any) -> MatchResult:
        '''Test whether a target matches the provided pattern.

        Every Matcher must implement this method.
        This method will be invoked by the assertions framework. Do not call this method directly.

        :param actual: the target to match.

        :return: the list of match failures. An empty array denotes a successful match.
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    @abc.abstractmethod
    def name(self) -> builtins.str:
        '''A name for the matcher.

        This is collected as part of the result and may be presented to the user.
        '''
        ...


class _MatcherProxy(Matcher):
    @jsii.member(jsii_name="test")
    def test(self, actual: typing.Any) -> MatchResult:
        '''Test whether a target matches the provided pattern.

        Every Matcher must implement this method.
        This method will be invoked by the assertions framework. Do not call this method directly.

        :param actual: the target to match.

        :return: the list of match failures. An empty array denotes a successful match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a8e18e5d3147fdd105018b28e92d58ac6230fc3d6ea5c23d1d4328a3b0511c9)
            check_type(argname="argument actual", value=actual, expected_type=type_hints["actual"])
        return typing.cast(MatchResult, jsii.invoke(self, "test", [actual]))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the matcher.

        This is collected as part of the result and may be presented to the user.
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Matcher).__jsii_proxy_class__ = lambda : _MatcherProxy


class Template(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.assertions.Template"):
    '''Suite of assertions that can be run on a CDK stack.

    Typically used, as part of unit tests, to validate that the rendered
    CloudFormation template has expected resources and properties.

    :exampleMetadata: nofixture infused

    Example::

        from aws_cdk import Stack
        from aws_cdk.assertions import Template
        
        stack = Stack()
        # ...
        template = Template.from_stack(stack)
    '''

    @jsii.member(jsii_name="fromJSON")
    @builtins.classmethod
    def from_json(
        cls,
        template: typing.Mapping[builtins.str, typing.Any],
        *,
        skip_cyclical_dependencies_check: typing.Optional[builtins.bool] = None,
    ) -> "Template":
        '''Base your assertions from an existing CloudFormation template formatted as an in-memory JSON object.

        :param template: the CloudFormation template formatted as a nested set of records.
        :param skip_cyclical_dependencies_check: If set to true, will skip checking for cyclical / circular dependencies. Should be set to false other than for templates that are valid despite containing cycles, such as unprocessed transform stacks. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6531cbb828e6143d2d6e79da05413d429d384d7cb2bdd314dfee1e6bb870758)
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        template_parsing_options = TemplateParsingOptions(
            skip_cyclical_dependencies_check=skip_cyclical_dependencies_check
        )

        return typing.cast("Template", jsii.sinvoke(cls, "fromJSON", [template, template_parsing_options]))

    @jsii.member(jsii_name="fromStack")
    @builtins.classmethod
    def from_stack(
        cls,
        stack: _Stack_2866e57f,
        *,
        skip_cyclical_dependencies_check: typing.Optional[builtins.bool] = None,
    ) -> "Template":
        '''Base your assertions on the CloudFormation template synthesized by a CDK ``Stack``.

        :param stack: the CDK Stack to run assertions on.
        :param skip_cyclical_dependencies_check: If set to true, will skip checking for cyclical / circular dependencies. Should be set to false other than for templates that are valid despite containing cycles, such as unprocessed transform stacks. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1f7e8bf67e204c5ef6dc59535ca21a2927ff210c4e9ba8b3594ecf4c86254eb)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
        template_parsing_options = TemplateParsingOptions(
            skip_cyclical_dependencies_check=skip_cyclical_dependencies_check
        )

        return typing.cast("Template", jsii.sinvoke(cls, "fromStack", [stack, template_parsing_options]))

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(
        cls,
        template: builtins.str,
        *,
        skip_cyclical_dependencies_check: typing.Optional[builtins.bool] = None,
    ) -> "Template":
        '''Base your assertions from an existing CloudFormation template formatted as a JSON string.

        :param template: the CloudFormation template in.
        :param skip_cyclical_dependencies_check: If set to true, will skip checking for cyclical / circular dependencies. Should be set to false other than for templates that are valid despite containing cycles, such as unprocessed transform stacks. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d6c783089c3a8e3fd10427e78eb00145b81512c3fc6b0c113e7bb35e3a80716)
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        template_parsing_options = TemplateParsingOptions(
            skip_cyclical_dependencies_check=skip_cyclical_dependencies_check
        )

        return typing.cast("Template", jsii.sinvoke(cls, "fromString", [template, template_parsing_options]))

    @jsii.member(jsii_name="allResources")
    def all_resources(self, type: builtins.str, props: typing.Any) -> None:
        '''Assert that all resources of the given type contain the given definition in the CloudFormation template.

        By default, performs partial matching on the resource, via the ``Match.objectLike()``.
        To configure different behavior, use other matchers in the ``Match`` class.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param props: the entire definition of the resources as they should be expected in the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c5c638f8664deb5211661650329fc0a12cdab2ecda1a1825a8a8575e0b6fe30)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(None, jsii.invoke(self, "allResources", [type, props]))

    @jsii.member(jsii_name="allResourcesProperties")
    def all_resources_properties(self, type: builtins.str, props: typing.Any) -> None:
        '''Assert that all resources of the given type contain the given properties CloudFormation template.

        By default, performs partial matching on the ``Properties`` key of the resource, via the
        ``Match.objectLike()``. To configure different behavior, use other matchers in the ``Match`` class.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param props: the 'Properties' section of the resource as should be expected in the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491ada0b4de838e2ab094795ac179de198543b8fd37b4a8d294d42c7d7a7563e)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(None, jsii.invoke(self, "allResourcesProperties", [type, props]))

    @jsii.member(jsii_name="findConditions")
    def find_conditions(
        self,
        logical_id: builtins.str,
        props: typing.Any = None,
    ) -> typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]:
        '''Get the set of matching Conditions that match the given properties in the CloudFormation template.

        :param logical_id: the name of the condition. Provide ``'*'`` to match all conditions in the template.
        :param props: by default, matches all Conditions in the template. When a literal object is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__044d164db8c00240ea1576f4d5575e8be0907ca080005764d7de0d08a013bb10)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]], jsii.invoke(self, "findConditions", [logical_id, props]))

    @jsii.member(jsii_name="findMappings")
    def find_mappings(
        self,
        logical_id: builtins.str,
        props: typing.Any = None,
    ) -> typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]:
        '''Get the set of matching Mappings that match the given properties in the CloudFormation template.

        :param logical_id: the name of the mapping. Provide ``'*'`` to match all mappings in the template.
        :param props: by default, matches all Mappings in the template. When a literal object is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c3407588afd1cdbe14644ae428ecc3fe37a424aeb66c8bdf1c91e74f45d9149)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]], jsii.invoke(self, "findMappings", [logical_id, props]))

    @jsii.member(jsii_name="findOutputs")
    def find_outputs(
        self,
        logical_id: builtins.str,
        props: typing.Any = None,
    ) -> typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]:
        '''Get the set of matching Outputs that match the given properties in the CloudFormation template.

        :param logical_id: the name of the output. Provide ``'*'`` to match all outputs in the template.
        :param props: by default, matches all Outputs in the template. When a literal object is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49e46c6a2e20ca04dd4c6671d9f59b5b9da1bb9deeed3e6209ac69f0afdb4435)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]], jsii.invoke(self, "findOutputs", [logical_id, props]))

    @jsii.member(jsii_name="findParameters")
    def find_parameters(
        self,
        logical_id: builtins.str,
        props: typing.Any = None,
    ) -> typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]:
        '''Get the set of matching Parameters that match the given properties in the CloudFormation template.

        :param logical_id: the name of the parameter. Provide ``'*'`` to match all parameters in the template.
        :param props: by default, matches all Parameters in the template. When a literal object is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a4fa7893d75011aa8e81115ebd00a067b2660a4bd77001b61a9101d7870bf61)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]], jsii.invoke(self, "findParameters", [logical_id, props]))

    @jsii.member(jsii_name="findResources")
    def find_resources(
        self,
        type: builtins.str,
        props: typing.Any = None,
    ) -> typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]:
        '''Get the set of matching resources of a given type and properties in the CloudFormation template.

        :param type: the type to match in the CloudFormation template.
        :param props: by default, matches all resources with the given type. When a literal is provided, performs a partial match via ``Match.objectLike()``. Use the ``Match`` APIs to configure a different behaviour.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dfdecc696a85cbadb9124975e7619b743acea4afb3b4cfdbc07ad48abf7e1ca)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]], jsii.invoke(self, "findResources", [type, props]))

    @jsii.member(jsii_name="hasCondition")
    def has_condition(self, logical_id: builtins.str, props: typing.Any) -> None:
        '''Assert that a Condition with the given properties exists in the CloudFormation template.

        By default, performs partial matching on the resource, via the ``Match.objectLike()``.
        To configure different behavior, use other matchers in the ``Match`` class.

        :param logical_id: the name of the mapping. Provide ``'*'`` to match all conditions in the template.
        :param props: the output as should be expected in the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5b639f55bbadd46a290effbbbd13769b71a711bcc8b3e04c9b2e4f29931a84)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(None, jsii.invoke(self, "hasCondition", [logical_id, props]))

    @jsii.member(jsii_name="hasMapping")
    def has_mapping(self, logical_id: builtins.str, props: typing.Any) -> None:
        '''Assert that a Mapping with the given properties exists in the CloudFormation template.

        By default, performs partial matching on the resource, via the ``Match.objectLike()``.
        To configure different behavior, use other matchers in the ``Match`` class.

        :param logical_id: the name of the mapping. Provide ``'*'`` to match all mappings in the template.
        :param props: the output as should be expected in the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7a46161e4bc7b293d2404210f7aaf235f78e54e42227340184ce19cb219c37d)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(None, jsii.invoke(self, "hasMapping", [logical_id, props]))

    @jsii.member(jsii_name="hasOutput")
    def has_output(self, logical_id: builtins.str, props: typing.Any) -> None:
        '''Assert that an Output with the given properties exists in the CloudFormation template.

        By default, performs partial matching on the resource, via the ``Match.objectLike()``.
        To configure different behavior, use other matchers in the ``Match`` class.

        :param logical_id: the name of the output. Provide ``'*'`` to match all outputs in the template.
        :param props: the output as should be expected in the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e8b9e1ad01747ba055720917c870b66308eaecc32d0a018ee9bf5e84f09cbf3)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(None, jsii.invoke(self, "hasOutput", [logical_id, props]))

    @jsii.member(jsii_name="hasParameter")
    def has_parameter(self, logical_id: builtins.str, props: typing.Any) -> None:
        '''Assert that a Parameter with the given properties exists in the CloudFormation template.

        By default, performs partial matching on the parameter, via the ``Match.objectLike()``.
        To configure different behavior, use other matchers in the ``Match`` class.

        :param logical_id: the name of the parameter. Provide ``'*'`` to match all parameters in the template.
        :param props: the parameter as should be expected in the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea2aad30c104b14a79f11a1c63591a323523bc13706d223a2c1b3a43927381fa)
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(None, jsii.invoke(self, "hasParameter", [logical_id, props]))

    @jsii.member(jsii_name="hasResource")
    def has_resource(self, type: builtins.str, props: typing.Any) -> None:
        '''Assert that a resource of the given type and given definition exists in the CloudFormation template.

        By default, performs partial matching on the resource, via the ``Match.objectLike()``.
        To configure different behavior, use other matchers in the ``Match`` class.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param props: the entire definition of the resource as should be expected in the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a7729907f2e5da95bef367aee244e65ed0dd005ebe4b1567fc3ce3bee49a969)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(None, jsii.invoke(self, "hasResource", [type, props]))

    @jsii.member(jsii_name="hasResourceProperties")
    def has_resource_properties(self, type: builtins.str, props: typing.Any) -> None:
        '''Assert that a resource of the given type and properties exists in the CloudFormation template.

        By default, performs partial matching on the ``Properties`` key of the resource, via the
        ``Match.objectLike()``. To configure different behavior, use other matchers in the ``Match`` class.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param props: the 'Properties' section of the resource as should be expected in the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2751c68339334102bcc7c1684b1fb5b8251d6b449a6be2c4d6e0ca5d07e9478a)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(None, jsii.invoke(self, "hasResourceProperties", [type, props]))

    @jsii.member(jsii_name="resourceCountIs")
    def resource_count_is(self, type: builtins.str, count: jsii.Number) -> None:
        '''Assert that the given number of resources of the given type exist in the template.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param count: number of expected instances.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38945080515cb1f2bcfa31e2d79145a229e31c7ad9f3a16282da008a6453614b)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        return typing.cast(None, jsii.invoke(self, "resourceCountIs", [type, count]))

    @jsii.member(jsii_name="resourcePropertiesCountIs")
    def resource_properties_count_is(
        self,
        type: builtins.str,
        props: typing.Any,
        count: jsii.Number,
    ) -> None:
        '''Assert that the given number of resources of the given type and properties exists in the CloudFormation template.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param props: the 'Properties' section of the resource as should be expected in the template.
        :param count: number of expected instances.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c629ce8cc817df9be71c03845c0b0cf2bd8bd44bfef55b72f0edfa4140ef743d)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        return typing.cast(None, jsii.invoke(self, "resourcePropertiesCountIs", [type, props, count]))

    @jsii.member(jsii_name="templateMatches")
    def template_matches(self, expected: typing.Any) -> None:
        '''Assert that the CloudFormation template matches the given value.

        :param expected: the expected CloudFormation template as key-value pairs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6a27c45f2dfd24a135882cdb36c7aac9836faf61c11bc3ed504ec8b564ef9c6)
            check_type(argname="argument expected", value=expected, expected_type=type_hints["expected"])
        return typing.cast(None, jsii.invoke(self, "templateMatches", [expected]))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''The CloudFormation template deserialized into an object.'''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "toJSON", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.assertions.TemplateParsingOptions",
    jsii_struct_bases=[],
    name_mapping={"skip_cyclical_dependencies_check": "skipCyclicalDependenciesCheck"},
)
class TemplateParsingOptions:
    def __init__(
        self,
        *,
        skip_cyclical_dependencies_check: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options to configure template parsing behavior, such as disregarding circular dependencies.

        :param skip_cyclical_dependencies_check: If set to true, will skip checking for cyclical / circular dependencies. Should be set to false other than for templates that are valid despite containing cycles, such as unprocessed transform stacks. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import assertions
            
            template_parsing_options = assertions.TemplateParsingOptions(
                skip_cyclical_dependencies_check=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__856b9d83a60c8b00ab2fa26da737d8d8b453dbb2f01dfe4d0a263ef8ae0944a7)
            check_type(argname="argument skip_cyclical_dependencies_check", value=skip_cyclical_dependencies_check, expected_type=type_hints["skip_cyclical_dependencies_check"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if skip_cyclical_dependencies_check is not None:
            self._values["skip_cyclical_dependencies_check"] = skip_cyclical_dependencies_check

    @builtins.property
    def skip_cyclical_dependencies_check(self) -> typing.Optional[builtins.bool]:
        '''If set to true, will skip checking for cyclical / circular dependencies.

        Should be set to false other than for
        templates that are valid despite containing cycles, such as unprocessed transform stacks.

        :default: false
        '''
        result = self._values.get("skip_cyclical_dependencies_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateParsingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Capture(
    Matcher,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.assertions.Capture",
):
    '''Capture values while matching templates.

    Using an instance of this class within a Matcher will capture the matching value.
    The ``as*()`` APIs on the instance can be used to get the captured value.

    :exampleMetadata: infused

    Example::

        # Given a template -
        # {
        #   "Resources": {
        #     "MyBar": {
        #       "Type": "Foo::Bar",
        #       "Properties": {
        #         "Fred": "Flob",
        #       }
        #     },
        #     "MyBaz": {
        #       "Type": "Foo::Bar",
        #       "Properties": {
        #         "Fred": "Quib",
        #       }
        #     }
        #   }
        # }
        
        fred_capture = Capture()
        template.has_resource_properties("Foo::Bar", {
            "Fred": fred_capture
        })
        
        fred_capture.as_string() # returns "Flob"
        fred_capture.next() # returns true
        fred_capture.as_string()
    '''

    def __init__(self, pattern: typing.Any = None) -> None:
        '''Initialize a new capture.

        :param pattern: a nested pattern or Matcher. If a nested pattern is provided ``objectLike()`` matching is applied.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66ec0ba3a693bb7603deea5eda438de4e7bd7d8baeeb015451d3b7569689a20f)
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
        jsii.create(self.__class__, self, [pattern])

    @jsii.member(jsii_name="asArray")
    def as_array(self) -> typing.List[typing.Any]:
        '''Retrieve the captured value as an array.

        An error is generated if no value is captured or if the value is not an array.
        '''
        return typing.cast(typing.List[typing.Any], jsii.invoke(self, "asArray", []))

    @jsii.member(jsii_name="asBoolean")
    def as_boolean(self) -> builtins.bool:
        '''Retrieve the captured value as a boolean.

        An error is generated if no value is captured or if the value is not a boolean.
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "asBoolean", []))

    @jsii.member(jsii_name="asNumber")
    def as_number(self) -> jsii.Number:
        '''Retrieve the captured value as a number.

        An error is generated if no value is captured or if the value is not a number.
        '''
        return typing.cast(jsii.Number, jsii.invoke(self, "asNumber", []))

    @jsii.member(jsii_name="asObject")
    def as_object(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''Retrieve the captured value as a JSON object.

        An error is generated if no value is captured or if the value is not an object.
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "asObject", []))

    @jsii.member(jsii_name="asString")
    def as_string(self) -> builtins.str:
        '''Retrieve the captured value as a string.

        An error is generated if no value is captured or if the value is not a string.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "asString", []))

    @jsii.member(jsii_name="next")
    def next(self) -> builtins.bool:
        '''When multiple results are captured, move the iterator to the next result.

        :return: true if another capture is present, false otherwise
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "next", []))

    @jsii.member(jsii_name="test")
    def test(self, actual: typing.Any) -> MatchResult:
        '''Test whether a target matches the provided pattern.

        Every Matcher must implement this method.
        This method will be invoked by the assertions framework. Do not call this method directly.

        :param actual: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d43e7554eaf5c3b4fbf1ccc90f5143c9879eed7bb7aea11e1251059a18833c67)
            check_type(argname="argument actual", value=actual, expected_type=type_hints["actual"])
        return typing.cast(MatchResult, jsii.invoke(self, "test", [actual]))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the matcher.

        This is collected as part of the result and may be presented to the user.
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))


__all__ = [
    "Annotations",
    "Capture",
    "Match",
    "MatchCapture",
    "MatchFailure",
    "MatchResult",
    "Matcher",
    "Template",
    "TemplateParsingOptions",
]

publication.publish()

def _typecheckingstub__6dffec3a2a7a1a9f1b88ff9e3533fd5895867e3261f050f0b21259953c59554f(
    stack: _Stack_2866e57f,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f6064e884b81060ed5691b5c77d99fe9171969d33e0f5c39db63629f9b14233(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8194b87ea6257ea629eb3ca14994457d25764fa7dc4dc21a1ecebfb7392cf893(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b9ed07482937b302b271f5ecd83ad83b12af81c8b5912069077f5465abc36a(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b7c83521585d4519a99991c56b91963a89741ac27b8a8914684737e203a2273(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4474081f3d9b4d5d317af8608f249a04ddea10859b5496e931c243fbd7bbffa9(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca70d40be65a245d658fb88df040d0e83e8e632fdd5e2ee95dc766f1c438a795(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c305e483a4c9a4cc2875c6b72244cf281efd6942b9742401ecc991a2aaa0fd2(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a9a4d7658d222b5a854156cb3f9e2156ce1fca2f67a73459ffe8631f270eae(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef14b35c0df2f219e2c887dd18c1ee458e984bcbfa8b30a116ad13762f24a5ad(
    construct_path: builtins.str,
    message: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc2fc6b89509c8782c1d71064aba95c7f8ce8825fb3287ada62d9f7a7fcd3ca3(
    pattern: typing.Sequence[typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fafc2dce97140cefc00887659682f218b01db7c89e52b4430b2843868fb3589f(
    pattern: typing.Sequence[typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd6b2bcc466f2428e69319f1508695c522a5e069b08ce97c06e72e3d2927aa57(
    pattern: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ac65d172037fe8d399409899d5d6843aaa87d02106d1021d4d528350f15adb(
    pattern: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26dde9bd8eb2015c3779e6c829fa6c442206244c4003e11e435d3f73943b01ac(
    pattern: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95fb0724e4fc6f68e1782f5f00503622e0a52a46523a159830c3f2092f1bb53c(
    pattern: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0764fac955478ef959c585f03fb2034993495f3f94a6cac7a567e56978cf4cee(
    pattern: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98a9c300f7bb1df47fc43d6b03131a9b5739f02259f381da6d7e61074f71c366(
    pattern: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaff32ba4b1c664eb41260f4e77edb8a54d7961b3b19bd287bf22ead0930c217(
    *,
    capture: Capture,
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e753d803b4a02068cb2dfb45661621427e697484daa7ddc1b6a680a4595c89(
    *,
    matcher: Matcher,
    message: builtins.str,
    path: typing.Sequence[builtins.str],
    cost: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5a29b76424d084bdc310c6b78a218fa7665792de6535b46e71143003dd6195(
    target: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5707d27d3d9ef8648d76144fef31bb7e8e203d4d97e24e6577be793184d6b06e(
    id: builtins.str,
    inner: MatchResult,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45bee7c8fb202d40364739632ae8bc933408a64dd4bc116fdba19be6d8af7683(
    matcher: Matcher,
    path: typing.Sequence[builtins.str],
    message: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34e173c6e90c1fe62d73014facdde86cc643902cca812a81d90683adef3cb82e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a8e18e5d3147fdd105018b28e92d58ac6230fc3d6ea5c23d1d4328a3b0511c9(
    actual: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6531cbb828e6143d2d6e79da05413d429d384d7cb2bdd314dfee1e6bb870758(
    template: typing.Mapping[builtins.str, typing.Any],
    *,
    skip_cyclical_dependencies_check: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1f7e8bf67e204c5ef6dc59535ca21a2927ff210c4e9ba8b3594ecf4c86254eb(
    stack: _Stack_2866e57f,
    *,
    skip_cyclical_dependencies_check: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d6c783089c3a8e3fd10427e78eb00145b81512c3fc6b0c113e7bb35e3a80716(
    template: builtins.str,
    *,
    skip_cyclical_dependencies_check: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c5c638f8664deb5211661650329fc0a12cdab2ecda1a1825a8a8575e0b6fe30(
    type: builtins.str,
    props: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491ada0b4de838e2ab094795ac179de198543b8fd37b4a8d294d42c7d7a7563e(
    type: builtins.str,
    props: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044d164db8c00240ea1576f4d5575e8be0907ca080005764d7de0d08a013bb10(
    logical_id: builtins.str,
    props: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c3407588afd1cdbe14644ae428ecc3fe37a424aeb66c8bdf1c91e74f45d9149(
    logical_id: builtins.str,
    props: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e46c6a2e20ca04dd4c6671d9f59b5b9da1bb9deeed3e6209ac69f0afdb4435(
    logical_id: builtins.str,
    props: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a4fa7893d75011aa8e81115ebd00a067b2660a4bd77001b61a9101d7870bf61(
    logical_id: builtins.str,
    props: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dfdecc696a85cbadb9124975e7619b743acea4afb3b4cfdbc07ad48abf7e1ca(
    type: builtins.str,
    props: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5b639f55bbadd46a290effbbbd13769b71a711bcc8b3e04c9b2e4f29931a84(
    logical_id: builtins.str,
    props: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a46161e4bc7b293d2404210f7aaf235f78e54e42227340184ce19cb219c37d(
    logical_id: builtins.str,
    props: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e8b9e1ad01747ba055720917c870b66308eaecc32d0a018ee9bf5e84f09cbf3(
    logical_id: builtins.str,
    props: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea2aad30c104b14a79f11a1c63591a323523bc13706d223a2c1b3a43927381fa(
    logical_id: builtins.str,
    props: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a7729907f2e5da95bef367aee244e65ed0dd005ebe4b1567fc3ce3bee49a969(
    type: builtins.str,
    props: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2751c68339334102bcc7c1684b1fb5b8251d6b449a6be2c4d6e0ca5d07e9478a(
    type: builtins.str,
    props: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38945080515cb1f2bcfa31e2d79145a229e31c7ad9f3a16282da008a6453614b(
    type: builtins.str,
    count: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c629ce8cc817df9be71c03845c0b0cf2bd8bd44bfef55b72f0edfa4140ef743d(
    type: builtins.str,
    props: typing.Any,
    count: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a27c45f2dfd24a135882cdb36c7aac9836faf61c11bc3ed504ec8b564ef9c6(
    expected: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__856b9d83a60c8b00ab2fa26da737d8d8b453dbb2f01dfe4d0a263ef8ae0944a7(
    *,
    skip_cyclical_dependencies_check: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66ec0ba3a693bb7603deea5eda438de4e7bd7d8baeeb015451d3b7569689a20f(
    pattern: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43e7554eaf5c3b4fbf1ccc90f5143c9879eed7bb7aea11e1251059a18833c67(
    actual: typing.Any,
) -> None:
    """Type checking stubs"""
    pass
