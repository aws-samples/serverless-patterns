import { Signer } from "@aws-sdk/rds-signer"; // ES Modules import
import mysql from  "mysql2/promise";

const signer = new Signer({
    region: process.env.AWS_REGION, // example: us-east-2
    hostname: process.env.PROXY_ENDPOINT,
    port: 3306,
    username: process.env.DB_USER
});

console.log ("IAM Token obtained\n");

const connectionConfig = {
  host: process.env.PROXY_ENDPOINT,
  user: process.env.DB_USER,
  database: process.env.DB_NAME,
  ssl: 'Amazon RDS',
  authPlugins: { mysql_clear_password: () => () => signer.getAuthToken() }
}

const connection = await mysql.createConnection(connectionConfig);

console.log('Connected to MySQL\n')

export async function handler(event, context) {
  let response = null;
  
  console.log('Event: ', event);
  console.log('Context: ', context);
  console.log('Processing order with id: ', event.pathParameters.itemId);
  const [rows,fields] = await connection.query('CALL GetMonthlyItemOrders(?)',event.pathParameters.itemId);
  console.log(rows,fields);

  response = {
    statusCode: 200,
    body: JSON.stringify(rows[0])
  };
  return response;
}