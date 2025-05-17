import boto3
import logging
import os
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)

region_name = os.environ["AWS_REGION"]
secret_name = os.environ["SECRET_NAME"]
session = boto3.session.Session()
client = session.client(service_name="secretsmanager", region_name=region_name)

verify_id_header_name = "x-origin-verify"


def lambda_handler(event, context):
    logger.info(f"event: {event}")
    logger.info(f"context {context}")

    # Get headers from incoming event
    headers = event["headers"]

    # Get CloudFront verify id
    if verify_id_header_name not in headers:
        logger.error("Invalid request - No x-origin-verify header")
        raise Exception("Unauthorized")

    # Get secret from Secrets Manager
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    logger.info(f"get_secret_value_response {get_secret_value_response}")
    secret_string = get_secret_value_response["SecretString"]

    header_verify_id = headers[verify_id_header_name]
    if secret_string != header_verify_id:
        logger.error("Invalid request - Invalid x-origin-verify header")
        raise Exception("Unauthorized")

    tmp = event["routeArn"].split(":")
    api_gateway_arn_tmp = tmp[5].split("/")
    region = tmp[3]
    aws_account_id = tmp[4]
    # initialize the policy
    principal_id = "*"
    policy = AuthPolicy(principal_id, aws_account_id)
    policy.restApiId = api_gateway_arn_tmp[0]
    policy.region = region
    policy.stage = api_gateway_arn_tmp[1]

    policy.allow_method(HttpVerb.GET, "/*")
    # Finally, build the policy
    auth_response = policy.build()
    return auth_response


# *** Section 3 : authorization policy helper classes
class HttpVerb:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    HEAD = "HEAD"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    ALL = "*"


class AuthPolicy(object):
    awsAccountId = ""
    """The AWS account id the policy will be generated for. This is used to create the method ARNs."""
    principalId = ""
    """The principal used for the policy, this should be a unique identifier for the end user."""
    version = "2012-10-17"
    """The policy version used for the evaluation. This should always be '2012-10-17'"""
    pathRegex = "^[/.a-zA-Z0-9-\*]+$"
    """The regular expression used to validate resource paths for the policy"""

    """these are the internal lists of allowed and denied methods. These are lists
    of objects and each object has 2 properties: A resource ARN and a nullable
    conditions statement.
    the build method processes these lists and generates the appropriate
    statements for the final policy"""
    allowMethods = []
    denyMethods = []

    restApiId = "<<restApiId>>"
    """ Replace the placeholder value with a default API Gateway API id to be used in the policy. 
    Beware of using '*' since it will not simply mean any API Gateway API id, because stars will greedily expand over '/' or other separators. 
    See https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html for more details. """

    region = "<<region>>"
    """ Replace the placeholder value with a default region to be used in the policy. 
    Beware of using '*' since it will not simply mean any region, because stars will greedily expand over '/' or other separators. 
    See https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html for more details. """

    stage = "<<stage>>"
    """ Replace the placeholder value with a default stage to be used in the policy. 
    Beware of using '*' since it will not simply mean any stage, because stars will greedily expand over '/' or other separators. 
    See https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html for more details. """

    def __init__(self, principal, aws_account_id):
        self.awsAccountId = aws_account_id
        self.principalId = principal
        self.allowMethods = []
        self.denyMethods = []

    def _add_method(self, effect, verb, resource, conditions):
        """Adds a method to the internal lists of allowed or denied methods. Each object in
        the internal list contains a resource ARN and a condition statement. The condition
        statement can be null."""
        if verb != "*" and not hasattr(HttpVerb, verb):
            raise NameError(
                "Invalid HTTP verb " + verb + ". Allowed verbs in HttpVerb class"
            )
        resource_pattern = re.compile(self.pathRegex)
        if not resource_pattern.match(resource):
            raise NameError(
                "Invalid resource path: "
                + resource
                + ". Path should match "
                + self.pathRegex
            )

        if resource[:1] == "/":
            resource = resource[1:]

        resource_arn = (
            "arn:aws:execute-api:"
            + self.region
            + ":"
            + self.awsAccountId
            + ":"
            + self.restApiId
            + "/"
            + self.stage
            + "/"
            + verb
            + "/"
            + resource
        )

        if effect.lower() == "allow":
            self.allowMethods.append(
                {"resourceArn": resource_arn, "conditions": conditions}
            )
        elif effect.lower() == "deny":
            self.denyMethods.append(
                {"resourceArn": resource_arn, "conditions": conditions}
            )

    def _get_empty_statement(self, effect):
        """Returns an empty statement object prepopulated with the correct action and the
        desired effect."""
        statement = {
            "Action": "execute-api:Invoke",
            "Effect": effect[:1].upper() + effect[1:].lower(),
            "Resource": [],
        }

        return statement

    def _get_statement_for_effect(self, effect, methods):
        """This function loops over an array of objects containing a resourceArn and
        conditions statement and generates the array of statements for the policy."""
        statements = []

        if len(methods) > 0:
            statement = self._get_empty_statement(effect)

            for curMethod in methods:
                if curMethod["conditions"] is None or len(curMethod["conditions"]) == 0:
                    statement["Resource"].append(curMethod["resourceArn"])
                else:
                    conditional_statement = self._get_empty_statement(effect)
                    conditional_statement["Resource"].append(curMethod["resourceArn"])
                    conditional_statement["Condition"] = curMethod["conditions"]
                    statements.append(conditional_statement)

            statements.append(statement)

        return statements

    def allow_all_methods(self):
        """Adds a '*' allow to the policy to authorize access to all methods of an API"""
        self._add_method("Allow", HttpVerb.ALL, "*", [])

    def deny_all_methods(self):
        """Adds a '*' allow to the policy to deny access to all methods of an API"""
        self._add_method("Deny", HttpVerb.ALL, "*", [])

    def allow_method(self, verb, resource):
        """Adds an API Gateway method (Http verb + Resource path) to the list of allowed
        methods for the policy"""
        self._add_method("Allow", verb, resource, [])

    def deny_method(self, verb, resource):
        """Adds an API Gateway method (Http verb + Resource path) to the list of denied
        methods for the policy"""
        self._add_method("Deny", verb, resource, [])

    def allow_method_with_conditions(self, verb, resource, conditions):
        """Adds an API Gateway method (Http verb + Resource path) to the list of allowed
        methods and includes a condition for the policy statement. More on AWS policy
        conditions here: http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition
        """
        self._add_method("Allow", verb, resource, conditions)

    def deny_method_with_conditions(self, verb, resource, conditions):
        """Adds an API Gateway method (Http verb + Resource path) to the list of denied
        methods and includes a condition for the policy statement. More on AWS policy
        conditions here: http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition
        """
        self._add_method("Deny", verb, resource, conditions)

    def build(self):
        """Generates the policy document based on the internal lists of allowed and denied
        conditions. This will generate a policy with two main statements for the effect:
        one statement for Allow and one statement for Deny.
        Methods that includes conditions will have their own statement in the policy."""
        if (self.allowMethods is None or len(self.allowMethods) == 0) and (
            self.denyMethods is None or len(self.denyMethods) == 0
        ):
            raise NameError("No statements defined for the policy")

        policy = {
            "principalId": self.principalId,
            "policyDocument": {"Version": self.version, "Statement": []},
        }

        policy["policyDocument"]["Statement"].extend(
            self._get_statement_for_effect("Allow", self.allowMethods)
        )
        policy["policyDocument"]["Statement"].extend(
            self._get_statement_for_effect("Deny", self.denyMethods)
        )

        return policy
