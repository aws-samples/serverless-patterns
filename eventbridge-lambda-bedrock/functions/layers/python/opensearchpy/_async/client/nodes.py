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


class NodesClient(NamespacedClient):
    @query_params("error_trace", "filter_path", "human", "pretty", "source", "timeout")
    async def reload_secure_settings(
        self,
        body: Any = None,
        node_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Reloads secure settings.


        :arg body: An object containing the password for the opensearch
            keystore
        :arg node_id: The names of particular nodes in the cluster to
            target.
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
        :arg timeout: Period to wait for a response.If no response is
            received before the timeout expires, the request fails and returns an
            error.
        """
        return await self.transport.perform_request(
            "POST",
            _make_path("_nodes", node_id, "reload_secure_settings"),
            params=params,
            headers=headers,
            body=body,
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
    async def info(
        self,
        node_id: Any = None,
        metric: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about nodes in the cluster.


        :arg node_id: Comma-separated list of node IDs or names used to
            limit returned information.
        :arg metric: Limits the information returned to the specific
            metrics. Supports a comma-separated list, such as http,ingest.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg flat_settings: If true, returns settings in flat format.
            Default is false.
        :arg human: Whether to return human readable values for
            statistics.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response. If no response is
            received before the timeout expires, the request fails and returns an
            error.
        """
        return await self.transport.perform_request(
            "GET", _make_path("_nodes", node_id, metric), params=params, headers=headers
        )

    @query_params(
        "completion_fields",
        "error_trace",
        "fielddata_fields",
        "fields",
        "filter_path",
        "groups",
        "human",
        "include_segment_file_sizes",
        "level",
        "pretty",
        "source",
        "timeout",
        "types",
    )
    async def stats(
        self,
        node_id: Any = None,
        metric: Any = None,
        index_metric: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns statistical information about nodes in the cluster.


        :arg node_id: Comma-separated list of node IDs or names used to
            limit returned information.
        :arg metric: Limit the information returned to the specified
            metrics
        :arg index_metric: Limit the information returned for indices
            metric to the specific index metrics. It can be used only if indices (or
            all) metric is specified.
        :arg completion_fields: Comma-separated list or wildcard
            expressions of fields to include in fielddata and suggest statistics.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg fielddata_fields: Comma-separated list or wildcard
            expressions of fields to include in fielddata statistics.
        :arg fields: Comma-separated list or wildcard expressions of
            fields to include in the statistics.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg groups: Comma-separated list of search groups to include in
            the search statistics.
        :arg human: Whether to return human readable values for
            statistics.
        :arg include_segment_file_sizes: If true, the call reports the
            aggregated disk usage of each one of the Lucene index files (only
            applies if segment stats are requested). Default is false.
        :arg level: Indicates whether statistics are aggregated at the
            cluster, index, or shard level. Valid choices are cluster, indices,
            shards.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response. If no response is
            received before the timeout expires, the request fails and returns an
            error.
        :arg types: A comma-separated list of document types for the
            indexing index metric.
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "stats", metric, index_metric),
            params=params,
            headers=headers,
        )

    @query_params(
        "doc_type",
        "error_trace",
        "filter_path",
        "human",
        "ignore_idle_threads",
        "interval",
        "pretty",
        "snapshots",
        "source",
        "threads",
        "timeout",
    )
    async def hot_threads(
        self,
        node_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about hot threads on each node in the cluster.


        :arg node_id: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg doc_type: The type to sample. Valid choices are cpu, wait,
            block.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg ignore_idle_threads: Don't show threads that are in known-
            idle places, such as waiting on a socket select or pulling from an empty
            task queue. Default is True.
        :arg interval: The interval for the second sampling of threads.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg snapshots: Number of samples of thread stacktrace. Default
            is 10.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg threads: Specify the number of threads to provide
            information for. Default is 3.
        :arg timeout: Operation timeout.
        """
        # type is a reserved word so it cannot be used, use doc_type instead
        if "doc_type" in params:
            params["type"] = params.pop("doc_type")

        return await self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "hot_threads"),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source", "timeout")
    async def usage(
        self,
        node_id: Any = None,
        metric: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns low-level information about REST actions usage on nodes.


        :arg node_id: A comma-separated list of node IDs or names to
            limit the returned information; use `_local` to return information from
            the node you're connecting to, leave empty to get information from all
            nodes
        :arg metric: Limits the information returned to the specific
            metrics. A comma-separated list of the following options: `_all`,
            `rest_actions`.
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
        :arg timeout: Period to wait for a response.If no response is
            received before the timeout expires, the request fails and returns an
            error.
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_nodes", node_id, "usage", metric),
            params=params,
            headers=headers,
        )
