/**
 * This code initializes logger, tracer and aws sdk clients for use with all lambdas.
 * © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
 * This AWS Content is provided subject to the terms of the AWS Customer Agreement
 * available at http://aws.amazon.com/agreement or other written agreement between
 * Customer and either Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.
 */

import { Logger } from '@aws-lambda-powertools/logger';
import { Tracer } from '@aws-lambda-powertools/tracer';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient } from '@aws-sdk/lib-dynamodb';
import { Table } from 'dynamodb-toolbox';
import { customAlphabet } from 'nanoid';

// Logger
const logger = new Logger({
	persistentLogAttributes: {
		aws_account_id: process.env.ACCOUNT_ID,
		aws_region: process.env.AWS_REGION,
		project: process.env.PROJECT,
	},
	environment: process.env.ENVIRONMENT,
	serviceName: process.env.SERVICE_NAME,
});

// X-Ray Tracer
const tracer = new Tracer({
	serviceName: process.env.SERVICE_NAME,
});

const marshallOptions = {
	convertEmptyValues: false,
};

const translateConfig = { marshallOptions };

// DynamoDB SDK Client
const DocumentClient = DynamoDBDocumentClient.from(
	tracer.captureAWSv3Client(new DynamoDBClient({ region: process.env.AWS_REGION })),
	translateConfig
);

// Instrument DynamoDB Calls
// const ddbClient = tracer.captureAWSv3Client(DocumentClient);

// Instantiate a table
const customerTable = new Table({
	// Specify table name (used by DynamoDB)
	name: String(process.env.CUSTOMER_DDB_NAME),

	// Define partition keys, sort keys and indexes
	partitionKey: 'pk',
	sortKey: 'sk',

	// Add the DocumentClient
	DocumentClient,
});

// Response Headers
const responseHeaders = {
	'Access-Control-Allow-Origin': '*', // Required for CORS support to work
	'Access-Control-Allow-Credentials': true, // Required for cookies, authorization headers with HTTPS
	'Content-Type': 'application/json',
};

// DynamoDB Partition Identifier Prefixes
const CUSTOMER_PARTITION_PREFIX = 'C';

// Generate DynamoDB composite key
function generateDynamodbKey(...params: string[]) {
	return params.join('#');
}

// Pagination: Page Size. Example 20 items per page
const PAGE_SIZE = 25;

/**
 * Generate an unique event id
 * @returns
 */
async function generateCustomerId() {
	const nanoid = customAlphabet('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', 15);
	return nanoid();
}

/**
 * Generate final response to be sent back.
 * @param code
 * @param body
 * @returns
 */
function getApiResponseObj(code: number, body: any) {
	return {
		statusCode: code,
		body: JSON.stringify(body),
		headers: responseHeaders,
	};
}

// Exports
export {
	logger,
	tracer,
	customerTable,
	responseHeaders,
	CUSTOMER_PARTITION_PREFIX,
	PAGE_SIZE,
	generateDynamodbKey,
	generateCustomerId,
	getApiResponseObj,
};
