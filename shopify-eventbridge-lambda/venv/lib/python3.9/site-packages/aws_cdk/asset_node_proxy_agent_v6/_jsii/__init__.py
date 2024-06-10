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

__jsii_assembly__ = jsii.JSIIAssembly.load(
    "@aws-cdk/asset-node-proxy-agent-v6",
    "2.0.3",
    __name__[0:-6],
    "asset-node-proxy-agent-v6@2.0.3.jsii.tgz",
)

__all__ = [
    "__jsii_assembly__",
]

publication.publish()
