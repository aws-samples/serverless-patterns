# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from typing import Any, Mapping, Optional

from .._async._extra_imports import aiohttp  # type: ignore
from .._async.http_aiohttp import AIOHttpConnection

class AsyncHttpConnection(AIOHttpConnection):
    session: Optional[aiohttp.ClientSession]
    def __init__(
        self,
        host: str = ...,
        port: Optional[int] = ...,
        http_auth: Optional[Any] = ...,
        use_ssl: bool = ...,
        verify_certs: bool = ...,
        ssl_show_warn: bool = ...,
        ca_certs: Optional[Any] = ...,
        client_cert: Optional[Any] = ...,
        client_key: Optional[Any] = ...,
        ssl_version: Optional[Any] = ...,
        ssl_assert_fingerprint: Optional[Any] = ...,
        maxsize: Optional[int] = ...,
        headers: Optional[Mapping[str, str]] = ...,
        ssl_context: Optional[Any] = ...,
        http_compress: Optional[bool] = ...,
        opaque_id: Optional[str] = ...,
        loop: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
