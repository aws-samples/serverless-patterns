var __defProp = Object.defineProperty;
var __markAsModule = (target) => __defProp(target, "__esModule", {value: true});
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, {get: all[name], enumerable: true});
};

// api/lambda/index.ts
__markAsModule(exports);
__export(exports, {
  ProxyLambda: () => handler
});

// api/config.json
var prefix = "WAFAPIGateway";
var description = "A VPC Lambda to get request from API Gateway protected by WAF";
var api = {
  handler: "ProxyLambda"
};
var headers = {
  "Content-Type": "text/plain;charset=utf-8"
};
var tags = [
  {key: "Key", value: "Value"},
  {key: "Project", value: "APIGatewayWAF"}
];
var config_default = {
  prefix,
  description,
  api,
  headers,
  tags
};

// api/lambda/api-handler.ts
var handler = async (event) => {
  return {
    body: `Success path: "${event.path}"`,
    headers: config_default.headers,
    statusCode: 200
  };
};
//# sourceMappingURL=index.js.map
