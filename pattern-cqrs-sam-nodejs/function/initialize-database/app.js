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
  
  console.log("REQUEST RECEIVED:\n" + JSON.stringify(event));

  console.log('Creating Database Schema');
  
  try {
    console.log('Creating table orders');
    let [rows,fields] = await connection.query(` 
        CREATE TABLE orders( 
      	orderid VARCHAR(40) PRIMARY KEY,
      	orderstatus VARCHAR(255),
      	orderdate DATETIME
      )
    `);
    console.log('Table orders created successfully:', rows);
    
    console.log('Creating table orderitems');
    [rows,fields] = await connection.query(` 
      CREATE TABLE orderitems(
      	orderitemid BINARY(16) PRIMARY KEY,
      	itemid VARCHAR(40),
      	quantity SMALLINT,
      	orderid VARCHAR(40),
      	CONSTRAINT fk_order
          FOREIGN KEY (orderid) 
              REFERENCES orders(orderid)
      )
    `);
    console.log('Table orderitems created successfully:', rows);
       
    console.log('Creating procedure InsertOrder');
    [rows,fields] = await connection.query(` 
      CREATE PROCEDURE InsertOrder(
      	IN p_orderid VARCHAR(40),
      	IN p_orderstatus VARCHAR(255),
      	IN p_orderdate BIGINT
      )
      
      BEGIN
      
      INSERT INTO orders (orderid, orderstatus, orderdate)
      VALUES (p_orderid,p_orderstatus,FROM_UNIXTIME(p_orderdate * 0.001));
      
      END
    `);
    console.log('Procedure InsertOrder created successfully:', rows);
       
    console.log('Creating procedure InsertOrderItem');
    [rows,fields] = await connection.query(` 
      CREATE PROCEDURE InsertOrderItem(
      	IN p_orderid VARCHAR(40),
      	IN p_itemid VARCHAR(40),
      	IN p_quantity SMALLINT
      )
      
      BEGIN
      
      INSERT INTO orderitems (orderitemid, orderid, itemid, quantity)
      VALUES (UUID_TO_BIN(UUID()), p_orderid, p_itemid, p_quantity);
      
      END
    `);
    console.log('Procedure InsertOrderItem created successfully:', rows);       
    
    console.log('Creating procedure GetItemReport');
    [rows,fields] = await connection.query(` 
      CREATE PROCEDURE GetItemReport()
      
      BEGIN
      
      SELECT a.itemid, SUM(a.quantity) as totalordered, DATE_FORMAT(MAX(b.orderdate),'%Y-%m-%d') as lastorderdate
      FROM orderitems a LEFT JOIN orders b ON a.orderid = b.orderid
      GROUP BY a.itemid;
      
      END
    `);
    console.log('Procedure GetItemReport created successfully:', rows);      
    
    console.log('Creating procedure GetMonthlyItemOrders');
    [rows,fields] = await connection.query(` 
      CREATE PROCEDURE GetMonthlyItemOrders(
      	IN p_itemid VARCHAR(40)
      )
      
      BEGIN
      
      SELECT DATE_FORMAT(b.orderdate,'%M %Y') as monthyear, SUM(a.quantity) as monthlyordered
      FROM orderitems a LEFT JOIN orders b ON a.orderid = b.orderid
      WHERE itemid = p_itemid
      GROUP BY year(b.orderdate),month(b.orderdate)
      ORDER BY b.orderdate DESC;
      
      END
    `);
    console.log('Procedure GetMonthlyItemOrders created successfully:', rows);

  }  
  catch (e){
       console.log('Error initializing database. : ' + JSON.stringify(e))
  }
}