import express from "express";

const app = express();
const port = 80;

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.get("/", (req, res) => {
  res.status(200).send({
    message: `Hello from AWS AppRunner service running in region ${process.env.region} !`,
  });
});

app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
