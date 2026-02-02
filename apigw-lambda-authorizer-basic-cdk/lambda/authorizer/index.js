// mock database for user credentials
const database = {
    user1: 'password1',
    user2: 'password2'
}

exports.handler = async (event) => {
    try {
        const credentials = decodeAuthorizationHeader(event.authorizationToken);
        const retrievedPassword = await retrieveUserPassword(credentials.username);

        const isUserAuthorizer = (retrievedPassword && retrievedPassword === credentials.password) ? 'Allow': 'Deny';
        const iamPolicy = generatePolicy(credentials.username, isUserAuthorizer, event.methodArn);

        

        return iamPolicy;
    } catch (error) {
        console.error("Error:", error);
        return generatePolicy('undefined', 'Deny', event.methodArn);
    }
};

// decode the authorization header
function decodeAuthorizationHeader(authorization) {
    if (!authorization.startsWith('Basic ')) {
        throw new Error('Invalid authorization header');
    }

    const encodedCredentials = authorization.split('Basic ')[1];
    const decodedCredentials = Buffer.from(encodedCredentials, 'base64').toString('utf-8');
    const [username, password] = decodedCredentials.split(":");

    return {username, password};
}

// retrieve the user password from the mock database
async function retrieveUserPassword(username) {
    return database[username];
}

// generate an IAM policy
function generatePolicy(principalId, effect, resource) {
    const iamPolicy = {
        principalId: principalId,
        policyDocument: {
            Version: '2012-10-17',
            Statement: [{
                Action: 'execute-api:Invoke',
                Effect: effect,
                Resource: resource
            }]
        }
    };

    return iamPolicy;
}
