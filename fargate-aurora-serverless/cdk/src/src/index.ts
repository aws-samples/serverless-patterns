import express from "express";
import AWS from "aws-sdk";

const app = express();
const port = 80;
AWS.config.update({ region: process.env.region });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const SECRET_ARN = process.env.secretArn;
const DB_CLUSTER_ARN = process.env.dbClusterArn;
const DB_NAME = process.env.dbName;

app.get("/", (req, res) => {
  res.status(200).send(`Hello Serverless Fargate! Integrating with Aurora Serverless Cluster ${DB_NAME} Database`);
});

app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
