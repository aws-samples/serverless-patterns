import express from "express";
import AWS from "aws-sdk";

const app = express();
const port = 80;
AWS.config.update({ region: process.env.region });
const eventbridge = new AWS.EventBridge({apiVersion: '2015-10-07'});

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const EVENT_BUS_NAME = process.env.eventBusName;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate EventBridge!");
});

app.post("/putevents", async (req, res) => {
  const params = {
    Entries: [
      {
        Detail: JSON.stringify({
          "message": req.body.message,
          "state": "new"
        }),
        DetailType: 'Message',
        EventBusName: EVENT_BUS_NAME,
        Source: 'demo.event',
        Time: new Date,
      }
    ]
  }

  try {
    const result = await eventbridge.putEvents(params).promise();
    return res.status(200).send({
      body: "OK!",
      eventBridgeResponse: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
