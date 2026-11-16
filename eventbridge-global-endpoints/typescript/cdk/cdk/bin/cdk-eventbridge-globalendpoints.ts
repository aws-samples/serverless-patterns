#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { EventBusStack } from '../lib/event-bus-stack';
import { GlobalEndpointStack } from '../lib/global-endpoint-stack';

import { PutEventsStack } from '../lib/put-events-stack';
import { BoilerPlateStack } from '../lib/boilerplate-stack';

const mainRegion = 'us-east-1';
const secondaryRegion = 'eu-west-1';
const eventBusName = 'EventBridgeGlobalEndpointPattern';

const app = new cdk.App();

// PRIMARY STACK ------
const eventBusStackMainRegion = new EventBusStack(
	app,
	'EventBusStackMainRegion',
	{
		eventBusName: eventBusName,
		env: {
			region: mainRegion,
		},
	}
);

// SECONDARY STACK ------
const eventBusStackSecondaryRegion = new EventBusStack(
	app,
	'EventBusStackSecondaryRegion',
	{
		eventBusName: eventBusName,
		env: {
			region: secondaryRegion,
		},
	}
);

// HEALTHCHECKS AND OTHER GLOBAL CONFIGURATIONS -----
const boilerPlateStack = new BoilerPlateStack(app, 'BoilerPlateStack', {
	env: {
		region: mainRegion,
	},
	eventBusName: eventBusName,
});

// GLOBAL ENDPOINT -----
const globalEndpointStack = new GlobalEndpointStack(
	app,
	'GlobalEndpointStack',
	{
		env: {
			region: mainRegion,
		},
		replicatedRegion: secondaryRegion,
		eventBusArn1: eventBusStackMainRegion.eventBusArn,
		eventBusArn2: eventBusStackSecondaryRegion.eventBusArn,
		healthCheckArn: boilerPlateStack.healthCheckArn,
		replicatedRoleArn: boilerPlateStack.replicationRoleArn,
	}
);

// TESTING STACK
new PutEventsStack(app, 'PutEventsStack', {
	env: {
		region: mainRegion,
	},
	eventBusName: eventBusName,
	endpointId: globalEndpointStack.endpointId,
});
