import express from "express";
import { SFNClient, StartExecutionCommand } from "@aws-sdk/client-sfn";
import moment from "moment";

const app = express();
const port = 80;
const sfnClient = new SFNClient({ region: process.env.region });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const STATE_MACHINE_ARN = process.env.stateMachineArn;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate Step Functions!");
});

app.post("/startexecution", async (req, res) => {
  const rightNow = moment().format("YYYYMMDD-hhmmss");

  const command = new StartExecutionCommand({
    stateMachineArn: STATE_MACHINE_ARN,
    input: JSON.stringify({
      IsHelloWorldExample: req.body.IsHelloWorldExample,
    }),
    name: `ArchiveAt${rightNow}`,
  });

  try {
    const result = await sfnClient.send(command);
    return res.status(200).send({
      body: "OK!",
      sfnResponse: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  console.log(`server started at http://localhost:${port}`);
});
