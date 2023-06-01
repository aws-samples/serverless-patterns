
const cognito = require('amazon-cognito-identity-js');

const poolData = {
    UserPoolId: process.env.COGNITO_USER_POOL,
    ClientId: process.env.COGNITO_USER_POOL_CLIENT
};
const userPool = new cognito.CognitoUserPool(poolData);

const getTokens = (authResult) => {
    const accessToken = authResult.getAccessToken().getJwtToken();
    const refreshToken = authResult.getRefreshToken().getToken();
    const tokenId = authResult.getIdToken().getJwtToken();

    return {
        accessToken,
        refreshToken,
        tokenId
    };
};

const authenticate = (cognitoUser, authenticationDetails) => {
    return new Promise((resolve, reject) => {
        cognitoUser.authenticateUser(authenticationDetails, {
            onSuccess: (result) => {
                resolve(getTokens(result))
            },
            onFailure: (error) => {
                reject(error);
            }
        })
    })
}

module.exports.handler = async (event, context) => {
    console.log(event)
    try {
        const data = JSON.parse(event.body)
        const user = data.user
        const password = data.password

        if(!user || !password) {
            const err = 'User and password must be provided for user authentication.';
            console.log(err)
            return {
                statusCode: 500,
                headers: {
                    'Content-Type': 'text/plain',
                    'Access-Control-Allow-Origin': '*'
                },
                body: err
            }
        }
        else {
            const authenticationData = {
                Username: user,
                Password: password
            };
            const authenticationDetails = new cognito.AuthenticationDetails(authenticationData);

            const userData = {
                Username: user,
                Pool: userPool
            };
            const cognitoUser = new cognito.CognitoUser(userData);

            const result = await authenticate(cognitoUser, authenticationDetails);

            const response = {
                token: result.tokenId,
                refresh: result.refreshToken,
                user
            }
            return {
                statusCode: 200,
                headers: {
                    'Content-Type': 'text/plain',
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify(response)
            }
        }
    } catch(err) {
        console.log(err)
        return {
            statusCode: 500,
            headers: {
                'Content-Type': 'text/plain',
                'Access-Control-Allow-Origin': '*'
            },
            body: 'Unable to authenticate user using AWS Cognito'
        }
    }
}