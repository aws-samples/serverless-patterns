#!/usr/bin/env node
import 'source-map-support/register'
import * as cdk from 'aws-cdk-lib'
import { AuthStack } from '../lib/AuthStack'
import { FileStorageStack } from '../lib/fileStorageStack'
import { DatabaseStack } from '../lib/DatabaseStack'
import { IdentityStack } from '../lib/IdentityStack'
import { APIStack } from '../lib/APIStack'

const app = new cdk.App()

const authStack = new AuthStack(app, 'ProductAuthStack', {})

const identityStack = new IdentityStack(app, 'ProductIdentityStack', {
	userpool: authStack.userpool,
	userpoolClient: authStack.userPoolClient,
})

const databaseStack = new DatabaseStack(app, 'ProductDatabaseStack', {})

const apiStack = new APIStack(app, 'ProductAppSyncAPIStack', {
	userpool: authStack.userpool,
	sampleTable: databaseStack.productTable,
	unauthenticatedRole: identityStack.unauthenticatedRole,
	identityPool: identityStack.identityPool,
})

const fileStorageStack = new FileStorageStack(app, 'ProductFileStorageStack', {
	authenticatedRole: identityStack.authenticatedRole,
	unauthenticatedRole: identityStack.unauthenticatedRole,
	allowedOrigins: ['http://localhost:3000'],
})
