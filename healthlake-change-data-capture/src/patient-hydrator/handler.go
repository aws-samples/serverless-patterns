package main

import (
	"context"
	"encoding/json"
	"os"
	"time"

	ddlambda "github.com/DataDog/datadog-lambda-go"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	v4 "github.com/aws/aws-sdk-go/aws/signer/v4"
	"github.com/bix-digital/golang-fhir-models/fhir-models/fhir"
	log "github.com/sirupsen/logrus"
	"gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer"

	"event-handler/lib"
)

var fhirClient lib.PatientFhirClient

func init() {
	sess, _ := session.NewSession(&aws.Config{
		Region: aws.String("us-west-2"),
	})

	log.SetFormatter(&log.JSONFormatter{
		PrettyPrint: false,
	})

	lib.SetLevel(os.Getenv("LOG_LEVEL"))
	signer := v4.NewSigner(sess.Config.Credentials)
	fhirClient = NewHealthLakePatientClient(
		"healthlake.us-west-2.amazonaws.com/datastore",
		os.Getenv("HL_STORE_ID"),
		"us-west-2",
		lib.NewHttpClient(),
		signer,
	)

}

func main() {
	lambda.Start(ddlambda.WrapFunction(handler, lib.DataDogConfig()))
}

func handler(ctx context.Context, event lib.IncomingEvent) (*lib.PatientList, error) {
	span, _ := tracer.SpanFromContext(ctx)
	newCtx := context.WithValue(ctx, "correlationId", event.CorrelationId)

	log.WithFields(
		log.Fields{
			"event":         event,
			"span_id":       span.Context().SpanID(),
			"trace_id":      span.Context().TraceID(),
			"correlationId": newCtx.Value("correlationId"),
		}).Info("Logging out the event")

	updated, err := fhirClient.GetPatientsByLastUpdated(newCtx, event.Details.EventTime)

	if err != nil {
		return nil, err
	}

	log.WithFields(
		log.Fields{
			"patientBundle": updated,
			"span_id":       span.Context().SpanID(),
			"trace_id":      span.Context().TraceID(),
			"correlationId": newCtx.Value("correlationId"),
		}).Info("The bundle ...")

	return splitBundle(newCtx, event, updated), err
}

func splitBundle(ctx context.Context, sourceEvent lib.IncomingEvent, bundle *fhir.Bundle) *lib.PatientList {
	span, _ := tracer.SpanFromContext(ctx)
	pl := lib.PatientList{
		Patients: []lib.PatientPublisherState{},
	}
	for _, b := range bundle.Entry {
		p := fhir.Patient{}
		_ = json.Unmarshal(b.Resource, &p)
		lastUpdated, err := time.Parse(time.RFC3339, *p.Meta.LastUpdated)
		if err != nil {
			log.WithFields(log.Fields{
				"span_id":       span.Context().SpanID(),
				"trace_id":      span.Context().TraceID(),
				"correlationId": ctx.Value("correlationId"),
				"err":           err,
			}).Error("Last updated could not be parsed")
			// skip along
			continue
		}
		pl.Patients = append(pl.Patients, lib.PatientPublisherState{
			Patient: p,
			MetaDetails: lib.MetaDetails{
				CorrelationId: ctx.Value("correlationId").(string),
				IdempotencyKey: lib.BuildIdempotencyKey(
					sourceEvent.Details.RequestParameters.ResourceType,
					*p.ID,
					lastUpdated),
				SourceTime: sourceEvent.Details.EventTime,
			},
		})
	}

	return &pl
}
