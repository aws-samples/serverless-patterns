const net = require('net');

// Simple RESP protocol client (no external deps needed)
async function sendCommand(host, port, ...args) {
  return new Promise((resolve, reject) => {
    const socket = new net.Socket();
    socket.setTimeout(5000);
    let data = '';
    const cmd = `*${args.length}\r\n${args.map(a => `$${Buffer.byteLength(a)}\r\n${a}`).join('\r\n')}\r\n`;
    socket.connect(parseInt(port), host, () => socket.write(cmd));
    socket.on('data', chunk => { data += chunk; socket.end(); });
    socket.on('end', () => resolve(data.split('\r\n')[1] || data));
    socket.on('error', reject);
    socket.on('timeout', () => { socket.destroy(); reject(new Error('timeout')); });
  });
}

exports.handler = async (event) => {
  const { CACHE_ENDPOINT, CACHE_PORT } = process.env;
  const body = JSON.parse(event.body || '{}');
  const { action, key, value, ttl } = body;

  if (!action || !key) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Missing action and key' }) };
  }

  let result;
  if (action === 'set') {
    result = ttl
      ? await sendCommand(CACHE_ENDPOINT, CACHE_PORT, 'SET', key, value || '', 'EX', String(ttl))
      : await sendCommand(CACHE_ENDPOINT, CACHE_PORT, 'SET', key, value || '');
  } else if (action === 'get') {
    result = await sendCommand(CACHE_ENDPOINT, CACHE_PORT, 'GET', key);
  } else if (action === 'del') {
    result = await sendCommand(CACHE_ENDPOINT, CACHE_PORT, 'DEL', key);
  } else {
    return { statusCode: 400, body: JSON.stringify({ error: 'Invalid action. Use: set, get, del' }) };
  }

  return { statusCode: 200, body: JSON.stringify({ action, key, result }) };
};
