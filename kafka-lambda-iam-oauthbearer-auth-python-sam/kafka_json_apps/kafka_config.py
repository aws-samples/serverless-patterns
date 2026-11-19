"""Shared helper that turns the Kafka client.properties file written by
refresh_token.sh into kwargs for a kafka-python producer/consumer.

Both the SASL/OAUTHBEARER patterns (static Cognito / AWS web-identity token
embedded in the properties file) and the MSK IAM pattern (token minted on demand
by the AWS MSK IAM SASL signer) are supported, so the producer/consumer code is
identical across all three patterns.

Requires kafka-python < 3 (the 2.x line), whose SASL/OAUTHBEARER support takes a
``sasl_oauth_token_provider`` implementing ``AbstractTokenProvider``. The 3.x
rewrite dropped that parameter, so pin ``kafka-python<3`` (see requirements.txt).
"""
import os
import re

try:
    # kafka-python OAUTHBEARER token-provider base class. Its location moved
    # between 2.x releases: kafka.sasl.oauth (>= 2.1) and kafka.oauth.abstract
    # (2.0.x). Try both.
    from kafka.sasl.oauth import AbstractTokenProvider as _TokenProviderBase
except Exception:
    try:
        from kafka.oauth.abstract import AbstractTokenProvider as _TokenProviderBase
    except Exception:  # kafka not importable (e.g. isolated unit test) - degrade gracefully
        class _TokenProviderBase:  # noqa: D401 - minimal stand-in
            pass


class _StaticTokenProvider(_TokenProviderBase):
    """Returns a pre-minted OAUTHBEARER access token (Cognito / AWS web-identity)."""

    def __init__(self, token):
        self._token = token

    def token(self):
        return self._token

    def extensions(self):
        return {}


class _MskTokenProvider(_TokenProviderBase):
    """Mints an MSK IAM OAUTHBEARER token via the AWS signer, optionally as a role."""

    def __init__(self, region, role_arn=None):
        self.region = region
        self.role_arn = role_arn

    def token(self):
        from aws_msk_iam_sasl_signer import MSKAuthTokenProvider
        if self.role_arn:
            token, _ = MSKAuthTokenProvider.generate_auth_token_from_role_arn(self.region, self.role_arn)
        else:
            token, _ = MSKAuthTokenProvider.generate_auth_token(self.region)
        return token

    def extensions(self):
        return {}


def load_properties(path):
    """Parse a Java-style key=value .properties file into a dict."""
    props = {}
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            props[key.strip()] = value.strip()
    return props


def client_kwargs(properties_file):
    """Build the common kafka-python connection kwargs from the properties file."""
    props = load_properties(properties_file)
    kwargs = {
        "bootstrap_servers": props["bootstrap.servers"].split(","),
        "security_protocol": "SASL_SSL",
        "sasl_mechanism": "OAUTHBEARER",
    }
    # TLS trust anchor: self-managed brokers present a self-signed cert whose CA
    # PEM sits on the client instance; MSK presents a publicly-trusted Amazon
    # cert, so we fall back to the default system trust store. The self-signed
    # cert carries the broker IPs as SANs, but disable hostname checking to stay
    # robust if a broker is reached by an address not listed in the SANs.
    ca_cert = os.environ.get("KAFKA_CA_CERT", "/home/ec2-user/kafka.crt")
    if os.path.isfile(ca_cert):
        kwargs["ssl_cafile"] = ca_cert
        kwargs["ssl_check_hostname"] = False

    region = os.environ.get("AWS_REGION", "us-west-2")
    jaas = props.get("sasl.jaas.config", "")
    token_match = re.search(r'oauth\.access\.token="([^"]+)"', jaas)
    if token_match:
        kwargs["sasl_oauth_token_provider"] = _StaticTokenProvider(token_match.group(1))
    else:
        # MSK IAM: mint an OAUTHBEARER token via the AWS signer, honoring an
        # awsRoleArn from the JAAS config if present.
        role_match = re.search(r'awsRoleArn="([^"]+)"', jaas)
        kwargs["sasl_oauth_token_provider"] = _MskTokenProvider(
            region, role_match.group(1) if role_match else None)
    return kwargs
