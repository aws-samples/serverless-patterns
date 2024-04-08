package main

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	v4 "github.com/aws/aws-sdk-go/aws/signer/v4"
	"github.com/bix-digital/golang-fhir-models/fhir-models/fhir"
	log "github.com/sirupsen/logrus"
	"gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer"
)

type HealthLakePatientClient struct {
	HealthLakeEndpoint  string
	HealthLakeDataStore string
	HealthLakeRegion    string
	HttpClient          *http.Client
	Signer              *v4.Signer
}

func NewHealthLakePatientClient(
	healthLakeEndpoint string,
	healthLakeDataStore string,
	healthLakeRegion string,
	httpClient *http.Client,
	signer *v4.Signer) *HealthLakePatientClient {

	return &HealthLakePatientClient{
		HealthLakeEndpoint:  healthLakeEndpoint,
		HealthLakeDataStore: healthLakeDataStore,
		HealthLakeRegion:    healthLakeRegion,
		HttpClient:          httpClient,
		Signer:              signer,
	}
}

func (h *HealthLakePatientClient) GetPatientsByLastUpdated(ctx context.Context, lastUpdated time.Time) (*fhir.Bundle, error) {
	span, _ := tracer.SpanFromContext(ctx)
	url := fmt.Sprintf("https://%s/%s/r4/Patient?_lastUpdated=ge%s", h.HealthLakeEndpoint, h.HealthLakeDataStore, lastUpdated.Format(time.RFC3339))
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)

	log.WithFields(log.Fields{
		"url":           url,
		"span_id":       span.Context().SpanID(),
		"trace_id":      span.Context().TraceID(),
		"lastUpdated":   lastUpdated,
		"correlationId": ctx.Value("correlationId"),
	}).Info("The URL request for patients")

	if err != nil {
		return nil, err
	}

	req.Header.Set("Content-Type", "application/json; charset=utf-8")
	_, err = h.Signer.Sign(req, nil, "healthlake", h.HealthLakeRegion, time.Now())

	if err != nil {
		return nil, err
	}

	resp, err := h.HttpClient.Do(req)
	if err != nil {
		return nil, err
	}

	defer resp.Body.Close()
	var patients fhir.Bundle
	decoder := json.NewDecoder(resp.Body)
	err = decoder.Decode(&patients)

	return &patients, err
}
