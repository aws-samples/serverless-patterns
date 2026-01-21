import { CognitoJwtVerifier } from "aws-jwt-verify";

let userPoolId = process.env.userPoolId;
let clientId = process.env.clientId;

// Verifier that expects valid access tokens:
const verifier = CognitoJwtVerifier.create({
  userPoolId: userPoolId,
  tokenUse: "access",
  clientId: clientId,
});

function generatePolicy(principalId, effect, resource) {
  const authResponse = {
    principalId,
  };

  if (effect && resource) {
    const policyDocument = {
      Version: '2012-10-17',
      Statement: [
        {
          Action: 'execute-api:Invoke',
          Effect: effect,
          Resource: resource,
        },
      ],
    };
    authResponse.policyDocument = policyDocument;
  }

  return JSON.stringify(authResponse);
}

function generateAllow(principalId, resource) {
  return generatePolicy(principalId, 'Allow', resource);
}

function generateDeny(principalId, resource) {
  return generatePolicy(principalId, 'Deny', resource);
}

export const handler = async (event) => {
  // TODO implement
    let Authtoken = event.headers.Authorization
    try {
    const payload = await verifier.verify(
      Authtoken 
    );
    console.log("Token is valid. Payload:", payload);
    const response = generateAllow('me', event.methodArn);
    return JSON.parse(response);
  } catch {
    console.log('unauthorized');
    const response = generateDeny('me', event.methodArn);
    return JSON.parse(response);
  }
};
