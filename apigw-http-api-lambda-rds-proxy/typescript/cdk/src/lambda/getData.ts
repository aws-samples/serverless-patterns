import { APIGatewayProxyResultV2 } from 'aws-lambda';
import { Stadium } from './sequelize';

exports.handler = async function (): Promise<APIGatewayProxyResultV2> {
  try {
    return {
      statusCode: 200,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(await Stadium.findAll())
    };
  } catch (error) {
    console.error('Unable to connect to the database:', error);
    return {
      statusCode: 500,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(error)
    }
  }
};
