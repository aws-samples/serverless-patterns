import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AttributeType, StreamViewType, Table } from "aws-cdk-lib/aws-dynamodb"
import { Pass, StateMachine } from "aws-cdk-lib/aws-stepfunctions"
import { DynamoWorkflowTrigger, EventName } from "./ddbstream-lambda-sfn"
import { FilterCriteria, FilterRule } from "aws-cdk-lib/aws-lambda";


export class DdbstreamLambdaSfnExampleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a test table
    const testTable = new Table(this, "TestTable", {
      partitionKey: {
        name: "Index",
        type: AttributeType.STRING
      },
      stream: StreamViewType.NEW_AND_OLD_IMAGES
    })

    // Create a test state machine
    const testStateMachine = new StateMachine(this, "TestStateMachine", {
      definition: new Pass(this, "TestPassState")
    })

    // Create a trigger on insert
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
          eventNames: [EventName.Modify],
          conditions: [{ jsonPath: "$.NewImage.testKey.S", value: "test8"}, { jsonPath: "$.OldImage.testKey.S", value: "test9"}], // Ensure this is always an array
          stateMachineConfig: {
            stateMachine: testStateMachine,
            input: {
              Index: "$.NewImage.Index.S",
              MapAttribute: "$.newImage.ListAttribute.l[0]"
            }
          }
        }
      ]
    })
  }
}