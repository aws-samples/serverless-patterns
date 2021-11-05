import express from "express";
import AWS from "aws-sdk";

const app = express();
const port = 80;
AWS.config.update({ region: process.env.region });
const sqs = new AWS.SQS({ apiVersion: "2012-11-05" });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const QUEUE_URL = process.env.queueUrl;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate SQS!");
});

app.post("/sendmessage", async (req, res) => {
  const params = {
    MessageBody: req.body.MessageBody,
    QueueUrl: QUEUE_URL,
  };

  try {
    const result = await sqs.sendMessage(params).promise();
    return res.status(200).send({
      body: "OK!",
      sqsResponse: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.get("/readmessage", async (req, res) => {
  const params = {
    QueueUrl: QUEUE_URL,
    MaxNumberOfMessages: 1,
  };

  try {
    const result = await sqs.receiveMessage(params).promise();
    if (result.Messages) {
      return res.status(200).send({
        body: "OK!",
        sqsResponse: result,
      });
    }
    return res.status(200).send({
      body: "no messages in the queue",
    });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
