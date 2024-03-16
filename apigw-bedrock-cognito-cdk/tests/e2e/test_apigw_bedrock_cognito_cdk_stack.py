import pytest
import requests
import jwt
import boto3
import time


# Update the following variables from the CDK Stack Outputs
API_ENDPOINT = ""
USER_POOL_ID = ""

# Test variables
TEST_EMAIL = "johndoe@example.com"
NON_ORG_TEST_EMAIL = None
TEST_FULLNAME = "John Doe"
TEST_PASSWORD = "HelloWorld123!"


class TestClass(object):
    # Helper function to setup the test class
    def setup_class(self):
        self.cognito_client = boto3.client("cognito-idp")

    # Helper function to tear down created users
    def teardown_class(self):
        self.cognito_client.admin_delete_user(
            UserPoolId=USER_POOL_ID, Username=TEST_EMAIL
        )

    # Helper function to handle API requests
    def make_request(self, path, method="post", json=None, headers=None):
        url = API_ENDPOINT + path
        method = method.lower()

        if method == "post":
            response = requests.post(url, json=json, headers=headers)
        elif method == "get":
            response = requests.get(url, headers=headers)
        else:
            raise ValueError("Invalid HTTP method")

        return response

    # Helper function to check common assertions
    def assert_common_response(
        self, response, expected_status_code, expected_message, expected_success=None
    ):
        assert response.status_code == expected_status_code

        response = response.json()

        assert response["message"] == expected_message
        if expected_success is not None:
            assert response["success"] == expected_success

    # Helper function to confirm user status in Cognito
    @pytest.fixture(scope="session")
    def confirm_user_status(self):
        try:
            self.cognito_client.admin_confirm_sign_up(
                UserPoolId=USER_POOL_ID, Username=TEST_EMAIL
            )
        except self.cognito_client.exceptions.NotAuthorizedException as error:
            if (
                error.response["Error"]["Code"] == "NotAuthorizedException"
                and error.response["Error"]["Message"]
                == "User cannot be confirmed. Current status is CONFIRMED"
            ):
                pass
            else:
                raise error

    # Helper function to login in and store the Id and API tokens for re-use
    @pytest.fixture(scope="session")
    def login(self, confirm_user_status):
        response = self.make_request(
            "/login", json={"email": TEST_EMAIL, "password": TEST_PASSWORD}
        )

        id_token = response.json()["message"]["IdToken"]
        api_token = jwt.decode(id_token, options={"verify_signature": False})[
            "custom:api_key"
        ]
        time.sleep(120)
        return id_token, api_token

    # Register empty user
    def test_register_empty_user(self):
        response = self.make_request(
            "/register", json={"email": "", "password": "", "fullname": ""}
        )
        self.assert_common_response(
            response, 422, "Missing required parameters.", False
        )

    # Register user without email
    def test_register_user_without_email(self):
        response = self.make_request(
            "/register",
            json={"email": "", "password": TEST_PASSWORD, "fullname": TEST_FULLNAME},
        )
        self.assert_common_response(
            response, 422, "Missing required parameters.", False
        )

    # Register user without password
    def test_register_user_without_password(self):
        response = self.make_request(
            "/register",
            json={"email": TEST_EMAIL, "password": "", "fullname": TEST_FULLNAME},
        )
        self.assert_common_response(
            response, 422, "Missing required parameters.", False
        )

    # Register user without fullname
    def test_register_user_without_fullname(self):
        response = self.make_request(
            "/register",
            json={"email": TEST_EMAIL, "password": TEST_PASSWORD, "fullname": ""},
        )
        self.assert_common_response(
            response, 422, "Missing required parameters.", False
        )

    # Invalid email format
    def test_register_invalid_email_format(self):
        response = self.make_request(
            "/register",
            json={
                "email": "helloworld",
                "password": TEST_PASSWORD,
                "fullname": TEST_FULLNAME,
            },
        )
        self.assert_common_response(
            response, 400, "Invalid email address format.", False
        )

    # Non org domain
    @pytest.mark.skipif(
        NON_ORG_TEST_EMAIL is None, reason="Non Org domain email is set to None."
    )
    def test_register_non_org_domain(self):
        response = self.make_request(
            "/register",
            json={
                "email": NON_ORG_TEST_EMAIL,
                "password": TEST_PASSWORD,
                "fullname": TEST_FULLNAME,
            },
        )
        assert response.status_code == 400

        response = response.json()

        assert response["message"].startswith(
            "PreSignUp failed with error Cannot register user as email is not part of domain: "
        )
        assert response["success"] == False

    # Unregistered user login
    def test_login_unregistered_user(self):
        response = self.make_request(
            "/login", json={"email": "XXXXXXXXXXXXXXXXXXXXX", "password": TEST_PASSWORD}
        )
        self.assert_common_response(response, 400, "User does not exist.", False)

    # Register User
    @pytest.mark.dependency(name="test_register_user")
    def test_register_user(self):
        response = self.make_request(
            "/register",
            json={
                "email": TEST_EMAIL,
                "password": TEST_PASSWORD,
                "fullname": TEST_FULLNAME,
            },
        )
        self.assert_common_response(
            response, 200, f"User {TEST_EMAIL} created successfully.", True
        )
        assert response.json()["data"]["API Key"] is not None

    # User re-register
    def test_register_user_again(self):
        response = self.make_request(
            "/register",
            json={
                "email": TEST_EMAIL,
                "password": TEST_PASSWORD,
                "fullname": TEST_FULLNAME,
            },
        )
        self.assert_common_response(response, 400, "User already exists", False)

    # Registered user login
    @pytest.mark.dependency(
        name="test_login_registered_user", depends=["test_register_user"]
    )
    def test_login_registered_user(self, login):
        response = self.make_request(
            "/login", json={"email": TEST_EMAIL, "password": TEST_PASSWORD}
        )
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["message"]["AccessToken"] is not None
        assert response.json()["message"]["RefreshToken"] is not None
        assert response.json()["message"]["IdToken"] is not None
        assert response.json()["message"]["ExpiresIn"] == 3600
        assert response.json()["message"]["TokenType"] == "Bearer"

    # GET on /bedrock endpoint without ID Token or API Token
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_get_gaterock(self):
        response = self.make_request("/bedrock", method="get")
        self.assert_common_response(response, 401, "Unauthorized")

    # GET on /bedrock endpoint with API Token and without ID Token
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_get_gaterock_with_api_token(self, login):
        _, api_token = login
        response = self.make_request(
            "/bedrock", method="get", headers={"x-api-key": api_token}
        )
        self.assert_common_response(response, 401, "Unauthorized")

    # GET on /bedrock endpoint with ID Token and without API Token
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_get_gaterock_with_id_token(self, login):
        id_token, _ = login
        response = self.make_request(
            "/bedrock", method="get", headers={"Authorization": id_token}
        )
        self.assert_common_response(response, 403, "Forbidden")

    # GET on /bedrock endpoint with ID Token and API Token
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_get_gaterock_with_id_token_and_api_token(self, login):
        id_token, api_token = login
        response = self.make_request(
            "/bedrock",
            method="get",
            headers={"x-api-key": api_token, "Authorization": id_token},
        )
        self.assert_common_response(
            response, 200, "Successfully retrieved foundation models list.", True
        )

    # POST on /bedrock endpoint for AI21 Jurrasic Mid Model
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_post_gaterock_ai21_jurrasic_ultra_model(self, login):
        id_token, api_token = login
        response = self.make_request(
            "/bedrock",
            json={
                "modelId": "ai21.j2-mid-v1",
                "inferenceParameters": {
                    "prompt": "Hello World!",
                    "maxTokens": 200,
                    "temperature": 0.7,
                    "topP": 1,
                },
            },
            headers={"x-api-key": api_token, "Authorization": id_token},
        )
        self.assert_common_response(
            response,
            200,
            "Successfully retrieved response from foundation model.",
            True,
        )
        assert response.json()["data"] is not None

    # POST on /bedrock endpoint for Anthropic Claude Instant Model
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_post_gaterock_anthropic_claude_2_1_model(self, login):
        id_token, api_token = login
        response = self.make_request(
            "/bedrock",
            json={
                "modelId": "anthropic.claude-instant-v1",
                "inferenceParameters": {
                    "prompt": "\n\nHuman:Hello World!\n\nAssistant:",
                    "max_tokens_to_sample": 200,
                    "stop_sequences": ["\n\nHuman:"],
                },
            },
            headers={"x-api-key": api_token, "Authorization": id_token},
        )
        self.assert_common_response(
            response,
            200,
            "Successfully retrieved response from foundation model.",
            True,
        )
        assert response.json()["data"] is not None

    # POST on /bedrock endpoint for Amazon Titan Model
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_post_gaterock_amazon_titan_model(self, login):
        id_token, api_token = login
        response = self.make_request(
            "/bedrock",
            json={
                "modelId": "amazon.titan-text-express-v1",
                "inferenceParameters": {"inputText": "Hello World!"},
            },
            headers={"x-api-key": api_token, "Authorization": id_token},
        )
        self.assert_common_response(
            response,
            200,
            "Successfully retrieved response from foundation model.",
            True,
        )
        assert response.json()["data"] is not None

    # POST on /bedrock endpoint for Meta Llama Model
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_post_gaterock_meta_llama_model(self, login):
        id_token, api_token = login
        response = self.make_request(
            "/bedrock",
            json={
                "modelId": "meta.llama2-13b-chat-v1",
                "inferenceParameters": {
                    "prompt": "Hello World",
                    "max_gen_len": 128,
                    "temperature": 0.1,
                    "top_p": 0.9,
                },
            },
            headers={"x-api-key": api_token, "Authorization": id_token},
        )
        self.assert_common_response(
            response,
            200,
            "Successfully retrieved response from foundation model.",
            True,
        )
        assert response.json()["data"] is not None

    # POST on /bedrock endpoint without modelId
    @pytest.mark.dependency(depends=["test_login_registered_user"])
    def test_post_gaterock_without_modelId(self, login):
        id_token, api_token = login
        response = self.make_request(
            "/bedrock",
            json={
                "inferenceParameters": {
                    "prompt": "Hello World",
                },
            },
            headers={"x-api-key": api_token, "Authorization": id_token},
        )
        self.assert_common_response(
            response, 422, "Missing required parameters.", False
        )
