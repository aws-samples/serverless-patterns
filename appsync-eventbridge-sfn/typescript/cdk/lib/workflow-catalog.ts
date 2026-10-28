import * as fs from "fs";
import * as os from "os";
import * as path from "path";
import {
  Annotations,
  ArnFormat,
  CfnOutput,
  Duration,
  RemovalPolicy,
  Stack,
  Tags,
} from "aws-cdk-lib";
import * as appsync from "aws-cdk-lib/aws-appsync";
import * as cloudwatch from "aws-cdk-lib/aws-cloudwatch";
import * as cognito from "aws-cdk-lib/aws-cognito";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as events from "aws-cdk-lib/aws-events";
import * as targets from "aws-cdk-lib/aws-events-targets";
import * as iam from "aws-cdk-lib/aws-iam";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as destinations from "aws-cdk-lib/aws-lambda-destinations";
import * as logs from "aws-cdk-lib/aws-logs";
import * as sqs from "aws-cdk-lib/aws-sqs";
import { Construct } from "constructs";

export interface WorkflowCatalogProps {
  /** How long execution records remain in DynamoDB. Defaults to 30 days. */
  readonly executionRetention?: Duration;

  /**
   * Removal policy for stateful resources (DynamoDB tables, log groups).
   * Defaults to DESTROY so the sample tears down cleanly. Set to RETAIN for
   * production so a stack deletion does not drop execution/registry data.
   */
  readonly removalPolicy?: RemovalPolicy;

  /**
   * AWS-level deletion protection on the registry and tracker tables. Defaults
   * to false so `cdk destroy` works in one shot. Set true for production: it
   * blocks table deletion from any tool/console, and you must set it back to
   * false (and deploy) before a later destroy.
   */
  readonly deletionProtection?: boolean;

  /** Require a workflowType tag before discovering a state machine. Defaults to true. */
  readonly requireWorkflowTypeTag?: boolean;

  /** Require a versioned JSON Schema before a discovered workflow is enabled. Defaults to true. */
  readonly requireExplicitSchema?: boolean;

  /** Maximum serialized workflow schema size. Defaults to 128 KiB. */
  readonly maxSchemaBytes?: number;

  /** Maximum serialized workflow request size. Defaults to 128 KiB. */
  readonly maxRequestPayloadBytes?: number;

  /** How often stale executions are reconciled. Defaults to 5 minutes. */
  readonly reconciliationInterval?: Duration;

  /** Age after which a nonterminal tracker record is stale. Defaults to 2 minutes. */
  readonly staleExecutionThreshold?: Duration;

  /** Maximum stale records processed by one reconciliation run. Defaults to 100. */
  readonly maxReconciliationsPerRun?: number;

  /** Prefix for readable physical resource names. Defaults to "workflow-catalog". */
  readonly resourceNamePrefix?: string;

  /**
   * Include full request/response content in the AppSync CloudWatch logs.
   * Defaults to false. Left off deliberately: the caller's `parameters` payload
   * is arbitrary workflow input that may contain sensitive data, and it is
   * already persisted (encrypted, with a TTL) in the execution tracker table, so
   * logging it again to CloudWatch widens exposure for little benefit. Field-level
   * ERROR logging and X-Ray tracing stay on regardless. Enable this only for
   * debugging or audit regimes on known-low-sensitivity workflows.
   */
  readonly verboseApiLogging?: boolean;

  /**
   * Role ARNs to attach the caller access policy to (the self-service fields:
   * requestWorkflow, getWorkflowExecution, listWorkflowExecutions). Optional;
   * if omitted the policy is still created for operators to attach manually.
   */
  readonly callerRoleArns?: string[];

  /**
   * Role ARNs to attach the admin access policy to (the privileged fields:
   * registerWorkflowContract and listWorkflowExecutionsByType, plus all caller
   * fields). Optional; if omitted the policy is still created for operators to
   * attach manually.
   */
  readonly adminRoleArns?: string[];

  /**
   * Optional Cognito user pool to accept as an ADDITIONAL authorization mode.
   * IAM remains the default. Supply this when plugging the API into a frontend
   * backed by a user pool so human users authenticate with their pool identity
   * (the resolver then identifies them by the token's `sub`). The construct
   * never creates a user pool; the consumer owns and passes in their own.
   */
  readonly userPool?: cognito.IUserPool;

