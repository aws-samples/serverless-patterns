/**
 * This Lambda function just writes a bunch of chunks progressively back to the caller
 */

/*
* We use the awslambda.streamify decorator to indicate we want to stream a response
* out of the Lambda function.
*
* The `responseStream` object implements a Node DuplexStream object that you can
* write to using `.write()`, `pipeline()` or `.pipe()`. 
*/
exports.handler = awslambda.streamifyResponse(
    async (event, responseStream, context) => {

        // Now we're ready to start writing bytes to the stream. 
        const strings = [
            "This",
            "function",
            "is",
            "streaming",
            "the",
            "response",
            "back",
            "and",
            "now",
            "it",
            "is",
            "finished!"
        ];

        // Writes a string back to the caller every 500ms
        for (let s in strings) {
            if (s == 4) {
                throw Error("This is a custom error mid-stream!");
            }
            responseStream.write(strings[s]);
            await new Promise(r => setTimeout(r, 500));
        }

        // When we are done writing to the stream, we need to call
        // `.end()` so that node knows that no more bytes will be written
        // to the stream
        responseStream.end();

    }
);