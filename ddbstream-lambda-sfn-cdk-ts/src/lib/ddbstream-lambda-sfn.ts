import { Duration, RemovalPolicy } from "aws-cdk-lib"
import { Dashboard } from "aws-cdk-lib/aws-cloudwatch"
import { ITable } from "aws-cdk-lib/aws-dynamodb"
import { ISecurityGroup, IVpc, Peer, Port, SecurityGroup, SubnetType } from "aws-cdk-lib/aws-ec2"
import { Key } from "aws-cdk-lib/aws-kms"
import { Function, Runtime, Code, StartingPosition } from "aws-cdk-lib/aws-lambda"
import { DynamoEventSource, SqsDlq } from "aws-cdk-lib/aws-lambda-event-sources"
import { RetentionDays } from "aws-cdk-lib/aws-logs"
import { Queue, QueueEncryption } from "aws-cdk-lib/aws-sqs"
import { IStateMachine } from "aws-cdk-lib/aws-stepfunctions"
import { Construct } from "constructs"
import * as path from 'path';

/**
 * DynamoDB event stream event names. Use this to filter events based on whether they are inserts, updates,
 * or deletes.
 */
export enum EventName {
  /**
   * A new item was inserted into the DDB table.
   */
  Insert = "INSERT",
  /**
   * An existing item was modified in the DDB table.
   */
  Modify = "MODIFY",
  /**
   * An item was removed from the DDB table.
   */
  Remove = "REMOVE"
}

/**
 * The state machine config describes which state machine to invoke, and what properties to input into it.
 */
export interface StateMachineConfig {
  /**
   * State machine to invoke.
   */
  stateMachine: IStateMachine
  /**
   * Input map.
   */
  input?: {
    [name: string]: string
  }
}

export interface Condition {
  jsonPath: string,
  value: string
}

/**
 * Each event handler describes a kind of change in DynamoDB to react to, and the state machine to trigger
 * when that event happens.
 */
export interface EventHandler {
  /**
   * Table to consume events from. The table must have streaming enabled and set to NEW_AND_OLD_IMAGES.
   */
  table: ITable
  /**
   * The types of events (INSERT, MODIFY, REMOVE) to trigger on.
   */
  eventNames?: EventName[]
  /**
   * Conditions that must be met for this event handler to trigger. These are JSONPath expressions that are
   * evaluated over the `dynamoDb` property of the event record.
   */
  conditions?: Condition[]
  /**
   * The state machine to execute if conditions are met.
   */
  stateMachineConfig: StateMachineConfig
}

/**
 * DynamoWorkflowTrigger construct properties.
 */
export interface DynamoWorkflowTriggerProps {
  /**
   * List of event handlers to trigger on. Each event handler describes a set of conditions that must be
   * met, and a state machine to trigger when those conditions are met.
   */
  eventHandlers: EventHandler[]
  /**
   * Number of times to re-try a failed Lambda invocation before sending it to the dead-letter queue.
   *
   * @default 3
   */
  retries?: number
  /**
   * VPC to run the trigger Lambda inside of.
   */
  vpc?: IVpc
  /**
   * SubnetType to use for VPC Subnet. Requires setting vpc.
   *
   * Defaults to SubnetType.ISOLATED if vpc is configured.
   */
  subnetType?: SubnetType
  /**
   * Additional security groups to apply to the event trigger lambda. Requires setting vpc.
   *
   * The event trigger lambda requires communication to the StepFunctions service endpoint. If a vpc is configured
   * but this prop is not specified, a default security group enabling all egress HTTPS traffic is used.
   * It is recommend that consumers of this construct provide a vpc and explicit security groups that limit traffic
   * to only the StepFunctions service endpoint over HTTPS (port 443) using a VPC interface endpoint.
   */
  additionalSecurityGroups?: ISecurityGroup[]
  /**
   * Add filter criteria option for event source.
   *
   * @default - None
   */
  readonly eventSourceFilters?: Array<{
    [key: string]: any
  }>
}

/**
 * State machine config that resolves the state machine to its ARN.
 */
export interface LambdaStateMachineConfig {
  /**
   * State machine ARN.
   */
  stateMachineArn: string
  /**
   * Input map.
   */
  input?: {
    [name: string]: string
  }
}

/**
 * Event handler representation that resolves each table to its event source ARN.
 */
interface LambdaEventHandler {
  /**
   * Table to consume events from. The table must have streaming enabled and set to NEW_AND_OLD_IMAGES.
   */
  eventSourceArn: string
  /**
   * The types of events (INSERT, MODIFY, REMOVE) to trigger on.
   */
  eventNames?: EventName[]
  /**
   * Conditions that must be met for this event handler to trigger. These are JSONPath expressions that are
   * evaluated over the `dynamoDb` property of the event record.
   */
  conditions?: Condition[]
  /**
   * The state machine to execute if conditions are met.
   */
  stateMachineConfig: LambdaStateMachineConfig
}

