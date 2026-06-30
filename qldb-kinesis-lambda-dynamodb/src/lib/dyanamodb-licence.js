const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, UpdateCommand } = require('@aws-sdk/lib-dynamodb');

const client = new DynamoDBClient();
const dynamodb = DynamoDBDocumentClient.from(client);

const { TABLE_NAME } = process.env;

const deleteLicence = async (id, version) => {
  const params = {
    TableName: TABLE_NAME,
    Key: { pk: id },
    UpdateExpression: 'set version=:version, isDeleted=:isDeleted',
    ExpressionAttributeValues: {
      ':version': version,
      ':isDeleted': true,
    },
    ConditionExpression: 'attribute_not_exists(pk) OR version <= :version',
  };

  try {
    await dynamodb.send(new UpdateCommand(params));
    console.log(`Successful deleted id ${id} with version ${version}`);
  } catch(err) {
    console.log(`Unable to update licence: ${id}. Error: ${err}`);
  }
};

const updateLicence = async (id, firstName, lastName, email, address, version) => {
  const params = {
    TableName: TABLE_NAME,
    Key: { pk: id },
    UpdateExpression: 'set firstName=:firstName, lastName=:lastName, email=:email, address=:address, version=:version',
    ExpressionAttributeValues: {
      ':firstName': firstName,
      ':lastName': lastName,
      ':email': email,
      ':address': address,
      ':version': version,
    },
    ConditionExpression: 'attribute_not_exists(pk) OR version <= :version',
  };

  try {
    await dynamodb.send(new UpdateCommand(params));
    console.log(`Successfully created/updated id ${id}`);
  } catch(err) {
    console.log(`Unable to update licence: ${id}. Error: ${err}`);
  }
};

module.exports = {
  deleteLicence,
  updateLicence,
};
