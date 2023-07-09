import util from 'util'; 
import stream from 'stream';
const { Readable } = stream;
const pipeline = util.promisify(stream.pipeline);

export const handler = awslambda.streamifyResponse(async (event, responseStream, _context) => {
  const requestStream = Readable.from(Buffer.from(new Array(1024*1024).join( '🚣' )));
  await pipeline(requestStream, responseStream);
});