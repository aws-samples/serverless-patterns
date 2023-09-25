package main

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

type Event map[string]interface{}

func HandleRequest(ctx context.Context, event events.KinesisEvent) error {

	// loop through each record and transform

	for _, r := range event.Records {
		event := &SampleEvent{}
		err := json.Unmarshal(r.Kinesis.Data, event)

		if err != nil {
			// log stuff

			return err

		}

	}

	// return the transformed records
	return fmt.Sprintf("Hello World"), nil
}

func main() {
	lambda.Start(HandleRequest)
}
