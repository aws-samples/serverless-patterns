
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

exports.handler = async function(event, context) {
  // For debug purposes only.
  // You should not log any sensitive information in production.
  console.log("EVENT: \n" + JSON.stringify(event, null, 2));

  const { headers, queryStringParameters, methodArn } = event;

  // This is for demo purposes only.
  // This check is probably not valuable in production.
  if((headers && headers['X-Forwarded-Proto'] === 'https') 
    || (queryStringParameters && queryStringParameters.proto === 'https')) {
    return createAuthorizedResponse(methodArn);
  } else {
    throw new Error('Unauthorized');
  }
}

