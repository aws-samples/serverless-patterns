# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

import warnings

from ..plugins.alerting import AlertingClient
from ..plugins.index_management import IndexManagementClient
from .utils import NamespacedClient


class PluginsClient(NamespacedClient):
    def __init__(self, client):
        super(PluginsClient, self).__init__(client)
        # self.query_workbench = QueryWorkbenchClient(client)
        # self.reporting = ReportingClient(client)
        # self.notebooks = NotebooksClient(client)
        self.alerting = AlertingClient(client)
        # self.anomaly_detection = AnomalyDetectionClient(client)
        # self.trace_analytics = TraceAnalyticsClient(client)
        self.index_management = IndexManagementClient(client)

        self._dynamic_lookup(client)

    def _dynamic_lookup(self, client):
        # Issue : https://github.com/opensearch-project/opensearch-py/issues/90#issuecomment-1003396742

        plugins = [
            # "query_workbench",
            # "reporting",
            # "notebooks",
            "alerting",
            # "anomaly_detection",
            # "trace_analytics",
            "index_management",
        ]
        for plugin in plugins:
            if not hasattr(client, plugin):
                setattr(client, plugin, getattr(self, plugin))
            else:
                warnings.warn(
                    f"Cannot load `{plugin}` directly to AsyncOpenSearch. `{plugin}` already exists in AsyncOpenSearch. Please use `AsyncOpenSearch.plugin.{plugin}` instead.",
                    category=RuntimeWarning,
                    stacklevel=2,
                )
