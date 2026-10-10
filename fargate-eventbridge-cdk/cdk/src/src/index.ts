import express from "express";
import { EventBridgeClient, PutEventsCommand } from "@aws-sdk/client-eventbridge";

const app = express();
const port = 80;
const eventbridge = new EventBridgeClient({ region: process.env.region });

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const EVENT_BUS_NAME = process.env.eventBusName;

app.get("/", (req, res) => {
  res.status(200).send("Hello Serverless Fargate EventBridge!");
});

app.post("/putevents", async (req, res) => {
  const command = new PutEventsCommand({
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
  });

  try {
    const result = await eventbridge.send(command);
    return res.status(200).send({
      body: "OK!",
      eventBridgeResponse: result,
    });
  } catch (err) {
    return res.send(err);
  }
});

app.listen(port, () => {
  console.log(`server started at http://localhost:${port}`);
});
