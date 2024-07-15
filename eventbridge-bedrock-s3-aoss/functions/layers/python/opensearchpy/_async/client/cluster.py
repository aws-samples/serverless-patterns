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


class ClusterClient(NamespacedClient):
    @query_params(
        "awareness_attribute",
        "cluster_manager_timeout",
        "error_trace",
        "expand_wildcards",
        "filter_path",
        "human",
        "level",
        "local",
        "master_timeout",
        "pretty",
        "source",
        "timeout",
        "wait_for_active_shards",
        "wait_for_events",
        "wait_for_no_initializing_shards",
        "wait_for_no_relocating_shards",
        "wait_for_nodes",
        "wait_for_status",
    )
    async def health(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns basic information about the health of the cluster.


        :arg index: Comma-separated list of data streams, indices, and
            index aliases used to limit the request. Wildcard expressions (*) are
            supported. To target all data streams and indices in a cluster, omit
            this parameter or use `_all` or `*`.
        :arg awareness_attribute: The awareness attribute for which the
            health is required.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg level: Can be one of cluster, indices or shards. Controls
            the details level of the health information returned. Valid choices are
            cluster, indices, shards, awareness_attributes.
        :arg local: If true, the request retrieves information from the
            local node only. Defaults to false, which means information is retrieved
            from the master node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node. If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response. If no response is
            received before the timeout expires, the request fails and returns an
            error.
        :arg wait_for_active_shards: A number controlling to how many
            active shards to wait for, all to wait for all shards in the cluster to
            be active, or 0 to not wait. Valid choices are all, index-setting.
        :arg wait_for_events: Can be one of immediate, urgent, high,
            normal, low, languid. Wait until all currently queued events with the
            given priority are processed. Valid choices are immediate, urgent, high,
            normal, low, languid.
        :arg wait_for_no_initializing_shards: A boolean value which
            controls whether to wait (until the timeout provided) for the cluster to
            have no shard initializations. Defaults to false, which means it will
            not wait for initializing shards.
        :arg wait_for_no_relocating_shards: A boolean value which
            controls whether to wait (until the timeout provided) for the cluster to
            have no shard relocations. Defaults to false, which means it will not
            wait for relocating shards.
        :arg wait_for_nodes: The request waits until the specified
            number N of nodes is available. It also accepts >=N, <=N, >N and <N.
            Alternatively, it is possible to use ge(N), le(N), gt(N) and lt(N)
            notation.
        :arg wait_for_status: One of green, yellow or red. Will wait
            (until the timeout provided) until the status of the cluster changes to
            the one provided or better, i.e. green > yellow > red. By default, will
            not wait for any status. Valid choices are green, yellow, red.
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_cluster", "health", index),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "source",
    )
    async def pending_tasks(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a list of any cluster-level changes (e.g. create index, update mapping,
        allocate or fail shard) which have not yet been executed.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: If `true`, the request retrieves information from
            the local node only.If `false`, information is retrieved from the master
            node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node.If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return await self.transport.perform_request(
            "GET", "/_cluster/pending_tasks", params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "error_trace",
        "expand_wildcards",
        "filter_path",
        "flat_settings",
        "human",
        "ignore_unavailable",
        "local",
        "master_timeout",
        "pretty",
        "source",
        "wait_for_metadata_version",
        "wait_for_timeout",
    )
    async def state(
        self,
        metric: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a comprehensive information about the state of the cluster.


        :arg metric: Limit the information returned to the specified
            metrics
        :arg index: A comma-separated list of index names; use `_all` or
            empty string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Specify timeout for connection
            to master
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg wait_for_metadata_version: Wait for the metadata version to
            be equal or greater than the specified metadata version
        :arg wait_for_timeout: The maximum time to wait for
            wait_for_metadata_version before timing out
        """
        if index and metric in SKIP_IN_PATH:
            metric = "_all"

        return await self.transport.perform_request(
            "GET",
            _make_path("_cluster", "state", metric, index),
            params=params,
            headers=headers,
        )

    @query_params(
        "error_trace",
        "filter_path",
        "flat_settings",
        "human",
        "pretty",
        "source",
        "timeout",
    )
    async def stats(
        self,
        node_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns high-level overview of cluster statistics.


        :arg node_id: Comma-separated list of node filters used to limit
            returned information. Defaults to all nodes in the cluster.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg flat_settings: If `true`, returns settings in flat format.
            Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for each node to respond.If a node
            does not respond before its timeout expires, the response does not
            include its stats.However, timed out nodes are included in the
            response’s `_nodes.failed` property. Defaults to no timeout.
        """
        return await self.transport.perform_request(
            "GET",
            (
                "/_cluster/stats"
                if node_id in SKIP_IN_PATH
                else _make_path("_cluster", "stats", "nodes", node_id)
            ),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "dry_run",
        "error_trace",
        "explain",
        "filter_path",
        "human",
        "master_timeout",
        "metric",
        "pretty",
        "retry_failed",
        "source",
        "timeout",
    )
    async def reroute(
        self,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to manually change the allocation of individual shards in the cluster.


        :arg body: The definition of `commands` to perform (`move`,
            `cancel`, `allocate`)
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg dry_run: If true, then the request simulates the operation
            only and returns the resulting state.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg explain: If true, then the response contains an explanation
            of why the commands can or cannot be executed.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node. If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg metric: Limits the information returned to the specified
            metrics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg retry_failed: If true, then retries allocation of shards
            that are blocked due to too many subsequent allocation failures.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response. If no response is
            received before the timeout expires, the request fails and returns an
            error.
        """
        return await self.transport.perform_request(
            "POST", "/_cluster/reroute", params=params, headers=headers, body=body
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "flat_settings",
        "human",
        "include_defaults",
        "master_timeout",
        "pretty",
        "source",
        "timeout",
    )
    async def get_settings(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns cluster settings.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg flat_settings: If `true`, returns settings in flat format.
            Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg include_defaults: If `true`, returns default cluster
            settings from the local node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node.If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response.If no response is
            received before the timeout expires, the request fails and returns an
            error.
        """
        return await self.transport.perform_request(
            "GET", "/_cluster/settings", params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "flat_settings",
        "human",
        "master_timeout",
        "pretty",
        "source",
        "timeout",
    )
    async def put_settings(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates the cluster settings.


        :arg body: The settings to be updated. Can be either `transient`
            or `persistent` (survives cluster restart).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Explicit operation timeout for
            connection to master node
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Explicit operation timeout
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PUT", "/_cluster/settings", params=params, headers=headers, body=body
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    async def remote_info(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns the information about configured remote clusters.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return await self.transport.perform_request(
            "GET", "/_remote/info", params=params, headers=headers
        )

    @query_params(
        "error_trace",
        "filter_path",
        "human",
        "include_disk_info",
        "include_yes_decisions",
        "pretty",
        "source",
    )
    async def allocation_explain(
        self,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides explanations for shard allocations in the cluster.


        :arg body: The index, shard, and primary flag to explain. Empty
            means 'explain the first unassigned shard'
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg include_disk_info: If true, returns information about disk
            usage and shard sizes. Default is false.
        :arg include_yes_decisions: If true, returns YES decisions in
            explanation. Default is false.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return await self.transport.perform_request(
            "POST",
            "/_cluster/allocation/explain",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "master_timeout",
        "pretty",
        "source",
        "timeout",
    )
    async def delete_component_template(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a component template.


        :arg name: Name of the component template to delete. Wildcard
            (*) expressions are supported.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node.If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response.If no response is
            received before the timeout expires, the request fails and returns an
            error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_component_template", name),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "source",
    )
    async def get_component_template(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns one or more component templates.


        :arg name: Name of the component template to retrieve. Wildcard
            (`*`) expressions are supported.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: If `true`, the request retrieves information from
            the local node only.If `false`, information is retrieved from the master
            node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node.If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_component_template", name),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "create",
        "error_trace",
        "filter_path",
        "human",
        "master_timeout",
        "pretty",
        "source",
        "timeout",
    )
    async def put_component_template(
        self,
        name: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates a component template.


        :arg name: Name of the component template to create. Opensearch
            includes the following built-in component templates: `logs-mappings`;
            'logs-settings`; `metrics-mappings`; `metrics-settings`;`synthetics-
            mapping`; `synthetics-settings`. Opensearch Agent uses these templates
            to configure backing indices for its data streams. If you use Opensearch
            Agent and want to overwrite one of these templates, set the `version`
            for your replacement template higher than the current version. If you
            don’t use Opensearch Agent and want to disable all built-in component
            and index templates, set `stack.templates.enabled` to `false` using the
            cluster update settings API.
        :arg body: The template definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg create: If `true`, this request cannot replace or update
            existing component templates. Default is false.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node.If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Operation timeout.
        """
        for param in (name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_component_template", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "source",
    )
    async def exists_component_template(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about whether a particular component template exist.


        :arg name: Name of the component template to check existence of.
            Wildcard (*) expressions are supported.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: If true, the request retrieves information from the
            local node only.Defaults to false, which means information is retrieved
            from the master node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node. If no response isreceived before the timeout
            expires, the request fails and returns anerror.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return await self.transport.perform_request(
            "HEAD",
            _make_path("_component_template", name),
            params=params,
            headers=headers,
        )

    @query_params(
        "error_trace", "filter_path", "human", "pretty", "source", "wait_for_removal"
    )
    async def delete_voting_config_exclusions(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Clears cluster voting config exclusions.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg wait_for_removal: Specifies whether to wait for all
            excluded nodes to be removed from thecluster before clearing the voting
            configuration exclusions list.Defaults to true, meaning that all
            excluded nodes must be removed fromthe cluster before this API takes any
            action. If set to false then thevoting configuration exclusions list is
            cleared even if some excludednodes are still in the cluster. Default is
            True.
        """
        return await self.transport.perform_request(
            "DELETE",
            "/_cluster/voting_config_exclusions",
            params=params,
            headers=headers,
        )

    @query_params(
        "error_trace",
        "filter_path",
        "human",
        "node_ids",
        "node_names",
        "pretty",
        "source",
        "timeout",
    )
    async def post_voting_config_exclusions(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates the cluster voting config exclusions by node ids or node names.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg node_ids: A comma-separated list of the persistent ids of
            the nodes to excludefrom the voting configuration. If specified, you may
            not also specify node_names.
        :arg node_names: A comma-separated list of the names of the
            nodes to exclude from thevoting configuration. If specified, you may not
            also specify node_ids.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: When adding a voting configuration exclusion, the
            API waits for thespecified nodes to be excluded from the voting
            configuration beforereturning. If the timeout expires before the
            appropriate conditionis satisfied, the request fails and returns an
            error.
        """
        return await self.transport.perform_request(
            "POST", "/_cluster/voting_config_exclusions", params=params, headers=headers
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    async def delete_decommission_awareness(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete any existing decommission.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return await self.transport.perform_request(
            "DELETE", "/_cluster/decommission/awareness", params=params, headers=headers
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    async def delete_weighted_routing(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete weighted shard routing weights.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return await self.transport.perform_request(
            "DELETE",
            "/_cluster/routing/awareness/weights",
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    async def get_decommission_awareness(
        self,
        awareness_attribute_name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Get details and status of decommissioned attribute.


        :arg awareness_attribute_name: Awareness attribute name.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if awareness_attribute_name in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'awareness_attribute_name'."
            )

        return await self.transport.perform_request(
            "GET",
            _make_path(
                "_cluster",
                "decommission",
                "awareness",
                awareness_attribute_name,
                "_status",
            ),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    async def get_weighted_routing(
        self,
        attribute: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Fetches weighted shard routing weights.


        :arg attribute: Awareness attribute name.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if attribute in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'attribute'.")

        return await self.transport.perform_request(
            "GET",
            _make_path("_cluster", "routing", "awareness", attribute, "weights"),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    async def put_decommission_awareness(
        self,
        awareness_attribute_name: Any,
        awareness_attribute_value: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Decommissions an awareness attribute.


        :arg awareness_attribute_name: Awareness attribute name.
        :arg awareness_attribute_value: Awareness attribute value.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        for param in (awareness_attribute_name, awareness_attribute_value):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path(
                "_cluster",
                "decommission",
                "awareness",
                awareness_attribute_name,
                awareness_attribute_value,
            ),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    async def put_weighted_routing(
        self,
        attribute: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates weighted shard routing weights.


        :arg attribute: Awareness attribute name.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if attribute in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'attribute'.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_cluster", "routing", "awareness", attribute, "weights"),
            params=params,
            headers=headers,
        )
