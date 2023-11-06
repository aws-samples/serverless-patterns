'''
# Constructs

> Software-defined persistent state

![Release](https://github.com/aws/constructs/workflows/Release/badge.svg)
[![npm version](https://badge.fury.io/js/constructs.svg)](https://badge.fury.io/js/constructs)
[![PyPI version](https://badge.fury.io/py/constructs.svg)](https://badge.fury.io/py/constructs)
[![NuGet version](https://badge.fury.io/nu/Constructs.svg)](https://badge.fury.io/nu/Constructs)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/software.constructs/constructs/badge.svg?style=plastic)](https://maven-badges.herokuapp.com/maven-central/software.constructs/constructs)

## What are constructs?

Constructs are classes which define a "piece of system state". Constructs can be composed together to form higher-level building blocks which represent more complex state.

Constructs are often used to represent the *desired state* of cloud applications. For example, in the AWS CDK, which is used to define the desired state for AWS infrastructure using CloudFormation, the lowest-level construct represents a *resource definition* in a CloudFormation template. These resources are composed to represent higher-level logical units of a cloud application, etc.

## Contributing

This project has adopted the [Amazon Open Source Code of
Conduct](https://aws.github.io/code-of-conduct).

We welcome community contributions and pull requests. See our [contribution
guide](./CONTRIBUTING.md) for more information on how to report issues, set up a
development environment and submit code.

## License

This project is distributed under the [Apache License, Version 2.0](./LICENSE).
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

from ._jsii import *


@jsii.enum(jsii_type="constructs.ConstructOrder")
class ConstructOrder(enum.Enum):
    '''In what order to return constructs.'''

    PREORDER = "PREORDER"
    '''Depth-first, pre-order.'''
    POSTORDER = "POSTORDER"
    '''Depth-first, post-order (leaf nodes first).'''


class Dependable(metaclass=jsii.JSIIAbstractClass, jsii_type="constructs.Dependable"):
    '''(experimental) Trait for IDependable.

    Traits are interfaces that are privately implemented by objects. Instead of
    showing up in the public interface of a class, they need to be queried
    explicitly. This is used to implement certain framework features that are
    not intended to be used by Construct consumers, and so should be hidden
    from accidental use.

    :stability: experimental

    Example::

        // Usage
        const roots = Dependable.of(construct).dependencyRoots;
        
        // Definition
        Dependable.implement(construct, {
              dependencyRoots: [construct],
        });
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="get")
    @builtins.classmethod
    def get(cls, instance: "IDependable") -> "Dependable":
        '''(deprecated) Return the matching Dependable for the given class instance.

        :param instance: -

        :deprecated: use ``of``

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__679510e0e5074b5be594d161aaffe1bcbf759129512d69821982adde36fb905d)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        return typing.cast("Dependable", jsii.sinvoke(cls, "get", [instance]))

    @jsii.member(jsii_name="implement")
    @builtins.classmethod
    def implement(cls, instance: "IDependable", trait: "Dependable") -> None:
        '''(experimental) Turn any object into an IDependable.

        :param instance: -
        :param trait: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fccfa163f8f38b89195d804e18f7122f2b59a7ba7b57ea51cf581e4ae5719bf9)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
            check_type(argname="argument trait", value=trait, expected_type=type_hints["trait"])
        return typing.cast(None, jsii.sinvoke(cls, "implement", [instance, trait]))

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, instance: "IDependable") -> "Dependable":
        '''(experimental) Return the matching Dependable for the given class instance.

        :param instance: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a9441299838c86c77ad919b31ab158da6bd872c3bf8bf55f147c17abeea083)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        return typing.cast("Dependable", jsii.sinvoke(cls, "of", [instance]))

    @builtins.property
    @jsii.member(jsii_name="dependencyRoots")
    @abc.abstractmethod
    def dependency_roots(self) -> typing.List["IConstruct"]:
        '''(experimental) The set of constructs that form the root of this dependable.

        All resources under all returned constructs are included in the ordering
        dependency.

        :stability: experimental
        '''
        ...


class _DependableProxy(Dependable):
    @builtins.property
    @jsii.member(jsii_name="dependencyRoots")
    def dependency_roots(self) -> typing.List["IConstruct"]:
        '''(experimental) The set of constructs that form the root of this dependable.

        All resources under all returned constructs are included in the ordering
        dependency.

        :stability: experimental
        '''
        return typing.cast(typing.List["IConstruct"], jsii.get(self, "dependencyRoots"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Dependable).__jsii_proxy_class__ = lambda : _DependableProxy


@jsii.interface(jsii_type="constructs.IDependable")
class IDependable(typing_extensions.Protocol):
    '''Trait marker for classes that can be depended upon.

    The presence of this interface indicates that an object has
    an ``IDependable`` implementation.

    This interface can be used to take an (ordering) dependency on a set of
    constructs. An ordering dependency implies that the resources represented by
    those constructs are deployed before the resources depending ON them are
    deployed.
    '''

    pass


class _IDependableProxy:
    '''Trait marker for classes that can be depended upon.

    The presence of this interface indicates that an object has
    an ``IDependable`` implementation.

    This interface can be used to take an (ordering) dependency on a set of
    constructs. An ordering dependency implies that the resources represented by
    those constructs are deployed before the resources depending ON them are
    deployed.
    '''

    __jsii_type__: typing.ClassVar[str] = "constructs.IDependable"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDependable).__jsii_proxy_class__ = lambda : _IDependableProxy


@jsii.interface(jsii_type="constructs.IValidation")
class IValidation(typing_extensions.Protocol):
    '''Implement this interface in order for the construct to be able to validate itself.'''

    @jsii.member(jsii_name="validate")
    def validate(self) -> typing.List[builtins.str]:
        '''Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        :return: An array of validation error messages, or an empty array if there the construct is valid.
        '''
        ...


class _IValidationProxy:
    '''Implement this interface in order for the construct to be able to validate itself.'''

    __jsii_type__: typing.ClassVar[str] = "constructs.IValidation"

    @jsii.member(jsii_name="validate")
    def validate(self) -> typing.List[builtins.str]:
        '''Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        :return: An array of validation error messages, or an empty array if there the construct is valid.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validate", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IValidation).__jsii_proxy_class__ = lambda : _IValidationProxy


