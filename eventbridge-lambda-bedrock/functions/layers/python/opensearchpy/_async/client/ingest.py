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


class IngestClient(NamespacedClient):
    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "master_timeout",
        "pretty",
        "source",
    )
    async def get_pipeline(
        self,
        id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a pipeline.


        :arg id: Comma-separated list of pipeline IDs to retrieve.
            Wildcard (`*`) expressions are supported. To get all ingest pipelines,
            omit this parameter or use `*`.
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
        """
        return await self.transport.perform_request(
            "GET", _make_path("_ingest", "pipeline", id), params=params, headers=headers
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
    async def put_pipeline(
        self,
        id: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates a pipeline.


        :arg id: ID of the ingest pipeline to create or update.
        :arg body: The ingest definition
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
            to the master node. If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response. If no response is
            received before the timeout expires, the request fails and returns an
            error.
        """
        for param in (id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_ingest", "pipeline", id),
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
    async def delete_pipeline(
        self,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a pipeline.


        :arg id: Pipeline ID or wildcard expression of pipeline IDs used
            to limit the request. To delete all ingest pipelines in a cluster, use a
            value of `*`.
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
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_ingest", "pipeline", id),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source", "verbose")
    async def simulate(
        self,
        body: Any,
        id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to simulate a pipeline with example documents.


        :arg body: The simulate definition
        :arg id: Pipeline to test. If you don’t specify a `pipeline` in
            the request body, this parameter is required.
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
        :arg verbose: If `true`, the response includes output data for
            each processor in the executed pipeline. Default is false.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_ingest", "pipeline", id, "_simulate"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    async def processor_grok(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a list of the built-in patterns.


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
            "GET", "/_ingest/processor/grok", params=params, headers=headers
        )
