const { SFNClient, StartExecutionCommand } = require('@aws-sdk/client-sfn');
const { createMetricsLogger } = require('aws-embedded-metrics');
const JsonPath = require('jsonpath');

/**
 * @typedef {Object} StateMachineConfig
 * @property {string} stateMachineArn
 * @property {Object.<string, string>} input
 * @property {string[]} executionNamePrefixKeys
 * @property {Object.<string, string>} traceContext
 */

/**
 * @typedef {Object} EventHandler
 * @property {string} eventSourceArn
 * @property {string[]} eventNames
 * @property {string[]} conditions
 * @property {StateMachineConfig} stateMachineConfig
 */

/**
 * @typedef {Object} EventStreamHandlerConfig
 * @property {EventHandler[]} eventHandlers
 */

class StreamEventStateMachineHandler {
  static get METRICS_OPERATION() { return 'HandleRecord'; }
  static get METRICS_EXECUTION_EXISTS() { return 'ExecutionAlreadyExists'; }
  static get METRICS_EXECUTION_STARTED() { return 'ExecutionStarted'; }
  static get METRICS_JSON_PATH_ERROR() { return 'JsonPathError'; }
  static get EVENT_HANDLER_CONFIG() { return 'EVENT_HANDLER_CONFIG'; }

  constructor() {
    this.metricsLogger = createMetricsLogger();
    this.metricsLogger.setNamespace(process.env.AWS_LAMBDA_FUNCTION_NAME || '');
    this.metricsLogger.setDimensions({ Operation: StreamEventStateMachineHandler.METRICS_OPERATION });

    this.stepFunctionsClient = new SFNClient({
      region: process.env.AWS_REGION
    });

    this.eventStreamHandlerConfig = this.parseConfigFromEnvironment();
  }

  parseConfigFromEnvironment() {
    console.log('Parsing configuration from environment');
    try {
      return JSON.parse(process.env.EVENT_HANDLER_CONFIG || '');
    } catch (ex) {
      console.error('Unable to parse configuration, cannot start!', ex, process.env.EVENT_HANDLER_CONFIG);
      throw ex;
    }
  }

  async handleRequest(event, context) {
    console.log('Received DynamoDB event:', JSON.stringify(event));

    for (const record of event.Records) {
      const startTime = Date.now();
      let success = false;

      try {
        await this.handleRecord(record);
        success = true;
      } finally {
        const endTime = Date.now();
        this.metricsLogger.putMetric('Time', endTime - startTime, 'Milliseconds');

        if (success) {
          this.metricsLogger.putMetric('SuccessLatency', endTime - startTime, 'Milliseconds');
        }

        this.metricsLogger.setProperty('StartTime', new Date(startTime).toISOString());
        this.metricsLogger.setProperty('EndTime', new Date(endTime).toISOString());
        this.metricsLogger.putMetric('Exception', success ? 0 : 1, 'Count');
        await this.metricsLogger.flush();
      }
    }
  }

  async handleRecord(record) {
    console.log('Processing DynamoDB record:', record.eventID);

    this.metricsLogger.putMetric(StreamEventStateMachineHandler.METRICS_JSON_PATH_ERROR, 0, 'Count');
    this.metricsLogger.putMetric(StreamEventStateMachineHandler.METRICS_EXECUTION_EXISTS, 0, 'Count');

    for (const eventHandler of this.eventStreamHandlerConfig.eventHandlers) {
      if (this.recordMatchesHandler(record, eventHandler)) {
        await this.startExecution(eventHandler.stateMachineConfig, record);
      }
      else {
        console.log('Record does not match handler', eventHandler);
      }
    }
  }

  recordMatchesHandler(record, eventHandler) {
    if (!record || !eventHandler) {
      console.error('Invalid parameters: record and eventHandler are required');
      return false;
    }

    if (eventHandler.eventNames.length > 0 && !eventHandler.eventNames.includes(record.eventName || '')) {
      console.log('Event name does not match', record.eventName, eventHandler.eventNames);
      return false;
    }

    const jsonRecord = record.dynamodb;
    if (!jsonRecord) {
      console.error('Invalid parameters: record.dynamodb is required');
      return false;
    }

    if (eventHandler.conditions.length > 0) {
      return eventHandler.conditions.every(element => {
        if (!element || !element.jsonPath) {
          return false;
        }

        const query = element.jsonPath;
        try {
          const matches = JsonPath.query(jsonRecord, query);
          if (matches.length === 0) {
            console.log('Unable find any match for the condition', query, 'value', element.value);
            return false;
          }
          console.log(`JsonPath query ${query} looking for value ${element.value} running on the following record: `,jsonRecord, " found the following potential match value",  matches[0]);
          return matches[0] === element.value;
        } catch (ex) {
          console.error('Unable to run the json query', ex, query, jsonRecord);
          this.metricsLogger.putMetric(StreamEventStateMachineHandler.METRICS_JSON_PATH_ERROR, 1, 'Count');
          return false;
        }
      });
    }

    return true;
  }

  async startExecution(stateMachineConfig, record) {
    try {
      const executionName = this.buildExecutionName(record);
      const input = this.buildExecutionInput(stateMachineConfig, record);

      console.log(`Starting execution ${executionName} for state machine ${stateMachineConfig.stateMachineArn}`);

      const command = new StartExecutionCommand({
        stateMachineArn: stateMachineConfig.stateMachineArn,
        name: executionName,
        input: JSON.stringify(input)
      });

      const response = await this.stepFunctionsClient.send(command);
      
      console.log('Started execution:', response.executionArn);
      this.metricsLogger.putMetric(StreamEventStateMachineHandler.METRICS_EXECUTION_STARTED, 1, 'Count');
    } catch (error) {
      if (error.name === 'ExecutionAlreadyExists') {
        console.log('Execution already exists');
        this.metricsLogger.putMetric(StreamEventStateMachineHandler.METRICS_EXECUTION_EXISTS, 1, 'Count');
      } else {
        throw error;
      }
    }
  }

  buildExecutionName(record) {
    return `${record.eventID || Date.now()}`;
  }

  buildExecutionInput(stateMachineConfig, record) {
    if (!stateMachineConfig || !record) {
        throw new Error('Invalid parameters: stateMachineConfig and record are required');
    }

    try {
        const result = {};
        // If input mapping is defined in stateMachineConfig
        if (stateMachineConfig.input && typeof stateMachineConfig.input === 'object') {
            // For each key-value pair in the input configuration
            Object.entries(stateMachineConfig.input).forEach(([key, jsonPath]) => {
                try {
                    // Evaluate the JSONPath expression against the dynamodb property
                    const matches = JsonPath.query(record.dynamodb, jsonPath);
                    
                    if (matches && matches.length > 0) {
                        result[key] = matches[0];
                    } else {
                        console.warn(`No matches found for JSONPath: ${jsonPath} for key: ${key}`);
                        result[key] = null;
                    }
                } catch (error) {
                    console.error(`Error evaluating JSONPath for key ${key}:`, error);
                    result[key] = null;
                }
            });
        }
        console.log('Built execution input:', result);
        return result;

    } catch (error) {
        console.error('Error building execution input:', error);
        throw new Error(`Failed to build execution input: ${error.message}`);
    }
  }
}

/**
 * Lambda handler function
 */
exports.handler = async (event, context) => {
  const handler = new StreamEventStateMachineHandler();
  return handler.handleRequest(event, context);
};