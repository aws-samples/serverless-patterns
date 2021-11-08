import { CfnWebACL, CfnWebACLAssociation } from '@aws-cdk/aws-wafv2';
import * as cdk from "@aws-cdk/core";
 
export class WafStack extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string) {
        super(scope, id);
 
        // const CustomHeader = new cdk.CfnParameter(this, "CustomHeader", {
        //     type: "String",
        //     default: "x-key"
        // });
 
        //Web ACL
        const APIGatewayWebACL = new CfnWebACL(this, "APIGatewayWebACL", {
            name: "demo-api-gateway-webacl",
            description: "This is WebACL for Auth APi Gateway",
            scope: "REGIONAL",
            defaultAction: { block: {} },
            visibilityConfig: {
                metricName: "demo-APIWebACL",
                cloudWatchMetricsEnabled: true,
                sampledRequestsEnabled: true
            },
            rules: [

                {
                    name: "demo-rateLimitRule",
                    priority: 20,
                    action: { block: {} },
                    visibilityConfig: {
                        metricName: "demo-rateLimitRule",
                        cloudWatchMetricsEnabled: true,
                        sampledRequestsEnabled: false
                    },
                    statement: {
                        rateBasedStatement: {
                            aggregateKeyType: "IP",
                            limit: 100
                        }
                    }
                },
                {
                    name: `demo-api-auth-gateway-geolocation-rule`,
                    priority: 30,
                    action: { allow: {} },
                    visibilityConfig: {
                        metricName: `demo-AuthAPIGeoLocationUS`,
                        cloudWatchMetricsEnabled: true,
                        sampledRequestsEnabled: false
                    },
                    statement: {
                        geoMatchStatement: {
                            countryCodes: ['US']
                        }
                    }
                },
                {
                    name: `demo-api-auth-gateway-sqli-rule`,
                    priority: 40,
                    action: { block: {} },
                    visibilityConfig: {
                        metricName: `demo-APIAuthGatewaySqliRule`,
                        cloudWatchMetricsEnabled: true,
                        sampledRequestsEnabled: false
                    },
                    statement: {
                        orStatement: {
                            statements: [{
                                sqliMatchStatement: {
                                    fieldToMatch: {
                                        allQueryArguments: {}
                                    },
                                   textTransformations: [{
                                        priority: 1,
                                        type: "URL_DECODE"
                                    },
                                    {
                                        priority: 2,
                                        type: "HTML_ENTITY_DECODE"
                                    }]
                                }
                            },
                            {
                                sqliMatchStatement: {
                                    fieldToMatch: {
                                        body: {}
                                    },
                                    textTransformations: [{
                                        priority: 1,
                                        type: "URL_DECODE"
                                    },
                                    {
                                        priority: 2,
                                        type: "HTML_ENTITY_DECODE"
                                    }]
                                }
                            },
                            {
                                sqliMatchStatement: {
                                    fieldToMatch: {
                                        uriPath: {}
                                    },
                                    textTransformations: [{
                                        priority: 1,
                                        type: "URL_DECODE"
                                    }]
                                }
                            }]
                        }
                    }
                },
                {
                    name: `demo-detect-xss`,
                    priority: 60,
                    action: { block: {} },
                    visibilityConfig: {
                        metricName: `demo-detect-xss`,
                        cloudWatchMetricsEnabled: true,
                        sampledRequestsEnabled: false
                    },
                    statement: {
                        orStatement: {
                            statements: [
                                {
                                    xssMatchStatement: {
                                        fieldToMatch: {
                                            uriPath: {}
                                        },
                                        textTransformations: [{
                                            priority: 1,
                                            type: "URL_DECODE"
                                        },
                                        {
                                            priority: 2,
                                            type: "HTML_ENTITY_DECODE"
                                        }]
                                    }
                                },
                                {
                                    xssMatchStatement: {
                                        fieldToMatch: {
                                            allQueryArguments: {}
                                        },
                                        textTransformations: [{
                                            priority: 1,
                                            type: "URL_DECODE"
                                        },
                                        {
                                            priority: 2,
                                            type: "HTML_ENTITY_DECODE"
                                        }]
                                    }
                                },
                               
                            ]
                        }
                    }
                }
            ]
        });
 
        // Web ACL Association
        // const APIGatewayWebACLAssociation = 
        new CfnWebACLAssociation(this, "APIGatewayWebACLAssociation", {
            webAclArn: APIGatewayWebACL.attrArn,
            resourceArn: cdk.Fn.join("", ["arn:aws:apigateway:us-east-1::/restapis/", cdk.Fn.importValue("demorestapiid"), "/stages/prod", ])
        });
    }
}
 