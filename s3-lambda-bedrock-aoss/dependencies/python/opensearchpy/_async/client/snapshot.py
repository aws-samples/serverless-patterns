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
    @query_params("cluster_manager_timeout", "master_timeout", "wait_for_completion")
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


        :arg repository: Repository name.
        :arg snapshot: Snapshot name.
        :arg body: The snapshot definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is false.
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

    @query_params("cluster_manager_timeout", "master_timeout")
    async def delete(
        self,
        repository: Any,
        snapshot: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a snapshot.


        :arg repository: Repository name.
        :arg snapshot: Snapshot name.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
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
        "cluster_manager_timeout", "ignore_unavailable", "master_timeout", "verbose"
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


        :arg repository: Repository name.
        :arg snapshot: Comma-separated list of snapshot names.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg ignore_unavailable: Whether to ignore unavailable
            snapshots, defaults to false which means a SnapshotMissingException is
            thrown. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg verbose: Whether to show verbose snapshot info or only show
            the basic info found in the repository index blob.
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

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
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
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_snapshot", repository),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "local", "master_timeout")
    async def get_repository(
        self,
        repository: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about a repository.


        :arg repository: Comma-separated list of repository names.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return await self.transport.perform_request(
            "GET", _make_path("_snapshot", repository), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout", "verify")
    async def create_repository(
        self,
        repository: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates a repository.


        :arg repository: Repository name.
        :arg body: The repository definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        :arg verify: Whether to verify the repository after creation.
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

    @query_params("cluster_manager_timeout", "master_timeout", "wait_for_completion")
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


        :arg repository: Repository name.
        :arg snapshot: Snapshot name.
        :arg body: Details of what to restore
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is false.
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

    @query_params("cluster_manager_timeout", "ignore_unavailable", "master_timeout")
    async def status(
        self,
        repository: Any = None,
        snapshot: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about the status of a snapshot.


        :arg repository: Repository name.
        :arg snapshot: Comma-separated list of snapshot names.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg ignore_unavailable: Whether to ignore unavailable
            snapshots, defaults to false which means a SnapshotMissingException is
            thrown. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_snapshot", repository, snapshot, "_status"),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def verify_repository(
        self,
        repository: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Verifies a repository.


        :arg repository: Repository name.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, "_verify"),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    async def cleanup_repository(
        self,
        repository: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Removes stale data from repository.


        :arg repository: Repository name.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if repository in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'repository'.")

        return await self.transport.perform_request(
            "POST",
            _make_path("_snapshot", repository, "_cleanup"),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "master_timeout")
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


        :arg repository: Repository name.
        :arg snapshot: Snapshot name.
        :arg target_snapshot: The name of the cloned snapshot to create.
        :arg body: The snapshot clone definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
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
