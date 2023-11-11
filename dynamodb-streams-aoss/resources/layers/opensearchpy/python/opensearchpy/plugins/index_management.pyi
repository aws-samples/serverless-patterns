# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from typing import Any, Union

from ..client.utils import NamespacedClient as NamespacedClient
from ..client.utils import query_params as query_params

class IndexManagementClient(NamespacedClient):
    def put_policy(
        self,
        policy: Any,
        body: Any | None = ...,
        params: Any | None = ...,
        headers: Any | None = ...,
    ) -> Union[bool, Any]: ...
    def add_policy(
        self,
        index: Any,
        body: Any | None = ...,
        params: Any | None = ...,
        headers: Any | None = ...,
    ) -> Union[bool, Any]: ...
    def get_policy(
        self,
        policy: Any,
        body: Any | None = ...,
        params: Any | None = ...,
        headers: Any | None = ...,
    ) -> Union[bool, Any]: ...
    def remove_policy_from_index(
        self,
        index: Any,
        body: Any | None = ...,
        params: Any | None = ...,
        headers: Any | None = ...,
    ) -> Union[bool, Any]: ...
    def change_policy(
        self,
        index: Any,
        body: Any | None = ...,
        params: Any | None = ...,
        headers: Any | None = ...,
    ) -> Union[bool, Any]: ...
    def retry(
        self,
        index: Any,
        body: Any | None = ...,
        params: Any | None = ...,
        headers: Any | None = ...,
    ) -> Union[bool, Any]: ...
    def explain_index(
        self,
        index: Any,
        body: Any | None = ...,
        params: Any | None = ...,
        headers: Any | None = ...,
    ) -> Union[bool, Any]: ...
    def delete_policy(
        self,
        policy: Any,
        body: Any | None = ...,
        params: Any | None = ...,
        headers: Any | None = ...,
    ) -> Union[bool, Any]: ...
