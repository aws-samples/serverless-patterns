import builtins
import sys
from collections import deque
from collections.abc import MutableSet as AbcMutableSet
from collections.abc import Set as AbcSet
from dataclasses import MISSING
from dataclasses import fields as dataclass_fields
from dataclasses import is_dataclass
from typing import AbstractSet as TypingAbstractSet
from typing import Any, Deque, Dict, FrozenSet, List
from typing import Mapping as TypingMapping
from typing import MutableMapping as TypingMutableMapping
from typing import MutableSequence as TypingMutableSequence
from typing import MutableSet as TypingMutableSet
from typing import NewType, Optional
from typing import Sequence as TypingSequence
from typing import Set as TypingSet
from typing import Tuple, get_type_hints

from attr import NOTHING, Attribute, Factory
from attr import fields as attrs_fields
from attr import resolve_types

try:
    from typing_extensions import TypedDict as ExtensionsTypedDict
except ImportError:
    ExtensionsTypedDict = None

try:
    from typing_extensions import _TypedDictMeta as ExtensionsTypedDictMeta
except ImportError:
    ExtensionsTypedDictMeta = None

__all__ = [
    "ExtensionsTypedDict",
    "is_py37",
    "is_py38",
    "is_py39_plus",
    "is_py310_plus",
    "is_py311_plus",
    "is_typeddict",
    "TypedDict",
]

version_info = sys.version_info[0:3]
is_py37 = version_info[:2] == (3, 7)
is_py38 = version_info[:2] == (3, 8)
is_py39_plus = version_info[:2] >= (3, 9)
is_py310_plus = version_info[:2] >= (3, 10)
is_py311_plus = version_info[:2] >= (3, 11)

if is_py37:

    def get_args(cl):
        return cl.__args__

    def get_origin(cl):
        return getattr(cl, "__origin__", None)

    from typing_extensions import Final, Protocol

else:
    from typing import Final, Protocol, get_args, get_origin

if "ExceptionGroup" not in dir(builtins):
    from exceptiongroup import ExceptionGroup
else:
    ExceptionGroup = ExceptionGroup


def has(cls):
    return hasattr(cls, "__attrs_attrs__") or hasattr(cls, "__dataclass_fields__")


def has_with_generic(cls):
    """Test whether the class if a normal or generic attrs or dataclass."""
    return has(cls) or has(get_origin(cls))


def fields(type):
    try:
        return type.__attrs_attrs__
    except AttributeError:
        try:
            return dataclass_fields(type)
        except AttributeError:
            raise Exception("Not an attrs or dataclass class.")


def _adapted_fields(cl) -> List[Attribute]:
    """Return the attrs format of `fields()` for attrs and dataclasses."""
    if is_dataclass(cl):
        attrs = dataclass_fields(cl)
        if any(isinstance(a.type, str) for a in attrs):
            # Do this conditionally in case `get_type_hints` fails, so
            # users can resolve on their own first.
            type_hints = get_type_hints(cl)
        else:
            type_hints = {}
        return [
            Attribute(
                attr.name,
                attr.default
                if attr.default is not MISSING
                else (
                    Factory(attr.default_factory)
                    if attr.default_factory is not MISSING
                    else NOTHING
                ),
                None,
                True,
                None,
                True,
                attr.init,
                True,
                type=type_hints.get(attr.name, attr.type),
            )
            for attr in attrs
        ]
    else:
        attribs = attrs_fields(cl)
        if any(isinstance(a.type, str) for a in attribs):
            # PEP 563 annotations - need to be resolved.
            resolve_types(cl)
            attribs = attrs_fields(cl)
        return attribs


def is_subclass(obj: type, bases) -> bool:
    """A safe version of issubclass (won't raise)."""
    try:
        return issubclass(obj, bases)
    except TypeError:
        return False


def is_hetero_tuple(type: Any) -> bool:
    origin = getattr(type, "__origin__", None)
    return origin is tuple and ... not in type.__args__


def is_protocol(type: Any) -> bool:
    return issubclass(type, Protocol) and getattr(type, "_is_protocol", False)


def is_bare_final(type) -> bool:
    return type is Final


def get_final_base(type) -> Optional[type]:
    """Return the base of the Final annotation, if it is Final."""
    if type is Final:
        return Any
    elif type.__class__ is _GenericAlias and type.__origin__ is Final:
        return type.__args__[0]
    else:
        return None


OriginAbstractSet = AbcSet
OriginMutableSet = AbcMutableSet

