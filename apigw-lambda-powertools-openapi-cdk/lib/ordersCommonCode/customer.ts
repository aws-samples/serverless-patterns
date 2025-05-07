import {
  APIGatewayProxyCognitoAuthorizer,
  APIGatewayProxyEvent,
} from "aws-lambda";

/**
 * Extracts the customer ID from the Cognito authentication information in the API Gateway event
 * @param {Object} params - The parameters object
 * @param {APIGatewayProxyEvent} params.event - The API Gateway event containing Cognito authorizer context
 * @returns {string} The customer ID (Cognito sub claim)
 * @throws {Error} If the authorizer or sub claim is not present
 */
export function getCustomerIdFromAuthInfo({
  event,
}: {
  event: APIGatewayProxyEvent;
}): string {
  return (event.requestContext.authorizer as APIGatewayProxyCognitoAuthorizer)
    .claims["sub"]!;
}
