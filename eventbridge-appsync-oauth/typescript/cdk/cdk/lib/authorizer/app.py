import os
import json
import time
import jwt
from jwt import PyJWKClient
from jwt.exceptions import DecodeError, ExpiredSignatureError, InvalidTokenError

region = os.environ['AWS_REGION']
user_pool_id = os.environ['USER_POOL_ID']
app_client_id = os.environ['APP_CLIENT_ID']

cognito_keys_url = "https://cognito-idp.{}.amazonaws.com/{}/.well-known/jwks.json".format(region, user_pool_id)

jwks_client = PyJWKClient(cognito_keys_url)

# Expected incoming payload:
# {
#     "authorizationToken": "ExampleAUTHtoken123123123",
#     "requestContext": {
#         "apiId": "aaaaaa123123123example123",
#         "accountId": "111122223333",
#         "requestId": "f4081827-1111-4444-5555-5cf4695f339f",
#         "queryString": "mutation CreateEvent {...}\n\nquery MyQuery {...}\n",
#         "operationName": "MyQuery",
#         "variables": {}
#     }
# }
#
# Response payload:
# {
#     "isAuthorized": <true|false>,
#     "resolverContext": {<JSON object, optional>},
#     "deniedFields": [
#         "<list of denied fields (ARNs or short names)>"
#     ],
#     "ttlOverride": <optional value in seconds that overrides the default ttl>
# }
def handler(event, context):
  print(event)
  # strip out Bearer before working with token
  token = event["authorizationToken"].replace("Bearer ", "")
  is_authorized = False

  signing_key = jwks_client.get_signing_key_from_jwt(token)

  try:
    data = jwt.decode(
      token,
      signing_key.key,
      algorithms=["RS256"],
      options= {
        "require": [ "exp", "iat", "sub" ]
      }
    )

    print(data)

    is_authorized = (
      data["iss"] == "https://cognito-idp.{}.amazonaws.com/{}".format(region, user_pool_id) and
      data["sub"] == app_client_id
    )
  except (DecodeError, ExpiredSignatureError, InvalidTokenError) as err:
    print("--- JWT Decode Error: Auth Failure ---")
    print(err)
    is_authorized = False
  except Exception as err:
    print(err)
    raise err
  finally:
    print(f"isAuthorized: {is_authorized}")
    return {
      "isAuthorized": is_authorized,
      "deniedFields": []
    }
