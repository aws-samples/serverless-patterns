# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#


import asyncio
import os
import ssl
import warnings

from .._async._extra_imports import aiohttp, aiohttp_exceptions
from .._async.compat import get_running_loop
from .._async.http_aiohttp import AIOHttpConnection
from ..compat import reraise_exceptions, string_types, urlencode
from ..exceptions import (
    ConnectionError,
    ConnectionTimeout,
    ImproperlyConfigured,
    SSLError,
)

VERIFY_CERTS_DEFAULT = object()
SSL_SHOW_WARN_DEFAULT = object()


class AsyncHttpConnection(AIOHttpConnection):
    def __init__(
        self,
        host="localhost",
        port=None,
        http_auth=None,
        use_ssl=False,
        verify_certs=VERIFY_CERTS_DEFAULT,
        ssl_show_warn=SSL_SHOW_WARN_DEFAULT,
        ca_certs=None,
        client_cert=None,
        client_key=None,
        ssl_version=None,
        ssl_assert_fingerprint=None,
        maxsize=10,
        headers=None,
        ssl_context=None,
        http_compress=None,
        opaque_id=None,
        loop=None,
        **kwargs
    ):
        self.headers = {}

        super().__init__(
            host=host,
            port=port,
            use_ssl=use_ssl,
            headers=headers,
            http_compress=http_compress,
            opaque_id=opaque_id,
            **kwargs
        )

        if http_auth is not None:
            if isinstance(http_auth, (tuple, list)):
                http_auth = aiohttp.BasicAuth(login=http_auth[0], password=http_auth[1])
            elif isinstance(http_auth, string_types):
                login, password = http_auth.split(":", 1)
                http_auth = aiohttp.BasicAuth(login=login, password=password)

        # if providing an SSL context, raise error if any other SSL related flag is used
        if ssl_context and (
            (verify_certs is not VERIFY_CERTS_DEFAULT)
            or (ssl_show_warn is not SSL_SHOW_WARN_DEFAULT)
            or ca_certs
            or client_cert
            or client_key
            or ssl_version
        ):
            warnings.warn(
                "When using `ssl_context`, all other SSL related kwargs are ignored"
            )

        self.ssl_assert_fingerprint = ssl_assert_fingerprint
        if self.use_ssl and ssl_context is None:
            if ssl_version is None:
                ssl_context = ssl.create_default_context()
            else:
                ssl_context = ssl.SSLContext(ssl_version)

            # Convert all sentinel values to their actual default
            # values if not using an SSLContext.
            if verify_certs is VERIFY_CERTS_DEFAULT:
                verify_certs = True
            if ssl_show_warn is SSL_SHOW_WARN_DEFAULT:
                ssl_show_warn = True

            if verify_certs:
                ssl_context.verify_mode = ssl.CERT_REQUIRED
                ssl_context.check_hostname = True
            else:
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE

            ca_certs = self.default_ca_certs() if ca_certs is None else ca_certs
            if verify_certs:
                if not ca_certs:
                    raise ImproperlyConfigured(
                        "Root certificates are missing for certificate "
                        "validation. Either pass them in using the ca_certs parameter or "
                        "install certifi to use it automatically."
                    )
                if os.path.isfile(ca_certs):
                    ssl_context.load_verify_locations(cafile=ca_certs)
                elif os.path.isdir(ca_certs):
                    ssl_context.load_verify_locations(capath=ca_certs)
                else:
                    raise ImproperlyConfigured("ca_certs parameter is not a path")
            else:
                if ssl_show_warn:
                    warnings.warn(
                        "Connecting to %s using SSL with verify_certs=False is insecure."
                        % self.host
                    )

            # Use client_cert and client_key variables for SSL certificate configuration.
            if client_cert and not os.path.isfile(client_cert):
                raise ImproperlyConfigured("client_cert is not a path to a file")
            if client_key and not os.path.isfile(client_key):
                raise ImproperlyConfigured("client_key is not a path to a file")
            if client_cert and client_key:
                ssl_context.load_cert_chain(client_cert, client_key)
            elif client_cert:
                ssl_context.load_cert_chain(client_cert)

        self.headers.setdefault("connection", "keep-alive")
        self.loop = loop
        self.session = None

        # Parameters for creating an aiohttp.ClientSession later.
        self._limit = maxsize
        self._http_auth = http_auth
        self._ssl_context = ssl_context

    async def perform_request(
        self, method, url, params=None, body=None, timeout=None, ignore=(), headers=None
    ):
        if self.session is None:
            await self._create_aiohttp_session()
        assert self.session is not None
        orig_body = body
        url_path = self.url_prefix + url
        if params:
            query_string = urlencode(params)
        else:
            query_string = ""

        # There is a bug in aiohttp that disables the re-use
        # of the connection in the pool when method=HEAD.
        # See: https://github.com/aio-libs/aiohttp/issues/1769
        is_head = False
        if method == "HEAD":
            method = "GET"
            is_head = True

        # Top-tier tip-toeing happening here. Basically
        # because Pip's old resolver is bad and wipes out
        # strict pins in favor of non-strict pins of extras
        # our [async] extra overrides aiohttp's pin of
        # yarl. yarl released breaking changes, aiohttp pinned
        # defensively afterwards, but our users don't get
        # that nice pin that aiohttp set. :( So to play around
        # this super-defensively we try to import yarl, if we can't
        # then we pass a string into ClientSession.request() instead.
        url = self.url_prefix + url
        if query_string:
            url = "%s?%s" % (url, query_string)
        url = self.host + url

        timeout = aiohttp.ClientTimeout(
            total=timeout if timeout is not None else self.timeout
        )

        req_headers = self.headers.copy()
        if headers:
            req_headers.update(headers)

        if self.http_compress and body:
            body = self._gzip_compress(body)
            req_headers["content-encoding"] = "gzip"

        auth = (
            self._http_auth if isinstance(self._http_auth, aiohttp.BasicAuth) else None
        )
        if callable(self._http_auth):
            req_headers = {
                **req_headers,
                **self._http_auth(method, url, query_string, body),
            }

        start = self.loop.time()
        try:
            async with self.session.request(
                method,
                url,
                data=body,
                auth=auth,
                headers=req_headers,
                timeout=timeout,
                fingerprint=self.ssl_assert_fingerprint,
            ) as response:
                if is_head:  # We actually called 'GET' so throw away the data.
                    await response.release()
                    raw_data = ""
                else:
                    raw_data = await response.text()
                duration = self.loop.time() - start

        # We want to reraise a cancellation or recursion error.
        except reraise_exceptions:
            raise
        except Exception as e:
            self.log_request_fail(
                method,
                str(url),
                url_path,
                orig_body,
                self.loop.time() - start,
                exception=e,
            )
            if isinstance(e, aiohttp_exceptions.ServerFingerprintMismatch):
                raise SSLError("N/A", str(e), e)
            if isinstance(
                e, (asyncio.TimeoutError, aiohttp_exceptions.ServerTimeoutError)
            ):
                raise ConnectionTimeout("TIMEOUT", str(e), e)
            raise ConnectionError("N/A", str(e), e)

        # raise warnings if any from the 'Warnings' header.
        warning_headers = response.headers.getall("warning", ())
        self._raise_warnings(warning_headers)

        # raise errors based on http status codes, let the client handle those if needed
        if not (200 <= response.status < 300) and response.status not in ignore:
            self.log_request_fail(
                method,
                str(url),
                url_path,
                orig_body,
                duration,
                status_code=response.status,
                response=raw_data,
            )
            self._raise_error(response.status, raw_data)

        self.log_request_success(
            method, str(url), url_path, orig_body, response.status, raw_data, duration
        )

        return response.status, response.headers, raw_data

    async def close(self):
        """
        Explicitly closes connection
        """
        if self.session:
            await self.session.close()

    async def _create_aiohttp_session(self):
        """Creates an aiohttp.ClientSession(). This is delayed until
        the first call to perform_request() so that AsyncTransport has
        a chance to set AIOHttpConnection.loop
        """
        if self.loop is None:
            self.loop = get_running_loop()
        self.session = aiohttp.ClientSession(
            headers=self.headers,
            skip_auto_headers=("accept", "accept-encoding"),
            auto_decompress=True,
            loop=self.loop,
            cookie_jar=aiohttp.DummyCookieJar(),
            response_class=OpenSearchClientResponse,
            connector=aiohttp.TCPConnector(
                limit=self._limit, use_dns_cache=True, ssl=self._ssl_context
            ),
        )


class OpenSearchClientResponse(aiohttp.ClientResponse):
    async def text(self, encoding=None, errors="strict"):
        if self._body is None:
            await self.read()

        return self._body.decode("utf-8", "surrogatepass")
