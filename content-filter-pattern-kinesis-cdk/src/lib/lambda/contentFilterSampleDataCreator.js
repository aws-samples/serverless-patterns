const { KinesisClient, PutRecordCommand } = require("@aws-sdk/client-kinesis");
const streamName = process.env.SOURCE_STREAM;

// AWS Lambda function that writes a sample event to a Kinesis stream
exports.handler = async (event) => {
   //log streamName
    console.log('Stream name:', streamName);
    const id = 'someID';
    
    const userCreated = {event_type: "USER_CREATED", user_name: "John Doe", birthday: "1995-01-01"};
    const order = {event_type: "ORDER", currency: "EUR", sum:45.99, user_name: "John Doe", birthday: "1995-01-01"};

    const userCreatedParams = {
        StreamName: streamName,
        Data: Buffer.from(JSON.stringify(userCreated)),
        PartitionKey: id
    };  

    const orderParams = {
        StreamName: streamName,
        Data: Buffer.from(JSON.stringify(order)),
        PartitionKey: id
    };  
        
    const client = new KinesisClient();

    await client.send(new PutRecordCommand(userCreatedParams));
    await client.send(new PutRecordCommand(orderParams));
    
    return {
        statusCode: 200,
        body: JSON.stringify('Success'),
    };
};