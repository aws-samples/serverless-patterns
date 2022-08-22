"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// api/lambda/index.ts
var lambda_exports = {};
__export(lambda_exports, {
  ApiLambda: () => handler
});
module.exports = __toCommonJS(lambda_exports);

// api/config.json
var config_default = {
  apiName: "ServerlessLand",
  apiDescription: "General purpose Lambda to get request from API Gateway with CDK",
  api: {
    handler: "ApiLambda"
  },
  headers: {
    "Content-Type": "text/plain;charset=utf-8",
    "X-Clacks-Overhead": "GNU Terry Pratchett"
  },
  tags: [
    {
      key: "Key",
      value: "Value"
    },
    {
      key: "Project",
      value: "ServerlessLand"
    }
  ]
};

// api/lambda/api.ts
var handler = async (event) => {
  return {
    body: `Hello Serverless Citizen, your happy path is: "${event.path} using ${event.httpMethod}"`,
    headers: config_default.headers,
    statusCode: 200
  };
};
// Annotate the CommonJS export names for ESM import in node:
0 && (module.exports = {
  ApiLambda
});
//# sourceMappingURL=index.js.map
