import { Signer } from "@aws-sdk/rds-signer"; // ES Modules import
import { unmarshall } from "@aws-sdk/util-dynamodb";
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

export async function handler(event, context, callback) {

  try {

        await Promise.all(event.Records.map(async (record) => {
            console.log('Stream record: ', JSON.stringify(record, null, 2));
            if (record.eventName == 'INSERT') {
                var obj = unmarshall(record.dynamodb.NewImage);
                console.log('Processing order with id: ', obj.orderid);

                const [rows,fields] = await connection.query('CALL InsertOrder(?, ?, ?)',
                    [
                        obj.orderid,
                        obj.status,
                        obj.lastUpdateDate
                    ]
                );
                console.log('orders insert result: ', rows);
                
                await Promise.all(obj.items.map(async (item) => {
                    console.log(obj.orderid, item.itemid, item.quantity);
                    const [rows,fields] = await connection.query('CALL InsertOrderItem(?, ?, ?)',
                        [
                            obj.orderid,
                            item.itemid,
                            item.quantity
                        ]
                    );                    
                }));
            }   
        }));
      
        const response = {
           statusCode: 200,
           body: `Processed ${event.Records.length} records.`
       };
       return response;
  
  }
  catch (e){
        const response = {
           statusCode: 500,
           body: 'Error porcessing records. : ' + JSON.stringify(e)
       };
       return response;      
  }

}
