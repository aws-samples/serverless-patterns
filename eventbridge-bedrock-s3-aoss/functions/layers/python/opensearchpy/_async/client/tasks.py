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


import warnings
from typing import Any

from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class TasksClient(NamespacedClient):
    @query_params(
        "actions",
        "detailed",
        "error_trace",
        "filter_path",
        "group_by",
        "human",
        "nodes",
        "parent_task_id",
        "pretty",
        "source",
        "timeout",
        "wait_for_completion",
    )
    async def list(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a list of tasks.


        :arg actions: Comma-separated list or wildcard expression of
            actions used to limit the request.
        :arg detailed: If `true`, the response includes detailed
            information about shard recoveries. Default is false.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg group_by: Key used to group tasks in the response. Valid
            choices are nodes, parents, none.
        :arg human: Whether to return human readable values for
            statistics.
        :arg nodes: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg parent_task_id: Parent task ID used to limit returned
            information. To return all tasks, omit this parameter or use a value of
            `-1`.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response. If no response is
            received before the timeout expires, the request fails and returns an
            error.
        :arg wait_for_completion: If `true`, the request blocks until
            the operation is complete. Default is false.
        """
        return await self.transport.perform_request(
            "GET", "/_tasks", params=params, headers=headers
        )

    @query_params(
        "actions",
        "error_trace",
        "filter_path",
        "human",
        "nodes",
        "parent_task_id",
        "pretty",
        "source",
        "wait_for_completion",
    )
    async def cancel(
        self,
        task_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Cancels a task, if it can be cancelled through an API.


        :arg task_id: ID of the task.
        :arg actions: Comma-separated list or wildcard expression of
            actions used to limit the request.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg nodes: Comma-separated list of node IDs or names used to
            limit the request.
        :arg parent_task_id: Parent task ID used to limit the tasks.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg wait_for_completion: Should the request block until the
            cancellation of the task and its descendant tasks is completed. Defaults
            to false Default is false.
        """
        return await self.transport.perform_request(
            "POST",
            _make_path("_tasks", task_id, "_cancel"),
            params=params,
            headers=headers,
        )

    @query_params(
        "error_trace",
        "filter_path",
        "human",
        "pretty",
        "source",
        "timeout",
        "wait_for_completion",
    )
    async def get(
        self,
        task_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about a task.


        :arg task_id: ID of the task.
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
        :arg wait_for_completion: If `true`, the request blocks until
            the task has completed. Default is false.
        """
        if task_id in SKIP_IN_PATH:
            warnings.warn(
                "Calling client.tasks.get() without a task_id is deprecated "
                "and will be removed in v8.0. Use client.tasks.list() instead.",
                category=DeprecationWarning,
                stacklevel=3,
            )

        return await self.transport.perform_request(
            "GET", _make_path("_tasks", task_id), params=params, headers=headers
        )
