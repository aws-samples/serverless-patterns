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
        "expand_wildcards",
        "level",
        "local",
        "master_timeout",
        "timeout",
        "wait_for_active_shards",
        "wait_for_events",
        "wait_for_no_initializing_shards",
        "wait_for_no_relocating_shards",
        "wait_for_nodes",
        "wait_for_status",
    )
    def health(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns basic information about the health of the cluster.


        :arg index: Limit the information returned to specific indicies.
        :arg awareness_attribute: The awareness attribute for which the
            health is required.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg level: Specify the level of detail for returned
            information. Valid choices are cluster, indices, shards,
            awareness_attributes.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Wait until the specified number of
            shards is active.
        :arg wait_for_events: Wait until all currently queued events
            with the given priority are processed. Valid choices are immediate,
            urgent, high, normal, low, languid.
        :arg wait_for_no_initializing_shards: Whether to wait until
            there are no initializing shards in the cluster.
        :arg wait_for_no_relocating_shards: Whether to wait until there
            are no relocating shards in the cluster.
        :arg wait_for_nodes: Wait until the specified number of nodes is
            available.
        :arg wait_for_status: Wait until cluster is in a specific state.
            Valid choices are green, yellow, red.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_cluster", "health", index),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "local", "master_timeout")
    def pending_tasks(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a list of any cluster-level changes (e.g. create index, update mapping,
        allocate or fail shard) which have not yet been executed.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return self.transport.perform_request(
            "GET", "/_cluster/pending_tasks", params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "cluster_manager_timeout",
        "expand_wildcards",
        "flat_settings",
        "ignore_unavailable",
        "local",
        "master_timeout",
        "wait_for_metadata_version",
        "wait_for_timeout",
    )
    def state(
        self,
        metric: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a comprehensive information about the state of the cluster.


        :arg metric: Limit the information returned to the specified
            metrics. Valid choices are _all, blocks, metadata, nodes, routing_table,
            routing_nodes, master_node, cluster_manager_node, version.
        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg wait_for_metadata_version: Wait for the metadata version to
            be equal or greater than the specified metadata version.
        :arg wait_for_timeout: The maximum time to wait for
            wait_for_metadata_version before timing out.
        """
        if index and metric in SKIP_IN_PATH:
            metric = "_all"

        return self.transport.perform_request(
            "GET",
            _make_path("_cluster", "state", metric, index),
            params=params,
            headers=headers,
        )

    @query_params("flat_settings", "timeout")
    def stats(
        self,
        node_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns high-level overview of cluster statistics.


        :arg node_id: Comma-separated list of node IDs or names to limit
            the returned information; use `_local` to return information from the
            node you're connecting to, leave empty to get information from all
            nodes.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg timeout: Operation timeout.
        """
        return self.transport.perform_request(
            "GET",
            "/_cluster/stats"
            if node_id in SKIP_IN_PATH
            else _make_path("_cluster", "stats", "nodes", node_id),
            params=params,
            headers=headers,
        )

    @query_params(
        "cluster_manager_timeout",
        "dry_run",
        "explain",
        "master_timeout",
        "metric",
        "retry_failed",
        "timeout",
    )
    def reroute(
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
        :arg dry_run: Simulate the operation only and return the
            resulting state.
        :arg explain: Return an explanation of why the commands can or
            cannot be executed.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg metric: Limit the information returned to the specified
            metrics. Defaults to all but metadata.
        :arg retry_failed: Retries allocation of shards that are blocked
            due to too many subsequent allocation failures.
        :arg timeout: Operation timeout.
        """
        return self.transport.perform_request(
            "POST", "/_cluster/reroute", params=params, headers=headers, body=body
        )

    @query_params(
        "cluster_manager_timeout",
        "flat_settings",
        "include_defaults",
        "master_timeout",
        "timeout",
    )
    def get_settings(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns cluster settings.


        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg include_defaults: Whether to return all default clusters
            setting. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        return self.transport.perform_request(
            "GET", "/_cluster/settings", params=params, headers=headers
        )

    @query_params(
        "cluster_manager_timeout", "flat_settings", "master_timeout", "timeout"
    )
    def put_settings(
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
        :arg flat_settings: Return settings in flat format. Default is
            false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PUT", "/_cluster/settings", params=params, headers=headers, body=body
        )

    @query_params()
    def remote_info(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns the information about configured remote clusters.

        """
        return self.transport.perform_request(
            "GET", "/_remote/info", params=params, headers=headers
        )

    @query_params("include_disk_info", "include_yes_decisions")
    def allocation_explain(
        self,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Provides explanations for shard allocations in the cluster.


        :arg body: The index, shard, and primary flag to explain. Empty
            means 'explain the first unassigned shard'
        :arg include_disk_info: Return information about disk usage and
            shard sizes. Default is false.
        :arg include_yes_decisions: Return 'YES' decisions in
            explanation. Default is false.
        """
        return self.transport.perform_request(
            "POST",
            "/_cluster/allocation/explain",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    def delete_component_template(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a component template.


        :arg name: The name of the template.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_component_template", name),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "local", "master_timeout")
    def get_component_template(
        self,
        name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns one or more component templates.


        :arg name: The Comma-separated names of the component templates.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_component_template", name),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "create", "master_timeout", "timeout")
    def put_component_template(
        self,
        name: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates a component template.


        :arg name: The name of the template.
        :arg body: The template definition
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg create: Whether the index template should only be added if
            new or can also replace an existing one. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        for param in (name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_component_template", name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("cluster_manager_timeout", "local", "master_timeout")
    def exists_component_template(
        self,
        name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about whether a particular component template exist.


        :arg name: The name of the template.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'name'.")

        return self.transport.perform_request(
            "HEAD",
            _make_path("_component_template", name),
            params=params,
            headers=headers,
        )

    @query_params("wait_for_removal")
    def delete_voting_config_exclusions(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Clears cluster voting config exclusions.


        :arg wait_for_removal: Specifies whether to wait for all
            excluded nodes to be removed from the cluster before clearing the voting
            configuration exclusions list. Default is True.
        """
        return self.transport.perform_request(
            "DELETE",
            "/_cluster/voting_config_exclusions",
            params=params,
            headers=headers,
        )

    @query_params("node_ids", "node_names", "timeout")
    def post_voting_config_exclusions(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates the cluster voting config exclusions by node ids or node names.


        :arg node_ids: Comma-separated list of the persistent ids of the
            nodes to exclude from the voting configuration. If specified, you may
            not also specify ?node_names.
        :arg node_names: Comma-separated list of the names of the nodes
            to exclude from the voting configuration. If specified, you may not also
            specify ?node_ids.
        :arg timeout: Operation timeout.
        """
        return self.transport.perform_request(
            "POST", "/_cluster/voting_config_exclusions", params=params, headers=headers
        )

    @query_params()
    def delete_decommission_awareness(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete any existing decommission.

        """
        return self.transport.perform_request(
            "DELETE", "/_cluster/decommission/awareness", params=params, headers=headers
        )

    @query_params()
    def delete_weighted_routing(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete weighted shard routing weights.

        """
        return self.transport.perform_request(
            "DELETE",
            "/_cluster/routing/awareness/weights",
            params=params,
            headers=headers,
        )

    @query_params()
    def get_decommission_awareness(
        self,
        awareness_attribute_name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Get details and status of decommissioned attribute.


        :arg awareness_attribute_name: Awareness attribute name.
        """
        if awareness_attribute_name in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'awareness_attribute_name'."
            )

        return self.transport.perform_request(
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

    @query_params()
    def get_weighted_routing(
        self,
        attribute: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Fetches weighted shard routing weights.


        :arg attribute: Awareness attribute name.
        """
        if attribute in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'attribute'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_cluster", "routing", "awareness", attribute, "weights"),
            params=params,
            headers=headers,
        )

    @query_params()
    def put_decommission_awareness(
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
        """
        for param in (awareness_attribute_name, awareness_attribute_value):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
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

    @query_params()
    def put_weighted_routing(
        self,
        attribute: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates weighted shard routing weights.


        :arg attribute: Awareness attribute name.
        """
        if attribute in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'attribute'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_cluster", "routing", "awareness", attribute, "weights"),
            params=params,
            headers=headers,
        )
