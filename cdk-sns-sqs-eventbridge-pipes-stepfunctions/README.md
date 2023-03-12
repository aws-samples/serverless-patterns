## README

CDK Pattern highlighting an architectual pattern that connects an SNS Message Producer to a Step Function by using EventBridge and SQS

![High Level Architecture](https://www.binaryheap.com/wp-content/uploads/2023/03/sns_pipes.png)

### Description of the Flow

-   A publisher submits a message to SNS
-   SNS will then trigger the message and post into an SQS. The subscription needs to be marked as `Raw Message Delivery`
-   An EventBridge Pipe listens to the SQS and then
    -   Filters the message for types of events it's interested in
    -   Tranforms the body from an SQS Message Body into something more usable for an EventBus
-   A Custom Event Bus has a `Rule` that handles the message and targets a Step Function
-   The State Machine is triggered and just does a Succeed tasks (more workflow could surely be added)

### Running the Solution

#### Deploying

To Deploy, run

```
make local-deploy
```

This will execute

-   CDK synth
-   Deploy out to your AWS Environment configured in your ~/.aws/profile

#### Triggering the workflow

Post a message onto the SNS Topic with the following structure

```javascript
{
    "eventType": "SampleEvent",
    "field1": "Sample Field 1",
    "field2": "Sample Field 2",
    "field3": "Sample Field 3"
}
```
