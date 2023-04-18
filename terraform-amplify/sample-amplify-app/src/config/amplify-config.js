// -- AWS AMPLIFY CONFIGURATION PARAMETERS --

// eslint-disable-next-line import/no-unresolved

// Uncomment this to test env vars
// console.log('env', import.meta.env);

const AmplifyConfig = {
  // Existing API
  API: {
    aws_appsync_graphqlEndpoint: import.meta.env.VITE_GRAPHQL_URL,
    aws_appsync_region: import.meta.env.VITE_REGION,
    aws_appsync_authenticationType: 'AMAZON_COGNITO_USER_POOLS', // No touchy
  },
  // Existing Auth
  Auth: {
    // REQUIRED only for Federated Authentication - Amazon Cognito Identity Pool ID
    identityPoolId: import.meta.env.VITE_IDENTITY_POOL_ID,

    // REQUIRED - Amazon Cognito Region
    region: import.meta.env.VITE_REGION,

    // OPTIONAL - Amazon Cognito Federated Identity Pool Region
    // Required only if it's different from Amazon Cognito Region
    identityPoolRegion: import.meta.env.VITE_REGION,

    // REQUIRED - Amazon Cognito User Pool ID
    userPoolId: import.meta.env.VITE_USER_POOL_ID,

    // REQUIRED - Amazon Cognito Web Client ID (26-char alphanumeric string)
    userPoolWebClientId: import.meta.env.VITE_APP_CLIENT_ID,

    // OPTIONAL - Enforce user authentication prior to accessing AWS resources or not
    mandatorySignIn: true,

    // OPTIONAL - Hosted UI configuration
    // oauth: {
    //   domain: 'your_cognito_domain',
    //   scope: [
    //     'phone',
    //     'email',
    //     'profile',
    //     'openid',
    //     'aws.cognito.signin.user.admin',
    //   ],
    //   redirectSignIn: 'http://localhost:3000/',
    //   redirectSignOut: 'http://localhost:3000/',
    //   responseType: 'code', // or 'token', note that REFRESH token will only be generated when the responseType is code
    // },
  },

  Storage: {
    AWSS3: {
      bucket: import.meta.env.VITE_LANDING_BUCKET, // REQUIRED -  Amazon S3 bucket name
      region: import.meta.env.VITE_REGION, // Required -  Amazon service region
    },
  },
};

export { AmplifyConfig };