/**
 * A CDK construct that to trigger StepFunctions workflows in response to changes in a DynamoDB table.
 *
 * The construct contains a Lambda function that evaluates JSONPath expressions against DynamoDB event
 * records to determine whether a workflow must be executed. An arbitrary number of event handlers can
 * be defined for a single table to handle different kinds of state transitions.
 *
 * The construct includes a dead-letter queue for failed invocations, as well as a dashboard and alarms.
 */
export class DynamoWorkflowTrigger extends Construct {
  /**
   * The Lambda function to be invoked for each DynamoDB event record.
   */
  public readonly lambda: Function

  /**
   * Generated CloudWatch dashboard.
   */
  public readonly deadLetterQueue: Queue

  /**
   * Generated CloudWatch dashboard.
   */
  public readonly dashboard?: Dashboard


  /**
   * Creates a new instance.
   *
   * @param parent parent construct.
   * @param id construct id.
   * @param props properties.
   */
  constructor(parent: Construct, id: string, props: DynamoWorkflowTriggerProps) {
    super(parent, id)

    const dlqKmsKey = new Key(parent, "DlqKey", {
      description: "SSE for encrypting the workflow trigger SQS DLQ.",
      enableKeyRotation: true,
      removalPolicy: RemovalPolicy.RETAIN
    })

    // Create a dead-letter queue for failed invocations.
    this.deadLetterQueue = new Queue(this, "Dlq", {
      retentionPeriod: Duration.days(14),
      encryption: QueueEncryption.KMS,
      encryptionMasterKey: dlqKmsKey,
    })

    // Construct event handler configuration for the Lambda function. This resolves CDK Table
    // constructs to their event stream ARNs.
    const lambdaEventHandlers: LambdaEventHandler[] = props.eventHandlers.map((handler) => {
      return {
        eventSourceArn: handler.table.tableStreamArn!,
        eventNames: handler.eventNames,
        conditions: handler.conditions,
        stateMachineConfig: {
          stateMachineArn: handler.stateMachineConfig.stateMachine.stateMachineArn,
          input: handler.stateMachineConfig.input,
        }
      }
    })

    if (!props.vpc && props.additionalSecurityGroups) {
      throw new Error("Cannot specify security groups without configuring a vpc.")
    }
    if (!props.vpc && props.subnetType) {
      throw new Error("Cannot specify subnetType without configuring a vpc.")
    }

    // If VPC is set build sane defaults into subnet type and security groups.
    const networkConfiguration = props.vpc
      ? {
        vpc: props.vpc,
        subnetType: props.subnetType ?? SubnetType.PRIVATE_ISOLATED,
        securityGroups: props.additionalSecurityGroups || [this.buildDefaultSecurityGroup(props.vpc)]
      }
      : {}

    // Create the Lambda function.
    this.lambda = new Function(this, "Lambda", {
      code: Code.fromAsset(path.join(__dirname, '../lambda')),
      handler: "index.handler",
      runtime: Runtime.NODEJS_20_X,
      memorySize: 2048,
      timeout: Duration.seconds(20),
      environment: {
        EVENT_HANDLER_CONFIG: JSON.stringify({
          eventHandlers: lambdaEventHandlers
        })
      },
      ...networkConfiguration,
      logRetention: RetentionDays.TEN_YEARS
    })

    // Give the Lambda function read access to the required tables and allow it to
    // start executions for the relevant state machines.
    props.eventHandlers.forEach((handler) => {
      handler.table.grantStreamRead(this.lambda)
      // grantStreamRead is supposed to grant decrypt to the KMS key but it doesn't
      handler.table.encryptionKey?.grantDecrypt(this.lambda)
      handler.stateMachineConfig.stateMachine.grantStartExecution(this.lambda)
    })

    // For each table, create an event source and wire it up to the Lambda function.
    const tables = new Set(props.eventHandlers.map((handler) => handler.table))
    tables.forEach((table) => {
      // Create event source for the Lambda function.
      const eventSource = new DynamoEventSource(table, {
        startingPosition: StartingPosition.TRIM_HORIZON,
        onFailure: new SqsDlq(this.deadLetterQueue),
        retryAttempts: props.retries || 10,
        bisectBatchOnError: true,
        filters: props.eventSourceFilters,
      })

      // Connect the DDB event source to the Lambda.
      this.lambda.addEventSource(eventSource)
    })
  }

  buildDefaultSecurityGroup(vpc: IVpc): SecurityGroup {
    const defaultSecurityGroup = new SecurityGroup(this, "DefaultSecurityGroup", {
      vpc: vpc,
      description: "DynamoWorkflowTrigger default security group.",
      allowAllOutbound: false
    })
    defaultSecurityGroup.addEgressRule(Peer.anyIpv4(), Port.tcp(443), "Enable HTTPS egress.")

    return defaultSecurityGroup
  }
}
