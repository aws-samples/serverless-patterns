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

from .utils import NamespacedClient, _make_path, query_params


class CatClient(NamespacedClient):
    @query_params("expand_wildcards", "format", "h", "help", "local", "s", "v")
    def aliases(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Shows information about currently configured aliases to indices including
        filter and routing infos.


        :arg name: Comma-separated list of alias names.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "aliases", name), params=params, headers=headers
        )

    @query_params("bytes", "format", "h", "help", "s", "v")
    def all_pit_segments(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Lists all active point-in-time segments.


        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/pit_segments/_all", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "v",
    )
    def allocation(
        self,
        node_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides a snapshot of how many shards are allocated to each data node and how
        much disk space they are using.


        :arg node_id: Comma-separated list of node IDs or names to limit
            the returned information.
        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_cat", "allocation", node_id),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "v",
    )
    def cluster_manager(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about the cluster-manager node.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/cluster_manager", params=params, headers=headers
        )

    @query_params("format", "h", "help", "s", "v")
    def count(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides quick access to the document count of the entire cluster, or
        individual indices.


        :arg index: Comma-separated list of indices to limit the
            returned information.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "count", index), params=params, headers=headers
        )

    @query_params("bytes", "format", "h", "help", "s", "v")
    def fielddata(
        self,
        fields: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Shows how much heap memory is currently being used by fielddata on every data
        node in the cluster.


        :arg fields: Comma-separated list of fields to return in the
            output.
        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_cat", "fielddata", fields),
            params=params,
            headers=headers,
        )

    @query_params("format", "h", "help", "s", "time", "ts", "v")
    def health(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a concise representation of the cluster health.


        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg ts: Set to false to disable timestamping. Default is True.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/health", params=params, headers=headers
        )

    @query_params("help", "s")
    def help(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns help for the Cat APIs.


        :arg help: Return help information. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        """
        return self.transport.perform_request(
            "GET", "/_cat", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "expand_wildcards",
        "format",
        "h",
        "health",
        "help",
        "include_unloaded_segments",
        "local",
        "master_timeout",
        "pri",
        "s",
        "time",
        "v",
    )
    def indices(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about indices: number of primaries and replicas, document
        counts, disk size, ...


        :arg index: Comma-separated list of indices to limit the
            returned information.
        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg health: Health status ('green', 'yellow', or 'red') to
            filter only indices matching the specified health status. Valid choices
            are green, yellow, red.
        :arg help: Return help information. Default is false.
        :arg include_unloaded_segments: If set to true segment stats
            will include stats for segments that are not currently loaded into
            memory. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pri: Set to true to return stats only for primary shards.
            Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "indices", index), params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "v",
    )
    def master(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about the cluster-manager node.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        from warnings import warn

        warn(
            "Deprecated: To promote inclusive language, please use '/_cat/cluster_manager' instead."
        )
        return self.transport.perform_request(
            "GET", "/_cat/master", params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "v",
    )
    def nodeattrs(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about custom node attributes.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/nodeattrs", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "format",
        "full_id",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "time",
        "v",
    )
    def nodes(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns basic statistics about performance of cluster nodes.


        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg full_id: Return the full node ID instead of the shortened
            version. Default is false.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local (Deprecated: This parameter does not cause this API
            to act locally.): Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/nodes", params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "time",
        "v",
    )
    def pending_tasks(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a concise representation of the cluster pending tasks.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/pending_tasks", params=params, headers=headers
        )

    @query_params("bytes", "format", "h", "help", "s", "v")
    def pit_segments(
        self,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        List segments for one or several PITs.


        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/pit_segments", params=params, headers=headers, body=body
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "v",
    )
    def plugins(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about installed plugins across nodes node.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/plugins", params=params, headers=headers
        )

    @query_params(
        "active_only", "bytes", "detailed", "format", "h", "help", "s", "time", "v"
    )
    def recovery(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about index shard recoveries, both on-going completed.


        :arg index: Comma-separated list or wildcard expression of index
            names to limit the returned information.
        :arg active_only: If `true`, the response only includes ongoing
            shard recoveries. Default is false.
        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg detailed: If `true`, the response includes detailed
            information about shard recoveries. Default is false.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "recovery", index), params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "v",
    )
    def repositories(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about snapshot repositories registered in the cluster.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/repositories", params=params, headers=headers
        )

    @query_params(
        "active_only",
        "allow_no_indices",
        "bytes",
        "completed_only",
        "detailed",
        "expand_wildcards",
        "format",
        "h",
        "help",
        "ignore_throttled",
        "ignore_unavailable",
        "s",
        "shards",
        "time",
        "timeout",
        "v",
    )
    def segment_replication(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about both on-going and latest completed Segment
        Replication events.


        :arg index: Comma-separated list or wildcard expression of index
            names to limit the returned information.
        :arg active_only: If `true`, the response only includes ongoing
            segment replication events. Default is false.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg completed_only: If `true`, the response only includes
            latest completed segment replication events. Default is false.
        :arg detailed: If `true`, the response includes detailed
            information about segment replications. Default is false.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg ignore_throttled: Whether specified concrete, expanded or
            aliased indices should be ignored when throttled.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg shards: Comma-separated list of shards to display.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg timeout: Operation timeout.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_cat", "segment_replication", index),
            params=params,
            headers=headers,
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "master_timeout",
        "s",
        "v",
    )
    def segments(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides low-level information about the segments in the shards of an index.


        :arg index: Comma-separated list of indices to limit the
            returned information.
        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "segments", index), params=params, headers=headers
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "time",
        "v",
    )
    def shards(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides a detailed view of shard allocation on nodes.


        :arg index: Comma-separated list of indices to limit the
            returned information.
        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "shards", index), params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "size",
        "v",
    )
    def thread_pool(
        self,
        thread_pool_patterns: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns cluster-wide thread pool statistics per node. By default the active,
        queue and rejected statistics are returned for all thread pools.


        :arg thread_pool_patterns: Comma-separated list of regular-
            expressions to filter the thread pools in the output.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg size: The multiplier in which to display values.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_cat", "thread_pool", thread_pool_patterns),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "ignore_unavailable",
        "master_timeout",
        "s",
        "time",
        "v",
    )
    def snapshots(
        self,
        repository: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns all snapshots in a specific repository.


        :arg repository: Comma-separated list of repository names.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed). Default is
            false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
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
    def tasks(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about the tasks currently executing on one or more nodes in
        the cluster.


        :arg actions: Comma-separated list of actions that should be
            returned. Leave empty to return all.
        :arg detailed: Return detailed task information. Default is
            false.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg nodes: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg parent_task_id: Return tasks with specified parent task id
            (node_id:task_number). Set to -1 to return all.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg time: The unit in which to display time values. Valid
            choices are d, h, m, s, ms, micros, nanos.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/tasks", params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "format",
        "h",
        "help",
        "local",
        "master_timeout",
        "s",
        "v",
    )
    def templates(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about existing templates.


        :arg name: The name of the template.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "templates", name), params=params, headers=headers
        )
