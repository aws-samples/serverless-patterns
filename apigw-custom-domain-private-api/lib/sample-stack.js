const {Stack} = require('aws-cdk-lib');
const route53 = require('aws-cdk-lib/aws-route53');
const apigateway = require('aws-cdk-lib/aws-apigateway');
const {PrivateApiCustomDomainConstruct} = require('./private-api-custom-domain-construct')
const {TestingConstruct} = require("./testing-construct");

// replace the values before deploy
const HOSTED_ZONE_ID = 'Z0000000XXXXXXXXXXXX';
const HOSTED_ZONE_NAME = 'domain.com';
const SERVICE_FQDN = 'api.domain.com';

/**
 * Sample CDK Stack using Route53 public hosted zone using.
 * This will one mock API at https://<SERVICE_FQDN>/hello
 */
class SampleStack extends Stack {
    /**
     *
     * @param {Construct} scope
     * @param {string} id
     * @param {StackProps=} props
     */
    constructor(scope, id, props) {
        super(scope, id, props);

        // import a Route53 hosted zone
        const publicZone = route53.HostedZone.fromHostedZoneAttributes(this, `HostedZone`, {
            hostedZoneId: HOSTED_ZONE_ID,
            zoneName: HOSTED_ZONE_NAME
        });

        // instantiate the construct
        const publicZoneCustomDomain = new PrivateApiCustomDomainConstruct(this, 'PrivateAPICustomDomain', {
            publicZone: publicZone,
            serviceFqdn: SERVICE_FQDN
        });

        // create an API using a construct utility method
        const api = publicZoneCustomDomain.createPrivateApi('private-api-1');

        // define a mock API
        api.root.addMethod('ANY',
            new apigateway.MockIntegration({
                integrationResponses: [
                    {
                        statusCode: '200',
                        responseTemplates: {
                            'application/json': `{ "message": "Hello from private API!" }`
                        }
                    }
                ],
                requestTemplates: {
                    'application/json': '{ "statusCode": 200 }'
                }
            }),
            {
                methodResponses: [
                    {statusCode: '200'},
                ]
            });

        // configure the API mapping using a construct utility method
        publicZoneCustomDomain.configureApiMapping(api, {basePath: 'hello'});

        // aux construct for testing
        new TestingConstruct(this, 'TestingStack', {vpc: publicZoneCustomDomain.vpc});
    }
}

module.exports = {SampleStack}