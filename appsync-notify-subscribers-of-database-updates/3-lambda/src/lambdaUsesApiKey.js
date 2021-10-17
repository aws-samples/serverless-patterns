const axios = require('axios');
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

exports.handler = async (event) => {
    try {
        const graphqlData = await axios({
            url: process.env.APPSYNC_ENDPOINT,
            method: 'post',
            headers: {
                'x-api-key': process.env.APPSYNC_APIKEY
            },
            data: {
                query: print(createTodo),
                variables: {
                    orderId: "123",
                    prevStatus: "PENDING",
                    status: "IN_PROGRESS",
                    updatedAt: "2021-10-07T20:38:18.683Z"

                }
            }
        });
        console.log("graphqlData ", graphqlData["data"]["errors"]);
        const body = {
            message: "successfully created todo!"
        }
        return {
            statusCode: 200,
            body: JSON.stringify(body),
            headers: {
                "Access-Control-Allow-Origin": "*",
            }
        }
    } catch (err) {
        console.log('error creating todo: ', err);
    }
}
