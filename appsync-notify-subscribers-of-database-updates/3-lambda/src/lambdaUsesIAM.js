require('isomorphic-fetch');
const AWS = require('aws-sdk/global');
const AUTH_TYPE = require('aws-appsync').AUTH_TYPE;
const AWSAppSyncClient = require('aws-appsync').default;
const gql = require('graphql-tag');

const config = {
    url: process.env.APPSYNC_ENDPOINT,
    region: process.env.AWS_REGION,
    auth: {
        type: AUTH_TYPE.AWS_IAM,
        credentials: AWS.config.credentials,
    },
    disableOffline: true
};

const createTodo = gql`
    mutation MyMutation(
        $orderId: ID!,
		    $status: Status!,
		    $prevStatus: Status,
		    $updatedAt: AWSDateTime!
    ) {
      publishStatusUpdate(
        orderId: $orderId,
		    status: $status,
		    prevStatus: $prevStatus,
		    updatedAt: $updatedAt
		  ) {
        orderId
        prevStatus
        status
        updatedAt
      }
    }
`;

const client = new AWSAppSyncClient(config);

exports.handler = async function (event) {
    console.log("event ", event);

    try {
        const result = await client.mutate({
            mutation: createTodo,
            variables: {
                orderId: "123",
                prevStatus: "PENDING",
                status: "IN_PROGRESS",
                updatedAt: "2021-10-07T20:38:18.683Z"
            }
        });
        console.log("result ", result);
    } catch (error) {
        console.log("error ", error);
    }
};
