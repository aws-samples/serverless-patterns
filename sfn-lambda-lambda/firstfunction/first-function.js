exports.handler = async (event) => {
    console.log(event)
    const response = {
        statusCode: 200,
        body: {
            "message":"from Lambda1"
        },
    };
    return response;
};