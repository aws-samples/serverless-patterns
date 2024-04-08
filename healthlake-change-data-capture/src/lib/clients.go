package lib

import (
	"context"
	"fmt"
	"net/http"
	"time"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"github.com/bix-digital/golang-fhir-models/fhir-models/fhir"

	awstrace "gopkg.in/DataDog/dd-trace-go.v1/contrib/aws/aws-sdk-go/aws"
	httptrace "gopkg.in/DataDog/dd-trace-go.v1/contrib/net/http"
)

func NewHttpClient() *http.Client {
	client := httptrace.WrapClient(&http.Client{}, httptrace.RTWithResourceNamer(func(h *http.Request) string {
		return fmt.Sprintf("%s %s://%s%s", h.Method, h.URL.Scheme, h.URL.Host, h.URL.Path)
	}))

	return client
}

type PatientFhirClient interface {
	GetPatientsByLastUpdated(context.Context, time.Time) (*fhir.Bundle, error)
}

// NewDynamoDBClient inits a DynamoDB session to be used throughout the services
func NewDynamoDBClient() *dynamodb.DynamoDB {
	c := &aws.Config{
		Region: aws.String("us-west-2"),
		//		Credentials: credentials.NewSharedCredentials("", "prod"),
	}

	sess := session.Must(session.NewSession(c))
	sess = awstrace.WrapSession(sess,
		awstrace.WithAnalytics(true),
		awstrace.WithAnalyticsRate(1.0))

	return dynamodb.New(sess)
}
