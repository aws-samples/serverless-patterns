
const { CognitoJwtVerifier } = require("aws-jwt-verify");

const userPoolId = process.env.COGNITO_USER_POOL,
  clientId = process.env.COGNITO_USER_POOL_CLIENT;

function createAuthorizedResponse(resource) {
  return {
    principalId: 'me',
    policyDocument: {
      Version: '2012-10-17',
      Statement: [{
        Action: 'execute-api:Invoke',
        Effect: 'Allow',
        Resource: resource
      }]
    }
  };
}

const verifier = CognitoJwtVerifier.create({
  userPoolId,
  tokenUse: "id",
  clientId
});

exports.handler = async function(event, context) {

  console.log("EVENT: \n" + JSON.stringify(event, null, 2));
  const { headers, queryStringParameters, methodArn } = event;
  if(queryStringParameters && queryStringParameters.Authorizer) {
    try {
    const payload = await verifier.verify(queryStringParameters.Authorizer);
    console.log("Token is valid. Payload:", payload);
    return createAuthorizedResponse(methodArn);
    } catch {
      console.log("Token not valid!");
      throw new Error("Token not valid!");
    }
  } else {
    throw new Error('Unauthorized');
  }
}
