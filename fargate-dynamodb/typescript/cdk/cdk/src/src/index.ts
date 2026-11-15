import express from 'express';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand } from '@aws-sdk/lib-dynamodb';
import moment from 'moment';

const app = express();
const port = 80;
const ddbClient = new DynamoDBClient({ region: process.env.region });
const documentClient = DynamoDBDocumentClient.from(ddbClient);

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.get( '/', ( req, res ) => {
  res.status(200).send( 'Hello world!' );
} );

app.post( '/additem', async ( req, res) => {
  console.log(req.body);

  const params = {
    TableName : process.env.databaseTable,
    Item: {
      ID: Math.floor(Math.random() * Math.floor(10000000)).toString(),
      created: moment().format('YYYYMMDD-hhmmss'),
      metadata: JSON.stringify(req.body),
    }
  }
  try {
    const data = await documentClient.send(new PutCommand(params));
  }
  catch (err) {
    console.log(err);
    return res.send( err );
  }
  return res.status(200).send( { body: 'OK!' } );
});

app.listen( port, () => {
  console.log( `server started at http://localhost:${ port }` );
});