  /**
   * Cognito group names whose members may call the admin fields
   * (registerWorkflowContract, listWorkflowExecutionsByType) when authenticated
   * through the Cognito user pool. REQUIRED if admins will act via a
   * Cognito-authenticated frontend - set it to your admin group(s), e.g.
   * ["platform-admins"].
   *
   * When empty (default), the admin fields are IAM-only and user-pool callers
   * cannot reach them at all. When set, the admin fields are also exposed to the
   * user pool and the resolver enforces that the caller belongs to one of these
   * groups. IAM admin access is always governed by the emitted
   * WorkflowAdminAccessPolicy, independent of this list.
   *
   * Only meaningful together with `userPool`.
   */
  readonly adminGroups?: string[];
}

export class WorkflowCatalog extends Construct {
  private logGroupCounter = 0;
  private readonly logRemovalPolicy: RemovalPolicy;

  public readonly api: appsync.GraphqlApi;
  public readonly workflowRegistryTable: dynamodb.Table;
  public readonly executionTrackerTable: dynamodb.Table;
  public readonly workflowEventBus: events.EventBus;

  public constructor(
    scope: Construct,
    id: string,
    props: WorkflowCatalogProps = {},
  ) {
    super(scope, id);

    const removalPolicy = props.removalPolicy ?? RemovalPolicy.DESTROY;
    this.logRemovalPolicy = removalPolicy;
    const deletionProtection = props.deletionProtection ?? false;
    const executionRetention = props.executionRetention ?? Duration.days(30);
    const requireWorkflowTypeTag = props.requireWorkflowTypeTag ?? true;
    const requireExplicitSchema = props.requireExplicitSchema ?? true;
    const maxSchemaBytes = props.maxSchemaBytes ?? 128 * 1024;
    const maxRequestPayloadBytes = props.maxRequestPayloadBytes ?? 128 * 1024;
    const adminGroups = props.adminGroups ?? [];
    const reconciliationInterval =
      props.reconciliationInterval ?? Duration.minutes(5);
    const staleExecutionThreshold =
      props.staleExecutionThreshold ?? Duration.minutes(2);
    const maxReconciliationsPerRun = props.maxReconciliationsPerRun ?? 100;
    const verboseApiLogging = props.verboseApiLogging ?? false;
    if (
      !Number.isInteger(maxReconciliationsPerRun) ||
      maxReconciliationsPerRun < 6
    ) {
      throw new Error(
        "maxReconciliationsPerRun must be an integer of at least 6",
      );
    }
    const resourceNamePrefix = props.resourceNamePrefix ?? "workflow-catalog";
    if (
      resourceNamePrefix.length > 40 ||
      !/^[A-Za-z0-9-_]+$/.test(resourceNamePrefix)
    ) {
      throw new Error(
        "resourceNamePrefix must be at most 40 characters and contain only letters, numbers, hyphens, and underscores",
      );
    }
    const requesterWorkflowTypeIndexName =
      "requesterWorkflowType-requestedAt-index";
    const statusLastUpdatedAtIndexName = "status-lastUpdatedAt-index";
    const workflowTypeIndexName = "workflowType-requestedAt-index";
    const stateMachineArnIndexName = "stateMachineArn-index";
    const eventSource = "workflow.catalog";
    const requestDetailType = "Workflow Requested";

    Annotations.of(this).addWarning(
      "Automatic state machine discovery requires CloudTrail management event logging in this Region. Existing state machines must be tagged or updated after deployment.",
    );

    this.workflowRegistryTable = new dynamodb.Table(this, "WorkflowRegistry", {
      tableName: `${resourceNamePrefix}-workflow-registry`,
      partitionKey: {
        name: "workflowType",
        type: dynamodb.AttributeType.STRING,
      },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      encryption: dynamodb.TableEncryption.AWS_MANAGED,
      pointInTimeRecoverySpecification: {
        pointInTimeRecoveryEnabled: true,
      },
      deletionProtection,
      removalPolicy,
    });
    Tags.of(this.workflowRegistryTable).add(
      "WorkflowComponent",
      "WorkflowRegistry",
    );
    this.workflowRegistryTable.addGlobalSecondaryIndex({
      indexName: stateMachineArnIndexName,
      partitionKey: {
        name: "stateMachineArn",
        type: dynamodb.AttributeType.STRING,
      },
      projectionType: dynamodb.ProjectionType.KEYS_ONLY,
    });

    this.executionTrackerTable = new dynamodb.Table(
      this,
      "WorkflowExecutionTracker",
      {
        tableName: `${resourceNamePrefix}-execution-tracker`,
        partitionKey: {
          name: "executionId",
          type: dynamodb.AttributeType.STRING,
        },
        billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
        encryption: dynamodb.TableEncryption.AWS_MANAGED,
        pointInTimeRecoverySpecification: {
          pointInTimeRecoveryEnabled: true,
        },
        timeToLiveAttribute: "expiresAt",
        deletionProtection,
        removalPolicy,
      },
    );
    Tags.of(this.executionTrackerTable).add(
      "WorkflowComponent",
      "ExecutionTracker",
    );
    this.executionTrackerTable.addGlobalSecondaryIndex({
      indexName: requesterWorkflowTypeIndexName,
      partitionKey: {
        name: "requesterWorkflowType",
        type: dynamodb.AttributeType.STRING,
      },
      sortKey: { name: "requestedAt", type: dynamodb.AttributeType.STRING },
      projectionType: dynamodb.ProjectionType.ALL,
    });
    this.executionTrackerTable.addGlobalSecondaryIndex({
      indexName: statusLastUpdatedAtIndexName,
      partitionKey: {
        name: "status",
        type: dynamodb.AttributeType.STRING,
      },
      sortKey: { name: "lastUpdatedAt", type: dynamodb.AttributeType.STRING },
      projectionType: dynamodb.ProjectionType.ALL,
    });
    // Admin query path: list every execution of a workflow type regardless of
    // caller. Partitioned on workflowType alone, unlike the per-requester index
    // used by listWorkflowExecutions. Access is expected to be restricted to
    // administrators at the AppSync field level (see ListExecutionsByTypeFieldArn).
    this.executionTrackerTable.addGlobalSecondaryIndex({
      indexName: workflowTypeIndexName,
      partitionKey: {
        name: "workflowType",
        type: dynamodb.AttributeType.STRING,
      },
      sortKey: { name: "requestedAt", type: dynamodb.AttributeType.STRING },
      projectionType: dynamodb.ProjectionType.ALL,
    });

    this.workflowEventBus = new events.EventBus(this, "WorkflowEventBus");

    const requestHandler = new lambda.Function(this, "WorkflowRequestHandler", {
      functionName: `${resourceNamePrefix}-request-handler`,
      description:
        "Validates AppSync workflow requests and publishes workflow events",
      runtime: lambda.Runtime.PYTHON_3_13,
      architecture: lambda.Architecture.ARM_64,
      handler: "workflow_request_handler.lambda_handler",
      code: lambda.Code.fromAsset(path.join(__dirname, "../lambda")),
      timeout: Duration.seconds(15),
      memorySize: 256,
      tracing: lambda.Tracing.ACTIVE,
      logGroup: this.createLogGroup(),
      environment: {
        WORKFLOW_REGISTRY_TABLE_NAME: this.workflowRegistryTable.tableName,
        WORKFLOW_EXECUTION_TRACKER_TABLE_NAME:
          this.executionTrackerTable.tableName,
        REQUESTER_WORKFLOW_TYPE_INDEX_NAME: requesterWorkflowTypeIndexName,
        WORKFLOW_TYPE_INDEX_NAME: workflowTypeIndexName,
        WORKFLOW_EVENT_BUS_NAME: this.workflowEventBus.eventBusName,
        WORKFLOW_EVENT_SOURCE: eventSource,
        WORKFLOW_EVENT_DETAIL_TYPE: requestDetailType,
        MAX_REQUEST_PAYLOAD_BYTES: maxRequestPayloadBytes.toString(),
        ADMIN_GROUPS: JSON.stringify(adminGroups),
      },
    });
    Tags.of(requestHandler).add("WorkflowComponent", "RequestHandler");
    this.workflowRegistryTable.grantReadData(requestHandler);
    this.executionTrackerTable.grantReadWriteData(requestHandler);
    this.workflowEventBus.grantPutEventsTo(requestHandler);
    // Allow the cancelWorkflowExecution resolver to stop a running execution.
    requestHandler.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["states:StopExecution"],
        resources: [
          Stack.of(this).formatArn({
            service: "states",
            resource: "execution",
            resourceName: "*:*",
            arnFormat: ArnFormat.COLON_RESOURCE_NAME,
          }),
        ],
      }),
    );

    const workflowTrigger = new lambda.Function(this, "WorkflowTrigger", {
      functionName: `${resourceNamePrefix}-workflow-trigger`,
      description:
        "Starts the registered Step Functions workflow for a request event",
      runtime: lambda.Runtime.PYTHON_3_13,
      architecture: lambda.Architecture.ARM_64,
      handler: "workflow_trigger.lambda_handler",
      code: lambda.Code.fromAsset(path.join(__dirname, "../lambda")),
      timeout: Duration.seconds(30),
      memorySize: 256,
      tracing: lambda.Tracing.ACTIVE,
      logGroup: this.createLogGroup(),
      environment: {
        WORKFLOW_REGISTRY_TABLE_NAME: this.workflowRegistryTable.tableName,
        WORKFLOW_EXECUTION_TRACKER_TABLE_NAME:
          this.executionTrackerTable.tableName,
        EXECUTION_RETENTION_DAYS: executionRetention.toDays().toString(),
      },
    });
    Tags.of(workflowTrigger).add("WorkflowComponent", "WorkflowTrigger");
    this.workflowRegistryTable.grantReadData(workflowTrigger);
    this.executionTrackerTable.grantReadWriteData(workflowTrigger);
    // Restrict StartExecution to state machines that carry a workflowType tag.
    // This is the same tag the discovery flow (record_step_function_info) already
    // requires before a state machine is registered, so it adds no extra work for
    // workflow owners: tagging a machine opts it in, and the absence of the tag
    // makes it impossible for this trigger to start it. It bounds the trigger's
    // blast radius from "every state machine in the Region" to "only workflows
    // that explicitly opted into this system." Callability is still separately
    // gated by an ACTIVE registry contract; this condition is defense in depth.
    workflowTrigger.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["states:StartExecution"],
        resources: [
          Stack.of(this).formatArn({
            service: "states",
            resource: "stateMachine",
            resourceName: "*",
            arnFormat: ArnFormat.COLON_RESOURCE_NAME,
          }),
        ],
        conditions: {
          Null: {
            "aws:ResourceTag/workflowType": "false",
          },
        },
      }),
    );
    workflowTrigger.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["states:DescribeExecution"],
        resources: [
          Stack.of(this).formatArn({
            service: "states",
            resource: "execution",
            resourceName: "*:*",
            arnFormat: ArnFormat.COLON_RESOURCE_NAME,
          }),
        ],
      }),
    );

    const registryHandler = new lambda.Function(
      this,
      "RecordStepFunctionInfo",
      {
        functionName: `${resourceNamePrefix}-registry-sync`,
        description:
          "Discovers Step Functions workflows and manages versioned contracts",
        runtime: lambda.Runtime.PYTHON_3_13,
        architecture: lambda.Architecture.ARM_64,
        handler: "record_step_function_info.lambda_handler",
        code: lambda.Code.fromAsset(path.join(__dirname, "../lambda")),
        timeout: Duration.seconds(30),
        memorySize: 256,
        tracing: lambda.Tracing.ACTIVE,
        logGroup: this.createLogGroup(),
        environment: {
          WORKFLOW_REGISTRY_TABLE_NAME: this.workflowRegistryTable.tableName,
          STATE_MACHINE_ARN_INDEX_NAME: stateMachineArnIndexName,
          REQUIRE_WORKFLOW_TYPE_TAG: requireWorkflowTypeTag.toString(),
          REQUIRE_EXPLICIT_SCHEMA: requireExplicitSchema.toString(),
          MAX_SCHEMA_BYTES: maxSchemaBytes.toString(),
          ADMIN_GROUPS: JSON.stringify(adminGroups),
        },
      },
    );
    Tags.of(registryHandler).add("WorkflowComponent", "RegistrySync");
    this.workflowRegistryTable.grantReadWriteData(registryHandler);
    registryHandler.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["states:DescribeStateMachine", "states:ListTagsForResource"],
        resources: [
          Stack.of(this).formatArn({
            service: "states",
            resource: "stateMachine",
            resourceName: "*",
            arnFormat: ArnFormat.COLON_RESOURCE_NAME,
          }),
        ],
      }),
    );

    const executionStatusHandler = new lambda.Function(
      this,
      "ExecutionStatusHandler",
      {
        functionName: `${resourceNamePrefix}-status-handler`,
        description:
          "Updates workflow tracker records from Step Functions status events",
        runtime: lambda.Runtime.PYTHON_3_13,
        architecture: lambda.Architecture.ARM_64,
        handler: "execution_status_handler.lambda_handler",
        code: lambda.Code.fromAsset(path.join(__dirname, "../lambda")),
        timeout: Duration.seconds(15),
        memorySize: 256,
        tracing: lambda.Tracing.ACTIVE,
        logGroup: this.createLogGroup(),
        environment: {
          WORKFLOW_EXECUTION_TRACKER_TABLE_NAME:
            this.executionTrackerTable.tableName,
          EXECUTION_RETENTION_DAYS: executionRetention.toDays().toString(),
          MAX_STATUS_VALUE_BYTES: (64 * 1024).toString(),
        },
      },
    );
    Tags.of(executionStatusHandler).add("WorkflowComponent", "StatusHandler");
    this.executionTrackerTable.grantWriteData(executionStatusHandler);

    const executionReconciler = new lambda.Function(
      this,
      "ExecutionReconciler",
      {
        functionName: `${resourceNamePrefix}-execution-reconciler`,
        description:
          "Repairs stale workflow tracker records using Step Functions state",
        runtime: lambda.Runtime.PYTHON_3_13,
        architecture: lambda.Architecture.ARM_64,
        handler: "execution_reconciler.lambda_handler",
        code: lambda.Code.fromAsset(path.join(__dirname, "../lambda")),
        timeout: Duration.minutes(2),
        memorySize: 256,
        tracing: lambda.Tracing.ACTIVE,
        logGroup: this.createLogGroup(),
        environment: {
          WORKFLOW_EXECUTION_TRACKER_TABLE_NAME:
            this.executionTrackerTable.tableName,
          STATUS_LAST_UPDATED_AT_INDEX_NAME: statusLastUpdatedAtIndexName,
          WORKFLOW_EVENT_BUS_NAME: this.workflowEventBus.eventBusName,
          WORKFLOW_EVENT_SOURCE: eventSource,
          WORKFLOW_EVENT_DETAIL_TYPE: requestDetailType,
          EXECUTION_RETENTION_DAYS: executionRetention.toDays().toString(),
          STALE_AFTER_SECONDS: staleExecutionThreshold.toSeconds().toString(),
          MAX_RECORDS_PER_RUN: maxReconciliationsPerRun.toString(),
          MAX_STATUS_VALUE_BYTES: (64 * 1024).toString(),
        },
      },
    );
    Tags.of(executionReconciler).add(
      "WorkflowComponent",
      "ExecutionReconciler",
    );
    this.executionTrackerTable.grantReadWriteData(executionReconciler);
    this.workflowEventBus.grantPutEventsTo(executionReconciler);
    executionReconciler.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["states:DescribeExecution"],
        resources: [
          Stack.of(this).formatArn({
            service: "states",
            resource: "execution",
            resourceName: "*:*",
            arnFormat: ArnFormat.COLON_RESOURCE_NAME,
          }),
        ],
      }),
    );

    const workflowTriggerDlq = this.createDeadLetterQueue("WorkflowTriggerDlq");
    const registryDlq = this.createDeadLetterQueue("RegistryDiscoveryDlq");
    const executionStatusDlq = this.createDeadLetterQueue("ExecutionStatusDlq");
    const executionReconcilerDlq = this.createDeadLetterQueue(
      "ExecutionReconcilerDlq",
    );

    workflowTrigger.configureAsyncInvoke({
      onFailure: new destinations.SqsDestination(workflowTriggerDlq),
      maxEventAge: Duration.hours(2),
      retryAttempts: 2,
    });
    registryHandler.configureAsyncInvoke({
      onFailure: new destinations.SqsDestination(registryDlq),
      maxEventAge: Duration.hours(2),
      retryAttempts: 2,
    });
    executionStatusHandler.configureAsyncInvoke({
      onFailure: new destinations.SqsDestination(executionStatusDlq),
      maxEventAge: Duration.hours(2),
      retryAttempts: 2,
    });
    executionReconciler.configureAsyncInvoke({
      onFailure: new destinations.SqsDestination(executionReconcilerDlq),
      maxEventAge: Duration.hours(2),
      retryAttempts: 2,
    });

    new events.Rule(this, "WorkflowRequestedRule", {
      eventBus: this.workflowEventBus,
      eventPattern: {
        source: [eventSource],
        detailType: [requestDetailType],
      },
      targets: [
        new targets.LambdaFunction(workflowTrigger, {
          deadLetterQueue: workflowTriggerDlq,
          maxEventAge: Duration.hours(2),
          retryAttempts: 3,
        }),
      ],
    });

    new events.Rule(this, "StateMachineRegistryRule", {
      eventPattern: {
        source: ["aws.states"],
        detailType: ["AWS API Call via CloudTrail"],
        detail: {
          eventSource: ["states.amazonaws.com"],
          eventName: [
            "CreateStateMachine",
            "UpdateStateMachine",
            "DeleteStateMachine",
            "TagResource",
            "UntagResource",
          ],
        },
      },
      targets: [
        new targets.LambdaFunction(registryHandler, {
          deadLetterQueue: registryDlq,
          maxEventAge: Duration.hours(2),
          retryAttempts: 3,
        }),
      ],
    });

    new events.Rule(this, "StepFunctionsExecutionStatusRule", {
      eventPattern: {
        source: ["aws.states"],
        detailType: ["Step Functions Execution Status Change"],
        detail: {
          status: [
            "RUNNING",
            "PENDING_REDRIVE",
            "SUCCEEDED",
            "FAILED",
            "TIMED_OUT",
            "ABORTED",
          ],
        },
      },
      targets: [
        new targets.LambdaFunction(executionStatusHandler, {
          deadLetterQueue: executionStatusDlq,
          maxEventAge: Duration.hours(2),
          retryAttempts: 3,
        }),
      ],
    });

    new events.Rule(this, "ExecutionReconciliationSchedule", {
      schedule: events.Schedule.rate(reconciliationInterval),
      targets: [
        new targets.LambdaFunction(executionReconciler, {
          deadLetterQueue: executionReconcilerDlq,
          maxEventAge: Duration.hours(2),
          retryAttempts: 3,
        }),
      ],
    });

    // Default authorization is IAM. When a consumer supplies their own Cognito
    // user pool, add it as an ADDITIONAL authorization mode (IAM stays the
    // default) so users authenticated against that pool can call the API
    // directly; the resolver identifies them by the token's `sub`.
    //
    // AppSync requires per-type auth directives once more than one mode exists:
    // an undirected field is reachable only via the default mode. So when a user
    // pool is enabled we annotate every object type with BOTH @aws_iam and
    // @aws_cognito_user_pools (keeping IAM access while adding user-pool access)
    // and load the schema from the transformed string. The schema file itself
    // stays directive-free so the IAM-only default remains valid.
    const schemaPath = path.join(__dirname, "../graphql/schema.graphql");
    let definition: appsync.Definition;
    if (props.userPool) {
      let annotatedSchema = fs
        .readFileSync(schemaPath, "utf-8")
        .replace(
          /^type (\w+) \{/gm,
          "type $1 @aws_iam @aws_cognito_user_pools {",
        );
      // The type-level directives above expose every field to both auth modes.
      // Unless a Cognito admin group is designated, pin the admin fields back to
      // IAM-only (a field-level directive overrides the type level) so user-pool
      // callers cannot reach them. When admin groups ARE configured, leave the
      // admin fields reachable by the user pool - the resolver then enforces that
      // the caller belongs to an admin group.
      if (adminGroups.length === 0) {
        annotatedSchema = annotatedSchema
          .replace(
            /(registerWorkflowContract\([^)]*\):\s*WorkflowRegistration!)/,
            "$1 @aws_iam",
          )
          .replace(
            /(listWorkflowExecutionsByType\([^)]*\):\s*WorkflowExecutionConnection!)/,
            "$1 @aws_iam",
          );
      }
      // This CDK version has no Definition.fromString and schemas are read from
      // disk, so write the annotated SDL to a temp file and load it. The file
      // only needs to exist during synthesis.
      const annotatedPath = path.join(
        os.tmpdir(),
        `workflow-schema-${this.node.addr}.graphql`,
      );
      fs.writeFileSync(annotatedPath, annotatedSchema);
      definition = appsync.Definition.fromFile(annotatedPath);
    } else {
      definition = appsync.Definition.fromFile(schemaPath);
    }

    this.api = new appsync.GraphqlApi(this, "WorkflowApi", {
      name: "workflow-catalog-api",
      definition,
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: appsync.AuthorizationType.IAM,
        },
        additionalAuthorizationModes: props.userPool
          ? [
              {
                authorizationType: appsync.AuthorizationType.USER_POOL,
                userPoolConfig: { userPool: props.userPool },
              },
            ]
          : undefined,
      },
      logConfig: {
        fieldLogLevel: appsync.FieldLogLevel.ERROR,
        excludeVerboseContent: !verboseApiLogging,
      },
      xrayEnabled: true,
    });

    const requestDataSource = this.api.addLambdaDataSource(
      "WorkflowRequestDataSource",
      requestHandler,
    );
    requestDataSource.createResolver("RequestWorkflowResolver", {
      typeName: "Mutation",
      fieldName: "requestWorkflow",
    });
    requestDataSource.createResolver("CancelWorkflowExecutionResolver", {
      typeName: "Mutation",
      fieldName: "cancelWorkflowExecution",
    });
    requestDataSource.createResolver("GetWorkflowExecutionResolver", {
      typeName: "Query",
      fieldName: "getWorkflowExecution",
    });
    requestDataSource.createResolver("ListWorkflowExecutionsResolver", {
      typeName: "Query",
      fieldName: "listWorkflowExecutions",
    });
    requestDataSource.createResolver("ListWorkflowExecutionsByTypeResolver", {
      typeName: "Query",
      fieldName: "listWorkflowExecutionsByType",
    });

    const registryDataSource = this.api.addLambdaDataSource(
      "WorkflowRegistryDataSource",
      registryHandler,
    );
    registryDataSource.createResolver("RegisterWorkflowContractResolver", {
      typeName: "Mutation",
      fieldName: "registerWorkflowContract",
    });
    registryDataSource.createResolver("GetWorkflowRegistrationResolver", {
      typeName: "Query",
      fieldName: "getWorkflowRegistration",
    });
    registryDataSource.createResolver("ListWorkflowRegistrationsResolver", {
      typeName: "Query",
      fieldName: "listWorkflowRegistrations",
    });

    const registerWorkflowContractFieldArn = Stack.of(this).formatArn({
      service: "appsync",
      resource: "apis",
      resourceName: `${this.api.apiId}/types/Mutation/fields/registerWorkflowContract`,
      arnFormat: ArnFormat.SLASH_RESOURCE_NAME,
    });
    const listExecutionsByTypeFieldArn = Stack.of(this).formatArn({
      service: "appsync",
      resource: "apis",
      resourceName: `${this.api.apiId}/types/Query/fields/listWorkflowExecutionsByType`,
      arnFormat: ArnFormat.SLASH_RESOURCE_NAME,
    });

    // Field-level access expressed as CDK-managed artifacts so operators attach
    // a policy instead of hand-writing IAM. The caller policy grants only the
    // self-service fields; the admin policy adds the privileged fields that
    // register contracts and list executions across all callers.
    //
    // NOTE: AppSync IAM authorization is allow-based and additive. Attaching
    // these grants the intended least-privilege access, but it cannot prevent a
    // broader policy elsewhere (e.g. AdministratorAccess or appsync:GraphQL on
    // apis/*) from also reaching these fields. For hard admin-only enforcement
    // independent of ambient IAM, enforce an admin allowlist in the resolver.
    const callerFieldNames = [
      "Mutation/fields/requestWorkflow",
      "Mutation/fields/cancelWorkflowExecution",
      "Query/fields/getWorkflowExecution",
      "Query/fields/listWorkflowExecutions",
      "Query/fields/getWorkflowRegistration",
      "Query/fields/listWorkflowRegistrations",
    ];
    const callerFieldArns = callerFieldNames.map((field) =>
      Stack.of(this).formatArn({
        service: "appsync",
        resource: "apis",
        resourceName: `${this.api.apiId}/types/${field}`,
        arnFormat: ArnFormat.SLASH_RESOURCE_NAME,
      }),
    );
    const adminFieldArns = [
      registerWorkflowContractFieldArn,
      listExecutionsByTypeFieldArn,
    ];

    const callerAccessPolicy = new iam.ManagedPolicy(
      this,
      "WorkflowCallerAccessPolicy",
      {
        statements: [
          new iam.PolicyStatement({
            actions: ["appsync:GraphQL"],
            resources: callerFieldArns,
          }),
        ],
      },
    );
    const adminAccessPolicy = new iam.ManagedPolicy(
      this,
      "WorkflowAdminAccessPolicy",
      {
        statements: [
          new iam.PolicyStatement({
            actions: ["appsync:GraphQL"],
            resources: [...callerFieldArns, ...adminFieldArns],
          }),
        ],
      },
    );

    (props.callerRoleArns ?? []).forEach((roleArn, index) => {
      callerAccessPolicy.attachToRole(
        iam.Role.fromRoleArn(this, `WorkflowCallerRole${index}`, roleArn, {
          mutable: true,
        }),
      );
    });
    (props.adminRoleArns ?? []).forEach((roleArn, index) => {
      adminAccessPolicy.attachToRole(
        iam.Role.fromRoleArn(this, `WorkflowAdminRole${index}`, roleArn, {
          mutable: true,
        }),
      );
    });

    new CfnOutput(this, "GraphqlApiId", { value: this.api.apiId });
    new CfnOutput(this, "GraphqlApiUrl", { value: this.api.graphqlUrl });
    new CfnOutput(this, "WorkflowRegistryTableName", {
      value: this.workflowRegistryTable.tableName,
    });
    new CfnOutput(this, "ExecutionTrackerTableName", {
      value: this.executionTrackerTable.tableName,
    });
    new CfnOutput(this, "WorkflowEventBusName", {
      value: this.workflowEventBus.eventBusName,
    });
    new CfnOutput(this, "RegisterWorkflowContractFieldArn", {
      value: registerWorkflowContractFieldArn,
      description:
        "Grant appsync:GraphQL on this ARN only to workflow contract administrators",
    });
    new CfnOutput(this, "ListExecutionsByTypeFieldArn", {
      value: listExecutionsByTypeFieldArn,
      description:
        "Grant appsync:GraphQL on this ARN only to workflow administrators; this field returns executions across all callers",
    });
    new CfnOutput(this, "WorkflowCallerAccessPolicyArn", {
      value: callerAccessPolicy.managedPolicyArn,
      description:
        "Attach to principals that may request and read their own workflow executions",
    });
    new CfnOutput(this, "WorkflowAdminAccessPolicyArn", {
      value: adminAccessPolicy.managedPolicyArn,
      description:
        "Attach to administrators; adds contract registration and cross-caller execution listing",
    });
  }

  private createLogGroup(): logs.LogGroup {
    this.logGroupCounter += 1;
    return new logs.LogGroup(this, `LambdaLogGroup${this.logGroupCounter}`, {
      retention: logs.RetentionDays.ONE_MONTH,
      removalPolicy: this.logRemovalPolicy,
    });
  }

  private createDeadLetterQueue(id: string): sqs.Queue {
    const queue = new sqs.Queue(this, id, {
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      enforceSSL: true,
      retentionPeriod: Duration.days(14),
    });
    new cloudwatch.Alarm(this, `${id}MessagesAlarm`, {
      metric: queue.metricApproximateNumberOfMessagesVisible(),
      threshold: 1,
      evaluationPeriods: 1,
      comparisonOperator:
        cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
      treatMissingData: cloudwatch.TreatMissingData.NOT_BREACHING,
    });
    return queue;
  }
}
