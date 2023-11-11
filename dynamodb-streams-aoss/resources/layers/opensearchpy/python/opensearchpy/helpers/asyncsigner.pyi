# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from typing import Any, Dict, List

class AWSV4SignerAsyncAuth:
    @property
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    @property
    def _sign_request(self, *args: Any, **kwargs: Any) -> Dict[str, List[str]]: ...
