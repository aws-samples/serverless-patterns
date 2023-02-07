// As described in the blog post, we would probably use either API Destinations or API Gateway to integrate with a geocoding endpoint.
// To still be able to explore the pattern, this sample uses a Lambda function to simulate the geocoding endpoint.

exports.handler = async (event) => {

    const responseBody = {
        coordinates: "38.897957, -77.036560"
    };

    const response = {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": JSON.stringify(responseBody),
        "isBase64Encoded": false
    };

    console.log("response: " + JSON.stringify(response))

    return response;
};