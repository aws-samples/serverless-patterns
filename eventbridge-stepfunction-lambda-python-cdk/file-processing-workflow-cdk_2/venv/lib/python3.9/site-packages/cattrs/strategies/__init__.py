"""High level strategies for converters."""
from ._subclasses import include_subclasses
from ._unions import configure_tagged_union

__all__ = ["configure_tagged_union", "include_subclasses"]
