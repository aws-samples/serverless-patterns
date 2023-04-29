const {Stack} = require('aws-cdk-lib');
const {PrivateApiCustomDomainConstruct} = require('./private-api-custom-domain-construct')
const apigateway = require('aws-cdk-lib/aws-apigateway');
const certificatemanager = require('aws-cdk-lib/aws-certificatemanager');
const {TestingConstruct} = require("./testing-construct");

// replace the values before deploy
const PRIVATE_CERTIFICATE_ARN = 'arn:aws:acm:<aws_region>:<account_id>:certificate/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee';

/**
 * Sample CDK Stack using Route53 private hosted zone using.
 * This will publish three mock APIs:
 *  - API 1 -> https://<SERVICE_FQDN>/
 *  - API 2 -> https://<SERVICE_FQDN>/api2
 *  - API 3 -> https://<SERVICE_FQDN>/api3
 */
class SamplePrivateZoneStack extends Stack {
    /**
     *
     * @param {Construct} scope
     * @param {string} id
     * @param {StackProps=} props
     */
    constructor(scope, id, props) {
        super(scope, id, props);

        const certificate = certificatemanager.Certificate.fromCertificateArn(this, 'privateCertificate', PRIVATE_CERTIFICATE_ARN);
        const privateZoneCustomDomain = new PrivateApiCustomDomainConstruct(this, 'PrivateAPICustomDomain', {
            vpc: undefined, // optional
            certificate: certificate,
            privateZone: undefined, // optional
            privateZoneDomain: 'private.domain.com', // required if privateZone is not provided
            serviceFqdn: 'api.private.domain.com'
        });

        createMockApi(privateZoneCustomDomain, 'private-api-1', 'hello from API 1!');
        createMockApi(privateZoneCustomDomain, 'private-api-2', 'hello from API 2!', 'api2');
        createMockApi(privateZoneCustomDomain, 'private-api-3', 'hello from API 3!', 'api3');

        new TestingConstruct(this, 'PrivateDomainTestingStack', {vpc: privateZoneCustomDomain.vpc});
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

module.exports = {SamplePrivateZoneStack}
