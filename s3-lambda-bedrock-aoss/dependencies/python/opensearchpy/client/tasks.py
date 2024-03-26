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
        "group_by",
        "nodes",
        "parent_task_id",
        "timeout",
        "wait_for_completion",
    )
    def list(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a list of tasks.


        :arg actions: Comma-separated list of actions that should be
            returned. Leave empty to return all.
        :arg detailed: Return detailed task information. Default is
            false.
        :arg group_by: Group tasks by nodes or parent/child
            relationships. Valid choices are nodes, parents, none.
        :arg nodes: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg parent_task_id: Return tasks with specified parent task id
            (node_id:task_number). Set to -1 to return all.
        :arg timeout: Operation timeout.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is false.
        """
        return self.transport.perform_request(
            "GET", "/_tasks", params=params, headers=headers
        )

    @query_params("actions", "nodes", "parent_task_id", "wait_for_completion")
    def cancel(
        self,
        task_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Cancels a task, if it can be cancelled through an API.


        :arg task_id: Cancel the task with specified task id
            (node_id:task_number).
        :arg actions: Comma-separated list of actions that should be
            cancelled. Leave empty to cancel all.
        :arg nodes: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg parent_task_id: Cancel tasks with specified parent task id
            (node_id:task_number). Set to -1 to cancel all.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is false.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_tasks", task_id, "_cancel"),
            params=params,
            headers=headers,
        )

    @query_params("timeout", "wait_for_completion")
    def get(
        self,
        task_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about a task.


        :arg task_id: Return the task with specified id
            (node_id:task_number).
        :arg timeout: Operation timeout.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is false.
        """
        if task_id in SKIP_IN_PATH:
            warnings.warn(
                "Calling client.tasks.get() without a task_id is deprecated "
                "and will be removed in v8.0. Use client.tasks.list() instead.",
                category=DeprecationWarning,
                stacklevel=3,
            )

        return self.transport.perform_request(
            "GET", _make_path("_tasks", task_id), params=params, headers=headers
        )
