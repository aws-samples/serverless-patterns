# New Pattern Submission — cdk-dotnet-durablefunction-travelbooking

## Pattern Details

- **Title:** Lambda Durable Function — Flight Booking with Payment Callback & Saga Compensation (.NET)
- **Description:** A durable function that checks availability, suspends while waiting for external payment confirmation (callback), authorizes and captures payment, books a flight, and handles failures with saga compensation — demonstrating callbacks, durable timers, and compensation in a realistic booking workflow.
- **Language:** .NET (C#)
- **Framework:** CDK
- **Level:** 300
- **Services:** AWS Lambda, Amazon DynamoDB, Amazon API Gateway

## How It Works

This pattern deploys a Lambda durable function that implements a realistic flight booking workflow:

1. Checks flight availability (fail-fast if no seats)
2. Creates a callback token and suspends — zero compute while waiting for the payment gateway
3. Payment gateway confirms (via POST to callback endpoint) — workflow resumes instantly
4. Authorizes payment (hold funds)
5. Books with the airline
6. If booking fails → saga compensation reverses the payment hold
7. Waits for airline confirmation (durable timer — 2 minutes)
8. Captures payment, sends confirmation email, persists result

The workflow spans minutes (callback wait + airline timer), making durable execution essential — a plain Lambda would time out. The starter Lambda pattern (async invoke + immediate 202) keeps API Gateway response times fast.

## GitHub PR for template:

<!-- Paste your PR link here, e.g.: #1234 -->

## Author

- **Name:** Vedanayagan Damodaran
- **Bio:** Cloud Application Architect at AWS, focused on .NET and serverless.
- **LinkedIn:** vedanayagandamodaran
