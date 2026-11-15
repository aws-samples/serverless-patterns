import express from "express";
import { SNSClient, PublishCommand } from "@aws-sdk/client-sns";

const app = express();
const port = 80;
const snsClient = new SNSClient({ region: process.env.region });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const TOPIC_ARN = process.env.topicArn;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate SNS!");
});

app.post("/sendmessage", async (req, res) => {
  const command = new PublishCommand({
    Message: req.body.Message,
    TopicArn: TOPIC_ARN,
  });

  try {
    const result = await snsClient.send(command);
    return res.status(200).send({
      body: "OK!",
      snsResponse: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  console.log(`server started at http://localhost:${port}`);
});
