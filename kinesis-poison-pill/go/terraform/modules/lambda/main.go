package main

import (
	"context"
	"encoding/json"

	"github.com/aws/aws-lambda-go/events"
	log "github.com/sirupsen/logrus"

	"github.com/aws/aws-lambda-go/lambda"
)

func handleRequest(ctx context.Context, e events.KinesisEvent) error {
	// Kinesis gives a batch of records, let's loop through them
	for _, r := range e.Records {
		event := &SampleEvent{}
		err := json.Unmarshal(r.Kinesis.Data, event)

		// if unmarshal fails, we can't do much so let's return an error
		// the batch fails but due to `bisectBatchOnError` the batch
		// will get split up until the failing item is pulled out
		if err != nil {
			log.WithFields(log.Fields{
				"err": err,
			}).Error("error encountered")

			return err
		}
	}

	log.Info("All good, see you later")

	return nil
}

func main() {
	lambda.Start(handleRequest)
}
