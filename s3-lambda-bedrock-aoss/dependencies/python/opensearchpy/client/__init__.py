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


from __future__ import unicode_literals

import logging
from typing import Any, Type

from ..transport import Transport, TransportError
from .cat import CatClient
from .client import Client
from .cluster import ClusterClient
from .dangling_indices import DanglingIndicesClient
from .features import FeaturesClient
from .http import HttpClient
from .indices import IndicesClient
from .ingest import IngestClient
from .nodes import NodesClient
from .plugins import PluginsClient
from .remote import RemoteClient
from .remote_store import RemoteStoreClient
from .security import SecurityClient
from .snapshot import SnapshotClient
from .tasks import TasksClient
from .utils import SKIP_IN_PATH, _bulk_body, _make_path, query_params

logger = logging.getLogger("opensearch")


class OpenSearch(Client):
    """
    OpenSearch client. Provides a straightforward mapping from
    Python to OpenSearch REST endpoints.

    The instance has attributes ``cat``, ``cluster``, ``indices``, ``ingest``,
    ``nodes``, ``snapshot`` and ``tasks`` that provide access to instances of
    :class:`~opensearchpy.client.CatClient`,
    :class:`~opensearchpy.client.ClusterClient`,
    :class:`~opensearchpy.client.IndicesClient`,
    :class:`~opensearchpy.client.IngestClient`,
    :class:`~opensearchpy.client.NodesClient`,
    :class:`~opensearchpy.client.SnapshotClient` and
    :class:`~opensearchpy.client.TasksClient` respectively. This is the
    preferred (and only supported) way to get access to those classes and their
    methods.

    You can specify your own connection class which should be used by providing
    the ``connection_class`` parameter::

        # create connection to localhost using the ThriftConnection
        client = OpenSearch(connection_class=ThriftConnection)

    If you want to turn on sniffing you have several options (described
    in :class:`~opensearchpy.Transport`)::

        # create connection that will automatically inspect the cluster to get
        # the list of active nodes. Start with nodes running on
        # 'opensearchnode1' and 'opensearchnode2'
        client = OpenSearch(
            ['opensearchnode1', 'opensearchnode2'],
            # sniff before doing anything
            sniff_on_start=True,
            # refresh nodes after a node fails to respond
            sniff_on_connection_fail=True,
            # and also every 60 seconds
            sniffer_timeout=60
        )

    Different hosts can have different parameters, use a dictionary per node to
    specify those::

        # connect to localhost directly and another node using SSL on port 443
        # and an url_prefix. Note that ``port`` needs to be an int.
        client = OpenSearch([
            {'host': 'localhost'},
            {'host': 'othernode', 'port': 443, 'url_prefix': 'opensearch', 'use_ssl': True},
        ])

    If using SSL, there are several parameters that control how we deal with
    certificates (see :class:`~opensearchpy.Urllib3HttpConnection` for
    detailed description of the options)::

        client = OpenSearch(
            ['localhost:443', 'other_host:443'],
            # turn on SSL
            use_ssl=True,
            # make sure we verify SSL certificates
            verify_certs=True,
            # provide a path to CA certs on disk
            ca_certs='/path/to/CA_certs'
        )

    If using SSL, but don't verify the certs, a warning message is showed
    optionally (see :class:`~opensearchpy.Urllib3HttpConnection` for
    detailed description of the options)::

        client = OpenSearch(
            ['localhost:443', 'other_host:443'],
            # turn on SSL
            use_ssl=True,
            # no verify SSL certificates
            verify_certs=False,
            # don't show warnings about ssl certs verification
            ssl_show_warn=False
        )

    SSL client authentication is supported
    (see :class:`~opensearchpy.Urllib3HttpConnection` for
    detailed description of the options)::

        client = OpenSearch(
            ['localhost:443', 'other_host:443'],
            # turn on SSL
            use_ssl=True,
            # make sure we verify SSL certificates
            verify_certs=True,
            # provide a path to CA certs on disk
            ca_certs='/path/to/CA_certs',
            # PEM formatted SSL client certificate
            client_cert='/path/to/clientcert.pem',
            # PEM formatted SSL client key
            client_key='/path/to/clientkey.pem'
        )

    Alternatively you can use RFC-1738 formatted URLs, as long as they are not
    in conflict with other options::

        client = OpenSearch(
            [
                'http://user:secret@localhost:9200/',
                'https://user:secret@other_host:443/production'
            ],
            verify_certs=True
        )

    By default, `JSONSerializer
    <https://github.com/opensearch-project/opensearch-py/blob/master/opensearch/serializer.py#L24>`_
    is used to encode all outgoing requests.
    However, you can implement your own custom serializer::

        from opensearchpy.serializer import JSONSerializer

        class SetEncoder(JSONSerializer):
            def default(self, obj):
                if isinstance(obj, set):
                    return list(obj)
                if isinstance(obj, Something):
                    return 'CustomSomethingRepresentation'
                return JSONSerializer.default(self, obj)

        client = OpenSearch(serializer=SetEncoder())

    """

    # include PIT functions inside _patch.py
    from ._patch import (  # type: ignore
        create_point_in_time,
        delete_point_in_time,
        list_all_point_in_time,
    )

    def __init__(
        self,
        hosts: Any = None,
        transport_class: Type[Transport] = Transport,
        **kwargs: Any
    ) -> None:
        """
        :arg hosts: list of nodes, or a single node, we should connect to.
            Node should be a dictionary ({"host": "localhost", "port": 9200}),
            the entire dictionary will be passed to the :class:`~opensearchpy.Connection`
            class as kwargs, or a string in the format of ``host[:port]`` which will be
            translated to a dictionary automatically.  If no value is given the
            :class:`~opensearchpy.Connection` class defaults will be used.

        :arg transport_class: :class:`~opensearchpy.Transport` subclass to use.

        :arg kwargs: any additional arguments will be passed on to the
            :class:`~opensearchpy.Transport` class and, subsequently, to the
            :class:`~opensearchpy.Connection` instances.
        """
        super().__init__(hosts, transport_class, **kwargs)

        # namespaced clients for compatibility with API names
        self.cat = CatClient(self)
        self.cluster = ClusterClient(self)
        self.dangling_indices = DanglingIndicesClient(self)
        self.indices = IndicesClient(self)
        self.ingest = IngestClient(self)
        self.nodes = NodesClient(self)
        self.remote = RemoteClient(self)
        self.security = SecurityClient(self)
        self.snapshot = SnapshotClient(self)
        self.tasks = TasksClient(self)
        self.remote_store = RemoteStoreClient(self)

        self.features = FeaturesClient(self)
        self.plugins = PluginsClient(self)
        self.http = HttpClient(self)

    def __repr__(self) -> Any:
        try:
            # get a list of all connections
            cons: Any = self.transport.hosts
            # truncate to 5 if there are too many
            if len(cons) > 5:
                cons = cons[:5] + ["..."]
            return "<{cls}({cons})>".format(cls=self.__class__.__name__, cons=cons)
        except Exception:
            # probably operating on custom transport and connection_pool, ignore
            return super(OpenSearch, self).__repr__()

    def __enter__(self) -> Any:
        if hasattr(self.transport, "_async_call"):
            self.transport._async_call()
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def close(self) -> None:
        """Closes the Transport and all internal connections"""
        self.transport.close()

    # AUTO-GENERATED-API-DEFINITIONS #
    @query_params()
    def ping(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns whether the cluster is running.

        """
        try:
            return self.transport.perform_request(
                "HEAD", "/", params=params, headers=headers
            )
        except TransportError:
            return False

    @query_params()
    def info(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns basic information about the cluster.

        """
        return self.transport.perform_request(
            "GET", "/", params=params, headers=headers
        )

    @query_params(
        "pipeline",
        "refresh",
        "routing",
        "timeout",
        "version",
        "version_type",
        "wait_for_active_shards",
    )
    def create(
        self,
        index: Any,
        id: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates a new document in the index.  Returns a 409 response when a document
        with a same ID already exists in the index.


        :arg index: Index name.
        :arg id: Document ID.
        :arg body: The document
        :arg pipeline: The pipeline id to preprocess incoming documents
            with.
        :arg refresh: If `true` then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh
            to make this operation visible to search, if `false` (the default) then
            do nothing with refreshes. Valid choices are true, false, wait_for.
        :arg routing: Routing value.
        :arg timeout: Operation timeout.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before proceeding with the operation. Defaults to 1,
            meaning the primary shard only. Set to `all` for all shard copies,
            otherwise set to any non-negative value less than or equal to the total
            number of copies for the shard (number of replicas + 1). Default is 1.
        """
        for param in (index, id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        path = _make_path(index, "_create", id)

        return self.transport.perform_request(
            "PUT", path, params=params, headers=headers, body=body
        )

    @query_params(
        "if_primary_term",
        "if_seq_no",
        "op_type",
        "pipeline",
        "refresh",
        "require_alias",
        "routing",
        "timeout",
        "version",
        "version_type",
        "wait_for_active_shards",
    )
    def index(
        self,
        index: Any,
        body: Any,
        id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates a document in an index.


        :arg index: Index name.
        :arg body: The document
        :arg id: Document ID.
        :arg if_primary_term: only perform the operation if the last
            operation that has changed the document has the specified primary term.
        :arg if_seq_no: only perform the operation if the last operation
            that has changed the document has the specified sequence number.
        :arg op_type: Explicit operation type. Defaults to `index` for
            requests with an explicit document ID, and to `create` for requests
            without an explicit document ID. Valid choices are index, create.
        :arg pipeline: The pipeline id to preprocess incoming documents
            with.
        :arg refresh: If `true` then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh
            to make this operation visible to search, if `false` (the default) then
            do nothing with refreshes. Valid choices are true, false, wait_for.
        :arg require_alias: When true, requires destination to be an
            alias. Default is false.
        :arg routing: Routing value.
        :arg timeout: Operation timeout.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before proceeding with the operation. Defaults to 1,
            meaning the primary shard only. Set to `all` for all shard copies,
            otherwise set to any non-negative value less than or equal to the total
            number of copies for the shard (number of replicas + 1). Default is 1.
        """
        for param in (index, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "POST" if id in SKIP_IN_PATH else "PUT",
            _make_path(index, "_doc", id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "pipeline",
        "refresh",
        "require_alias",
        "routing",
        "timeout",
        "wait_for_active_shards",
    )
    def bulk(
        self,
        body: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to perform multiple index/update/delete operations in a single request.


        :arg body: The operation definition and data (action-data
            pairs), separated by newlines
        :arg index: Default index for items which don't provide one.
        :arg _source: True or false to return the _source field or not,
            or default list of fields to return, can be overridden on each sub-
            request.
        :arg _source_excludes: Default list of fields to exclude from
            the returned _source field, can be overridden on each sub-request.
        :arg _source_includes: Default list of fields to extract and
            return from the _source field, can be overridden on each sub-request.
        :arg pipeline: The pipeline id to preprocess incoming documents
            with.
        :arg refresh: If `true` then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh
            to make this operation visible to search, if `false` (the default) then
            do nothing with refreshes. Valid choices are true, false, wait_for.
        :arg require_alias: Sets require_alias for all incoming
            documents. Default is false.
        :arg routing: Routing value.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before proceeding with the operation. Defaults to 1,
            meaning the primary shard only. Set to `all` for all shard copies,
            otherwise set to any non-negative value less than or equal to the total
            number of copies for the shard (number of replicas + 1). Default is 1.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        body = _bulk_body(self.transport.serializer, body)
        return self.transport.perform_request(
            "POST",
            _make_path(index, "_bulk"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def clear_scroll(
        self,
        body: Any = None,
        scroll_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Explicitly clears the search context for a scroll.


        :arg body: Comma-separated list of scroll IDs to clear if none
            was specified via the scroll_id parameter
        :arg scroll_id: Comma-separated list of scroll IDs to clear.
        """
        if scroll_id in SKIP_IN_PATH and body in SKIP_IN_PATH:
            raise ValueError("You need to supply scroll_id or body.")
        elif scroll_id and not body:
            body = {"scroll_id": [scroll_id]}
        elif scroll_id:
            params["scroll_id"] = scroll_id

        return self.transport.perform_request(
            "DELETE", "/_search/scroll", params=params, headers=headers, body=body
        )

    @query_params(
        "allow_no_indices",
        "analyze_wildcard",
        "analyzer",
        "default_operator",
        "df",
        "expand_wildcards",
        "ignore_throttled",
        "ignore_unavailable",
        "lenient",
        "min_score",
        "preference",
        "q",
        "routing",
        "terminate_after",
    )
    def count(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns number of documents matching a query.


        :arg body: Query to restrict the results specified with the
            Query DSL (optional)
        :arg index: Comma-separated list of indices to restrict the
            results.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg analyze_wildcard: Specify whether wildcard and prefix
            queries should be analyzed. Default is false.
        :arg analyzer: The analyzer to use for the query string.
        :arg default_operator: The default operator for query string
            query (AND or OR). Valid choices are AND, OR.
        :arg df: The field to use as default where no field prefix is
            given in the query string.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_throttled: Whether specified concrete, expanded or
            aliased indices should be ignored when throttled.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg lenient: Specify whether format-based query failures (such
            as providing text to a numeric field) should be ignored.
        :arg min_score: Include only documents with a specific `_score`
            value in the result.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg q: Query in the Lucene query string syntax.
        :arg routing: Comma-separated list of specific routing values.
        :arg terminate_after: The maximum number of documents to collect
            for each shard, upon reaching which the query execution will terminate
            early.
        """
        return self.transport.perform_request(
            "POST",
            _make_path(index, "_count"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "if_primary_term",
        "if_seq_no",
        "refresh",
        "routing",
        "timeout",
        "version",
        "version_type",
        "wait_for_active_shards",
    )
    def delete(
        self,
        index: Any,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Removes a document from the index.


        :arg index: Index name.
        :arg id: Document ID.
        :arg if_primary_term: only perform the operation if the last
            operation that has changed the document has the specified primary term.
        :arg if_seq_no: only perform the operation if the last operation
            that has changed the document has the specified sequence number.
        :arg refresh: If `true` then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh
            to make this operation visible to search, if `false` (the default) then
            do nothing with refreshes. Valid choices are true, false, wait_for.
        :arg routing: Routing value.
        :arg timeout: Operation timeout.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before proceeding with the operation. Defaults to 1,
            meaning the primary shard only. Set to `all` for all shard copies,
            otherwise set to any non-negative value less than or equal to the total
            number of copies for the shard (number of replicas + 1). Default is 1.
        """
        for param in (index, id):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "DELETE", _make_path(index, "_doc", id), params=params, headers=headers
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "allow_no_indices",
        "analyze_wildcard",
        "analyzer",
        "conflicts",
        "default_operator",
        "df",
        "expand_wildcards",
        "from_",
        "ignore_unavailable",
        "lenient",
        "max_docs",
        "preference",
        "q",
        "refresh",
        "request_cache",
        "requests_per_second",
        "routing",
        "scroll",
        "scroll_size",
        "search_timeout",
        "search_type",
        "size",
        "slices",
        "sort",
        "stats",
        "terminate_after",
        "timeout",
        "version",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    def delete_by_query(
        self,
        index: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes documents matching the provided query.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg body: The search definition using the Query DSL
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg analyze_wildcard: Specify whether wildcard and prefix
            queries should be analyzed. Default is false.
        :arg analyzer: The analyzer to use for the query string.
        :arg conflicts: What to do when the operation encounters version
            conflicts?. Valid choices are abort, proceed.
        :arg default_operator: The default operator for query string
            query (AND or OR). Valid choices are AND, OR.
        :arg df: The field to use as default where no field prefix is
            given in the query string.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg from_: Starting offset. Default is 0.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg lenient: Specify whether format-based query failures (such
            as providing text to a numeric field) should be ignored.
        :arg max_docs: Maximum number of documents to process (default:
            all documents).
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg q: Query in the Lucene query string syntax.
        :arg refresh: Refresh the shard containing the document before
            performing the operation.
        :arg request_cache: Specify if request cache should be used for
            this request or not, defaults to index level setting.
        :arg requests_per_second: The throttle for this request in sub-
            requests per second. -1 means no throttle. Default is 0.
        :arg routing: Comma-separated list of specific routing values.
        :arg scroll: Specify how long a consistent view of the index
            should be maintained for scrolled search.
        :arg scroll_size: Size on the scroll request powering the
            operation. Default is 100.
        :arg search_timeout: Explicit timeout for each search request.
            Defaults to no timeout.
        :arg search_type: Search operation type. Valid choices are
            query_then_fetch, dfs_query_then_fetch.
        :arg size: Deprecated, please use `max_docs` instead.
        :arg slices: The number of slices this task should be divided
            into. Defaults to 1, meaning the task isn't sliced into subtasks. Can be
            set to `auto`. Default is 1.
        :arg sort: Comma-separated list of <field>:<direction> pairs.
        :arg stats: Specific 'tag' of the request for logging and
            statistical purposes.
        :arg terminate_after: The maximum number of documents to collect
            for each shard, upon reaching which the query execution will terminate
            early.
        :arg timeout: Time each individual bulk request should wait for
            shards that are unavailable. Default is 1m.
        :arg version: Whether to return document version as part of a
            hit.
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before proceeding with the operation. Defaults to 1,
            meaning the primary shard only. Set to `all` for all shard copies,
            otherwise set to any non-negative value less than or equal to the total
            number of copies for the shard (number of replicas + 1). Default is 1.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is True.
        """
        # from is a reserved word so it cannot be used, use from_ instead
        if "from_" in params:
            params["from"] = params.pop("from_")

        for param in (index, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "POST",
            _make_path(index, "_delete_by_query"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("requests_per_second")
    def delete_by_query_rethrottle(
        self,
        task_id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Changes the number of requests per second for a particular Delete By Query
        operation.


        :arg task_id: The task id to rethrottle.
        :arg requests_per_second: The throttle for this request in sub-
            requests per second. -1 means no throttle.
        """
        if task_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'task_id'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_delete_by_query", task_id, "_rethrottle"),
            params=params,
            headers=headers,
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    def delete_script(
        self,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes a script.


        :arg id: Script ID.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "DELETE", _make_path("_scripts", id), params=params, headers=headers
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "stored_fields",
        "version",
        "version_type",
    )
    def exists(
        self,
        index: Any,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about whether a document exists in an index.


        :arg index: Index name.
        :arg id: Document ID.
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg realtime: Specify whether to perform the operation in
            realtime or search mode.
        :arg refresh: Refresh the shard containing the document before
            performing the operation.
        :arg routing: Routing value.
        :arg stored_fields: Comma-separated list of stored fields to
            return.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        """
        for param in (index, id):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "HEAD", _make_path(index, "_doc", id), params=params, headers=headers
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "version",
        "version_type",
    )
    def exists_source(
        self,
        index: Any,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about whether a document source exists in an index.


        :arg index: Index name.
        :arg id: Document ID.
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg realtime: Specify whether to perform the operation in
            realtime or search mode.
        :arg refresh: Refresh the shard containing the document before
            performing the operation.
        :arg routing: Routing value.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        """
        for param in (index, id):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        path = _make_path(index, "_source", id)

        return self.transport.perform_request(
            "HEAD", path, params=params, headers=headers
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "analyze_wildcard",
        "analyzer",
        "default_operator",
        "df",
        "lenient",
        "preference",
        "q",
        "routing",
        "stored_fields",
    )
    def explain(
        self,
        index: Any,
        id: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about why a specific matches (or doesn't match) a query.


        :arg index: Index name.
        :arg id: Document ID.
        :arg body: The query definition using the Query DSL
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg analyze_wildcard: Specify whether wildcards and prefix
            queries in the query string query should be analyzed. Default is false.
        :arg analyzer: The analyzer to use for the query string.
        :arg default_operator: The default operator for query string
            query (AND or OR). Valid choices are AND, OR.
        :arg df: The default field for query string query. Default is
            _all.
        :arg lenient: Specify whether format-based query failures (such
            as providing text to a numeric field) should be ignored.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg q: Query in the Lucene query string syntax.
        :arg routing: Routing value.
        :arg stored_fields: Comma-separated list of stored fields to
            return.
        """
        for param in (index, id):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        path = _make_path(index, "_explain", id)

        return self.transport.perform_request(
            "POST", path, params=params, headers=headers, body=body
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "fields",
        "ignore_unavailable",
        "include_unmapped",
    )
    def field_caps(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns the information about the capabilities of fields among multiple
        indices.


        :arg body: An index filter specified with the Query DSL
        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg fields: Comma-separated list of field names.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg include_unmapped: Indicates whether unmapped fields should
            be included in the response. Default is false.
        """
        return self.transport.perform_request(
            "POST",
            _make_path(index, "_field_caps"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "stored_fields",
        "version",
        "version_type",
    )
    def get(
        self,
        index: Any,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a document.


        :arg index: Index name.
        :arg id: Document ID.
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg realtime: Specify whether to perform the operation in
            realtime or search mode.
        :arg refresh: Refresh the shard containing the document before
            performing the operation.
        :arg routing: Routing value.
        :arg stored_fields: Comma-separated list of stored fields to
            return.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        """
        for param in (index, id):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "GET", _make_path(index, "_doc", id), params=params, headers=headers
        )

    @query_params("cluster_manager_timeout", "master_timeout")
    def get_script(
        self,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns a script.


        :arg id: Script ID.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "GET", _make_path("_scripts", id), params=params, headers=headers
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "version",
        "version_type",
    )
    def get_source(
        self,
        index: Any,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns the source of a document.


        :arg index: Index name.
        :arg id: Document ID.
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg realtime: Specify whether to perform the operation in
            realtime or search mode.
        :arg refresh: Refresh the shard containing the document before
            performing the operation.
        :arg routing: Routing value.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        """
        for param in (index, id):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        path = _make_path(index, "_source", id)

        return self.transport.perform_request(
            "GET", path, params=params, headers=headers
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "stored_fields",
    )
    def mget(
        self,
        body: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to get multiple documents in one request.


        :arg body: Document identifiers; can be either `docs`
            (containing full document information) or `ids` (when index is provided
            in the URL.
        :arg index: Index name.
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg realtime: Specify whether to perform the operation in
            realtime or search mode.
        :arg refresh: Refresh the shard containing the document before
            performing the operation.
        :arg routing: Routing value.
        :arg stored_fields: Comma-separated list of stored fields to
            return.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "POST",
            _make_path(index, "_mget"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "ccs_minimize_roundtrips",
        "max_concurrent_searches",
        "max_concurrent_shard_requests",
        "pre_filter_shard_size",
        "rest_total_hits_as_int",
        "search_type",
        "typed_keys",
    )
    def msearch(
        self,
        body: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to execute several search operations in one request.


        :arg body: The request definitions (metadata-search request
            definition pairs), separated by newlines
        :arg index: Comma-separated list of indices to use as default.
        :arg ccs_minimize_roundtrips: Indicates whether network round-
            trips should be minimized as part of cross-cluster search requests
            execution. Default is True.
        :arg max_concurrent_searches: Controls the maximum number of
            concurrent searches the multi search api will execute.
        :arg max_concurrent_shard_requests: The number of concurrent
            shard requests each sub search executes concurrently per node. This
            value should be used to limit the impact of the search on the cluster in
            order to limit the number of concurrent shard requests. Default is 5.
        :arg pre_filter_shard_size: Threshold that enforces a pre-filter
            round-trip to prefilter search shards based on query rewriting if the
            number of shards the search request expands to exceeds the threshold.
            This filter round-trip can limit the number of shards significantly if
            for instance a shard can not match any documents based on its rewrite
            method ie. if date filters are mandatory to match but the shard bounds
            and the query are disjoint.
        :arg rest_total_hits_as_int: Indicates whether hits.total should
            be rendered as an integer or an object in the rest search response.
            Default is false.
        :arg search_type: Search operation type. Valid choices are
            query_then_fetch, query_and_fetch, dfs_query_then_fetch,
            dfs_query_and_fetch.
        :arg typed_keys: Specify whether aggregation and suggester names
            should be prefixed by their respective types in the response.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        body = _bulk_body(self.transport.serializer, body)
        return self.transport.perform_request(
            "POST",
            _make_path(index, "_msearch"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "ccs_minimize_roundtrips",
        "max_concurrent_searches",
        "rest_total_hits_as_int",
        "search_type",
        "typed_keys",
    )
    def msearch_template(
        self,
        body: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to execute several search template operations in one request.


        :arg body: The request definitions (metadata-search request
            definition pairs), separated by newlines
        :arg index: Comma-separated list of indices to use as default.
        :arg ccs_minimize_roundtrips: Indicates whether network round-
            trips should be minimized as part of cross-cluster search requests
            execution. Default is True.
        :arg max_concurrent_searches: Controls the maximum number of
            concurrent searches the multi search api will execute.
        :arg rest_total_hits_as_int: Indicates whether hits.total should
            be rendered as an integer or an object in the rest search response.
            Default is false.
        :arg search_type: Search operation type. Valid choices are
            query_then_fetch, query_and_fetch, dfs_query_then_fetch,
            dfs_query_and_fetch.
        :arg typed_keys: Specify whether aggregation and suggester names
            should be prefixed by their respective types in the response.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        body = _bulk_body(self.transport.serializer, body)
        return self.transport.perform_request(
            "POST",
            _make_path(index, "_msearch", "template"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "field_statistics",
        "fields",
        "ids",
        "offsets",
        "payloads",
        "positions",
        "preference",
        "realtime",
        "routing",
        "term_statistics",
        "version",
        "version_type",
    )
    def mtermvectors(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns multiple termvectors in one request.


        :arg body: Define ids, documents, parameters or a list of
            parameters per document here. You must at least provide a list of
            document ids. See documentation.
        :arg index: The index in which the document resides.
        :arg field_statistics: Specifies if document count, sum of
            document frequencies and sum of total term frequencies should be
            returned. Applies to all returned documents unless otherwise specified
            in body 'params' or 'docs'. Default is True.
        :arg fields: Comma-separated list of fields to return. Applies
            to all returned documents unless otherwise specified in body 'params' or
            'docs'.
        :arg ids: Comma-separated list of documents ids. You must define
            ids as parameter or set 'ids' or 'docs' in the request body.
        :arg offsets: Specifies if term offsets should be returned.
            Applies to all returned documents unless otherwise specified in body
            'params' or 'docs'. Default is True.
        :arg payloads: Specifies if term payloads should be returned.
            Applies to all returned documents unless otherwise specified in body
            'params' or 'docs'. Default is True.
        :arg positions: Specifies if term positions should be returned.
            Applies to all returned documents unless otherwise specified in body
            'params' or 'docs'. Default is True.
        :arg preference: Specify the node or shard the operation should
            be performed on. Applies to all returned documents unless otherwise
            specified in body 'params' or 'docs'. Default is random.
        :arg realtime: Specifies if requests are real-time as opposed to
            near-real-time. Default is True.
        :arg routing: Routing value. Applies to all returned documents
            unless otherwise specified in body 'params' or 'docs'.
        :arg term_statistics: Specifies if total term frequency and
            document frequency should be returned. Applies to all returned documents
            unless otherwise specified in body 'params' or 'docs'. Default is false.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        """
        path = _make_path(index, "_mtermvectors")

        return self.transport.perform_request(
            "POST", path, params=params, headers=headers, body=body
        )

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    def put_script(
        self,
        id: Any,
        body: Any,
        context: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates a script.


        :arg id: Script ID.
        :arg body: The document
        :arg context: Script context.
        :arg cluster_manager_timeout: Operation timeout for connection
            to cluster-manager node.
        :arg master_timeout (Deprecated: To promote inclusive language,
            use 'cluster_manager_timeout' instead.): Operation timeout for
            connection to master node.
        :arg timeout: Operation timeout.
        """
        for param in (id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_scripts", id, context),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices", "expand_wildcards", "ignore_unavailable", "search_type"
    )
    def rank_eval(
        self,
        body: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to evaluate the quality of ranked search results over a set of typical
        search queries.


        :arg body: The ranking evaluation search definition, including
            search requests, document ratings and ranking metric definition.
        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg search_type: Search operation type. Valid choices are
            query_then_fetch, dfs_query_then_fetch.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "POST",
            _make_path(index, "_rank_eval"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "max_docs",
        "refresh",
        "requests_per_second",
        "scroll",
        "slices",
        "timeout",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    def reindex(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to copy documents from one index to another, optionally filtering the
        source documents by a query, changing the destination index settings, or
        fetching the documents from a remote cluster.


        :arg body: The search definition using the Query DSL and the
            prototype for the index request.
        :arg max_docs: Maximum number of documents to process (default:
            all documents).
        :arg refresh: Should the affected indexes be refreshed?.
        :arg requests_per_second: The throttle for this request in sub-
            requests per second. -1 means no throttle. Default is 0.
        :arg scroll: Specify how long a consistent view of the index
            should be maintained for scrolled search.
        :arg slices: The number of slices this task should be divided
            into. Defaults to 1, meaning the task isn't sliced into subtasks. Can be
            set to `auto`. Default is 1.
        :arg timeout: Time each individual bulk request should wait for
            shards that are unavailable. Default is 1m.
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before proceeding with the operation. Defaults to 1,
            meaning the primary shard only. Set to `all` for all shard copies,
            otherwise set to any non-negative value less than or equal to the total
            number of copies for the shard (number of replicas + 1). Default is 1.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is True.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "POST", "/_reindex", params=params, headers=headers, body=body
        )

    @query_params("requests_per_second")
    def reindex_rethrottle(
        self,
        task_id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Changes the number of requests per second for a particular Reindex operation.


        :arg task_id: The task id to rethrottle.
        :arg requests_per_second: The throttle for this request in sub-
            requests per second. -1 means no throttle.
        """
        if task_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'task_id'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_reindex", task_id, "_rethrottle"),
            params=params,
            headers=headers,
        )

    @query_params()
    def render_search_template(
        self,
        body: Any = None,
        id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to use the Mustache language to pre-render a search definition.


        :arg body: The search definition template and its params
        :arg id: The id of the stored search template.
        """
        return self.transport.perform_request(
            "POST",
            _make_path("_render", "template", id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def scripts_painless_execute(
        self,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows an arbitrary script to be executed and a result to be returned.


        :arg body: The script to execute
        """
        return self.transport.perform_request(
            "POST",
            "/_scripts/painless/_execute",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("rest_total_hits_as_int", "scroll")
    def scroll(
        self,
        body: Any = None,
        scroll_id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to retrieve a large numbers of results from a single search request.


        :arg body: The scroll ID if not passed by URL or query
            parameter.
        :arg scroll_id: Scroll ID.
        :arg rest_total_hits_as_int: Indicates whether hits.total should
            be rendered as an integer or an object in the rest search response.
            Default is false.
        :arg scroll: Specify how long a consistent view of the index
            should be maintained for scrolled search.
        """
        if scroll_id in SKIP_IN_PATH and body in SKIP_IN_PATH:
            raise ValueError("You need to supply scroll_id or body.")
        elif scroll_id and not body:
            body = {"scroll_id": scroll_id}
        elif scroll_id:
            params["scroll_id"] = scroll_id

        return self.transport.perform_request(
            "POST", "/_search/scroll", params=params, headers=headers, body=body
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "allow_no_indices",
        "allow_partial_search_results",
        "analyze_wildcard",
        "analyzer",
        "batched_reduce_size",
        "ccs_minimize_roundtrips",
        "default_operator",
        "df",
        "docvalue_fields",
        "expand_wildcards",
        "explain",
        "from_",
        "ignore_throttled",
        "ignore_unavailable",
        "include_named_queries_score",
        "lenient",
        "max_concurrent_shard_requests",
        "pre_filter_shard_size",
        "preference",
        "q",
        "request_cache",
        "rest_total_hits_as_int",
        "routing",
        "scroll",
        "search_pipeline",
        "search_type",
        "seq_no_primary_term",
        "size",
        "sort",
        "stats",
        "stored_fields",
        "suggest_field",
        "suggest_mode",
        "suggest_size",
        "suggest_text",
        "terminate_after",
        "timeout",
        "track_scores",
        "track_total_hits",
        "typed_keys",
        "version",
    )
    def search(
        self,
        body: Any = None,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns results matching a query.


        :arg body: The search definition using the Query DSL
        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg allow_partial_search_results: Indicate if an error should
            be returned if there is a partial search failure or timeout. Default is
            True.
        :arg analyze_wildcard: Specify whether wildcard and prefix
            queries should be analyzed. Default is false.
        :arg analyzer: The analyzer to use for the query string.
        :arg batched_reduce_size: The number of shard results that
            should be reduced at once on the coordinating node. This value should be
            used as a protection mechanism to reduce the memory overhead per search
            request if the potential number of shards in the request can be large.
            Default is 512.
        :arg ccs_minimize_roundtrips: Indicates whether network round-
            trips should be minimized as part of cross-cluster search requests
            execution. Default is True.
        :arg default_operator: The default operator for query string
            query (AND or OR). Valid choices are AND, OR.
        :arg df: The field to use as default where no field prefix is
            given in the query string.
        :arg docvalue_fields: Comma-separated list of fields to return
            as the docvalue representation of a field for each hit.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg explain: Specify whether to return detailed information
            about score computation as part of a hit.
        :arg from_: Starting offset. Default is 0.
        :arg ignore_throttled: Whether specified concrete, expanded or
            aliased indices should be ignored when throttled.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg include_named_queries_score: Indicates whether
            hit.matched_queries should be rendered as a map that includes the name
            of the matched query associated with its score (true) or as an array
            containing the name of the matched queries (false) Default is false.
        :arg lenient: Specify whether format-based query failures (such
            as providing text to a numeric field) should be ignored.
        :arg max_concurrent_shard_requests: The number of concurrent
            shard requests per node this search executes concurrently. This value
            should be used to limit the impact of the search on the cluster in order
            to limit the number of concurrent shard requests. Default is 5.
        :arg pre_filter_shard_size: Threshold that enforces a pre-filter
            round-trip to prefilter search shards based on query rewriting if the
            number of shards the search request expands to exceeds the threshold.
            This filter round-trip can limit the number of shards significantly if
            for instance a shard can not match any documents based on its rewrite
            method ie. if date filters are mandatory to match but the shard bounds
            and the query are disjoint.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg q: Query in the Lucene query string syntax.
        :arg request_cache: Specify if request cache should be used for
            this request or not, defaults to index level setting.
        :arg rest_total_hits_as_int: Indicates whether hits.total should
            be rendered as an integer or an object in the rest search response.
            Default is false.
        :arg routing: Comma-separated list of specific routing values.
        :arg scroll: Specify how long a consistent view of the index
            should be maintained for scrolled search.
        :arg search_pipeline: Customizable sequence of processing stages
            applied to search queries.
        :arg search_type: Search operation type. Valid choices are
            query_then_fetch, dfs_query_then_fetch.
        :arg seq_no_primary_term: Specify whether to return sequence
            number and primary term of the last modification of each hit.
        :arg size: Number of hits to return. Default is 10.
        :arg sort: Comma-separated list of <field>:<direction> pairs.
        :arg stats: Specific 'tag' of the request for logging and
            statistical purposes.
        :arg stored_fields: Comma-separated list of stored fields to
            return.
        :arg suggest_field: Specify which field to use for suggestions.
        :arg suggest_mode: Specify suggest mode. Valid choices are
            missing, popular, always.
        :arg suggest_size: How many suggestions to return in response.
        :arg suggest_text: The source text for which the suggestions
            should be returned.
        :arg terminate_after: The maximum number of documents to collect
            for each shard, upon reaching which the query execution will terminate
            early.
        :arg timeout: Operation timeout.
        :arg track_scores: Whether to calculate and return scores even
            if they are not used for sorting.
        :arg track_total_hits: Indicate if the number of documents that
            match the query should be tracked.
        :arg typed_keys: Specify whether aggregation and suggester names
            should be prefixed by their respective types in the response.
        :arg version: Whether to return document version as part of a
            hit.
        """
        # from is a reserved word so it cannot be used, use from_ instead
        if "from_" in params:
            params["from"] = params.pop("from_")

        return self.transport.perform_request(
            "POST",
            _make_path(index, "_search"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "allow_no_indices",
        "expand_wildcards",
        "ignore_unavailable",
        "local",
        "preference",
        "routing",
    )
    def search_shards(
        self,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information about the indices and shards that a search request would be
        executed against.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg local: Return local information, do not retrieve the state
            from cluster-manager node. Default is false.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg routing: Routing value.
        """
        return self.transport.perform_request(
            "GET", _make_path(index, "_search_shards"), params=params, headers=headers
        )

    @query_params(
        "allow_no_indices",
        "ccs_minimize_roundtrips",
        "expand_wildcards",
        "explain",
        "ignore_throttled",
        "ignore_unavailable",
        "preference",
        "profile",
        "rest_total_hits_as_int",
        "routing",
        "scroll",
        "search_type",
        "typed_keys",
    )
    def search_template(
        self,
        body: Any,
        index: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Allows to use the Mustache language to pre-render a search definition.


        :arg body: The search definition template and its params
        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg ccs_minimize_roundtrips: Indicates whether network round-
            trips should be minimized as part of cross-cluster search requests
            execution. Default is True.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg explain: Specify whether to return detailed information
            about score computation as part of a hit.
        :arg ignore_throttled: Whether specified concrete, expanded or
            aliased indices should be ignored when throttled.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg profile: Specify whether to profile the query execution.
        :arg rest_total_hits_as_int: Indicates whether hits.total should
            be rendered as an integer or an object in the rest search response.
            Default is false.
        :arg routing: Comma-separated list of specific routing values.
        :arg scroll: Specify how long a consistent view of the index
            should be maintained for scrolled search.
        :arg search_type: Search operation type. Valid choices are
            query_then_fetch, query_and_fetch, dfs_query_then_fetch,
            dfs_query_and_fetch.
        :arg typed_keys: Specify whether aggregation and suggester names
            should be prefixed by their respective types in the response.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "POST",
            _make_path(index, "_search", "template"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params(
        "field_statistics",
        "fields",
        "offsets",
        "payloads",
        "positions",
        "preference",
        "realtime",
        "routing",
        "term_statistics",
        "version",
        "version_type",
    )
    def termvectors(
        self,
        index: Any,
        body: Any = None,
        id: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns information and statistics about terms in the fields of a particular
        document.


        :arg index: The index in which the document resides.
        :arg body: Define parameters and or supply a document to get
            termvectors for. See documentation.
        :arg id: Document ID. When not specified a doc param should be
            supplied.
        :arg field_statistics: Specifies if document count, sum of
            document frequencies and sum of total term frequencies should be
            returned. Default is True.
        :arg fields: Comma-separated list of fields to return.
        :arg offsets: Specifies if term offsets should be returned.
            Default is True.
        :arg payloads: Specifies if term payloads should be returned.
            Default is True.
        :arg positions: Specifies if term positions should be returned.
            Default is True.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg realtime: Specifies if request is real-time as opposed to
            near-real-time. Default is True.
        :arg routing: Routing value.
        :arg term_statistics: Specifies if total term frequency and
            document frequency should be returned. Default is false.
        :arg version: Explicit version number for concurrency control.
        :arg version_type: Specific version type. Valid choices are
            internal, external, external_gte, force.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        path = _make_path(index, "_termvectors", id)

        return self.transport.perform_request(
            "POST", path, params=params, headers=headers, body=body
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "if_primary_term",
        "if_seq_no",
        "lang",
        "refresh",
        "require_alias",
        "retry_on_conflict",
        "routing",
        "timeout",
        "wait_for_active_shards",
    )
    def update(
        self,
        index: Any,
        id: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates a document with a script or partial document.


        :arg index: Index name.
        :arg id: Document ID.
        :arg body: The request definition requires either `script` or
            partial `doc`
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg if_primary_term: only perform the operation if the last
            operation that has changed the document has the specified primary term.
        :arg if_seq_no: only perform the operation if the last operation
            that has changed the document has the specified sequence number.
        :arg lang: The script language. Default is painless.
        :arg refresh: If `true` then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh
            to make this operation visible to search, if `false` (the default) then
            do nothing with refreshes. Valid choices are true, false, wait_for.
        :arg require_alias: When true, requires destination to be an
            alias. Default is false.
        :arg retry_on_conflict: Specify how many times should the
            operation be retried when a conflict occurs. Default is 0.
        :arg routing: Routing value.
        :arg timeout: Operation timeout.
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before proceeding with the operation. Defaults to 1,
            meaning the primary shard only. Set to `all` for all shard copies,
            otherwise set to any non-negative value less than or equal to the total
            number of copies for the shard (number of replicas + 1). Default is 1.
        """
        for param in (index, id, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        path = _make_path(index, "_update", id)

        return self.transport.perform_request(
            "POST", path, params=params, headers=headers, body=body
        )

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "allow_no_indices",
        "analyze_wildcard",
        "analyzer",
        "conflicts",
        "default_operator",
        "df",
        "expand_wildcards",
        "from_",
        "ignore_unavailable",
        "lenient",
        "max_docs",
        "pipeline",
        "preference",
        "q",
        "refresh",
        "request_cache",
        "requests_per_second",
        "routing",
        "scroll",
        "scroll_size",
        "search_timeout",
        "search_type",
        "size",
        "slices",
        "sort",
        "stats",
        "terminate_after",
        "timeout",
        "version",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    def update_by_query(
        self,
        index: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Performs an update on every document in the index without changing the source,
        for example to pick up a mapping change.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg body: The search definition using the Query DSL
        :arg _source: True or false to return the _source field or not,
            or a list of fields to return.
        :arg _source_excludes: List of fields to exclude from the
            returned _source field.
        :arg _source_includes: List of fields to extract and return from
            the _source field.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified).
        :arg analyze_wildcard: Specify whether wildcard and prefix
            queries should be analyzed. Default is false.
        :arg analyzer: The analyzer to use for the query string.
        :arg conflicts: What to do when the operation encounters version
            conflicts?. Valid choices are abort, proceed.
        :arg default_operator: The default operator for query string
            query (AND or OR). Valid choices are AND, OR.
        :arg df: The field to use as default where no field prefix is
            given in the query string.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg from_: Starting offset. Default is 0.
        :arg ignore_unavailable: Whether specified concrete indices
            should be ignored when unavailable (missing or closed).
        :arg lenient: Specify whether format-based query failures (such
            as providing text to a numeric field) should be ignored.
        :arg max_docs: Maximum number of documents to process (default:
            all documents).
        :arg pipeline: The pipeline id to preprocess incoming documents
            with.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg q: Query in the Lucene query string syntax.
        :arg refresh: Should the affected indexes be refreshed?.
        :arg request_cache: Specify if request cache should be used for
            this request or not, defaults to index level setting.
        :arg requests_per_second: The throttle for this request in sub-
            requests per second. -1 means no throttle. Default is 0.
        :arg routing: Comma-separated list of specific routing values.
        :arg scroll: Specify how long a consistent view of the index
            should be maintained for scrolled search.
        :arg scroll_size: Size on the scroll request powering the
            operation. Default is 100.
        :arg search_timeout: Explicit timeout for each search request.
            Defaults to no timeout.
        :arg search_type: Search operation type. Valid choices are
            query_then_fetch, dfs_query_then_fetch.
        :arg size: Deprecated, please use `max_docs` instead.
        :arg slices: The number of slices this task should be divided
            into. Defaults to 1, meaning the task isn't sliced into subtasks. Can be
            set to `auto`. Default is 1.
        :arg sort: Comma-separated list of <field>:<direction> pairs.
        :arg stats: Specific 'tag' of the request for logging and
            statistical purposes.
        :arg terminate_after: The maximum number of documents to collect
            for each shard, upon reaching which the query execution will terminate
            early.
        :arg timeout: Time each individual bulk request should wait for
            shards that are unavailable. Default is 1m.
        :arg version: Whether to return document version as part of a
            hit.
        :arg wait_for_active_shards: Sets the number of shard copies
            that must be active before proceeding with the operation. Defaults to 1,
            meaning the primary shard only. Set to `all` for all shard copies,
            otherwise set to any non-negative value less than or equal to the total
            number of copies for the shard (number of replicas + 1). Default is 1.
        :arg wait_for_completion: Should this request wait until the
            operation has completed before returning. Default is True.
        """
        # from is a reserved word so it cannot be used, use from_ instead
        if "from_" in params:
            params["from"] = params.pop("from_")

        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return self.transport.perform_request(
            "POST",
            _make_path(index, "_update_by_query"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("requests_per_second")
    def update_by_query_rethrottle(
        self,
        task_id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Changes the number of requests per second for a particular Update By Query
        operation.


        :arg task_id: The task id to rethrottle.
        :arg requests_per_second: The throttle for this request in sub-
            requests per second. -1 means no throttle.
        """
        if task_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'task_id'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_update_by_query", task_id, "_rethrottle"),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_script_context(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns all script contexts.

        """
        return self.transport.perform_request(
            "GET", "/_script_context", params=params, headers=headers
        )

    @query_params()
    def get_script_languages(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns available script types, languages and contexts.

        """
        return self.transport.perform_request(
            "GET", "/_script_language", params=params, headers=headers
        )

    @query_params(
        "allow_partial_pit_creation",
        "expand_wildcards",
        "keep_alive",
        "preference",
        "routing",
    )
    def create_pit(
        self,
        index: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates point in time context.


        :arg index: Comma-separated list of indices; use `_all` or empty
            string to perform the operation on all indices.
        :arg allow_partial_pit_creation: Allow if point in time can be
            created with partial failures.
        :arg expand_wildcards: Whether to expand wildcard expression to
            concrete indices that are open, closed or both. Valid choices are all,
            open, closed, hidden, none.
        :arg keep_alive: Specify the keep alive for point in time.
        :arg preference: Specify the node or shard the operation should
            be performed on. Default is random.
        :arg routing: Comma-separated list of specific routing values.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return self.transport.perform_request(
            "POST",
            _make_path(index, "_search", "point_in_time"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_all_pits(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes all active point in time searches.

        """
        return self.transport.perform_request(
            "DELETE", "/_search/point_in_time/_all", params=params, headers=headers
        )

    @query_params()
    def delete_pit(
        self,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes one or more point in time searches based on the IDs passed.


        :arg body: The point-in-time ids to be deleted
        """
        return self.transport.perform_request(
            "DELETE",
            "/_search/point_in_time",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_all_pits(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Lists all active point in time searches.

        """
        return self.transport.perform_request(
            "GET", "/_search/point_in_time/_all", params=params, headers=headers
        )
