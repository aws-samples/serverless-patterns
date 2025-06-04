import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AttributeType, StreamViewType, Table } from "aws-cdk-lib/aws-dynamodb"
import { Pass, StateMachine } from "aws-cdk-lib/aws-stepfunctions"
import { DynamoWorkflowTrigger, EventName } from "./ddbstream-lambda-sfn"
import { FilterCriteria, FilterRule } from "aws-cdk-lib/aws-lambda";


export class DdbstreamLambdaSfnExampleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a DynamoDB table with streaming enabled and 'Index' as partition key. 
    // You can also import your own table. But it should have DDB streaming enabled.
    const testTable = new Table(this, "TestTable", {
      partitionKey: {
        name: "Index",
        type: AttributeType.STRING
      },
      stream: StreamViewType.NEW_AND_OLD_IMAGES // Required for the trigger to work
    })

    // Create a simple Step Functions state machine with a single Pass state. 
    // You can import any other step function here as well. 
    const testStateMachine = new StateMachine(this, "TestStateMachine", {
      definition: new Pass(this, "TestPassState")
    })

    // Create a DynamoDB stream trigger with event filtering and conditional execution
    const exampleTrigger = new DynamoWorkflowTrigger(this, "TestTrigger", {
      eventSourceFilters: [
        FilterCriteria.filter({
          dynamodb: {
            NewImage: {
              SkipMe: {
                // Only trigger when attribute "SkipMe" does not exist
                S: FilterRule.notExists(),
              },
            },
          },
        }),
      ],
      eventHandlers: [
        {
          table: testTable,
          // Only trigger on MODIFY events
          eventNames: [EventName.Modify],
          // Only execute when:
          // 1. NewImage.testKey = "test8"
          // 2. OldImage.testKey = "test9"
          conditions: [{ jsonPath: "$.NewImage.testKey.S", value: "test8"}, { jsonPath: "$.OldImage.testKey.S", value: "test9"}], // Ensure this is always an array
          // Configure Step Functions execution with dynamic input mapping
          stateMachineConfig: {
            stateMachine: testStateMachine,
            input: {
              Index: "$.NewImage.Index.S",
              MapAttribute: "$.NewImage.ListAttribute.L[0]"
            }
          }
        }
      ]
    })
  }
}