"""Line-cache functionality."""
import linecache
import uuid
from typing import Any


def generate_unique_filename(cls: Any, func_name: str, reserve: bool = True) -> str:
    """
    Create a "filename" suitable for a function being generated.
    """
    unique_id = uuid.uuid4()
    extra = ""
    count = 1

    while True:
        unique_filename = "<cattrs generated {0} {1}.{2}{3}>".format(
            func_name, cls.__module__, getattr(cls, "__qualname__", cls.__name__), extra
        )
        if not reserve:
            return unique_filename
        # To handle concurrency we essentially "reserve" our spot in
        # the linecache with a dummy line.  The caller can then
        # set this value correctly.
        cache_line = (1, None, (str(unique_id),), unique_filename)
        if linecache.cache.setdefault(unique_filename, cache_line) == cache_line:
            return unique_filename

        # Looks like this spot is taken. Try again.
        count += 1
        extra = "-{0}".format(count)
