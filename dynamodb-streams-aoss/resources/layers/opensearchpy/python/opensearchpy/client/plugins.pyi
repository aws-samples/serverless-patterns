# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
from typing import Any

from ..client import OpenSearch
from ..plugins.alerting import AlertingClient as AlertingClient
from .utils import NamespacedClient as NamespacedClient

class PluginsClient(NamespacedClient):
    alerting: Any
    index_management: Any
    def __init__(self, client: OpenSearch) -> None: ...
