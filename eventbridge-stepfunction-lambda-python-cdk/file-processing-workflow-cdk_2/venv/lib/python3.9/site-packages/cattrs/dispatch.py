from functools import lru_cache, singledispatch
from typing import Any, Callable, List, Optional, Tuple, Union

import attr


@attr.s
class _DispatchNotFound:
    """A dummy object to help signify a dispatch not found."""

    pass


class MultiStrategyDispatch:
    """
    MultiStrategyDispatch uses a combination of exact-match dispatch,
    singledispatch, and FunctionDispatch.
    """

    __slots__ = (
        "_direct_dispatch",
        "_function_dispatch",
        "_single_dispatch",
        "_generators",
        "_fallback_func",
        "dispatch",
    )

    def __init__(self, fallback_func: Callable[[Any, Any], Any]):
        self._direct_dispatch = {}
        self._function_dispatch = FunctionDispatch()
        self._single_dispatch = singledispatch(_DispatchNotFound)
        self.dispatch = lru_cache(maxsize=None)(self._dispatch)
        self._fallback_func = fallback_func

    def _dispatch(self, typ: Any) -> Callable[[Any, Any], Any]:
        try:
            dispatch = self._single_dispatch.dispatch(typ)
            if dispatch is not _DispatchNotFound:
                return dispatch
        except Exception:
            pass

        direct_dispatch = self._direct_dispatch.get(typ)
        if direct_dispatch is not None:
            return direct_dispatch

        res = self._function_dispatch.dispatch(typ)
        return res if res is not None else self._fallback_func

    def register_cls_list(self, cls_and_handler, direct: bool = False) -> None:
        """Register a class to direct or singledispatch."""
        for cls, handler in cls_and_handler:
            if direct:
                self._direct_dispatch[cls] = handler
            else:
                self._single_dispatch.register(cls, handler)
                self.clear_direct()
        self.dispatch.cache_clear()

    def register_func_list(
        self,
        pred_and_handler: List[
            Union[
                Tuple[Callable[[Any], bool], Any],
                Tuple[Callable[[Any], bool], Any, bool],
            ]
        ],
    ):
        """
        Register a predicate function to determine if the handle
        should be used for the type.
        """
        for tup in pred_and_handler:
            if len(tup) == 2:
                func, handler = tup
                self._function_dispatch.register(func, handler)
            else:
                func, handler, is_gen = tup
                self._function_dispatch.register(func, handler, is_generator=is_gen)
        self.clear_direct()
        self.dispatch.cache_clear()

    def clear_direct(self):
        """Clear the direct dispatch."""
        self._direct_dispatch.clear()

    def clear_cache(self):
        """Clear all caches."""
        self._direct_dispatch.clear()
        self.dispatch.cache_clear()

    def get_num_fns(self) -> int:
        return self._function_dispatch.get_num_fns()

    def copy_to(self, other: "MultiStrategyDispatch", skip: int = 0):
        self._function_dispatch.copy_to(other._function_dispatch, skip=skip)
        for cls, fn in self._single_dispatch.registry.items():
            other._single_dispatch.register(cls, fn)


@attr.s(slots=True)
class FunctionDispatch:
    """
    FunctionDispatch is similar to functools.singledispatch, but
    instead dispatches based on functions that take the type of the
    first argument in the method, and return True or False.

    objects that help determine dispatch should be instantiated objects.
    """

    _handler_pairs: List[
        Tuple[Callable[[Any], bool], Callable[[Any, Any], Any], bool]
    ] = attr.ib(factory=list)

    def register(self, can_handle: Callable[[Any], bool], func, is_generator=False):
        self._handler_pairs.insert(0, (can_handle, func, is_generator))

    def dispatch(self, typ: Any) -> Optional[Callable[[Any, Any], Any]]:
        """
        returns the appropriate handler, for the object passed.
        """
        for can_handle, handler, is_generator in self._handler_pairs:
            # can handle could raise an exception here
            # such as issubclass being called on an instance.
            # it's easier to just ignore that case.
            try:
                ch = can_handle(typ)
            except Exception:
                continue
            if ch:
                if is_generator:
                    return handler(typ)
                else:
                    return handler
        return None

    def get_num_fns(self) -> int:
        return len(self._handler_pairs)

    def copy_to(self, other: "FunctionDispatch", skip: int = 0):
        other._handler_pairs.extend(self._handler_pairs[skip:])
