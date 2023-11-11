# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from ..client.utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class SecurityClient(NamespacedClient):
    @query_params()
    def get_account_details(self, params=None, headers=None):
        """
        Returns account details for the current user.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "account"),
            params=params,
            headers=headers,
        )

    @query_params()
    def change_password(self, body, params=None, headers=None):
        """
        Changes the password for the current user.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "account"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_action_group(self, action_group, params=None, headers=None):
        """
        Retrieves one action group.
        """
        if action_group in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'action-group'."
            )

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_action_groups(self, params=None, headers=None):
        """
        Retrieves all action groups.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "actiongroups"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_action_group(self, action_group, params=None, headers=None):
        """
        Deletes the specified action group.
        """
        if action_group in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'action-group'."
            )

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_action_group(self, action_group, body, params=None, headers=None):
        """
        Creates or replaces the specified action group.
        """
        for param in (action_group, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_action_group(self, action_group, body, params=None, headers=None):
        """
        Updates individual attributes of an action group.
        """
        for param in (action_group, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_action_groups(self, body, params=None, headers=None):
        """
        Creates, updates, or deletes multiple action groups in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "actiongroups"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_user(self, username, params=None, headers=None):
        """
        Retrieves one user.
        """
        if username in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'username'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_users(self, params=None, headers=None):
        """
        Retrieves all users.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "internalusers"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_user(self, username, params=None, headers=None):
        """
        Deletes the specified user.
        """
        if username in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'username'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_user(self, username, body, params=None, headers=None):
        """
        Creates or replaces the specified user.
        """
        for param in (username, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_user(self, username, body, params=None, headers=None):
        """
        Updates individual attributes of an internal user.
        """
        for param in (username, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_users(self, body, params=None, headers=None):
        """
        Creates, updates, or deletes multiple internal users in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "internalusers"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_role(self, role, params=None, headers=None):
        """
        Retrieves one role.
        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_roles(self, params=None, headers=None):
        """
        Retrieves all roles.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "roles"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_role(self, role, params=None, headers=None):
        """
        Deletes the specified role.
        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_role(self, role, body, params=None, headers=None):
        """
        Creates or replaces the specified role.
        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_role(self, role, body, params=None, headers=None):
        """
        Updates individual attributes of a role.
        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_roles(self, body, params=None, headers=None):
        """
        Creates, updates, or deletes multiple roles in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "roles"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_role_mapping(self, role, params=None, headers=None):
        """
        Retrieves one role mapping.
        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_role_mappings(self, params=None, headers=None):
        """
        Retrieves all role mappings.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "rolesmapping"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_role_mapping(self, role, params=None, headers=None):
        """
        Deletes the specified role mapping.
        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_role_mapping(self, role, body, params=None, headers=None):
        """
        Creates or replaces the specified role mapping.
        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_role_mapping(self, role, body, params=None, headers=None):
        """
        Updates individual attributes of a role mapping.
        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_role_mappings(self, body, params=None, headers=None):
        """
        Creates or updates multiple role mappings in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "rolesmapping"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_tenant(self, tenant, params=None, headers=None):
        """
        Retrieves one tenant.
        """
        if tenant in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'tenant'.")

        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_tenants(self, params=None, headers=None):
        """
        Retrieves all tenants.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "tenants"),
            params=params,
            headers=headers,
        )

    @query_params()
    def delete_tenant(self, tenant, params=None, headers=None):
        """
        Deletes the specified tenant.
        """
        if tenant in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'tenant'.")

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
        )

    @query_params()
    def create_tenant(self, tenant, body, params=None, headers=None):
        """
        Creates or replaces the specified tenant.
        """
        for param in (tenant, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_tenant(self, tenant, body, params=None, headers=None):
        """
        Add, delete, or modify a single tenant.
        """
        for param in (tenant, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_tenants(self, body, params=None, headers=None):
        """
        Add, delete, or modify multiple tenants in a single call.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "tenants"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_configuration(self, params=None, headers=None):
        """
        Retrieves the current Security plugin configuration in JSON format.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "securityconfig"),
            params=params,
            headers=headers,
        )

    @query_params()
    def update_configuration(self, body, params=None, headers=None):
        """
        Retrieves the current Security plugin configuration in JSON format.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "securityconfig", "config"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_configuration(self, body, params=None, headers=None):
        """
        Updates the existing configuration using the REST API.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "securityconfig"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def get_distinguished_names(self, cluster_name=None, params=None, headers=None):
        """
        Retrieves all distinguished names in the allow list.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
        )

    @query_params()
    def update_distinguished_names(self, cluster_name, body, params=None, headers=None):
        """
        Adds or updates the specified distinguished names in the cluster's or node's allow list.
        """
        for param in (cluster_name, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def delete_distinguished_names(self, cluster_name, params=None, headers=None):
        """
        Deletes all distinguished names in the specified cluster's or node's allow list.
        """
        if cluster_name in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'cluster-name'."
            )

        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_certificates(self, params=None, headers=None):
        """
        Retrieves the cluster's security certificates.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "ssl", "certs"),
            params=params,
            headers=headers,
        )

    @query_params()
    def reload_transport_certificates(self, params=None, headers=None):
        """
        Reloads SSL certificates that are about to expire without restarting the OpenSearch node.
        """
        return self.transport.perform_request(
            "PUT",
            _make_path(
                "_opendistro", "_security", "api", "ssl", "transport", "reloadcerts"
            ),
            params=params,
            headers=headers,
        )

    @query_params()
    def reload_http_certificates(self, params=None, headers=None):
        """
        Reloads SSL certificates that are about to expire without restarting the OpenSearch node.
        """
        return self.transport.perform_request(
            "PUT",
            _make_path("_opendistro", "_security", "api", "ssl", "http", "reloadcerts"),
            params=params,
            headers=headers,
        )

    @query_params()
    def flush_cache(self, params=None, headers=None):
        """
        Flushes the Security plugin user, authentication, and authorization cache.
        """
        return self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "cache"),
            params=params,
            headers=headers,
        )

    @query_params()
    def health_check(self, params=None, headers=None):
        """
        Checks to see if the Security plugin is up and running.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "health"),
            params=params,
            headers=headers,
        )

    @query_params()
    def get_audit_configuration(self, params=None, headers=None):
        """
        A GET call retrieves the audit configuration.
        """
        return self.transport.perform_request(
            "GET",
            _make_path("_opendistro", "_security", "api", "audit"),
            params=params,
            headers=headers,
        )

    @query_params()
    def update_audit_config(self, body, params=None, headers=None):
        """
        A PUT call updates the audit configuration.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PUT",
            _make_path("_opendistro", "_security", "api", "audit", "config"),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    def patch_audit_configuration(self, body, params=None, headers=None):
        """
        A PATCH call is used to update specified fields in the audit configuration.
        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return self.transport.perform_request(
            "PATCH",
            _make_path("_opendistro", "_security", "api", "audit"),
            params=params,
            headers=headers,
            body=body,
        )
