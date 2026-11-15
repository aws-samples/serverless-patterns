//Lambda Runtime delivers a batch of messages to the lambda function
//Each batch of messages has two fields EventSource and EventSourceARN
//Each batch of messages also has a field called Records
//The Records is a map with multiple keys and values
//Each key is a combination of the Topic Name and the Partition Number
//One batch of messages can contain messages from multiple partitions

export const handler = async (event) => {
    // Iterate through keys
    for (let key in event.records) {
      console.log('Key: ', key)
      // Iterate through messages inside a key
      event.records[key].map((record) => {
		//printing the fields of each message
        console.log('Record: ', record)
        console.log('Topic: ', record.topic)
        console.log('Partition: ', record.partition)
        console.log('Offset: ', record.offset)
        console.log('Timestamp: ', record.timestamp)
        console.log('TimestampType: ', record.timestampType)
        //key and value are base64 encoded and need to be decoded
        if (null != record.key){
          const thisKey = Buffer.from(record.key, 'base64').toString()
          console.log('Key:', thisKey)
        } else {
          console.log('Key:', 'null')
        }
        const value = Buffer.from(record.value, 'base64').toString()
        console.log('Value:', value)
      }) 
    }
}