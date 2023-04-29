const {Construct} = require('constructs');
const apigateway = require('aws-cdk-lib/aws-apigateway');
const route53 = require('aws-cdk-lib/aws-route53');
const route53_targets = require('aws-cdk-lib/aws-route53-targets');
const ec2 = require('aws-cdk-lib/aws-ec2');
const certificatemanager = require('aws-cdk-lib/aws-certificatemanager');
const iam = require('aws-cdk-lib/aws-iam');
const elbv2 = require('aws-cdk-lib/aws-elasticloadbalancingv2');
const elbv2_targets = require('aws-cdk-lib/aws-elasticloadbalancingv2-targets');
const cr = require('aws-cdk-lib/custom-resources');
const cdk = require("aws-cdk-lib");
const {Names} = require("aws-cdk-lib");

class PrivateApiCustomDomainConstruct extends Construct {
    /**
     *
     * @param {Construct} scope
     * @param {string} id
     * @param {StackProps=} props
     */
    constructor(scope, id, props) {
        super(scope, id, props);

        const isPublicZone = (props.publicZone || false);
        const isPrivateZone = (props.privateZone || props.privateZoneDomain || false);

        if(isPublicZone && isPrivateZone) {
            throw new Error('Unsupported zone type, it must be either public or private');
        }

        if (isPrivateZone && !props.certificate) {
            throw new Error('Certificate must be specified when using private zone');
        }

        if (isPrivateZone && !props.privateZone && !props.privateZoneDomain) {
            throw new Error('Either privateZone or privateZoneDomain must be specified');
        }

        const createVpc = (!props.vpc);
        const createCertificate = (isPublicZone && !props.certificate);
        const createPrivateZone = (isPrivateZone && !props.privateZone);

        console.table({
            'Zone Type': (isPublicZone) ? 'Public':'Private',
            'Create Zone': (isPrivateZone) ? createPrivateZone:false,
            'Create Certificate': createCertificate,
            'Create VPC': createVpc
        });

        // create or use the provided vpc
        const vpc = (!createVpc) ? props.vpc :
            new ec2.Vpc(this, `Vpc`, {
                vpcName: 'apigatewayPrivateDomain',
                maxAzs: 2,
                subnetConfiguration: [
                    {
                        name: 'apigatewayPrivateDomain',
                        subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
                    }
                ]
            });

        const privateZone = (!createPrivateZone) ? props.privateZone :
            new route53.PrivateHostedZone(this, 'PrivateZone', {
                zoneName: props.privateZoneDomain,
                vpc: vpc // At least one VPC has to be added to a Private Hosted Zone.
            });
        const zone = (isPublicZone) ? props.publicZone:privateZone;

        // create or use the provided certificate
        const certificate = (!createCertificate) ? props.certificate :
            new certificatemanager.Certificate(this, 'Certificate', {
                domainName: props.serviceFqdn,
                validation: certificatemanager.CertificateValidation.fromDns(props.publicZone)
            });

        const cid = Names.uniqueId(this).slice(-8); // extract construct id
        // provision the nlb
        const nlb = new elbv2.NetworkLoadBalancer(this, 'NlbApiGateway', {
            vpc: vpc,
            loadBalancerName: `nlb-apigateway-${cid}`,
            internetFacing: false,
            crossZoneEnabled: true
        });

        const nlbListener = nlb.addListener(`NlbHttpsListener`, {
            port: 443,
            protocol: elbv2.Protocol.TLS,
            certificates: [certificate]
        });

        const vpcEndpoint = vpc.addInterfaceEndpoint('ApiEndpoint', {
            service: ec2.InterfaceVpcEndpointAwsService.APIGATEWAY
        });

        // use a custom resource to retrieve the nic's ip of the apigateway endpoint
        const getEndpointIp = new cr.AwsCustomResource(this, `GetEndpointIps`, {
            onUpdate: {
                service: 'EC2',
                action: 'describeNetworkInterfaces',
                parameters: {NetworkInterfaceIds: vpcEndpoint.vpcEndpointNetworkInterfaceIds},
                physicalResourceId: cr.PhysicalResourceId.of('EndpointNics'), // Update physical id to always fetch the latest version
            },
            policy: cr.AwsCustomResourcePolicy.fromSdkCalls({
                resources: cr.AwsCustomResourcePolicy.ANY_RESOURCE,
            }),
        });

        // adds the endpoint ip addresses as targets in the NLB
        let nlbTargets = [];
        for (let i = 0; i <= vpcEndpoint.vpcEndpointNetworkInterfaceIds.length; i++) {
            let ipAddress = getEndpointIp.getResponseField(`NetworkInterfaces.${i}.PrivateIpAddress`);
            let ipTarget = new elbv2_targets.IpTarget(ipAddress);
            nlbTargets.push(ipTarget);
        }

        const nlbTargetGroup = new elbv2.NetworkTargetGroup(this, 'ApiGatewayTargetGroup', {
            targetGroupName: `tg-apigateway-${cid}`,
            vpc: vpc,
            port: 443,
            targetType: elbv2.TargetType.IP,
            protocol: elbv2.Protocol.TLS,
            targets: nlbTargets,
            healthCheck: {
                protocol: elbv2.Protocol.HTTPS,
                path: '/ping',
                healthyHttpCodes: '200'
            }
        });
        nlbListener.addTargetGroups('AddApiGatewayTargetGroup', nlbTargetGroup);

        new route53.ARecord(this, `AliasRecord`, {
            recordName: props.serviceFqdn,
            zone: zone,
            target: route53.RecordTarget.fromAlias(new route53_targets.LoadBalancerTarget(nlb)),
        });

        // create a policy to grant vpc access in the api
        const apiResourcePolicy = new iam.PolicyDocument({
            statements: [
                new iam.PolicyStatement({
                    effect: iam.Effect.ALLOW,
                    principals: [new iam.StarPrincipal()],
                    actions: ['execute-api:Invoke'],
                    resources: ['execute-api:/*'],
                    conditions: {
                        StringEquals: {
                            'aws:sourceVpce': vpcEndpoint.vpcEndpointId
                        }
                    }
                })
            ]
        });

        // configure custom domain and map the API
        const domainName = new apigateway.DomainName(this, `ApiGatewayCustomDomain`, {
            domainName: props.serviceFqdn,
            certificate: certificate,
            endpointType: apigateway.EndpointType.REGIONAL,
            securityPolicy: apigateway.SecurityPolicy.TLS_1_2,
        });

        // expose construct properties
        this.zone = zone;
        this.certificate = certificate;
        this.vpc = vpc;
        this.vpcEndpoint = vpcEndpoint;
        this.nlb = nlb;
        this.apigwDomain = domainName;
        this.apigwDefaultResourcePolicy = apiResourcePolicy;
    }

