"""Records an approver's decision for a Step Functions task token.

The approval email links to the Amazon Cognito managed login page. After the
approver signs in, Cognito redirects to this function with an authorization
code. The function exchanges the code for tokens, checks that the user is in
the approvers group, and returns the decision to Step Functions.

The OAuth `state` parameter carries "<action>:<URL-safe task token>". It is only
trusted after the sign-in succeeds and the group check passes.
"""
import base64
import html
import json
import os
import urllib.error
import urllib.parse
import urllib.request

import boto3

USER_POOL_ID = os.environ["USER_POOL_ID"]
CLIENT_ID = os.environ["CLIENT_ID"]
COGNITO_DOMAIN = os.environ["COGNITO_DOMAIN"]  # https://<prefix>.auth.<region>.amazoncognito.com
CALLBACK_URL = os.environ["CALLBACK_URL"]
APPROVER_GROUP = os.environ["APPROVER_GROUP"]

cognito = boto3.client("cognito-idp")
sfn = boto3.client("stepfunctions")
_client_secret = None


def _secret():
    # Read the app client secret from Cognito instead of storing it in an
    # environment variable.
    global _client_secret
    if _client_secret is None:
        client = cognito.describe_user_pool_client(UserPoolId=USER_POOL_ID, ClientId=CLIENT_ID)
        _client_secret = client["UserPoolClient"]["ClientSecret"]
    return _client_secret


def _page(status, message):
    body = (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width, initial-scale=1'>"
        f"<title>Approval</title></head><body><main><h1>{html.escape(message)}</h1></main></body></html>"
    )
    return {"statusCode": status, "headers": {"Content-Type": "text/html; charset=utf-8"}, "body": body}


def _id_token_claims(code):
    """Exchange the authorization code at the Cognito token endpoint.

    The ID token comes straight from Cognito over TLS on this back-channel
    call, authenticated with the client secret, so its claims can be read
    without a separate signature check (OpenID Connect Core 3.1.3.7).
    """
    data = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "code": code,
        "redirect_uri": CALLBACK_URL,
    }).encode()
    basic = base64.b64encode(f"{CLIENT_ID}:{_secret()}".encode()).decode()
    request = urllib.request.Request(
        f"{COGNITO_DOMAIN}/oauth2/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {basic}"},
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        tokens = json.load(response)
    payload = tokens["id_token"].split(".")[1]
    claims = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))
    if claims.get("aud") != CLIENT_ID or claims.get("token_use") != "id":
        raise ValueError("unexpected token")
    return claims


def handler(event, context):
    params = event.get("queryStringParameters") or {}
    code, state = params.get("code"), params.get("state", "")
    action, _, safe_token = state.partition(":")
    # The workflow made the token URL-safe (+ -> -, / -> _, = -> .). Undo that.
    task_token = safe_token.translate(str.maketrans("-_.", "+/="))
    if not code or action not in ("approve", "reject") or not task_token:
        return _page(400, "This link is not valid.")

    try:
        claims = _id_token_claims(code)
    except (urllib.error.HTTPError, KeyError, ValueError):
        return _page(401, "Sign-in failed. Open the link from the email again.")

    if APPROVER_GROUP not in claims.get("cognito:groups", []):
        return _page(403, "Your user is not allowed to approve requests.")

    decision = {"decision": "approved" if action == "approve" else "rejected",
                "approver": claims.get("email", claims["sub"])}
    try:
        sfn.send_task_success(taskToken=task_token, output=json.dumps(decision))
    except (sfn.exceptions.TaskDoesNotExist, sfn.exceptions.TaskTimedOut, sfn.exceptions.InvalidToken):
        return _page(410, "This request is no longer waiting for a decision.")
    return _page(200, f"Recorded: {decision['decision']}.")
