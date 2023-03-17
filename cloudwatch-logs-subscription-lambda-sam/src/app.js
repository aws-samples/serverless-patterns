const zlib = require('zlib');

exports.handler = function(event, context) {
  console.log(JSON.stringify(event, 0, null))
  
  if (event.awslogs) {
	var payload = new Buffer.from(event.awslogs.data, 'base64')
	zlib.gunzip(payload, function(e, result) {
        if (e) { 
            context.fail(e);
        } else {
            result = JSON.parse(result.toString());
            console.log("Event Data:", JSON.stringify(result, null, 2));
            context.succeed();
        }
    });
    
  }
}