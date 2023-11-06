from collections import defaultdict
from typing import Any, Callable, Dict, Optional, Type

from attrs import NOTHING

from cattrs import Converter

__all__ = ["default_tag_generator", "configure_tagged_union"]


def default_tag_generator(typ: Type) -> str:
    """Return the class name."""
    return typ.__name__


def configure_tagged_union(
    union: Any,
    converter: Converter,
    tag_generator: Callable[[Type], str] = default_tag_generator,
    tag_name: str = "_type",
    default: Optional[Type] = NOTHING,
) -> None:
    """
    Configure the converter so that `union` (which should be a union) is
    un/structured with the help of an additional piece of data in the
    unstructured payload, the tag.

    :param converter: The converter to apply the strategy to.
    :param tag_generator: A `tag_generator` function is used to map each
        member of the union to a tag, which is then included in the
        unstructured payload. The default tag generator returns the name of
        the class.
    :param tag_name: The key under which the tag will be set in the
        unstructured payload. By default, `'_type'`.
    :param default: An optional class to be used if the tag information
        is not present when structuring.

    The tagged union strategy currently only works with the dict
    un/structuring base strategy.

    .. versionadded:: 23.1.0
    """
    args = union.__args__
    tag_to_hook = {}
    exact_cl_unstruct_hooks = {}
    for cl in args:
        tag = tag_generator(cl)
        struct_handler = converter._structure_func.dispatch(cl)
        unstruct_handler = converter._unstructure_func.dispatch(cl)

        def structure_union_member(val: dict, _cl=cl, _h=struct_handler) -> cl:
            return _h(val, _cl)

        def unstructure_union_member(val: union, _h=unstruct_handler) -> dict:
            return _h(val)

        tag_to_hook[tag] = structure_union_member
        exact_cl_unstruct_hooks[cl] = unstructure_union_member

    cl_to_tag = {cl: tag_generator(cl) for cl in args}

    if default is not NOTHING:
        default_handler = converter._structure_func.dispatch(default)

        def structure_default(val: dict, _cl=default, _h=default_handler):
            return _h(val, _cl)

        tag_to_hook = defaultdict(lambda: structure_default, tag_to_hook)
        cl_to_tag = defaultdict(lambda: default, cl_to_tag)

    def unstructure_tagged_union(
        val: union,
        _exact_cl_unstruct_hooks=exact_cl_unstruct_hooks,
        _cl_to_tag=cl_to_tag,
        _tag_name=tag_name,
    ) -> Dict:
        res = _exact_cl_unstruct_hooks[val.__class__](val)
        res[_tag_name] = _cl_to_tag[val.__class__]
        return res

    if default is NOTHING:

        def structure_tagged_union(
            val: dict, _, _tag_to_cl=tag_to_hook, _tag_name=tag_name
        ) -> union:
            return _tag_to_cl[val[_tag_name]](val)

    else:

        def structure_tagged_union(
            val: dict,
            _,
            _tag_to_hook=tag_to_hook,
            _tag_name=tag_name,
            _dh=default_handler,
            _default=default,
        ) -> union:
            if _tag_name in val:
                return _tag_to_hook[val[_tag_name]](val)
            else:
                return _dh(val, _default)

    converter.register_unstructure_hook(union, unstructure_tagged_union)
    converter.register_structure_hook(union, structure_tagged_union)
