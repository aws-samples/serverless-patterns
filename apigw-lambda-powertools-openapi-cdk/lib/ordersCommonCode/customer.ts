import {
  APIGatewayProxyCognitoAuthorizer,
  APIGatewayProxyEvent,
} from "aws-lambda";

/**
 * Extracts the customer ID from the authentication information in the API Gateway event
 * @param {Object} params - The parameters object
 * @param {APIGatewayProxyEvent} params.event - The API Gateway event containing authorizer context
 * @returns {string} The customer ID (from Cognito username or sub claim)
 */
export function getCustomerIdFromAuthInfo({
  event,
}: {
  event: APIGatewayProxyEvent;
}): string {
  try {
    // Check for JWT authorizer (API Gateway v2)
    if (event.requestContext?.authorizer?.jwt?.claims) {
      const claims = event.requestContext.authorizer.jwt.claims;
      return claims["cognito:username"] || claims["sub"] || "TEST-CUSTOMER";
    }
    
    // Check for Lambda authorizer or Cognito authorizer (API Gateway v1)
    if (event.requestContext?.authorizer?.claims) {
      const claims = event.requestContext.authorizer.claims;
      return claims["cognito:username"] || claims["sub"] || "TEST-CUSTOMER";
    }
    
    // Fallback for testing
    return "TEST-CUSTOMER";
  } catch (error) {
    console.warn("Could not extract customer ID from auth info:", error);
    return "TEST-CUSTOMER";
  }
}