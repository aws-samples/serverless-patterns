import { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from 'aws-lambda';
import { sequelize, Stadium } from './sequelize';
import stadiumData from './stadium-data.json';

exports.handler = async function (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> {
  try {
    await sequelize.authenticate();
    await Stadium.sync({ force: true });
    for(const stadium of stadiumData.stadiums) {
      await Stadium.create(stadium);
    }
  } catch (error) {
    console.error('Unable to connect to the database:', error);
    return {
      statusCode: 500,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(error)
    }
  }
  
  return {
    statusCode: 201,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ "message": "Stadium table and data successfully created." })
  };
};
