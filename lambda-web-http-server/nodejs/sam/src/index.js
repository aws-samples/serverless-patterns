import http from 'http';
import os from 'os';

// Lambda Web runtime sets AWS_LAMBDA_HTTP_ENDPOINT (0.0.0.0:3000) and waits for
// the app to listen there. PORT is honored only as a local-dev fallback.
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? `0.0.0.0:${process.env.PORT || 3000}`).split(':');
const PORT = Number(PORT_STR) || 3000;

// Concurrency tracking
let activeRequests = 0;
let peakConcurrency = 0;
let totalRequests = 0;

// Create HTTP server
const server = http.createServer((req, res) => {
  const requestStartTime = Date.now();
  const timestamp = new Date().toISOString();
  
  // Increment counters
  activeRequests++;
  totalRequests++;
  if (activeRequests > peakConcurrency) {
    peakConcurrency = activeRequests;
  }
  const currentConcurrency = activeRequests;
  
  console.log(`Request received at ${timestamp} (concurrency: ${currentConcurrency})`);
  
  // Read request body
  let body = '';
  
  req.on('data', chunk => {
    body += chunk.toString();
  });
  
  req.on('end', async () => {
    // Artificial delay for concurrency testing
    await new Promise(resolve => setTimeout(resolve, 100));
    
    // Capture metrics at response time
    const peakDuringRequest = peakConcurrency;
    activeRequests--;
    const activeAtResponse = activeRequests;
    
    // Set response headers
    res.writeHead(200, {'Content-Type': 'application/json'});
    
    // Create response object with concurrency metrics
    // Note that we only echo back select information, like 'user-agent'.
    // Echoing back all fields from objects like req.headers or process.env
    // is not recommended as these may change over time.
    const responseBody = {
      message: `Answered at ${timestamp}`,
      timestamp: timestamp,
      requestMethod: req.method,
      requestUrl: req.url,
      requestUserAgent: req.headers['user-agent'],
      requestBodyLength: body.length,
      workingDirectory: process.env['PWD'],
      concurrencyMetrics: {
        currentConcurrency: currentConcurrency,
        peakConcurrency: peakDuringRequest,
        activeAtResponse: activeAtResponse,
        totalRequests: totalRequests,
        processingTimeMs: Date.now() - requestStartTime
      }
    };
    
    // Send response
    res.end(JSON.stringify(responseBody, null, 2));
  });
});

// Start server
server.listen(PORT, HOST, () => {
  console.log(`Lambda function listening on ${HOST}:${PORT}`);
  console.log(`Hostname: ${os.hostname()}`);
});

// Handle server errors
server.on('error', (err) => {
  console.error('Server error:', err);
});

// Handle process termination
process.on('SIGTERM', () => {
  console.log('SIGTERM received, shutting down gracefully');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});