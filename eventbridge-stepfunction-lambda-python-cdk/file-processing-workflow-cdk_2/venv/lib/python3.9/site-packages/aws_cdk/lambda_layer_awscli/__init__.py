'''
# AWS Lambda Layer with AWS CLI

This module exports a single class called `AwsCliLayer` which is a `lambda.Layer` that bundles the AWS CLI.

Any Lambda Function that uses this layer must use a Python 3.x runtime.

Usage:

```python
# AwsCliLayer bundles the AWS CLI in a lambda layer
from aws_cdk.lambda_layer_awscli import AwsCliLayer

# fn: lambda.Function

fn.add_layers(AwsCliLayer(self, "AwsCliLayer"))
```

The CLI will be installed under `/opt/awscli/aws`.

## Alternatives

This module bundles AWS cli v1. To use AWS cli v2, you can use the
external module [awscdk-asset-awscli](https://github.com/cdklabs/awscdk-asset-awscli/tree/awscli-v2/main).
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
from ..aws_lambda import LayerVersion as _LayerVersion_9ca26241


class AwsCliLayer(
    _LayerVersion_9ca26241,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.lambda_layer_awscli.AwsCliLayer",
):
    '''An AWS Lambda layer that includes the AWS CLI.

    :exampleMetadata: infused

    Example::

        # AwsCliLayer bundles the AWS CLI in a lambda layer
        from aws_cdk.lambda_layer_awscli import AwsCliLayer
        
        # fn: lambda.Function
        
        fn.add_layers(AwsCliLayer(self, "AwsCliLayer"))
    '''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c4c04a3bd0e81227b6f6cea95381918fe1a67f2603e9459f027659f8bcf0bd6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])


__all__ = [
    "AwsCliLayer",
]

publication.publish()

def _typecheckingstub__6c4c04a3bd0e81227b6f6cea95381918fe1a67f2603e9459f027659f8bcf0bd6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
