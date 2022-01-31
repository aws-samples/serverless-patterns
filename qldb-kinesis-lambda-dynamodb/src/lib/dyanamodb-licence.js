// see https://theburningmonk.com/2019/03/just-how-expensive-is-the-full-aws-sdk/
const DynamoDB = require('aws-sdk/clients/dynamodb');

const dynamodb = new DynamoDB.DocumentClient();

const AWSXRay = require('aws-xray-sdk-core');
AWSXRay.captureAWS(require('aws-sdk'));

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
    await dynamodb.update(params).promise();
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
    await dynamodb.update(params).promise();
    console.log(`Successfully created/updated id ${id}`);    
  } catch(err) {
    console.log(`Unable to update licence: ${id}. Error: ${err}`);
  }
};

module.exports = {
  deleteLicence,
  updateLicence,
};