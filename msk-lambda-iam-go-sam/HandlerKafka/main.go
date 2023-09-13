package main

import (
	"context"
	b64 "encoding/base64"
	"fmt"
	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

//Core lambda Kafka event handling logic

func handler(ctx context.Context, kafkaEvent events.KafkaEvent) error {

	//Lambda Runtime delivers a batch of messages to the lambda function
	//Each batch of messages has two fields EventSource and EventSourceARN
	//Each batch of messages also has a field called Records
	//The Records is a map with multiple keys and values
	//Each key is a combination of the Topic Name and the Partition Number
	//One batch of messages can contain messages from multiple partitions
	eventSource := kafkaEvent.EventSource
	eventSourceARN := kafkaEvent.EventSourceARN
	records := kafkaEvent.Records
	fmt.Println("EventSource = ", eventSource)
	fmt.Println("EventSourceARN = ", eventSourceARN)
	//Defining a variable to keep track of the message number in the batch
	var i = 1
	//Now looping through the keys in the map
	for key, arrayOfKafkaMessage := range records {
		fmt.Println("This Key = ", key)
		//Each key (topic-partition) can in turn have a number of messages
		//Now looping through the messages in a particular key and getting fields in the message
		for _, thisKafkaMessage := range arrayOfKafkaMessage {
			fmt.Println("**********")
			fmt.Println("Start of message ", i)
			fmt.Println("Topic = ", thisKafkaMessage.Topic)
			fmt.Println("Partition = ", thisKafkaMessage.Partition)
			fmt.Println("Offset = ", thisKafkaMessage.Offset)
			fmt.Println("Timestamp = ", thisKafkaMessage.Timestamp)
			fmt.Println("TimestampType = ", thisKafkaMessage.TimestampType)
			//Each message in turn has a key and a value which are base64 encoded and need to be decoded
			var thisKafkaMessageKey = "null"
			if thisKafkaMessage.Key != "" {
				var thisKafkaMessageKeyBase64 = thisKafkaMessage.Key
				var thisKafkaMessageKeyDecodedInByteArray, _ = b64.StdEncoding.DecodeString(thisKafkaMessageKeyBase64)
				thisKafkaMessageKey = string(thisKafkaMessageKeyDecodedInByteArray)
			}
			fmt.Println("Key = ", thisKafkaMessageKey)
			var thisKafkaMessageValue = "null"
			if thisKafkaMessage.Value != "" {
				var thisKafkaMessageValueBase64 = thisKafkaMessage.Value
				var thisKafkaMessageValueDecodedInByteArray, _ = b64.StdEncoding.DecodeString(thisKafkaMessageValueBase64)
				thisKafkaMessageValue = string(thisKafkaMessageValueDecodedInByteArray)

			}
			fmt.Println("Value = ", thisKafkaMessageValue)
			fmt.Println("End of message ", i)
			fmt.Println("**********")
			i = i + 1
		}
	}

	return nil
}

func main() {
	lambda.Start(handler)
}
