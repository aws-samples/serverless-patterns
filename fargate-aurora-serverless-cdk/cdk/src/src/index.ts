import express from "express";
import AWS from "aws-sdk";

const app = express();
const port = 80;

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const rdsDataService = new AWS.RDSDataService();

const SECRET_ARN = process.env.secretArn;
const DB_CLUSTER_ARN = process.env.dbClusterArn;
const DB_NAME = process.env.dbName;

let sqlParams = {
  secretArn: SECRET_ARN,
  resourceArn: DB_CLUSTER_ARN,
  database: DB_NAME,
  includeResultMetadata: true,
  sql: "",
};

app.get("/", (req, res) => {
  res.status(200).send(`Hello Serverless Fargate! Integrating with Aurora Serverless Cluster ${DB_NAME} Database`);
});

app.post("/createtable", async (req, res) => {
  const tableName = req.body.tableName;
  const sqlCreateTable = `CREATE TABLE IF NOT EXISTS ${tableName} (id INT AUTO_INCREMENT PRIMARY KEY, foo VARCHAR(128), bar VARCHAR(128));`;
  sqlParams["sql"] = sqlCreateTable;

  try {
    const result = await rdsDataService.executeStatement(sqlParams).promise();
    return res.status(200).send({
      body: "OK!",
      response: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.get("/showtables", async (req, res) => {
  const sqlShowTables = "SHOW TABLES;";
  sqlParams["sql"] = sqlShowTables;

  try {
    const result = await rdsDataService.executeStatement(sqlParams).promise();
    return res.status(200).send({
      body: "OK!",
      response: result.records,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
