# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from typing import Any

from _typeshed import Incomplete

from opensearchpy import AsyncOpenSearch as AsyncOpenSearch
from opensearchpy.exceptions import ConnectionError as ConnectionError

OPENSEARCH_URL: Incomplete

async def get_test_client(nowait: bool = ..., **kwargs: Any) -> Any: ...
