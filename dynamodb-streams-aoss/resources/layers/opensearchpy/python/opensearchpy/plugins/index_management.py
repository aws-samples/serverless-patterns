# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.


from ..client.utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class IndexManagementClient(NamespacedClient):
    @query_params()
    def put_policy(self, policy, body=None, params=None, headers=None):
        """
        Creates, or updates, a policy.

        :arg policy: The name of the policy
        """
        if policy in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'policy'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_ism", "policies", policy),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def add_policy(self, index, body=None, params=None, headers=None):
        """
        Adds a policy to an index. This operation does not change the policy if the index already has one.

        :arg index: The name of the index to add policy on
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "add", index),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_policy(self, policy, params=None, headers=None):
        """
        Gets the policy by `policy_id`.

        :arg policy: The name of the policy
        """
        if policy in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'policy'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_ism", "policies", policy),
            params=params,
            headers=headers,
        )

    @query_params()
    def remove_policy_from_index(self, index, params=None, headers=None):
        """
        Removes any ISM policy from the index.

        :arg index: The name of the index to remove policy on
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "remove", index),
            params=params,
            headers=headers,
        )

    @query_params()
    def change_policy(self, index, body=None, params=None, headers=None):
        """
        Updates the managed index policy to a new policy (or to a new version of the policy).

        :arg index: The name of the index to change policy on
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "change_policy", index),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def retry(self, index, body=None, params=None, headers=None):
        """
        Retries the failed action for an index.

        :arg index: The name of the index whose is in a failed state
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return self.transport.perform_request(
            "POST",
            _make_path("_plugins", "_ism", "retry", index),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params("show_policy")
    def explain_index(self, index, params=None, headers=None):
        """
        Gets the current state of the index.

        :arg index: The name of the index to explain
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'index'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_ism", "explain", index),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_policy(self, policy, params=None, headers=None):
        """
        Deletes the policy by `policy_id`.

        :arg policy: The name of the policy to delete
        """
        if policy in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'policy'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_ism", "policies", policy),
            params=params,
            headers=headers,
        )
