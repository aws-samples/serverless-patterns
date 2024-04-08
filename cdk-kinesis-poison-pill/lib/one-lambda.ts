import { Construct } from "constructs";
import { GoFunction } from "@aws-cdk/aws-lambda-go-alpha";
import { Duration } from "aws-cdk-lib";
import { Stream } from "aws-cdk-lib/aws-kinesis";
import { Queue } from "aws-cdk-lib/aws-sqs";
import * as path from "path";
import { KinesisEventSource } from "aws-cdk-lib/aws-lambda-event-sources";
import { StartingPosition } from "aws-cdk-lib/aws-lambda";
import { SqsDestination } from "aws-cdk-lib/aws-lambda-destinations";

export class OneLambda extends Construct {
    constructor(scope: Construct, id: string) {
        super(scope, id);

        // create the go function from src
        let func = new GoFunction(this, `OneLambda`, {
            entry: path.join(__dirname, `../src`),
            functionName: `sample-func`,
            timeout: Duration.seconds(30),
        });

        // create a kinesis stream (ignoring encryption, but you should encrypt this)
        let stream = new Stream(this, "TheStream", {
            streamName: "sample-stream",
            shardCount: 1,
        });

        // create a SQS Queue for Failure
        // (ignoring encryption, but you should encrypt this and I believe AWS does now by default)
        let queue = new Queue(this, "FailureQueue", {
            queueName: `sample-failure-queue`,
        });

        // grant the func to have read access to the stream
        stream.grantRead(func);

        // create an event source for the Lambda to read from kinesis
        func.addEventSource(
            new KinesisEventSource(stream, {
                startingPosition: StartingPosition.TRIM_HORIZON, // Start reading the beginning of data persistence
                batchSize: 10, // how many to pull
                retryAttempts: 5, // how many times to retry
                bisectBatchOnError: true, // kinesis will split the batch up to work it's way to isolate the error
                onFailure: new SqsDestination(queue), // where do the failed reads go
            })
        );
    }
}
