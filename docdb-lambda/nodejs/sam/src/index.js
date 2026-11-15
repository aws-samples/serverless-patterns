console.log('Loading function');
        exports.handler = async (event) => {
          // TODO implement
          console.log('Received event:', JSON.stringify(event, null, 2));
            return 'OK';
        };