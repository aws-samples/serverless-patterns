# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

import warnings
from typing import Any

from .utils import SKIP_IN_PATH, query_params


@query_params()
async def list_all_point_in_time(
    self: Any, params: Any = None, headers: Any = None
) -> Any:
    """
    Returns the list of active point in times searches

    .. warning::

        This API will be removed in a future version.
        Use 'get_all_pits' API instead.

    """
    warnings.warn(
        "The 'list_all_point_in_time' API is deprecated and will be removed in a future version. Use 'get_all_pits' API instead.",
        DeprecationWarning,
    )

    return await self.get_all_pits(params=params, headers=headers)


@query_params(
    "expand_wildcards", "ignore_unavailable", "keep_alive", "preference", "routing"
)
async def create_point_in_time(
    self: Any, index: Any, params: Any = None, headers: Any = None
) -> Any:
    """
    Create a point in time that can be used in subsequent searches


    :arg index: A comma-separated list of index names to open point
        in time; use `_all` or empty string to perform the operation on all
        indices
    :arg expand_wildcards: Whether to expand wildcard expression to
        concrete indices that are open, closed or both.  Valid choices: open,
        closed, hidden, none, all  Default: open
    :arg ignore_unavailable: Whether specified concrete indices
        should be ignored when unavailable (missing or closed)
    :arg keep_alive: Specific the time to live for the point in time
    :arg preference: Specify the node or shard the operation should
        be performed on (default: random)
    :arg routing: Specific routing value

    .. warning::

        This API will be removed in a future version.
        Use 'create_pit' API instead.

    """
    warnings.warn(
        "The 'create_point_in_time' API is deprecated and will be removed in a future version. Use 'create_pit' API instead.",
        DeprecationWarning,
    )

    return await self.create_pit(index=index, params=params, headers=headers)


@query_params()
async def delete_point_in_time(
    self: Any,
    body: Any = None,
    all: bool = False,
    params: Any = None,
    headers: Any = None,
) -> Any:
    """
    Delete a point in time


    :arg body: a point-in-time id to delete
    :arg all: set it to `True` to delete all alive point in time.

    .. warning::

        This API will be removed in a future version.
        Use 'delete_all_pits' or 'delete_pit' API instead.

    """
    warnings.warn(
        "The 'delete_point_in_time' API is deprecated and will be removed in a future version. Use 'delete_all_pits' or 'delete_pit' API instead.",
        DeprecationWarning,
    )

    if all:
        return await self.delete_all_pits(params=params, headers=headers)
    else:
        return await self.delete_pit(body=body, params=params, headers=headers)


@query_params()
async def health_check(self: Any, params: Any = None, headers: Any = None) -> Any:
    """
    Checks to see if the Security plugin is up and running.

    .. warning::

        This API will be removed in a future version.
        Use 'health' API instead.

    """
    warnings.warn(
        "The 'health_check' API in security client is deprecated and will be removed in a future version. Use 'health' API instead.",
        DeprecationWarning,
    )

    return await self.health(params=params, headers=headers)


@query_params()
async def update_audit_config(
    self: Any, body: Any, params: Any = None, headers: Any = None
) -> Any:
    """
    A PUT call updates the audit configuration.

    .. warning::

        This API will be removed in a future version.
        Use 'update_audit_configuration' API instead.

    """
    warnings.warn(
        "The 'update_audit_config' API in security client is deprecated and will be removed in a future version. Use 'update_audit_configuration' API instead.",
        DeprecationWarning,
    )

    if body in SKIP_IN_PATH:
        raise ValueError("Empty value passed for a required argument 'body'.")

    return await self.update_audit_configuration(
        params=params, headers=headers, body=body
    )