    /**
     * Utility method to create private API in API Gateway.
     * Note: If properties contains endpointConfiguration it must also specify types and vpcEndpoints.
     *
     * @param id
     * @param props
     * @returns {RestApi}
     */
    createPrivateApi(id, props) {
        props = props || { };
        props.endpointConfiguration = props.endpointConfiguration || {
            types: [apigateway.EndpointType.PRIVATE],
            vpcEndpoints: [this.vpcEndpoint]
        }
        props.policy = props.policy || this.apigwDefaultResourcePolicy;
        props.disableExecuteApiEndpoint = props.disableExecuteApiEndpoint || true;

        return new apigateway.RestApi(this, id, props);
    }

    /**
     * Utility method to configure an API Mapping.
     * Properties specify basePath or stage.
     *
     * @param api
     * @param props
     * @returns {BasePathMapping}
     */
    configureApiMapping(api, props) {
        let mappingProperties = {
            domainName: this.apigwDomain,
            restApi: api
        };

        if(props) {
            if (props.basePath) mappingProperties.basePath = props.basePath;
            if (props.stage) mappingProperties.stage = props.stage;
        }

        let url = (mappingProperties.basePath) ?
            `https://${this.apigwDomain.domainName}/${mappingProperties.basePath}`:
            `https://${this.apigwDomain.domainName}/`;

        new cdk.CfnOutput(this, `${api.restApiName}Out`, {value: url, description: `${api.restApiName} endpoint`});

        return new apigateway.BasePathMapping(this, `Mapping${api.restApiName}`, mappingProperties);
    }
}

module.exports = {PrivateApiCustomDomainConstruct}
