const { SignatureV4 } = require('@aws-sdk/signature-v4');
const { HttpRequest } = require('@smithy/protocol-http');
const { defaultProvider } = require('@aws-sdk/credential-provider-node');
const { Sha256 } = require('@aws-crypto/sha256-js');
const gql = require('graphql-tag');
const graphql = require('graphql');
const { print } = graphql;

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

const signer = new SignatureV4({
    credentials: defaultProvider(),
    region: process.env.AWS_REGION,
    service: 'appsync',
    sha256: Sha256
});

exports.handler = async function (event) {
    console.log("event ", event);

    try {
        const url = new URL(process.env.APPSYNC_ENDPOINT);
        const query = print(createTodo);
        const variables = {
            orderId: "123",
            prevStatus: "PENDING",
            status: "IN_PROGRESS",
            updatedAt: "2021-10-07T20:38:18.683Z"
        };

        const requestBody = JSON.stringify({ query, variables });

        const request = new HttpRequest({
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                host: url.host
            },
            hostname: url.hostname,
            path: url.pathname,
            body: requestBody
        });

        const signedRequest = await signer.sign(request);

        const response = await fetch(process.env.APPSYNC_ENDPOINT, {
            method: signedRequest.method,
            headers: signedRequest.headers,
            body: requestBody
        });

        const result = await response.json();
        console.log("result ", result);
    } catch (error) {
        console.log("error ", error);
    }
};
