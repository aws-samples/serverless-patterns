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


from .utils import NamespacedClient, _make_path, query_params


class CatClient(NamespacedClient):
    @query_params("expand_wildcards", "format", "h", "help", "local", "s", "v")
    async def aliases(self, name=None, params=None, headers=None):
        """
        Shows information about currently configured aliases to indices including
        filter and routing infos.


        :arg name: A comma-separated list of alias names to return
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: all
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", _make_path("_cat", "aliases", name), params=params, headers=headers
        )

    @query_params(
        "bytes",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "v",
    )
    async def allocation(self, node_id=None, params=None, headers=None):
        """
        Provides a snapshot of how many shards are allocated to each data node and how
        much disk space they are using.


        :arg node_id: A comma-separated list of node IDs or names to
            limit the returned information
        :arg bytes: The unit in which to display byte values  Valid
            choices: b, k, kb, m, mb, g, gb, t, tb, p, pb
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_cat", "allocation", node_id),
            params=params,
            headers=headers,
        )

    @query_params("format", "h", "help", "s", "v")
    async def count(self, index=None, params=None, headers=None):
        """
        Provides quick access to the document count of the entire cluster, or
        individual indices.


        :arg index: A comma-separated list of index names to limit the
            returned information
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", _make_path("_cat", "count", index), params=params, headers=headers
        )

    @query_params("format", "h", "help", "s", "time", "ts", "v")
    async def health(self, params=None, headers=None):
        """
        Returns a concise representation of the cluster health.


        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg ts: Set to false to disable timestamping  Default: True
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", "/_cat/health", params=params, headers=headers
        )

    @query_params("help", "s")
    async def help(self, params=None, headers=None):
        """
        Returns help for the Cat APIs.


        :arg help: Return help information
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        """
        return await self.transport.perform_request(
            "GET", "/_cat", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "expand_wildcards",
        "format",
        "h",
        "health",
        "help",
        "include_unloaded_segments",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "pri",
        "s",
        "time",
        "v",
    )
    async def indices(self, index=None, params=None, headers=None):
        """
        Returns information about indices: number of primaries and replicas, document
        counts, disk size, ...


        :arg index: A comma-separated list of index names to limit the
            returned information
        :arg bytes: The unit in which to display byte values  Valid
            choices: b, k, kb, m, mb, g, gb, t, tb, p, pb
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both.  Valid choices: open,
            closed, hidden, none, all  Default: all
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg health: A health status ("green", "yellow", or "red" to
            filter only indices matching the specified health status  Valid choices:
            green, yellow, red
        :arg help: Return help information
        :arg include_unloaded_segments: If set to true segment stats
            will include stats for segments that are not currently loaded into
            memory
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg pri: Set to true to return stats only for primary shards
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", _make_path("_cat", "indices", index), params=params, headers=headers
        )

    @query_params(
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "v",
    )
    async def master(self, params=None, headers=None):
        """
        Returns information about the master node.


        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        from warnings import warn

        warn("Deprecated: use `cluster_manager` instead")
        return await self.transport.perform_request(
            "GET", "/_cat/master", params=params, headers=headers
        )

    @query_params("format", "h", "help", "local", "cluster_manager", "s", "v")
    async def cluster_manager(self, params=None, headers=None):
        """
        Returns information about the cluster_manager node.


        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", "/_cat/cluster_manager", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "format",
        "full_id",
        "h",
        "help",
        "include_unloaded_segments",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "time",
        "v",
    )
    async def nodes(self, params=None, headers=None):
        """
        Returns basic statistics about performance of cluster nodes.


        :arg bytes: The unit in which to display byte values  Valid
            choices: b, k, kb, m, mb, g, gb, t, tb, p, pb
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg full_id: Return the full node ID instead of the shortened
            version (default: false)
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg include_unloaded_segments: If set to true segment stats
            will include stats for segments that are not currently loaded into
            memory
        :arg local: Calculate the selected nodes using the local cluster
            state rather than the state from master node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", "/_cat/nodes", params=params, headers=headers
        )

    @query_params(
        "active_only", "bytes", "detailed", "format", "h", "help", "s", "time", "v"
    )
    async def recovery(self, index=None, params=None, headers=None):
        """
        Returns information about index shard recoveries, both on-going completed.


        :arg index: Comma-separated list or wildcard expression of index
            names to limit the returned information
        :arg active_only: If `true`, the response only includes ongoing
            shard recoveries
        :arg bytes: The unit in which to display byte values  Valid
            choices: b, k, kb, m, mb, g, gb, t, tb, p, pb
        :arg detailed: If `true`, the response includes detailed
            information about shard recoveries
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", _make_path("_cat", "recovery", index), params=params, headers=headers
        )

    @query_params(
        "bytes",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "time",
        "v",
    )
    async def shards(self, index=None, params=None, headers=None):
        """
        Provides a detailed view of shard allocation on nodes.


        :arg index: A comma-separated list of index names to limit the
            returned information
        :arg bytes: The unit in which to display byte values  Valid
            choices: b, k, kb, m, mb, g, gb, t, tb, p, pb
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", _make_path("_cat", "shards", index), params=params, headers=headers
        )

    @query_params("bytes", "format", "h", "help", "s", "v")
    async def segments(self, index=None, params=None, headers=None):
        """
        Provides low-level information about the segments in the shards of an index.


        :arg index: A comma-separated list of index names to limit the
            returned information
        :arg bytes: The unit in which to display byte values  Valid
            choices: b, k, kb, m, mb, g, gb, t, tb, p, pb
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", _make_path("_cat", "segments", index), params=params, headers=headers
        )

    @query_params(
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "time",
        "v",
    )
    async def pending_tasks(self, params=None, headers=None):
        """
        Returns a concise representation of the cluster pending tasks.


        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", "/_cat/pending_tasks", params=params, headers=headers
        )

    @query_params(
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "size",
        "v",
    )
    async def thread_pool(self, thread_pool_patterns=None, params=None, headers=None):
        """
        Returns cluster-wide thread pool statistics per node. By default the active,
        queue and rejected statistics are returned for all thread pools.


        :arg thread_pool_patterns: A comma-separated list of regular-
            expressions to filter the thread pools in the output
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg size: The multiplier in which to display values  Valid
            choices: , k, m, g, t, p
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_cat", "thread_pool", thread_pool_patterns),
            params=params,
            headers=headers,
        )

    @query_params("bytes", "format", "h", "help", "s", "v")
    async def fielddata(self, fields=None, params=None, headers=None):
        """
        Shows how much heap memory is currently being used by fielddata on every data
        node in the cluster.


        :arg fields: A comma-separated list of fields to return in the
            output
        :arg bytes: The unit in which to display byte values  Valid
            choices: b, k, kb, m, mb, g, gb, t, tb, p, pb
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_cat", "fielddata", fields),
            params=params,
            headers=headers,
        )

    @query_params(
        "format",
        "h",
        "help",
        "include_bootstrap",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "v",
    )
    async def plugins(self, params=None, headers=None):
        """
        Returns information about installed plugins across nodes node.


        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg include_bootstrap: Include bootstrap plugins in the
            response
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", "/_cat/plugins", params=params, headers=headers
        )

    @query_params(
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "v",
    )
    async def nodeattrs(self, params=None, headers=None):
        """
        Returns information about custom node attributes.


        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", "/_cat/nodeattrs", params=params, headers=headers
        )

    @query_params(
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "v",
    )
    async def repositories(self, params=None, headers=None):
        """
        Returns information about snapshot repositories registered in the cluster.


        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from master node
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", "/_cat/repositories", params=params, headers=headers
        )

    @query_params(
        "format",
        "h",
        "help",
        "ignore_unavailable",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "time",
        "v",
    )
    async def snapshots(self, repository=None, params=None, headers=None):
        """
        Returns all snapshots in a specific repository.


        :arg repository: Name of repository from which to fetch the
            snapshot information
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg ignore_unavailable: Set to true to ignore unavailable
            snapshots
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_cat", "snapshots", repository),
            params=params,
            headers=headers,
        )

    @query_params(
        "actions",
        "detailed",
        "format",
        "h",
        "help",
        "nodes",
        "parent_task_id",
        "s",
        "time",
        "v",
    )
    async def tasks(self, params=None, headers=None):
        """
        Returns information about the tasks currently executing on one or more nodes in
        the cluster.


        :arg actions: A comma-separated list of actions that should be
            returned. Leave empty to return all.
        :arg detailed: Return detailed task information (default: false)
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg nodes: A comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all nodes
        :arg parent_task_id: Return tasks with specified parent task id
            (node_id:task_number). Set to -1 to return all.
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", "/_cat/tasks", params=params, headers=headers
        )

    @query_params(
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "cluster_manager_timeout",
        "s",
        "v",
    )
    async def templates(self, name=None, params=None, headers=None):
        """
        Returns information about existing templates.


        :arg name: A pattern that returned template names must match
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg local: Return local information, do not retrieve the state
            from cluster_manager node (default: false)
        :arg master_timeout (Deprecated: use cluster_manager_timeout): Explicit operation timeout for connection
            to master node
        :arg cluster_manager_timeout: Explicit operation timeout for connection
            to cluster_manager node
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg v: Verbose mode. Display column headers
        """
        return await self.transport.perform_request(
            "GET", _make_path("_cat", "templates", name), params=params, headers=headers
        )

    @query_params(
        "allow_no_match", "format", "from_", "h", "help", "s", "size", "time", "v"
    )
    async def transforms(self, transform_id=None, params=None, headers=None):
        """
        Gets configuration and usage information about transforms.


        :arg transform_id: The id of the transform for which to get
            stats. '_all' or '*' implies all transforms
        :arg allow_no_match: Whether to ignore if a wildcard expression
            matches no transforms. (This includes `_all` string or when no
            transforms have been specified)
        :arg format: a short version of the Accept header, e.g. json,
            yaml
        :arg from_: skips a number of transform configs, defaults to 0
        :arg h: Comma-separated list of column names to display
        :arg help: Return help information
        :arg s: Comma-separated list of column names or column aliases
            to sort by
        :arg size: specifies a max number of transforms to get, defaults
            to 100
        :arg time: The unit in which to display time values  Valid
            choices: d, h, m, s, ms, micros, nanos
        :arg v: Verbose mode. Display column headers
        """
        # from is a reserved word so it cannot be used, use from_ instead
        if "from_" in params:
            params["from"] = params.pop("from_")

        return await self.transport.perform_request(
            "GET",
            _make_path("_cat", "transforms", transform_id),
            params=params,
            headers=headers,
        )
