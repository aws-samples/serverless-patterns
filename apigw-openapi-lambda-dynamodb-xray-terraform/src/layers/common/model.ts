/**
 * Model Objects.
 * © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
 * This AWS Content is provided subject to the terms of the AWS Customer Agreement
 * available at http://aws.amazon.com/agreement or other written agreement between
 * Customer and either Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.
 */

import { Expose, Type } from 'class-transformer';
import { Entity } from 'dynamodb-toolbox';
import 'reflect-metadata';
import {
	CUSTOMER_PARTITION_PREFIX,
	customerTable,
	generateDynamodbKey,
} from '/opt/common/util';

export class CustomerRequest {
	@Expose() firstname: string;
	@Expose() lastname: string;
	@Expose() zipcode: string;
}

export class CustomerResponse {
	@Expose() id: string;
	@Expose() firstname: string;
	@Expose() lastname: string;
	@Expose() zipcode: string;
	@Type(() => Error)
	@Expose()
	errors: Error[] = [];
}

export class GenericResponse {
	@Type(() => Data)
	@Expose()
	data: Data;
	@Type(() => Error)
	@Expose()
	errors: Error[] = [];
}

export class Data {
	@Expose()
	message: string;
}

export class Error {
	@Expose()
	message: string;
}

/**
 * DynamoDB Entity Definitions
 */
export const CustomerEntity = new Entity({
	name: 'customer',
	table: customerTable,
	autoParse: true,
	attributes: {
		pk: {
			partitionKey: true,
			hidden: true,
			default: (data: any) =>
				generateDynamodbKey(CUSTOMER_PARTITION_PREFIX, data.id),
		},
		sk: {
			sortKey: true,
			hidden: true,
			default: (data: any) => generateDynamodbKey(data.id),
		},
		id: { type: 'string', required: true },
		firstname: { type: 'string' },
		lastname: { type: 'string' },
		zipcode: { type: 'string' },
	},
} as const);
