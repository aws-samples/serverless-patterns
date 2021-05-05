var path = require("path");

const redirects = {
  // "/redirect-from/example1": { to: "/target1", statusCode: 301 },
  // "/redirect-from/example2": { to: "/target2", statusCode: 302 },
};

exports.onViewerRequest = async (event) => {
  const { request } = event.Records[0].cf;
  const normalisedUri = normalise(request.uri);
  const redirect = redirects[normalisedUri];
  if (redirect) {
    return redirectTo(redirect.to, redirect.statusCode);
  }
  if (!hasExtension(normalisedUri)) {
    // Support default documents in subdirectories within S3.
    request.uri += "/index.html";
  }
  return request;
};

const trimSlash = (uri) => (hasTrailingSlash(uri) ? uri.slice(0, -1) : uri);
const normalise = (uri) => trimSlash(uri).toLowerCase();
const hasExtension = (uri) => path.extname(uri) !== "";
const hasTrailingSlash = (uri) => uri.endsWith("/");

const redirectTo = (to, statusCode) => ({
  status: statusCode.toString(),
  statusDescription: "Found",
  headers: {
    location: [
      {
        key: "Location",
        value: to,
      },
    ],
  },
});
