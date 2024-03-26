# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.


# ------------------------------------------------------------------------------------------
# THIS CODE IS AUTOMATICALLY GENERATED AND MANUAL EDITS WILL BE LOST
#
# To contribute, kindly make modifications in the opensearch-py client generator
# or in the OpenSearch API specification, and run `nox -rs generate`. See DEVELOPER_GUIDE.md
# and https://github.com/opensearch-project/opensearch-api-specification for details.
# -----------------------------------------------------------------------------------------+


from typing import Any

from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class IndicesClient(NamespacedClient):
    @query_params()
    async def analyze(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Performs the analysis process on a text and return the tokens breakdown of the
        text.


        :arg body: Define analyzer/tokenizer parameters and the text on
            which the analysis should be performed
        :arg index: The name of the index to scope the operation.
        """
        return await self.transport.perform_request(
            "POST",
            _make_path(index, "_analyze"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable")
    async def refresh(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Performs the refresh operation in one or more indices.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_refresh"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "force",
        "ignore_unavailable",
        "wait_if_ongoing",
    )
    async def flush(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Performs the flush operation on one or more indices.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg force: Whether a flush should be forced even if it is not
            necessarily needed ie. if no changes will be committed to the index.
            This is useful if transaction log IDs should be incremented even if no
            uncommitted changes are present. (This setting can be considered as
            internal).
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg wait_if_ongoing: If set to true the flush operation will
            block until the flush can be executed if another flush operation is
            already executing. If set to false the flush will be skipped iff if
            another flush operation is already running. Default is True.
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_flush"), params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout", "master_timeout", "timeout", "wait_for_active_shards"
    )
    async def create(
        self,
        index: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates an index with optional settings and mappings.


        :arg index: Index name.
        :arg body: The configuration for the index (`settings` and
            `mappings`)
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Set the number of active shards to
            wait for before the operation returns.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "PUT", _make_path(index), params=params, headers=headers, body=body
        )

    @query_params(
        "cluster_manager_timeout",
        "master_timeout",
        "task_execution_timeout",
        "timeout",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    async def clone(
        self,
        index: Any,
        target: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Clones an index.


        :arg index: The name of the source index to clone.
        :arg target: The name of the target index.
        :arg body: The configuration for the target index (`settings`
            and `aliases`)
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg task_execution_timeout: Explicit task execution timeout,
            only useful when wait_for_completion is false, defaults to 1h.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Set the number of active shards to
            wait for on the cloned index before the operation returns.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is True.
        """
        for param in (index, target):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_clone", target),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "include_defaults",
        "local",
        "master_timeout",
    )
    async def get(
        self,
        index: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about one or more indices.


        :arg index: Comma-separated list of indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified). Default is false.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed). Default is
            false.
        :arg include_defaults: Whether to return all default setting for
            each of the indices. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "GET", _make_path(index), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "task_execution_timeout",
        "timeout",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    async def open(
        self,
        index: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Opens an index.


        :arg index: Comma-separated list of indices to open.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg task_execution_timeout: Explicit task execution timeout,
            only useful when wait_for_completion is false, defaults to 1h.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Sets the number of active shards to
            wait for before the operation returns.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is True.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "POST", _make_path(index, "_open"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def close(
        self,
        index: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Closes an index.


        :arg index: Comma-separated list of indices to close.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Sets the number of active shards to
            wait for before the operation returns.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "POST", _make_path(index, "_close"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "timeout",
    )
    async def delete(
        self,
        index: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes an index.


        :arg index: Comma-separated list of indices to delete; use
            `_all` or `*` string to delete all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified). Default is false.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed). Default is
            false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "DELETE", _make_path(index), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "include_defaults",
        "local",
    )
    async def exists(
        self,
        index: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about whether a particular index exists.


        :arg index: Comma-separated list of indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified). Default is false.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed). Default is
            false.
        :arg include_defaults: Whether to return all default setting for
            each of the indices. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return await self.transport.perform_request(
            "HEAD", _make_path(index), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "timeout",
        "write_index_only",
    )
    async def put_mapping(
        self,
        body: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates the index mappings.


        :arg body: The mapping definition
        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        :arg write_index_only: When true, applies mappings only to the
            write index of an alias or data stream. Default is false.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        if index in SKIP_IN_PATH:
            index = "_all"

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_mapping"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "ignore_unavailable",
        "local",
        "master_timeout",
    )
    async def get_mapping(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns mappings for one or more indices.


        :arg index: Comma-separated list of indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg local (Deprecated: This parameter is a no-op and field
            mappings are always retrieved locally.): Return local information, do
            not retrieve the state from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_mapping"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "include_defaults",
        "local",
    )
    async def get_field_mapping(
        self,
        fields: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns mapping for one or more fields.


        :arg fields: Comma-separated list of fields.
        :arg index: Comma-separated list of indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg include_defaults: Whether the default mapping values should
            be returned as well.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        """
        if fields in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'fields'.")

        return await self.transport.perform_request(
            "GET",
            _make_path(index, "_mapping", "field", fields),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def put_alias(
        self,
        index: Any,
        name: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates an alias.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg name: The name of the alias to be created or updated.
        :arg body: The settings for the alias, such as `routing` or
            `filter`
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        for param in (index, name):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_alias", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable", "local")
    async def exists_alias(
        self,
        name: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about whether a particular alias exists.


        :arg name: Comma-separated list of alias names.
        :arg index: Comma-separated list of indices to filter aliases.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "HEAD", _make_path(index, "_alias", name), params=params, headers=headers
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable", "local")
    async def get_alias(
        self,
        index: Any = None,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns an alias.


        :arg index: Comma-separated list of indices to filter aliases.
        :arg name: Comma-separated list of alias names.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_alias", name), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def update_aliases(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates index aliases.


        :arg body: The definition of `actions` to perform
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "POST", "/_aliases", params=params, headers=headers, body=body
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def delete_alias(
        self,
        index: Any,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes an alias.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg name: Comma-separated list of aliases to delete (supports
            wildcards); use `_all` to delete all aliases for the specified indices.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        for param in (index, name):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "DELETE", _make_path(index, "_alias", name), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "create", "master_timeout", "order")
    async def put_template(
        self,
        name: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates an index template.


        :arg name: The name of the template.
        :arg body: The template definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg create: Whether the index template should only be added if
            new or can also replace an existing one. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg order: The order for this template when merging multiple
            matching ones (higher numbers are merged later, overriding the lower
            numbers).
        """
        for param in (name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_template", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("cluster_manager_timeout", "flat_settings", "local", "master_timeout")
    async def exists_template(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about whether a particular index template exists.


        :arg name: Comma-separated names of the index templates.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "HEAD", _make_path("_template", name), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "flat_settings", "local", "master_timeout")
    async def get_template(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns an index template.


        :arg name: Comma-separated names of the index templates.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return await self.transport.perform_request(
            "GET", _make_path("_template", name), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def delete_template(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes an index template.


        :arg name: The name of the template.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "DELETE", _make_path("_template", name), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "include_defaults",
        "local",
        "master_timeout",
    )
    async def get_settings(
        self,
        index: Any = None,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns settings for one or more indices.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg name: Comma-separated list of settings.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg include_defaults: Whether to return all default setting for
            each of the indices. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_settings", name), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "master_timeout",
        "preserve_existing",
        "timeout",
    )
    async def put_settings(
        self,
        body: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates the index settings.


        :arg body: The index settings to be updated
        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg preserve_existing: Whether to update existing settings. If
            set to `true` existing settings on an index remain unchanged. Default is
            false.
        :arg timeout: Operation timeout.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_settings"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "completion_fields",
        "expand_wildcards",
        "fielddata_fields",
        "fields",
        "forbid_closed_indices",
        "groups",
        "include_segment_file_sizes",
        "include_unloaded_segments",
        "level",
    )
    async def stats(
        self,
        index: Any = None,
        metric: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides statistics on operations happening in an index.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg metric: Limit the information returned the specific
            metrics. Valid choices are _all, store, indexing, get, search, merge,
            flush, refresh, query_cache, fielddata, docs, warmer, completion,
            segments, translog, suggest, request_cache, recovery.
        :arg completion_fields: Comma-separated list of fields for
            `fielddata` and `suggest` index metric (supports wildcards).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg fielddata_fields: Comma-separated list of fields for
            `fielddata` index metric (supports wildcards).
        :arg fields: Comma-separated list of fields for `fielddata` and
            `completion` index metric (supports wildcards).
        :arg forbid_closed_indices: If set to false stats will also
            collected from closed indices if explicitly specified or if
            expand_wildcards expands to closed indices. Default is True.
        :arg groups: Comma-separated list of search groups for `search`
            index metric.
        :arg include_segment_file_sizes: Whether to report the
            aggregated disk usage of each one of the Lucene index files (only
            applies if segment stats are requested). Default is false.
        :arg include_unloaded_segments: If set to true segment stats
            will include stats for segments that are not currently loaded into
            memory. Default is false.
        :arg level: Return stats aggregated at cluster, index or shard
            level. Valid choices are cluster, indices, shards.
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_stats", metric), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices", "expand_wildcards", "ignore_unavailable", "verbose"
    )
    async def segments(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides low-level information about segments in a Lucene index.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg verbose: Includes detailed memory usage by Lucene. Default
            is false.
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_segments"), params=params, headers=headers
        )

    @query_params(
        "all_shards",
        "allow_no_indices",
        "analyze_wildcard",
        "analyzer",
        "default_operator",
        "df",
        "expand_wildcards",
        "explain",
        "ignore_unavailable",
        "lenient",
        "q",
        "rewrite",
    )
    async def validate_query(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows a user to validate a potentially expensive query without executing it.


        :arg body: The query definition specified with the Query DSL
        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg all_shards: Execute validation on all shards instead of one
            random shard per index.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg analyze_wildcard: Specify whether wildcard and prefix
            queries should be analyzed. Default is false.
        :arg analyzer: The analyzer to use for the query string.
        :arg default_operator: The default operator for query string
            query (AND or OR). Valid choices are AND, OR.
        :arg df: The field to use as default where no field prefix is
            given in the query string.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg explain: Return detailed information about the error.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg lenient: Specify whether format-based query failures (such
            as providing text to a numeric field) should be ignored.
        :arg q: Query in the Lucene query string syntax.
        :arg rewrite: Provide a more detailed explanation showing the
            actual Lucene query that will be executed.
        """
        return await self.transport.perform_request(
            "POST",
            _make_path(index, "_validate", "query"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "fielddata",
        "fields",
        "ignore_unavailable",
        "query",
        "request",
    )
    async def clear_cache(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Clears all or specific caches for one or more indices.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg fielddata: Clear field data.
        :arg fields: Comma-separated list of fields to clear when using
            the `fielddata` parameter (default: all).
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg query: Clear query caches.
        :arg request: Clear request cache.
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_cache", "clear"), params=params, headers=headers
        )

    @query_params("active_only", "detailed")
    async def recovery(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about ongoing index shard recoveries.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg active_only: Display only those recoveries that are
            currently on-going. Default is false.
        :arg detailed: Whether to display detailed information about
            shard recovery. Default is false.
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_recovery"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "only_ancient_segments",
        "wait_for_completion",
    )
    async def upgrade(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        The _upgrade API is no longer useful and will be removed.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg only_ancient_segments: If true, only ancient (an older
            Lucene major release) segments will be upgraded.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is false.
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_upgrade"), params=params, headers=headers
        )

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable")
    async def get_upgrade(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        The _upgrade API is no longer useful and will be removed.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_upgrade"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices", "expand_wildcards", "ignore_unavailable", "status"
    )
    async def shard_stores(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides store information for shard copies of indices.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg status: Comma-separated list of statuses used to filter on
            shards to get store information for.
        """
        return await self.transport.perform_request(
            "GET", _make_path(index, "_shard_stores"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "flush",
        "ignore_unavailable",
        "max_num_segments",
        "only_expunge_deletes",
        "primary_only",
        "wait_for_completion",
    )
    async def forcemerge(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Performs the force merge operation on one or more indices.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg flush: Specify whether the index should be flushed after
            performing the operation. Default is True.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg max_num_segments: The number of segments the index should
            be merged into (default: dynamic).
        :arg only_expunge_deletes: Specify whether the operation should
            only expunge deleted documents.
        :arg primary_only: Specify whether the operation should only
            perform on primary shards. Defaults to false. Default is false.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is True.
        """
        return await self.transport.perform_request(
            "POST", _make_path(index, "_forcemerge"), params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "copy_settings",
        "master_timeout",
        "task_execution_timeout",
        "timeout",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    async def shrink(
        self,
        index: Any,
        target: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allow to shrink an existing index into a new index with fewer primary shards.


        :arg index: The name of the source index to shrink.
        :arg target: The name of the target index.
        :arg body: The configuration for the target index (`settings`
            and `aliases`)
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg copy_settings: whether or not to copy settings from the
            source index. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg task_execution_timeout: Explicit task execution timeout,
            only useful when wait_for_completion is false, defaults to 1h.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Set the number of active shards to
            wait for on the shrunken index before the operation returns.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is True.
        """
        for param in (index, target):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_shrink", target),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "cluster_manager_timeout",
        "copy_settings",
        "master_timeout",
        "task_execution_timeout",
        "timeout",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    async def split(
        self,
        index: Any,
        target: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows you to split an existing index into a new index with more primary
        shards.


        :arg index: The name of the source index to split.
        :arg target: The name of the target index.
        :arg body: The configuration for the target index (`settings`
            and `aliases`)
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg copy_settings: whether or not to copy settings from the
            source index. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg task_execution_timeout: Explicit task execution timeout,
            only useful when wait_for_completion is false, defaults to 1h.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Set the number of active shards to
            wait for on the shrunken index before the operation returns.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is True.
        """
        for param in (index, target):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(index, "_split", target),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "cluster_manager_timeout",
        "dry_run",
        "master_timeout",
        "timeout",
        "wait_for_active_shards",
    )
    async def rollover(
        self,
        alias: Any,
        body: Any = None,
        new_index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates an alias to point to a new index when the existing index is considered
        to be too large or too old.


        :arg alias: The name of the alias to rollover.
        :arg body: The conditions that needs to be met for executing
            rollover
        :arg new_index: The name of the rollover index.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg dry_run: If set to true the rollover action will only be
            validated but not actually performed even if a condition matches.
            Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Set the number of active shards to
            wait for on the newly created rollover index before the operation
            returns.
        """
        if alias in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'alias'.")

        return await self.transport.perform_request(
            "POST",
            _make_path(alias, "_rollover", new_index),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def create_data_stream(
        self,
        name: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates a data stream.


        :arg name: The name of the data stream.
        :arg body: The data stream definition
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_data_stream", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def delete_data_stream(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a data stream.


        :arg name: Comma-separated list of data streams; use `_all` or
            empty string to perform the operation on all data streams.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "DELETE", _make_path("_data_stream", name), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def delete_index_template(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes an index template.


        :arg name: The name of the template.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_index_template", name),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "flat_settings", "local", "master_timeout")
    async def exists_index_template(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about whether a particular index template exists.


        :arg name: The name of the template.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "HEAD", _make_path("_index_template", name), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "flat_settings", "local", "master_timeout")
    async def get_index_template(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns an index template.


        :arg name: Comma-separated names of the index templates.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return await self.transport.perform_request(
            "GET", _make_path("_index_template", name), params=params, headers=headers
        )

    @query_params("cause", "cluster_manager_timeout", "create", "master_timeout")
    async def put_index_template(
        self,
        name: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates an index template.


        :arg name: The name of the template.
        :arg body: The template definition
        :arg cause: User defined reason for creating/updating the index
            template. Default is false.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg create: Whether the index template should only be added if
            new or can also replace an existing one. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        for param in (name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_index_template", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("cause", "cluster_manager_timeout", "create", "master_timeout")
    async def simulate_index_template(
        self,
        name: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Simulate matching the given index name against the index templates in the
        system.


        :arg name: The name of the index (it must be a concrete index
            name).
        :arg body: New index template definition, which will be included
            in the simulation, as if it already exists in the system
        :arg cause: User defined reason for dry-run creating the new
            template for simulation purposes. Default is false.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg create: Whether the index template we optionally defined in
            the body should only be dry-run added if new or can also replace an
            existing one. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_index_template", "_simulate_index", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def get_data_stream(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns data streams.


        :arg name: Comma-separated list of data streams; use `_all` or
            empty string to perform the operation on all data streams.
        """
        return await self.transport.perform_request(
            "GET", _make_path("_data_stream", name), params=params, headers=headers
        )

    @query_params("cause", "cluster_manager_timeout", "create", "master_timeout")
    async def simulate_template(
        self,
        body: Any = None,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Simulate resolving the given template name or body.


        :arg body: New index template definition to be simulated, if no
            index template name is specified
        :arg name: The name of the template.
        :arg cause: User defined reason for dry-run creating the new
            template for simulation purposes. Default is false.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg create: Whether the index template we optionally defined in
            the body should only be dry-run added if new or can also replace an
            existing one. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return await self.transport.perform_request(
            "POST",
            _make_path("_index_template", "_simulate", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("expand_wildcards")
    async def resolve_index(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about any matching indices, aliases, and data streams.


        :arg name: Comma-separated list of names or wildcard
            expressions.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "GET", _make_path("_resolve", "index", name), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "ignore_unavailable",
        "master_timeout",
        "timeout",
    )
    async def add_block(
        self,
        index: Any,
        block: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Adds a block to an index.


        :arg index: Comma-separated list of indices to add a block to.
        :arg block: The block to add (one of read, write, read_only or
            metadata).
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        for param in (index, block):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT", _make_path(index, "_block", block), params=params, headers=headers
        )

    @query_params()
    async def data_streams_stats(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides statistics on operations happening in a data stream.


        :arg name: Comma-separated list of data streams; use `_all` or
            empty string to perform the operation on all data streams.
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_data_stream", name, "_stats"),
            params=params,
            headers=headers,
        )
