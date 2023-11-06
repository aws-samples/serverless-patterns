"""Preconfigured converters for cbor2."""
from datetime import datetime, timezone
from typing import Any, Type, TypeVar

from cbor2 import dumps, loads

from cattrs._compat import AbstractSet

from ..converters import BaseConverter, Converter

T = TypeVar("T")


class Cbor2Converter(Converter):
    def dumps(self, obj: Any, unstructure_as: Any = None, **kwargs: Any) -> bytes:
        return dumps(self.unstructure(obj, unstructure_as=unstructure_as), **kwargs)

    def loads(self, data: bytes, cl: Type[T], **kwargs: Any) -> T:
        return self.structure(loads(data, **kwargs), cl)


def configure_converter(converter: BaseConverter):
    """
    Configure the converter for use with the cbor2 library.

    * datetimes are serialized as timestamp floats
    * sets are serialized as lists
    """
    converter.register_unstructure_hook(datetime, lambda v: v.timestamp())
    converter.register_structure_hook(
        datetime, lambda v, _: datetime.fromtimestamp(v, timezone.utc)
    )


def make_converter(*args: Any, **kwargs: Any) -> Cbor2Converter:
    kwargs["unstruct_collection_overrides"] = {
        AbstractSet: list,
        **kwargs.get("unstruct_collection_overrides", {}),
    }
    res = Cbor2Converter(*args, **kwargs)
    configure_converter(res)

    return res