@jsii.data_type(
    jsii_type="constructs.MetadataEntry",
    jsii_struct_bases=[],
    name_mapping={"data": "data", "type": "type", "trace": "trace"},
)
class MetadataEntry:
    def __init__(
        self,
        *,
        data: typing.Any,
        type: builtins.str,
        trace: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''An entry in the construct metadata table.

        :param data: The data.
        :param type: The metadata entry type.
        :param trace: Stack trace at the point of adding the metadata. Only available if ``addMetadata()`` is called with ``stackTrace: true``. Default: - no trace information
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac0c2f394c95b32376bd2487bfa65b455507f8363a71e56bbcfef3a690552658)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument trace", value=trace, expected_type=type_hints["trace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data": data,
            "type": type,
        }
        if trace is not None:
            self._values["trace"] = trace

    @builtins.property
    def data(self) -> typing.Any:
        '''The data.'''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The metadata entry type.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trace(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Stack trace at the point of adding the metadata.

        Only available if ``addMetadata()`` is called with ``stackTrace: true``.

        :default: - no trace information
        '''
        result = self._values.get("trace")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetadataEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="constructs.MetadataOptions",
    jsii_struct_bases=[],
    name_mapping={
        "stack_trace": "stackTrace",
        "trace_from_function": "traceFromFunction",
    },
)
class MetadataOptions:
    def __init__(
        self,
        *,
        stack_trace: typing.Optional[builtins.bool] = None,
        trace_from_function: typing.Any = None,
    ) -> None:
        '''Options for ``construct.addMetadata()``.

        :param stack_trace: Include stack trace with metadata entry. Default: false
        :param trace_from_function: A JavaScript function to begin tracing from. This option is ignored unless ``stackTrace`` is ``true``. Default: addMetadata()
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75d38f18f5b98ff8e52a193cc40da1d25ab1a4740362b86cea0782ada618178b)
            check_type(argname="argument stack_trace", value=stack_trace, expected_type=type_hints["stack_trace"])
            check_type(argname="argument trace_from_function", value=trace_from_function, expected_type=type_hints["trace_from_function"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if stack_trace is not None:
            self._values["stack_trace"] = stack_trace
        if trace_from_function is not None:
            self._values["trace_from_function"] = trace_from_function

    @builtins.property
    def stack_trace(self) -> typing.Optional[builtins.bool]:
        '''Include stack trace with metadata entry.

        :default: false
        '''
        result = self._values.get("stack_trace")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def trace_from_function(self) -> typing.Any:
        '''A JavaScript function to begin tracing from.

        This option is ignored unless ``stackTrace`` is ``true``.

        :default: addMetadata()
        '''
        result = self._values.get("trace_from_function")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetadataOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Node(metaclass=jsii.JSIIMeta, jsii_type="constructs.Node"):
    '''Represents the construct node in the scope tree.'''

    def __init__(
        self,
        host: "Construct",
        scope: "IConstruct",
        id: builtins.str,
    ) -> None:
        '''
        :param host: -
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3d6f98f49be8b52dd81458a10a699ba3c2baedf270e915aff9ad4a199629f16)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [host, scope, id])

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, construct: "IConstruct") -> "Node":
        '''(deprecated) Returns the node associated with a construct.

        :param construct: the construct.

        :deprecated: use ``construct.node`` instead

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e976ef1a5da0fe82b55c8d7dec2b729e665c685a6fd4cf13e79d119b83e883b)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast("Node", jsii.sinvoke(cls, "of", [construct]))

    @jsii.member(jsii_name="addDependency")
    def add_dependency(self, *deps: IDependable) -> None:
        '''Add an ordering dependency on another construct.

        An ``IDependable``

        :param deps: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45cad7dd42c6c671e9f87ba7d66096044214dd8c5bfed807ecb8eee7b41edd21)
            check_type(argname="argument deps", value=deps, expected_type=typing.Tuple[type_hints["deps"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addDependency", [*deps]))

    @jsii.member(jsii_name="addMetadata")
    def add_metadata(
        self,
        type: builtins.str,
        data: typing.Any,
        *,
        stack_trace: typing.Optional[builtins.bool] = None,
        trace_from_function: typing.Any = None,
    ) -> None:
        '''Adds a metadata entry to this construct.

        Entries are arbitrary values and will also include a stack trace to allow tracing back to
        the code location for when the entry was added. It can be used, for example, to include source
        mapping in CloudFormation templates to improve diagnostics.

        :param type: a string denoting the type of metadata.
        :param data: the value of the metadata (can be a Token). If null/undefined, metadata will not be added.
        :param stack_trace: Include stack trace with metadata entry. Default: false
        :param trace_from_function: A JavaScript function to begin tracing from. This option is ignored unless ``stackTrace`` is ``true``. Default: addMetadata()
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__023b8c3b11b2c1279fbfa8d54f858cec54fb8d9621c584addfbcccc63dbce202)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        options = MetadataOptions(
            stack_trace=stack_trace, trace_from_function=trace_from_function
        )

        return typing.cast(None, jsii.invoke(self, "addMetadata", [type, data, options]))

    @jsii.member(jsii_name="addValidation")
    def add_validation(self, validation: IValidation) -> None:
        '''Adds a validation to this construct.

        When ``node.validate()`` is called, the ``validate()`` method will be called on
        all validations and all errors will be returned.

        :param validation: The validation object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67eb37a7475000d487d8124e00d1a8f5c0da44f9b68527dd02d18a3a789e11a0)
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
        return typing.cast(None, jsii.invoke(self, "addValidation", [validation]))

    @jsii.member(jsii_name="findAll")
    def find_all(
        self,
        order: typing.Optional[ConstructOrder] = None,
    ) -> typing.List["IConstruct"]:
        '''Return this construct and all of its children in the given order.

        :param order: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc361d795aa7b43307a9b4d8126549b970305e1487dfba0b95baabe4805e7c1b)
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
        return typing.cast(typing.List["IConstruct"], jsii.invoke(self, "findAll", [order]))

    @jsii.member(jsii_name="findChild")
    def find_child(self, id: builtins.str) -> "IConstruct":
        '''Return a direct child by id.

        Throws an error if the child is not found.

        :param id: Identifier of direct child.

        :return: Child with the given id.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fad30dac2587986f1ad461ddbfadd8c7bdb66542692e2272c9ea5e2487f4fa5f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast("IConstruct", jsii.invoke(self, "findChild", [id]))

    @jsii.member(jsii_name="getContext")
    def get_context(self, key: builtins.str) -> typing.Any:
        '''Retrieves a value from tree context if present. Otherwise, would throw an error.

        Context is usually initialized at the root, but can be overridden at any point in the tree.

        :param key: The context key.

        :return: The context value or throws error if there is no context value for this key
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fdfdfb2b2e83a2845cb899305c37d4e37ae13634e2150fa9895e715f45e2752)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(typing.Any, jsii.invoke(self, "getContext", [key]))

    @jsii.member(jsii_name="lock")
    def lock(self) -> None:
        '''Locks this construct from allowing more children to be added.

        After this
        call, no more children can be added to this construct or to any children.
        '''
        return typing.cast(None, jsii.invoke(self, "lock", []))

    @jsii.member(jsii_name="setContext")
    def set_context(self, key: builtins.str, value: typing.Any) -> None:
        '''This can be used to set contextual values.

        Context must be set before any children are added, since children may consult context info during construction.
        If the key already exists, it will be overridden.

        :param key: The context key.
        :param value: The context value.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c20143e21f2a664bb5dbe7722603b1619d511e670df423c20328efe6ebfea2)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "setContext", [key, value]))

    @jsii.member(jsii_name="tryFindChild")
    def try_find_child(self, id: builtins.str) -> typing.Optional["IConstruct"]:
        '''Return a direct child by id, or undefined.

        :param id: Identifier of direct child.

        :return: the child if found, or undefined
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dd332a688f70d4b16d58ad213f452996e4d14aa0f1ab9a377000ebd711a387e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(typing.Optional["IConstruct"], jsii.invoke(self, "tryFindChild", [id]))

    @jsii.member(jsii_name="tryGetContext")
    def try_get_context(self, key: builtins.str) -> typing.Any:
        '''Retrieves a value from tree context.

        Context is usually initialized at the root, but can be overridden at any point in the tree.

        :param key: The context key.

        :return: The context value or ``undefined`` if there is no context value for this key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__736aac5a797564303e88fbc9bbd5d9ec05b62a898284a05b7d16b1761c28b181)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(typing.Any, jsii.invoke(self, "tryGetContext", [key]))

    @jsii.member(jsii_name="tryRemoveChild")
    def try_remove_child(self, child_name: builtins.str) -> builtins.bool:
        '''(experimental) Remove the child with the given name, if present.

        :param child_name: -

        :return: Whether a child with the given name was deleted.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cebd94ba5b2c7d277443dcec352c8c4c87ccbf209e78088ca08a915eb956e36)
            check_type(argname="argument child_name", value=child_name, expected_type=type_hints["child_name"])
        return typing.cast(builtins.bool, jsii.invoke(self, "tryRemoveChild", [child_name]))

    @jsii.member(jsii_name="validate")
    def validate(self) -> typing.List[builtins.str]:
        '''Validates this construct.

        Invokes the ``validate()`` method on all validations added through
        ``addValidation()``.

        :return:

        an array of validation error messages associated with this
        construct.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validate", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PATH_SEP")
    def PATH_SEP(cls) -> builtins.str:
        '''Separator used to delimit construct path components.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PATH_SEP"))

    @builtins.property
    @jsii.member(jsii_name="addr")
    def addr(self) -> builtins.str:
        '''Returns an opaque tree-unique address for this construct.

        Addresses are 42 characters hexadecimal strings. They begin with "c8"
        followed by 40 lowercase hexadecimal characters (0-9a-f).

        Addresses are calculated using a SHA-1 of the components of the construct
        path.

        To enable refactorings of construct trees, constructs with the ID ``Default``
        will be excluded from the calculation. In those cases constructs in the
        same tree may have the same addreess.

        Example::

            c83a2846e506bcc5f10682b564084bca2d275709ee
        '''
        return typing.cast(builtins.str, jsii.get(self, "addr"))

    @builtins.property
    @jsii.member(jsii_name="children")
    def children(self) -> typing.List["IConstruct"]:
        '''All direct children of this construct.'''
        return typing.cast(typing.List["IConstruct"], jsii.get(self, "children"))

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["IConstruct"]:
        '''Return all dependencies registered on this node (non-recursive).'''
        return typing.cast(typing.List["IConstruct"], jsii.get(self, "dependencies"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''The id of this construct within the current scope.

        This is a a scope-unique id. To obtain an app-unique id for this construct, use ``addr``.
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="locked")
    def locked(self) -> builtins.bool:
        '''Returns true if this construct or the scopes in which it is defined are locked.'''
        return typing.cast(builtins.bool, jsii.get(self, "locked"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.List[MetadataEntry]:
        '''An immutable array of metadata objects associated with this construct.

        This can be used, for example, to implement support for deprecation notices, source mapping, etc.
        '''
        return typing.cast(typing.List[MetadataEntry], jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''The full, absolute path of this construct in the tree.

        Components are separated by '/'.
        '''
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="root")
    def root(self) -> "IConstruct":
        '''Returns the root of the construct tree.

        :return: The root of the construct tree.
        '''
        return typing.cast("IConstruct", jsii.get(self, "root"))

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List["IConstruct"]:
        '''All parent scopes of this construct.

        :return:

        a list of parent scopes. The last element in the list will always
        be the current construct and the first element will be the root of the
        tree.
        '''
        return typing.cast(typing.List["IConstruct"], jsii.get(self, "scopes"))

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> typing.Optional["IConstruct"]:
        '''Returns the scope in which this construct is defined.

        The value is ``undefined`` at the root of the construct scope tree.
        '''
        return typing.cast(typing.Optional["IConstruct"], jsii.get(self, "scope"))

    @builtins.property
    @jsii.member(jsii_name="defaultChild")
    def default_child(self) -> typing.Optional["IConstruct"]:
        '''Returns the child construct that has the id ``Default`` or ``Resource"``.

        This is usually the construct that provides the bulk of the underlying functionality.
        Useful for modifications of the underlying construct that are not available at the higher levels.
        Override the defaultChild property.

        This should only be used in the cases where the correct
        default child is not named 'Resource' or 'Default' as it
        should be.

        If you set this to undefined, the default behavior of finding
        the child named 'Resource' or 'Default' will be used.

        :return: a construct or undefined if there is no default child

        :throws: if there is more than one child
        '''
        return typing.cast(typing.Optional["IConstruct"], jsii.get(self, "defaultChild"))

    @default_child.setter
    def default_child(self, value: typing.Optional["IConstruct"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bbcfb9c1c2a97493a49545b146e41d7f6c46f63ff45f96526d7abf737620ea6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultChild", value)


@jsii.implements(IDependable)
class DependencyGroup(metaclass=jsii.JSIIMeta, jsii_type="constructs.DependencyGroup"):
    '''(experimental) A set of constructs to be used as a dependable.

    This class can be used when a set of constructs which are disjoint in the
    construct tree needs to be combined to be used as a single dependable.

    :stability: experimental
    '''

    def __init__(self, *deps: IDependable) -> None:
        '''
        :param deps: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__352fc9ab190809e73b4fcb80cbc3398602d98955aad9386dfbc7162176aa6cbc)
            check_type(argname="argument deps", value=deps, expected_type=typing.Tuple[type_hints["deps"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*deps])

    @jsii.member(jsii_name="add")
    def add(self, *scopes: IDependable) -> None:
        '''(experimental) Add a construct to the dependency roots.

        :param scopes: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0e6908dfe4df8e9318ecca332ccd3a1a3e28fcf76f414daa5a764cba186ef02)
            check_type(argname="argument scopes", value=scopes, expected_type=typing.Tuple[type_hints["scopes"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "add", [*scopes]))


@jsii.interface(jsii_type="constructs.IConstruct")
class IConstruct(IDependable, typing_extensions.Protocol):
    '''Represents a construct.'''

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> Node:
        '''The tree node.'''
        ...


class _IConstructProxy(
    jsii.proxy_for(IDependable), # type: ignore[misc]
):
    '''Represents a construct.'''

    __jsii_type__: typing.ClassVar[str] = "constructs.IConstruct"

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> Node:
        '''The tree node.'''
        return typing.cast(Node, jsii.get(self, "node"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConstruct).__jsii_proxy_class__ = lambda : _IConstructProxy


@jsii.implements(IConstruct)
class Construct(metaclass=jsii.JSIIMeta, jsii_type="constructs.Construct"):
    '''Represents the building block of the construct graph.

    All constructs besides the root construct must be created within the scope of
    another construct.
    '''

    def __init__(self, scope: "Construct", id: builtins.str) -> None:
        '''Creates a new construct node.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings. If the ID includes a path separator (``/``), then it will be replaced by double dash ``--``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__020ca90e326a91c7b0f70a5c5df3471c78175b709d5adcbee2cb463d0367e387)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @jsii.member(jsii_name="isConstruct")
    @builtins.classmethod
    def is_construct(cls, x: typing.Any) -> builtins.bool:
        '''Checks if ``x`` is a construct.

        Use this method instead of ``instanceof`` to properly detect ``Construct``
        instances, even when the construct library is symlinked.

        Explanation: in JavaScript, multiple copies of the ``constructs`` library on
        disk are seen as independent, completely different libraries. As a
        consequence, the class ``Construct`` in each copy of the ``constructs`` library
        is seen as a different class, and an instance of one class will not test as
        ``instanceof`` the other class. ``npm install`` will not create installations
        like this, but users may manually symlink construct libraries together or
        use a monorepo tool: in those cases, multiple copies of the ``constructs``
        library can be accidentally installed, and ``instanceof`` will behave
        unpredictably. It is safest to avoid using ``instanceof``, and using
        this type-testing method instead.

        :param x: Any object.

        :return: true if ``x`` is an object created from a class which extends ``Construct``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd6a4114560af835bb1c07485e906499cadbf16cf78d7e344bc100586fce523f)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isConstruct", [x]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of this construct.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> Node:
        '''The tree node.'''
        return typing.cast(Node, jsii.get(self, "node"))


__all__ = [
    "Construct",
    "ConstructOrder",
    "Dependable",
    "DependencyGroup",
    "IConstruct",
    "IDependable",
    "IValidation",
    "MetadataEntry",
    "MetadataOptions",
    "Node",
]

publication.publish()

def _typecheckingstub__679510e0e5074b5be594d161aaffe1bcbf759129512d69821982adde36fb905d(
    instance: IDependable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fccfa163f8f38b89195d804e18f7122f2b59a7ba7b57ea51cf581e4ae5719bf9(
    instance: IDependable,
    trait: Dependable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a9441299838c86c77ad919b31ab158da6bd872c3bf8bf55f147c17abeea083(
    instance: IDependable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac0c2f394c95b32376bd2487bfa65b455507f8363a71e56bbcfef3a690552658(
    *,
    data: typing.Any,
    type: builtins.str,
    trace: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d38f18f5b98ff8e52a193cc40da1d25ab1a4740362b86cea0782ada618178b(
    *,
    stack_trace: typing.Optional[builtins.bool] = None,
    trace_from_function: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d6f98f49be8b52dd81458a10a699ba3c2baedf270e915aff9ad4a199629f16(
    host: Construct,
    scope: IConstruct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e976ef1a5da0fe82b55c8d7dec2b729e665c685a6fd4cf13e79d119b83e883b(
    construct: IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45cad7dd42c6c671e9f87ba7d66096044214dd8c5bfed807ecb8eee7b41edd21(
    *deps: IDependable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__023b8c3b11b2c1279fbfa8d54f858cec54fb8d9621c584addfbcccc63dbce202(
    type: builtins.str,
    data: typing.Any,
    *,
    stack_trace: typing.Optional[builtins.bool] = None,
    trace_from_function: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67eb37a7475000d487d8124e00d1a8f5c0da44f9b68527dd02d18a3a789e11a0(
    validation: IValidation,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc361d795aa7b43307a9b4d8126549b970305e1487dfba0b95baabe4805e7c1b(
    order: typing.Optional[ConstructOrder] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad30dac2587986f1ad461ddbfadd8c7bdb66542692e2272c9ea5e2487f4fa5f(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fdfdfb2b2e83a2845cb899305c37d4e37ae13634e2150fa9895e715f45e2752(
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c20143e21f2a664bb5dbe7722603b1619d511e670df423c20328efe6ebfea2(
    key: builtins.str,
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd332a688f70d4b16d58ad213f452996e4d14aa0f1ab9a377000ebd711a387e(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__736aac5a797564303e88fbc9bbd5d9ec05b62a898284a05b7d16b1761c28b181(
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cebd94ba5b2c7d277443dcec352c8c4c87ccbf209e78088ca08a915eb956e36(
    child_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bbcfb9c1c2a97493a49545b146e41d7f6c46f63ff45f96526d7abf737620ea6(
    value: typing.Optional[IConstruct],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__352fc9ab190809e73b4fcb80cbc3398602d98955aad9386dfbc7162176aa6cbc(
    *deps: IDependable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0e6908dfe4df8e9318ecca332ccd3a1a3e28fcf76f414daa5a764cba186ef02(
    *scopes: IDependable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__020ca90e326a91c7b0f70a5c5df3471c78175b709d5adcbee2cb463d0367e387(
    scope: Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd6a4114560af835bb1c07485e906499cadbf16cf78d7e344bc100586fce523f(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass
