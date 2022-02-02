import express from "express";
import AWS from "aws-sdk";
import moment from "moment";

const app = express();
const port = 80;
AWS.config.update({ region: process.env.region });
const sfn = new AWS.StepFunctions({ apiVersion: "2016-11-23" });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const STATE_MACHINE_ARN = process.env.stateMachineArn;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate Step Functions!");
});

app.post("/startexecution", async (req, res) => {
  const rightNow = moment().format("YYYYMMDD-hhmmss");

  const params = {
    stateMachineArn: STATE_MACHINE_ARN,
    input: JSON.stringify({
      IsHelloWorldExample: req.body.IsHelloWorldExample,
    }),
    name: `ArchiveAt${rightNow}`,
  };

  try {
    const result = await sfn.startExecution(params).promise();
    return res.status(200).send({
      body: "OK!",
      sfnResponse: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
