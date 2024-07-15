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


class SnapshotClient(NamespacedClient):
    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "master_timeout",
        "pretty",
        "source",
        "wait_for_completion",
    )
    async def create(
        self,
        repository: Any,
        snapshot: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates a snapshot in a repository.


        :arg repository: Repository for the snapshot.
        :arg snapshot: Name of the snapshot. Must be unique in the
            repository.
        :arg body: The snapshot definition
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
        :arg wait_for_completion: If `true`, the request returns a
            response when the snapshot is complete. If `false`, the request returns
            a response when the snapshot initializes. Default is false.
        """
        for param in (repository, snapshot):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_snapshot", repository, snapshot),
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
    )
    async def delete(
        self,
        repository: Any,
        snapshot: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a snapshot.


        :arg repository: A repository name
        :arg snapshot: A comma-separated list of snapshot names
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Explicit operation timeout for
            connection to master node
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        for param in (repository, snapshot):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_snapshot", repository, snapshot),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "ignore_unavailable",
        "master_timeout",
        "pretty",
        "source",
        "verbose",
    )
    async def get(
        self,
        repository: Any,
        snapshot: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about a snapshot.


        :arg repository: Comma-separated list of snapshot repository
            names used to limit the request. Wildcard (*) expressions are supported.
        :arg snapshot: Comma-separated list of snapshot names to
            retrieve. Also accepts wildcards (*). - To get information about all
            snapshots in a registered repository, use a wildcard (*) or _all. - To
            get information about any snapshots that are currently running, use
            _current.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg ignore_unavailable: If false, the request returns an error
            for any snapshots that are unavailable. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Period to wait for a connection
            to the master node. If no response is received before the timeout
            expires, the request fails and returns an error.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg verbose: If true, returns additional information about each
            snapshot such as the version of Opensearch which took the snapshot, the
            start and end times of the snapshot, and the number of shards
            snapshotted.
        """
        for param in (repository, snapshot):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "GET",
            _make_path("_snapshot", repository, snapshot),
            params=params,
            headers=headers,
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
    async def delete_repository(
        self,
        repository: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a repository.


        :arg repository: Name of the snapshot repository to unregister.
            Wildcard (`*`) patterns are supported.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
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
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_snapshot", repository),
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
    async def get_repository(
        self,
        repository: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about a repository.


        :arg repository: A comma-separated list of repository names
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Explicit operation timeout for
            connection to master node
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return await self.transport.perform_request(
            "GET", _make_path("_snapshot", repository), params=params, headers=headers
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
        "verify",
    )
    async def create_repository(
        self,
        repository: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates a repository.


        :arg repository: A repository name
        :arg body: The repository definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
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
        :arg verify: Whether to verify the repository after creation
        """
        for param in (repository, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_snapshot", repository),
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
        "wait_for_completion",
    )
    async def restore(
        self,
        repository: Any,
        snapshot: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Restores a snapshot.


        :arg repository: A repository name
        :arg snapshot: A snapshot name
        :arg body: Details of what to restore
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Explicit operation timeout for
            connection to master node
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning Default is false.
        """
        for param in (repository, snapshot):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, snapshot, "_restore"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "ignore_unavailable",
        "master_timeout",
        "pretty",
        "source",
    )
    async def status(
        self,
        repository: Any = None,
        snapshot: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about the status of a snapshot.


        :arg repository: A repository name
        :arg snapshot: A comma-separated list of snapshot names
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg ignore_unavailable: Whether to ignore unavailable
            snapshots, defaults to false which means a SnapshotMissingException is
            thrown Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Explicit operation timeout for
            connection to master node
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_snapshot", repository, snapshot, "_status"),
            params=params,
            headers=headers,
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
    async def verify_repository(
        self,
        repository: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Verifies a repository.


        :arg repository: A repository name
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
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
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, "_verify"),
            params=params,
            headers=headers,
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
    async def cleanup_repository(
        self,
        repository: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Removes stale data from repository.


        :arg repository: Snapshot repository to clean up.
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
            to the master node.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        :arg timeout: Period to wait for a response.
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, "_cleanup"),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "error_trace",
        "filter_path",
        "human",
        "master_timeout",
        "pretty",
        "source",
    )
    async def clone(
        self,
        repository: Any,
        snapshot: Any,
        target_snapshot: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Clones indices from one snapshot into another snapshot in the same repository.


        :arg repository: A repository name
        :arg snapshot: The name of the snapshot to clone from
        :arg target_snapshot: The name of the cloned snapshot to create
        :arg body: The snapshot clone definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Explicit operation timeout for
            connection to master node
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        for param in (repository, snapshot, target_snapshot, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_snapshot", repository, snapshot, "_clone", target_snapshot),
            params=params,
            headers=headers,
            body=body,
        )
