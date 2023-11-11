# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

import sys

import requests

PY3 = sys.version_info[0] == 3

if PY3:
    from urllib.parse import parse_qs, urlencode, urlparse


def fetch_url(prepared_request):  # type: ignore
    """
    This is a util method that helps in reconstructing the request url.
    :param prepared_request: unsigned request
    :return: reconstructed url
    """
    url = urlparse(prepared_request.url)
    path = url.path or "/"

    # fetch the query string if present in the request
    querystring = ""
    if url.query:
        querystring = "?" + urlencode(
            parse_qs(url.query, keep_blank_values=True), doseq=True
        )

    # fetch the host information from headers
    headers = dict(
        (key.lower(), value) for key, value in prepared_request.headers.items()
    )
    location = headers.get("host") or url.netloc

    # construct the url and return
    return url.scheme + "://" + location + path + querystring


class AWSV4SignerAuth(requests.auth.AuthBase):
    """
    AWS V4 Request Signer for Requests.
    """

    def __init__(self, credentials, region, service="es"):  # type: ignore
        if not credentials:
            raise ValueError("Credentials cannot be empty")
        self.credentials = credentials

        if not region:
            raise ValueError("Region cannot be empty")
        self.region = region

        if not service:
            raise ValueError("Service name cannot be empty")
        self.service = service

    def __call__(self, request):  # type: ignore
        return self._sign_request(request)  # type: ignore

    def _sign_request(self, prepared_request):  # type: ignore
        """
        This method helps in signing the request by injecting the required headers.
        :param prepared_request: unsigned request
        :return: signed request
        """

        from botocore.auth import SigV4Auth
        from botocore.awsrequest import AWSRequest

        url = fetch_url(prepared_request)  # type: ignore

        # create an AWS request object and sign it using SigV4Auth
        aws_request = AWSRequest(
            method=prepared_request.method.upper(),
            url=url,
            data=prepared_request.body,
        )

        # credentials objects expose access_key, secret_key and token attributes
        # via @property annotations that call _refresh() on every access,
        # creating a race condition if the credentials expire before secret_key
        # is called but after access_key- the end result is the access_key doesn't
        # correspond to the secret_key used to sign the request. To avoid this,
        # get_frozen_credentials() which returns non-refreshing credentials is
        # called if it exists.
        credentials = (
            self.credentials.get_frozen_credentials()
            if hasattr(self.credentials, "get_frozen_credentials")
            and callable(self.credentials.get_frozen_credentials)
            else self.credentials
        )

        sig_v4_auth = SigV4Auth(credentials, self.service, self.region)
        sig_v4_auth.add_auth(aws_request)

        # copy the headers from AWS request object into the prepared_request
        prepared_request.headers.update(dict(aws_request.headers.items()))
        prepared_request.headers["X-Amz-Content-SHA256"] = sig_v4_auth.payload(
            aws_request
        )

        return prepared_request
