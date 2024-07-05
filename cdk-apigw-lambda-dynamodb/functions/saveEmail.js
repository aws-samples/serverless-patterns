const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, PutCommand } = require("@aws-sdk/lib-dynamodb");

const client = new DynamoDBClient({region: "us-east-1"});
const docClient = DynamoDBDocumentClient.from(client);
const tableName = process.env.table_name // "CdkApigwLambdaDynamodbStack-CdkSampleTable3353A408-KTF8QLT0JK38"//


const generateUniqueId = (userId) => {
  const timestamp = Date.now().toString();
  return `${userId}-${timestamp}`;
};

const saveEmail = async (email) => {
  const params = {
    TableName: tableName,
    Item: {
      id: generateUniqueId(email),
      email,
    }
  };

  try {
    const res = await docClient.send(new PutCommand(params));
    console.log(res);
    return {
      statusCode: 200,
      body: JSON.stringify("Your email has been saved!"),
    };
  } catch (error) {
      return {
        statusCode: 500,
        body: JSON.stringify({ error: `Error putting into the DB: ${error.message}` }),
      };
    }
};

module.exports.handler = async (event, context) => {
  const { email } = JSON.parse(event.body);

  if (!email) {
    return {
      statusCode: 400,
      body: "Request must have an email address",
    };
  }

  return saveEmail(email);
};

const event = {
  body: JSON.stringify({ email: "email12@example.com" }),
};

module.exports.handler(event).then((res) => console.log(res));
