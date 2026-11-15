var path = require("path");

const cors = {
  allow: ["*"],
  allowCredentials: true,
};

exports.onOriginResponse = async (event) => {
  const request = event.Records[0].cf.request;
  const response = event.Records[0].cf.response;
  if (!response.headers) {
    response.headers = {};
  }
  if ("origin" in request.headers && isAllowed(request.headers.origin)) {
    response.headers["access-control-allow-origin"] = [
      { key: "Access-Control-Allow-Origin", value: "*" },
    ];
    response.headers["access-control-allow-methods"] = [
      { key: "Access-Control-Allow-Methods", value: "GET, HEAD, POST" },
    ];
    response.headers["access-control-max-age"] = [
      { key: "Access-Control-Max-Age", value: "86400" },
    ];
  }
  return response;
};

const isAllowed = (origin) =>
  origin == undefined ||
  cors.allow === "*" ||
  cors.allow
    .map((ao) => ao == "*" || ao.indexOf(origin) !== -1)
    .reduce((prev, current) => prev || current);
