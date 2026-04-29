#!/usr/bin/env python3

from aws_cdk import (
    Stack,
    CfnOutput,
    Fn,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
)
from constructs import Construct


class CloudFrontStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, a2a_agent_runtime_arn: str, http_agent_runtime_arn: str, mcp_agent_runtime_arn: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        a2a_encoded_arn = Fn.join("", Fn.split(":", Fn.join("%3A", Fn.split(":", a2a_agent_runtime_arn))))
        a2a_encoded_arn = Fn.join("", Fn.split("/", Fn.join("%2F", Fn.split("/", a2a_encoded_arn))))

        http_encoded_arn = Fn.join("", Fn.split(":", Fn.join("%3A", Fn.split(":", http_agent_runtime_arn))))
        http_encoded_arn = Fn.join("", Fn.split("/", Fn.join("%2F", Fn.split("/", http_encoded_arn))))

        mcp_encoded_arn = Fn.join("", Fn.split(":", Fn.join("%3A", Fn.split(":", mcp_agent_runtime_arn))))
        mcp_encoded_arn = Fn.join("", Fn.split("/", Fn.join("%2F", Fn.split("/", mcp_encoded_arn))))

        a2a_agentcore_origin = origins.HttpOrigin(
            f"bedrock-agentcore.{self.region}.amazonaws.com",
            origin_path=Fn.join("", ["/runtimes/", a2a_encoded_arn, "/invocations"]),
            protocol_policy=cloudfront.OriginProtocolPolicy.HTTPS_ONLY
        )

        http_agentcore_origin = origins.HttpOrigin(
            f"bedrock-agentcore.{self.region}.amazonaws.com",
            origin_path=Fn.join("", ["/runtimes/", http_encoded_arn]),
            protocol_policy=cloudfront.OriginProtocolPolicy.HTTPS_ONLY
        )

        mcp_agentcore_origin = origins.HttpOrigin(
            f"bedrock-agentcore.{self.region}.amazonaws.com",
            origin_path=Fn.join("", ["/runtimes/", mcp_encoded_arn]),
            protocol_policy=cloudfront.OriginProtocolPolicy.HTTPS_ONLY
        )

        strip_a2a_prefix_fn = cloudfront.Function(self, "StripA2aPrefixFunction",
            code=cloudfront.FunctionCode.from_inline("""
function handler(event) {
    var request = event.request;
    request.uri = request.uri.replace(/^\\/a2a/, '');
    if (request.uri === '') request.uri = '/';
    return request;
}
"""),
            runtime=cloudfront.FunctionRuntime.JS_2_0
        )

        strip_http_prefix_fn = cloudfront.Function(self, "StripHttpPrefixFunction",
            code=cloudfront.FunctionCode.from_inline("""
function handler(event) {
    var request = event.request;
    request.uri = request.uri.replace(/^\\/rest/, '');
    if (request.uri === '') request.uri = '/';
    return request;
}
"""),
            runtime=cloudfront.FunctionRuntime.JS_2_0
        )

        strip_mcp_prefix_fn = cloudfront.Function(self, "StripMcpPrefixFunction",
            code=cloudfront.FunctionCode.from_inline("""
function handler(event) {
    var request = event.request;
    request.uri = request.uri.replace(/^\\/mcp/, '');
    if (request.uri === '') request.uri = '/';
    return request;
}
"""),
            runtime=cloudfront.FunctionRuntime.JS_2_0
        )

        dummy_origin = origins.HttpOrigin("aws.amazon.com")

        distribution = cloudfront.Distribution(self, "Distribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=dummy_origin,
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                cache_policy=cloudfront.CachePolicy.CACHING_DISABLED
            ),
            additional_behaviors={
                "/a2a/*": cloudfront.BehaviorOptions(
                    origin=a2a_agentcore_origin,
                    viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                    allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                    cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                    origin_request_policy=cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER,
                    function_associations=[
                        cloudfront.FunctionAssociation(
                            function=strip_a2a_prefix_fn,
                            event_type=cloudfront.FunctionEventType.VIEWER_REQUEST
                        )
                    ]
                ),
                "/rest/*": cloudfront.BehaviorOptions(
                    origin=http_agentcore_origin,
                    viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                    allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                    cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                    origin_request_policy=cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER,
                    function_associations=[
                        cloudfront.FunctionAssociation(
                            function=strip_http_prefix_fn,
                            event_type=cloudfront.FunctionEventType.VIEWER_REQUEST
                        )
                    ]
                ),
                "/mcp/*": cloudfront.BehaviorOptions(
                    origin=mcp_agentcore_origin,
                    viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                    allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                    cache_policy=cloudfront.CachePolicy.CACHING_DISABLED,
                    origin_request_policy=cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER,
                    function_associations=[
                        cloudfront.FunctionAssociation(
                            function=strip_mcp_prefix_fn,
                            event_type=cloudfront.FunctionEventType.VIEWER_REQUEST
                        )
                    ]
                )
            },
            price_class=cloudfront.PriceClass.PRICE_CLASS_100
        )

        CfnOutput(self, "DistributionUrl", value=f"https://{distribution.distribution_domain_name}")
