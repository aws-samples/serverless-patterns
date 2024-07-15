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
    @query_params(
        "error_trace",
        "expand_wildcards",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "pretty",
        "s",
        "source",
        "v",
    )
    def aliases(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Shows information about currently configured aliases to indices including
        filter and routing infos.


        :arg name: A comma-separated list of aliases to retrieve.
            Supports wildcards (`*`).  To retrieve all aliases, omit this parameter
            or use `*` or `_all`.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "aliases", name), params=params, headers=headers
        )

    @query_params(
        "bytes",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "pretty",
        "s",
        "source",
        "v",
    )
    def all_pit_segments(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Lists all active point-in-time segments.


        :arg bytes: The unit in which to display byte values. Valid
            choices are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/pit_segments/_all", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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


        :arg node_id: Comma-separated list of node identifiers or names
            used to limit the returned information.
        :arg bytes: The unit used to display byte values. Valid choices
            are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
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
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/cluster_manager", params=params, headers=headers
        )

    @query_params(
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "pretty",
        "s",
        "source",
        "v",
    )
    def count(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides quick access to the document count of the entire cluster, or
        individual indices.


        :arg index: Comma-separated list of data streams, indices, and
            aliases used to limit the request. Supports wildcards (`*`). To target
            all data streams and indices, omit this parameter or use `*` or `_all`.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "count", index), params=params, headers=headers
        )

    @query_params(
        "bytes",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "pretty",
        "s",
        "source",
        "v",
    )
    def fielddata(
        self,
        fields: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Shows how much heap memory is currently being used by fielddata on every data
        node in the cluster.


        :arg fields: Comma-separated list of fields used to limit
            returned information.
        :arg bytes: The unit used to display byte values. Valid choices
            are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_cat", "fielddata", fields),
            params=params,
            headers=headers,
        )

    @query_params(
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "pretty",
        "s",
        "source",
        "time",
        "ts",
        "v",
    )
    def health(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a concise representation of the cluster health.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit used to display time values. Valid choices
            are nanos, micros, ms, s, m, h, d.
        :arg ts: If true, returns `HH:MM:SS` and Unix epoch timestamps.
            Default is True.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/health", params=params, headers=headers
        )

    @query_params(
        "error_trace", "filter_path", "help", "human", "pretty", "s", "source"
    )
    def help(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns help for the Cat APIs.


        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return self.transport.perform_request(
            "GET", "/_cat", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "error_trace",
        "expand_wildcards",
        "filter_path",
        "format",
        "h",
        "health",
        "help",
        "human",
        "include_unloaded_segments",
        "local",
        "master_timeout",
        "pretty",
        "pri",
        "s",
        "source",
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


        :arg index: Comma-separated list of data streams, indices, and
            aliases used to limit the request. Supports wildcards (`*`). To target
            all data streams and indices, omit this parameter or use `*` or `_all`.
        :arg bytes: The unit used to display byte values. Valid choices
            are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg expand_wildcards: The type of index that wildcard patterns
            can match. Valid choices are all, open, closed, hidden, none.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg health: The health status used to limit returned indices.
            By default, the response includes indices of any health status. Valid
            choices are green, yellow, red.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg include_unloaded_segments: If true, the response includes
            information from segments that are not loaded into memory. Default is
            false.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg pri: If true, the response only includes information from
            primary shards. Default is false.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit used to display time values. Valid choices
            are nanos, micros, ms, s, m, h, d.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "indices", index), params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
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
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/nodeattrs", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "full_id",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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


        :arg bytes: The unit used to display byte values. Valid choices
            are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg full_id: If `true`, return the full node ID. If `false`,
            return the shortened node ID. Default is false.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local (Deprecated: This parameter does not cause this API
            to act locally.): Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit in which to display time values. Valid
            choices are nanos, micros, ms, s, m, h, d.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/nodes", params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit in which to display time values. Valid
            choices are nanos, micros, ms, s, m, h, d.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/pending_tasks", params=params, headers=headers
        )

    @query_params(
        "bytes",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "pretty",
        "s",
        "source",
        "v",
    )
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
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/pit_segments", params=params, headers=headers, body=body
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/plugins", params=params, headers=headers
        )

    @query_params(
        "active_only",
        "bytes",
        "detailed",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "pretty",
        "s",
        "source",
        "time",
        "v",
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
        :arg bytes: The unit used to display byte values. Valid choices
            are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg detailed: If `true`, the response includes detailed
            information about shard recoveries. Default is false.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit in which to display time values. Valid
            choices are nanos, micros, ms, s, m, h, d.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "recovery", index), params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
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
        "error_trace",
        "expand_wildcards",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "ignore_throttled",
        "ignore_unavailable",
        "pretty",
        "s",
        "shards",
        "source",
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
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg ignore_throttled: Whether specified concrete, expanded or
            aliased indices should be ignored when throttled.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg shards: Comma-separated list of shards to display.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit in which to display time values. Valid
            choices are nanos, micros, ms, s, m, h, d.
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
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "master_timeout",
        "pretty",
        "s",
        "source",
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


        :arg index: A comma-separated list of data streams, indices, and
            aliases used to limit the request. Supports wildcards (`*`). To target
            all data streams and indices, omit this parameter or use `*` or `_all`.
        :arg bytes: The unit used to display byte values. Valid choices
            are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "segments", index), params=params, headers=headers
        )

    @query_params(
        "bytes",
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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


        :arg index: A comma-separated list of data streams, indices, and
            aliases used to limit the request. Supports wildcards (`*`). To target
            all data streams and indices, omit this parameter or use `*` or `_all`.
        :arg bytes: The unit used to display byte values. Valid choices
            are b, k, kb, m, mb, g, gb, t, tb, p, pb.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit in which to display time values. Valid
            choices are nanos, micros, ms, s, m, h, d.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "shards", index), params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "size",
        "source",
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


        :arg thread_pool_patterns: A comma-separated list of thread pool
            names used to limit the request. Accepts wildcard expressions.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg size: The multiplier in which to display values.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
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
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "ignore_unavailable",
        "master_timeout",
        "pretty",
        "s",
        "source",
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


        :arg repository: A comma-separated list of snapshot repositories
            used to limit the request. Accepts wildcard expressions. `_all` returns
            all repositories. If any repository fails during the request, Opensearch
            returns an error.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg ignore_unavailable: If `true`, the response does not
            include information from unavailable snapshots. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit in which to display time values. Valid
            choices are nanos, micros, ms, s, m, h, d.
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
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "nodes",
        "parent_task_id",
        "pretty",
        "s",
        "source",
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


        :arg actions: The task action names, which are used to limit the
            response.
        :arg detailed: If `true`, the response includes detailed
            information about shard recoveries. Default is false.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg nodes: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg parent_task_id: The parent task identifier, which is used
            to limit the response.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg time: The unit in which to display time values. Valid
            choices are nanos, micros, ms, s, m, h, d.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_cat/tasks", params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "format",
        "h",
        "help",
        "human",
        "local",
        "master_timeout",
        "pretty",
        "s",
        "source",
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


        :arg name: The name of the template to return. Accepts wildcard
            expressions. If omitted, all templates are returned.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg format: A short version of the Accept header, e.g. json,
            yaml.
        :arg h: Comma-separated list of column names to display.
        :arg help: Return help information. Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg s: Comma-separated list of column names or column aliases
            to sort by.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg v: Verbose mode. Display column headers. Default is false.
        """
        return self.transport.perform_request(
            "GET", _make_path("_cat", "templates", name), params=params, headers=headers
        )
