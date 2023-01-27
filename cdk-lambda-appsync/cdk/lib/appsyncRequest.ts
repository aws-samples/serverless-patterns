import * as https from 'https'
import { URL } from 'url'

const AWS = require('aws-sdk')
import { HttpRequest, Endpoint } from 'aws-sdk'

const region = process.env.AWS_REGION!

export type QueryDetails = {
	query: string
	variables?: { [key: string]: any }
}

export interface GraphQLResult<T = object> {
	data?: T
	errors?: any[]
	extensions?: { [key: string]: any }
}

/**
 *
 * @param {Object} queryDetails the query, operationName, and variables
 * @param {String} appsyncUrl url of your AppSync API
 * @param {String} apiKey the api key to include in headers. if null, will sign with SigV4
 */
const request = <T = object>(
	queryDetails: QueryDetails,
	appsyncUrl: string,
	apiKey?: string
) => {
	const endpoint = new URL(appsyncUrl).hostname
	const req = new HttpRequest(new Endpoint(endpoint), region)

	req.method = 'POST'
	req.path = '/graphql'
	req.headers.host = endpoint
	req.headers['Content-Type'] = 'application/json'
	req.body = JSON.stringify(queryDetails)

	if (apiKey) {
		req.headers['x-api-key'] = apiKey
	} else {
		const signer = new AWS.Signers.V4(req, 'appsync', true)
		signer.addAuthorization(AWS.config.credentials, AWS.util.date.getDate())
	}

	return new Promise<GraphQLResult<T>>((resolve, reject) => {
		const httpRequest = https.request({ ...req, host: endpoint }, (result) => {
			result.on('data', (data) => {
				resolve(JSON.parse(data.toString()))
			})
		})
		httpRequest.write(req.body)
		httpRequest.end()
	})
}

export default request
