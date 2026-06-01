import express from "express";
import { S3Client, ListObjectsV2Command, PutObjectCommand, GetObjectCommand } from "@aws-sdk/client-s3";

const app = express();
const port = 80;
const s3 = new S3Client({ region: process.env.region });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate with S3!");
});

const BUCKET = process.env.bucketName;

app.get("/listobjects", async (req, res) => {
  try {
    const data = await s3.send(new ListObjectsV2Command({
      Bucket: BUCKET,
      MaxKeys: 2,
    }));
    const s3Objects = (data.Contents || []).map((obj) => obj.Key);
    return res.status(200).send({ body: s3Objects });
  } catch (err) {
    return res.send(err);
  }
});

app.post("/putobject", async (req, res) => {
  try {
    await s3.send(new PutObjectCommand({
      Body: req.body.Body,
      Bucket: BUCKET,
      Key: req.body.Key,
    }));
  } catch (err) {
    return res.send(err);
  }
  return res.status(200).send({ body: "OK!" });
});

app.get("/getobject", async (req, res) => {
  try {
    const data = await s3.send(new GetObjectCommand({
      Bucket: BUCKET,
      Key: req.body.Key,
    }));
    const dataContent = await data.Body!.transformToString("utf-8");
    return res.status(200).send({ body: dataContent });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  console.log(`server started at http://localhost:${port}`);
});
