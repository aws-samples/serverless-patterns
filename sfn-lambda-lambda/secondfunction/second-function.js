exports.handler = async (event) => {
    console.log('event from the first Lambda:')
    console.log(event)
    const response = {
        statusCode: 200,
        body: {
            "message":"from Lambda1 finally to Lambda2"
        },
    };
    return response;
};