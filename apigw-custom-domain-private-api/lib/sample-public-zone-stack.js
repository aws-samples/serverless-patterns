const {Stack} = require('aws-cdk-lib');
const route53 = require('aws-cdk-lib/aws-route53');
const apigateway = require('aws-cdk-lib/aws-apigateway');
const {PrivateApiCustomDomainConstruct} = require('./private-api-custom-domain-construct')
const {TestingConstruct} = require("./testing-construct");

// replace the values before deploy
const HOSTED_ZONE_ID = 'Z0000000000000000000';
const HOSTED_ZONE_NAME = 'domain.com';
const SERVICE_FQDN = 'api.domain.com';


/**
 * Sample CDK Stack using Route53 public hosted zone using.
 * This stack will publish three mock APIs:
 *  - API 1 -> https://<SERVICE_FQDN>/
 *  - API 2 -> https://<SERVICE_FQDN>/api2
 *  - API 3 -> https://<SERVICE_FQDN>/api3
 */
class SamplePublicZoneStack extends Stack {
    /**
     *
     * @param {Construct} scope
     * @param {string} id
     * @param {StackProps=} props
     */
    constructor(scope, id, props) {
        super(scope, id, props);

        const publicZone = route53.HostedZone.fromHostedZoneAttributes(this, `HostedZone`, {
            hostedZoneId: HOSTED_ZONE_ID,
            zoneName: HOSTED_ZONE_NAME
        });

        const publicZoneCustomDomain = new PrivateApiCustomDomainConstruct(this, 'PrivateAPICustomDomain', {
            vpc: undefined, // optional
            publicZone: publicZone,
            certificate: undefined, // optional - Note: it must match the serviceFqdn.
            serviceFqdn: SERVICE_FQDN
        });

        createMockApi(publicZoneCustomDomain, 'private-api-1', 'hello from API 1!');
        createMockApi(publicZoneCustomDomain, 'private-api-2', 'hello from API 2!', 'api2');
        createMockApi(publicZoneCustomDomain, 'private-api-3', 'hello from API 3!', 'api3');

        // aux construct for testing
        new TestingConstruct(this, 'TestingStack', {vpc: publicZoneCustomDomain.vpc});
    }
}

function createMockApi(hostedZone, apiId, message, basePath) {
    const mockIntegration = new apigateway.MockIntegration({
        integrationResponses: [
            {
                statusCode: '200',
                responseTemplates: {
                    'application/json': `{ "message": "${message}" }`
                }
            }
        ],
        requestTemplates: {
            'application/json': '{ "statusCode": 200 }'
        }
    });
    const methodOptions = {
        methodResponses: [
            {statusCode: '200'},
        ]
    };

    const api = hostedZone.createPrivateApi(apiId);
    api.root.addMethod('ANY', mockIntegration, methodOptions);
    hostedZone.configureApiMapping(api, {basePath: basePath});

    return api;
}

module.exports = {SamplePublicZoneStack}
