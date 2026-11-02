import http from "node:http";

// Lambda passes the address to listen on in AWS_LAMBDA_HTTP_ENDPOINT ("host:port").
// The fallback applies only when you run the server locally.
const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || "localhost:3000").split(":");

// Set by the deploy scripts on each revision.
const commit = process.env.GIT_SHA ?? "local";

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
}

const server = http.createServer((req, res) => {
  // Lambda adds this header to every request. The deploy scripts name preview endpoints pr-<number>.
  const endpoint = req.headers["lambda-web-endpoint-name"] ?? "local";
  const pr = /^pr-(\d+)$/.exec(endpoint)?.[1];

  if (req.url === "/api/version") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ endpoint, pullRequest: pr ? Number(pr) : null, commit }));
  }

  const banner = pr
    ? `<div class="banner preview">Preview of pull request #${escapeHtml(pr)}</div>`
    : `<div class="banner production">Production</div>`;

  res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  res.end(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${pr ? `PR #${escapeHtml(pr)} preview` : "Production"}</title>
  <style>
    :root { color-scheme: light dark; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { margin: 0; display: grid; place-items: center; min-height: 100vh; }
    main { text-align: center; padding: 24px; }
    .banner { display: inline-block; padding: 10px 22px; border-radius: 999px; font-weight: 600; color: #fff; }
    .preview { background: #b45309; }
    .production { background: #15803d; }
    h1 { font-size: 32px; margin: 24px 0 8px; }
    code { font-size: 15px; }
  </style>
</head>
<body>
  <main>
    ${banner}
    <h1>Hello from AWS Lambda Web Functions</h1>
    <p>Endpoint <code>${escapeHtml(endpoint)}</code>, commit <code>${escapeHtml(commit.slice(0, 7))}</code></p>
  </main>
</body>
</html>`);
});

server.listen(Number(port), host, () => console.log(`listening on ${host}:${port}, commit ${commit}`));

// Lambda sends SIGTERM before it removes an execution environment.
process.on("SIGTERM", () => server.close(() => process.exit(0)));
