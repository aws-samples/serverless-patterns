import express from "express";
import AWS from "aws-sdk";

const app = express();
const port = 80;
AWS.config.update({ region: process.env.region });
const s3 = new AWS.S3({ apiVersion: "2006-03-01" });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate with S3!");
});

const BUCKET = process.env.bucketName;

app.get("/listobjects", async (req, res) => {
  const params = {
    Bucket: BUCKET,
    MaxKeys: 2,
  };

  try {
    const data = await s3.listObjectsV2(params).promise();
    const s3Objects = data.Contents.map((obj) => obj.Key);
    return res.status(200).send({ body: s3Objects });
  } catch (err) {
    return res.send(err);
  }
});

app.post("/putobject", async (req, res) => {
  const params = {
    Body: req.body.Body,
    Bucket: BUCKET,
    Key: req.body.Key,
  };

  try {
    await s3.putObject(params).promise();
  } catch (err) {
    return res.send(err);
  }
  return res.status(200).send({ body: "OK!" });
});

app.get("/getobject", async (req, res) => {
  const params = {
    Bucket: BUCKET,
    Key: req.body.Key,
  };

  try {
    const data = await s3.getObject(params).promise();
    const dataContent = data.Body.toString("utf-8");
    return res.status(200).send({ body: dataContent });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
