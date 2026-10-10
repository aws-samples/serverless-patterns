import express from "express";
import { SNSClient, PublishCommand } from "@aws-sdk/client-sns";
import { SQSClient, ReceiveMessageCommand, DeleteMessageCommand } from "@aws-sdk/client-sqs";

const app = express();
const port = 80;
const region = process.env.region;
const sns = new SNSClient({ region });
const sqs = new SQSClient({ region });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const TOPIC_ARN = process.env.snsTopicArn;
const QUEUE_URL = process.env.queueUrl;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate SNS!");
});

app.post("/publishmessage", async (req, res) => {
  try {
    const result = await sns.send(
      new PublishCommand({
        Message: req.body.MessageBody,
        TopicArn: TOPIC_ARN,
      })
    );
    return res.status(200).send({
      body: "OK!",
      snsResponse: result,
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