if is_py37 or is_py38:
    Set = TypingSet
    AbstractSet = TypingAbstractSet
    MutableSet = TypingMutableSet

    Sequence = TypingSequence
    MutableSequence = TypingMutableSequence
    MutableMapping = TypingMutableMapping
    Mapping = TypingMapping
    FrozenSetSubscriptable = FrozenSet
    TupleSubscriptable = Tuple

    from collections import Counter as ColCounter
    from typing import Counter, Union, _GenericAlias
    from typing_extensions import Annotated, NotRequired, Required
    from typing_extensions import get_origin as te_get_origin

    if is_py38:
        from typing import TypedDict, _TypedDictMeta
    else:
        _TypedDictMeta = None
        TypedDict = ExtensionsTypedDict

    def is_annotated(type) -> bool:
        return te_get_origin(type) is Annotated

    def is_tuple(type):
        return type in (Tuple, tuple) or (
            type.__class__ is _GenericAlias and issubclass(type.__origin__, Tuple)
        )

    def is_union_type(obj):
        return (
            obj is Union or isinstance(obj, _GenericAlias) and obj.__origin__ is Union
        )

    def get_newtype_base(typ: Any) -> Optional[type]:
        supertype = getattr(typ, "__supertype__", None)
        if (
            supertype is not None
            and getattr(typ, "__qualname__", "") == "NewType.<locals>.new_type"
            and typ.__module__ in ("typing", "typing_extensions")
        ):
            return supertype
        return None

    def is_sequence(type: Any) -> bool:
        return type in (List, list, Tuple, tuple) or (
            type.__class__ is _GenericAlias
            and (
                type.__origin__ not in (Union, Tuple, tuple)
                and issubclass(type.__origin__, TypingSequence)
            )
            or (type.__origin__ in (Tuple, tuple) and type.__args__[1] is ...)
        )

    def is_deque(type: Any) -> bool:
        return (
            type in (deque, Deque)
            or (type.__class__ is _GenericAlias and issubclass(type.__origin__, deque))
            or type.__origin__ is deque
        )

    def is_mutable_set(type):
        return type is set or (
            type.__class__ is _GenericAlias and issubclass(type.__origin__, MutableSet)
        )

    def is_frozenset(type):
        return type is frozenset or (
            type.__class__ is _GenericAlias and issubclass(type.__origin__, FrozenSet)
        )

    def is_mapping(type):
        return type in (TypingMapping, dict) or (
            type.__class__ is _GenericAlias
            and issubclass(type.__origin__, TypingMapping)
        )

    bare_generic_args = {
        List.__args__,
        TypingSequence.__args__,
        TypingMapping.__args__,
        Dict.__args__,
        TypingMutableSequence.__args__,
        Tuple.__args__,
        None,  # non-parametrized containers do not have `__args__ attribute in py3.7-8
    }

    def is_bare(type):
        return getattr(type, "__args__", None) in bare_generic_args

    def is_counter(type):
        return (
            type in (Counter, ColCounter)
            or getattr(type, "__origin__", None) is ColCounter
        )

    if is_py38:
        from typing import Literal

        def is_literal(type) -> bool:
            return type.__class__ is _GenericAlias and type.__origin__ is Literal

    else:
        # No literals in 3.7.
        def is_literal(_) -> bool:
            return False

    def is_generic(obj):
        return isinstance(obj, _GenericAlias)

    def copy_with(type, args):
        """Replace a generic type's arguments."""
        return type.copy_with(args)

    def is_typeddict(cls) -> bool:
        return (
            cls.__class__ is _TypedDictMeta
            or (is_generic(cls) and (cls.__origin__.__class__ is _TypedDictMeta))
            or (
                ExtensionsTypedDictMeta is not None
                and cls.__class__ is ExtensionsTypedDictMeta
                or (
                    is_generic(cls)
                    and (cls.__origin__.__class__ is ExtensionsTypedDictMeta)
                )
            )
        )

    def get_notrequired_base(type) -> "Union[Any, Literal[NOTHING]]":
        if get_origin(type) in (NotRequired, Required):
            return get_args(type)[0]
        return NOTHING

