/**
 * This code is a lambda function returns list of events.
 * © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
 * This AWS Content is provided subject to the terms of the AWS Customer Agreement
 * available at http://aws.amazon.com/agreement or other written agreement between
 * Customer and either Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.
 */

'use strict';
import { injectLambdaContext } from '@aws-lambda-powertools/logger';
import { captureLambdaHandler } from '@aws-lambda-powertools/tracer';
import middy from '@middy/core';
import httpHeaderNormalizer from '@middy/http-header-normalizer';
import httpRouterHandler from '@middy/http-router';
import { plainToClass, plainToInstance } from 'class-transformer';
import {
	CustomerEntity,
	CustomerRequest,
	CustomerResponse,
	GenericResponse,
} from '/opt/common/model';
import {
	CUSTOMER_PARTITION_PREFIX,
	generateCustomerId,
	generateDynamodbKey,
	getApiResponseObj,
	logger,
	tracer,
} from '/opt/common/util';

/**
 * Handler to serve retrival of customer by id
 */
const getCustomerHandler = middy()
	.use(captureLambdaHandler(tracer))
	.handler(async (event: any, context: any) => {
		let apiResp;
		let customerResponse: CustomerResponse = new CustomerResponse();
		try {
			const customerId = event.pathParameters['id'];
			const customer = {
				pk: generateDynamodbKey(CUSTOMER_PARTITION_PREFIX, customerId),
				sk: generateDynamodbKey(customerId),
			};
			const response: any = await CustomerEntity.get(customer);
			logger.info(response);
			if (response.Item) {
				customerResponse = mapResponseToCustomer(response.Item);
				apiResp = getApiResponseObj(200, customerResponse);
			} else {
				const message = 'No customers found';
				logger.warn(message);
				customerResponse = mapResponseToCustomer({
					errors: [{ message: message }],
				});
				apiResp = getApiResponseObj(404, customerResponse);
			}
		} catch (err: any) {
			const message = 'Unknown error occurred, please check logs';
			logger.error(message, err);
			customerResponse = mapResponseToCustomer({
				errors: [{ message: message }],
			});
			apiResp = getApiResponseObj(500, customerResponse);
		}
		return apiResp;
	});

/**
 * Handler to serve adding new customer
 */
const addCustomerHandler = middy()
	.use(captureLambdaHandler(tracer))
	.handler(async (event: any, context: any) => {
		let apiResp;
		let customerResponse: CustomerResponse = new CustomerResponse();
		try {
			const request = getRequestObj(event);
			const id = await generateCustomerId();
			const customer = {
				id: id,
				firstname: request.firstname,
				lastname: request.lastname,
				zipcode: request.zipcode,
			};
			const response: any = await CustomerEntity.put(customer);
			logger.info(response);
			customerResponse = mapResponseToCustomer(customer);
			apiResp = getApiResponseObj(200, customerResponse);
		} catch (err: any) {
			const message = 'Unknown error occurred, please check logs';
			logger.error(message, err);
			customerResponse = mapResponseToCustomer({
				errors: [{ message: message }],
			});
			apiResp = getApiResponseObj(500, customerResponse);
		}
		return apiResp;
	});

/**
 * Handler to serve updating a customer
 */
const updateCustomerHandler = middy()
	.use(captureLambdaHandler(tracer))
	.handler(async (event: any, context: any) => {
		let apiResp;
		let genericResponse: GenericResponse = new GenericResponse();
		try {
			const request = getRequestObj(event);
			const customerId = event.pathParameters['id'];
			const customer = {
				id: customerId,
				firstname: request.firstname,
				lastname: request.lastname,
				zipcode: request.zipcode,
			};
			const response: any = await CustomerEntity.update(customer);
			logger.info(response);
			genericResponse = mapResponseToGeneric({
				data: { message: 'Customer successfully updated' },
			});
			apiResp = getApiResponseObj(200, genericResponse);
		} catch (err: any) {
			const message = 'Unknown error occurred, please check logs';
			logger.error(message, err);
			genericResponse = mapResponseToGeneric({
				errors: [{ message: message }],
			});
			apiResp = getApiResponseObj(500, genericResponse);
		}
		return apiResp;
	});

/**
 * Handler to serve deleting a customer
 */
const removeCustomerHandler = middy()
	.use(captureLambdaHandler(tracer))
	.handler(async (event: any, context: any) => {
		let apiResp;
		let genericResponse: GenericResponse = new GenericResponse();
		try {
			const customerId = event.pathParameters['id'];
			const customer = {
				pk: generateDynamodbKey(CUSTOMER_PARTITION_PREFIX, customerId),
				sk: generateDynamodbKey(customerId),
			};
			const response: any = await CustomerEntity.delete(customer);
			logger.info(response);
			genericResponse = mapResponseToGeneric({
				data: { message: 'Customer successfully removed' },
			});
			apiResp = getApiResponseObj(200, genericResponse);
		} catch (err: any) {
			const message = 'Unknown error occurred, please check logs';
			logger.error(message, err);
			genericResponse = mapResponseToGeneric({
				errors: [{ message: message }],
			});
			apiResp = getApiResponseObj(500, genericResponse);
		}
		return apiResp;
	});

/**
 * Parse event body into request object
 * @param event
 * @returns
 */
function getRequestObj(event: any) {
	const request: CustomerRequest = plainToClass(
		CustomerRequest,
		JSON.parse(event.body),
		{
			excludeExtraneousValues: true,
		}
	);
	logger.info(JSON.stringify(request));
	return request;
}

/**
 * Map DynamoDB response to Customer response object
 * @param item
 * @returns
 */
function mapResponseToCustomer(item: any) {
	const customer: CustomerResponse = plainToInstance(CustomerResponse, item, {
		excludeExtraneousValues: true,
	});
	return customer;
}

/**
 * Map DynamoDB response to Customer response object
 * @param item
 * @returns
 */
function mapResponseToGeneric(item: any) {
	const generic: GenericResponse = plainToInstance(GenericResponse, item, {
		excludeExtraneousValues: true,
	});
	return generic;
}

/**
 * Http route definition
 */
const routes: any = [
	{
		method: 'POST',
		path: '/customers',
		handler: addCustomerHandler,
	},
	{
		method: 'GET',
		path: '/customers/{id}',
		handler: getCustomerHandler,
	},
	{
		method: 'PUT',
		path: '/customers/{id}',
		handler: updateCustomerHandler,
	},
	{
		method: 'DELETE',
		path: '/customers/{id}',
		handler: removeCustomerHandler,
	},
];

/**
 * Lambda handler wraped inside middy
 * Entrypoint
 */
exports.handler = middy()
	.use(
		injectLambdaContext(logger, {
			clearState: true,
			logEvent: true,
		})
	)
	.use(httpHeaderNormalizer())
	.handler(httpRouterHandler(routes))
	// .use(captureLambdaHandler(tracer));
