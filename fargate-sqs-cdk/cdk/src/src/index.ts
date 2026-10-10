import express from "express";
import {
  SQSClient,
  SendMessageCommand,
  ReceiveMessageCommand,
  DeleteMessageCommand,
} from "@aws-sdk/client-sqs";

const app = express();
const port = 80;
const sqs = new SQSClient({ region: process.env.region });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const QUEUE_URL = process.env.queueUrl;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate SQS!");
});

app.post("/sendmessage", async (req, res) => {
  try {
    const result = await sqs.send(
      new SendMessageCommand({
        MessageBody: req.body.MessageBody,
        QueueUrl: QUEUE_URL,
      })
    );
    return res.status(200).send({
      body: "OK!",
      sqsResponse: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.get("/readmessage", async (req, res) => {
  try {
    const result = await sqs.send(
      new ReceiveMessageCommand({
        QueueUrl: QUEUE_URL,
        MaxNumberOfMessages: 1,
      })
    );
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
  console.log(`server started at http://localhost:${port}`);
});