else:
    # 3.9+
    from collections import Counter
    from collections.abc import Mapping as AbcMapping
    from collections.abc import MutableMapping as AbcMutableMapping
    from collections.abc import MutableSequence as AbcMutableSequence
    from collections.abc import MutableSet as AbcMutableSet
    from collections.abc import Sequence as AbcSequence
    from collections.abc import Set as AbcSet
    from types import GenericAlias
    from typing import Annotated
    from typing import Counter as TypingCounter
    from typing import (
        Generic,
        TypedDict,
        Union,
        _AnnotatedAlias,
        _GenericAlias,
        _SpecialGenericAlias,
        _TypedDictMeta,
        _UnionGenericAlias,
    )

    try:
        # Not present on 3.9.0, so we try carefully.
        from typing import _LiteralGenericAlias

        def is_literal(type) -> bool:
            return type.__class__ is _LiteralGenericAlias

    except ImportError:

        def is_literal(_) -> bool:
            return False

    Set = AbcSet
    AbstractSet = AbcSet
    MutableSet = AbcMutableSet
    Sequence = AbcSequence
    MutableSequence = AbcMutableSequence
    MutableMapping = AbcMutableMapping
    Mapping = AbcMapping
    FrozenSetSubscriptable = frozenset
    TupleSubscriptable = tuple

    def is_annotated(type) -> bool:
        return getattr(type, "__class__", None) is _AnnotatedAlias

    def is_tuple(type):
        return (
            type in (Tuple, tuple)
            or (type.__class__ is _GenericAlias and issubclass(type.__origin__, Tuple))
            or (getattr(type, "__origin__", None) is tuple)
        )

    if is_py310_plus:

        def is_union_type(obj):
            from types import UnionType

            return (
                obj is Union
                or (isinstance(obj, _UnionGenericAlias) and obj.__origin__ is Union)
                or isinstance(obj, UnionType)
            )

        def get_newtype_base(typ: Any) -> Optional[type]:
            if typ is NewType or isinstance(typ, NewType):
                return typ.__supertype__
            return None

        if is_py311_plus:
            from typing import NotRequired, Required
        else:
            from typing_extensions import NotRequired, Required

    else:
        from typing_extensions import NotRequired, Required

        def is_union_type(obj):
            return (
                obj is Union
                or isinstance(obj, _UnionGenericAlias)
                and obj.__origin__ is Union
            )

        def get_newtype_base(typ: Any) -> Optional[type]:
            supertype = getattr(typ, "__supertype__", None)
            if (
                supertype is not None
                and getattr(typ, "__qualname__", "") == "NewType.<locals>.new_type"
                and typ.__module__ in ("typing", "typing_extensions")
            ):
                return supertype
            return None

    def is_typeddict(cls) -> bool:
        return (
            cls.__class__ is _TypedDictMeta
            or (is_generic(cls) and (cls.__origin__.__class__ is _TypedDictMeta))
            or (
                ExtensionsTypedDictMeta is not None
                and cls.__class__ is ExtensionsTypedDictMeta
                or (
                    is_generic(cls)
                    and (cls.__origin__.__class__ is ExtensionsTypedDictMeta)
                )
            )
        )

    def get_notrequired_base(type) -> "Union[Any, Literal[NOTHING]]":
        if get_origin(type) in (NotRequired, Required):
            return get_args(type)[0]
        return NOTHING

    def is_sequence(type: Any) -> bool:
        origin = getattr(type, "__origin__", None)
        return (
            type
            in (
                List,
                list,
                TypingSequence,
                TypingMutableSequence,
                AbcMutableSequence,
                tuple,
                Tuple,
                deque,
                Deque,
            )
            or (
                type.__class__ is _GenericAlias
                and (
                    (origin is not tuple)
                    and issubclass(origin, TypingSequence)
                    or origin is tuple
                    and type.__args__[1] is ...
                )
            )
            or (origin in (list, deque, AbcMutableSequence, AbcSequence))
            or (origin is tuple and type.__args__[1] is ...)
        )

    def is_deque(type):
        return (
            type in (deque, Deque)
            or (type.__class__ is _GenericAlias and issubclass(type.__origin__, deque))
            or (getattr(type, "__origin__", None) is deque)
        )

    def is_mutable_set(type):
        return (
            type in (TypingSet, TypingMutableSet, set)
            or (
                type.__class__ is _GenericAlias
                and issubclass(type.__origin__, TypingMutableSet)
            )
            or (getattr(type, "__origin__", None) in (set, AbcMutableSet, AbcSet))
        )

    def is_frozenset(type):
        return (
            type in (FrozenSet, frozenset)
            or (
                type.__class__ is _GenericAlias
                and issubclass(type.__origin__, FrozenSet)
            )
            or (getattr(type, "__origin__", None) is frozenset)
        )

    def is_bare(type):
        return isinstance(type, _SpecialGenericAlias) or (
            not hasattr(type, "__origin__") and not hasattr(type, "__args__")
        )

    def is_mapping(type):
        return (
            type in (dict, Dict, TypingMapping, TypingMutableMapping, AbcMutableMapping)
            or (
                type.__class__ is _GenericAlias
                and issubclass(type.__origin__, TypingMapping)
            )
            or (
                getattr(type, "__origin__", None)
                in (dict, AbcMutableMapping, AbcMapping)
            )
            or issubclass(type, dict)
        )

    def is_counter(type):
        return (
            type in (Counter, TypingCounter)
            or getattr(type, "__origin__", None) is Counter
        )

    def is_generic(obj) -> bool:
        return (
            isinstance(obj, _GenericAlias)
            or isinstance(obj, GenericAlias)
            or is_subclass(obj, Generic)
        )

    def copy_with(type, args):
        """Replace a generic type's arguments."""
        if is_annotated(type):
            # typing.Annotated requires a special case.
            return Annotated[args]  # type: ignore
        return type.__origin__[args]


def is_generic_attrs(type):
    return is_generic(type) and has(type.__origin__)
