export const handler =  function(event, context, callback) {
    console.log(event);
    var token = event.authorizationToken;
    
    switch (token) {
        case 'allow':
            // callback(null, generatePolicy('user', 'Allow', event.methodArn));
            callback(null, generatePolicy('user', 'Allow', event.methodArn));
            break;
        case 'deny':
            // callback(null, generatePolicy('user', 'Deny', event.methodArn));
            callback(null, generatePolicy('user', 'Deny', event.methodArn));
            break;
        case 'unauthorized':
            callback("Unauthorized");   // Return a 401 Unauthorized response
            break;
        default:
            callback(null, generatePolicy('user', 'Deny', event.methodArn));
    }
};

// Help function to generate an IAM policy
var generatePolicy = function(principalId, effect, resource) {
    var authResponse = {};
    
    authResponse.principalId = principalId;
    if (effect && resource) {
        var policyDocument = {};
        policyDocument.Version = '2012-10-17'; 
        policyDocument.Statement = [];
        var statementOne = {};
        statementOne.Action = 'execute-api:Invoke'; 
        statementOne.Effect = effect;
        statementOne.Resource = resource;
        policyDocument.Statement[0] = statementOne;
        authResponse.policyDocument = policyDocument;
    }
    
    // enrichment stub, add code here to add enrichment data
    authResponse.context = {
        "enrichment": "This data comes from Lambda Authorizer"
    };
    return authResponse;
}