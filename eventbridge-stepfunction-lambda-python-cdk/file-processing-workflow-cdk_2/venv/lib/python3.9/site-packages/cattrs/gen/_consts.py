from threading import local
from typing import Any, Callable, Optional

from attr import frozen


@frozen
class AttributeOverride:
    omit_if_default: Optional[bool] = None
    rename: Optional[str] = None
    omit: bool = False  # Omit the field completely.
    struct_hook: Optional[Callable[[Any, Any], Any]] = None  # Structure hook to use.
    unstruct_hook: Optional[Callable[[Any], Any]] = None  # Structure hook to use.


neutral = AttributeOverride()
already_generating = local()
