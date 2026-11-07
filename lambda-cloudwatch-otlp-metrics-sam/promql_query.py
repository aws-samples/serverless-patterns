#!/usr/bin/env python3
"""Run a Prometheus Query Language (PromQL) query against the Amazon CloudWatch
Prometheus-compatible HTTP API.

The API requires AWS Signature Version 4 (SigV4) signed requests, which plain curl
cannot produce, so this script signs the request with botocore (installed with the
AWS CLI v2 bundle, or with "python3 -m pip install botocore").

Usage:
    python3 promql_query.py 'sum({__name__="orders.processed"})' [region]
"""
import json
import sys
import urllib.parse
import urllib.request

import botocore.session
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest


def main():
    if len(sys.argv) < 2:
        sys.exit('usage: python3 promql_query.py \'<promql>\' [region]')
    query = sys.argv[1]
    session = botocore.session.get_session()
    region = sys.argv[2] if len(sys.argv) > 2 else session.get_config_variable('region')
    if not region:
        sys.exit('no AWS Region configured, pass it as the second argument')

    url = 'https://monitoring.%s.amazonaws.com/api/v1/query' % region
    # The body must be form encoded, otherwise a query containing "+" or "&" is
    # mangled by the endpoint and comes back as an invalid PromQL query.
    body = urllib.parse.urlencode({'query': query})
    request = AWSRequest(
        method='POST',
        url=url,
        data=body,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )
    SigV4Auth(session.get_credentials(), 'monitoring', region).add_auth(request)

    prepared = urllib.request.Request(
        url, data=body.encode('utf-8'), headers=dict(request.headers), method='POST'
    )
    try:
        with urllib.request.urlopen(prepared) as response:
            print(json.dumps(json.loads(response.read()), indent=2))
    except urllib.request.HTTPError as error:
        print('HTTP %s: %s' % (error.code, error.read().decode('utf-8')))
        sys.exit(1)


if __name__ == '__main__':
    main()
