'''
# AWS Lambda Layer with kubectl (and helm)

This module exports a single class called `KubectlLayer` which is a `lambda.Layer` that bundles the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/kubectl/) and the [`helm`](https://helm.sh/) command line.

> * Helm Version: 3.5.4
> * Kubectl Version: 1.20.0

Usage:

```python
# KubectlLayer bundles the 'kubectl' and 'helm' command lines
from aws_cdk.lambda_layer_kubectl import KubectlLayer

# fn: lambda.Function

fn.add_layers(KubectlLayer(self, "KubectlLayer"))
```

`kubectl` will be installed under `/opt/kubectl/kubectl`, and `helm` will be installed under `/opt/helm/helm`.

## Alternatives

This module bundles Kubectl v1.20.0 and the associated helm version
To use alternative Kubectl versions, including the latest available,
you can use the external module
[awscdk-asset-kubectl](https://github.com/cdklabs/awscdk-asset-kubectl).
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


class KubectlLayer(
    _LayerVersion_9ca26241,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.lambda_layer_kubectl.KubectlLayer",
):
    '''An AWS Lambda layer that includes ``kubectl`` and ``helm``.

    :exampleMetadata: infused

    Example::

        # KubectlLayer bundles the 'kubectl' and 'helm' command lines
        from aws_cdk.lambda_layer_kubectl import KubectlLayer
        
        # fn: lambda.Function
        
        fn.add_layers(KubectlLayer(self, "KubectlLayer"))
    '''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a61d55df5a1b777f7a2482d2235a901972d3dfe410f7f352551fe03e70c8058)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])


__all__ = [
    "KubectlLayer",
]

publication.publish()

def _typecheckingstub__6a61d55df5a1b777f7a2482d2235a901972d3dfe410f7f352551fe03e70c8058(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
