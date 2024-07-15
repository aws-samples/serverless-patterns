# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

# ------------------------------------------------------------------------------------------
# THIS CODE IS AUTOMATICALLY GENERATED AND MANUAL EDITS WILL BE LOST
#
# To contribute, kindly make modifications in the opensearch-py client generator
# or in the OpenSearch API specification, and run `nox -rs generate`. See DEVELOPER_GUIDE.md
# and https://github.com/opensearch-project/opensearch-api-specification for details.
# -----------------------------------------------------------------------------------------+


from typing import Any

from ..client.utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class RollupsClient(NamespacedClient):
    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def delete(
        self,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete index rollup.


        :arg id: Rollup to access
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
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_rollup", "jobs", id),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def explain(
        self,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Get a rollup's current status.


        :arg id: Rollup to access
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
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_rollup", "jobs", id, "_explain"),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def get(
        self,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Get an index rollup.


        :arg id: Rollup to access
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
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_rollup", "jobs", id),
            params=params,
            headers=headers,
        )

    @query_params(
        "error_trace",
        "filter_path",
        "human",
        "if_primary_term",
        "if_seq_no",
        "pretty",
        "source",
    )
    def put(
        self,
        id: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Create or update index rollup.


        :arg id: Rollup to access
        :arg error_trace: Whether to include the stack trace of returned
            errors.
        :arg filter_path: Comma-separated list of filters used to reduce
            the response.
        :arg human: Whether to return human readable values for
            statistics.
        :arg if_primary_term: Only perform the operation if the document
            has this primary term.
        :arg if_seq_no: Only perform the operation if the document has
            this sequence number.
        :arg pretty: Whether to pretty format the returned JSON
            response.
        :arg source: The URL-encoded request definition. Useful for
            libraries that do not accept a request body for non-POST requests.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_rollup", "jobs", id),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def start(
        self,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Start rollup.


        :arg id: Rollup to access
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
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_rollup", "jobs", id, "_start"),
            params=params,
            headers=headers,
        )

    @query_params("error_trace", "filter_path", "human", "pretty", "source")
    def stop(
        self,
        id: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Stop rollup.


        :arg id: Rollup to access
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
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'id'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_rollup", "jobs", id, "_stop"),
            params=params,
            headers=headers,
        )
