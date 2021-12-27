import express from "express";
import AWS from "aws-sdk";

const app = express();
const port = 80;
AWS.config.update({ region: process.env.region });
const sns = new AWS.SNS({ apiVersion: "2010-03-31" });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const TOPIC_ARN = process.env.topicArn;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate SNS!");
});

app.post("/sendmessage", async (req, res) => {
  const params = {
    Message: req.body.Message,
    TopicArn: TOPIC_ARN,
  };

  try {
    const result = await sns.publish(params).promise();
    return res.status(200).send({
      body: "OK!",
      snsResponse: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
