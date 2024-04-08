package main

import (
	"context"
	"fmt"
	"strings"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/ssm"
	log "github.com/sirupsen/logrus"
	awstrace "gopkg.in/DataDog/dd-trace-go.v1/contrib/aws/aws-sdk-go-v2/aws"
)

type Parameter struct {
	Name  string
	Value string
}

// ParameterFetcher interface for dealing with parameter retrieval
type ParameterFetcher interface {
	Initialize(context.Context, string) error
	GetParameterByName(context.Context, string, string) (*Parameter, error)
}

// AwsParameterFetcher implements the Parameter Fetcher as it relates to AWS
type AwsParameterFetcher struct {
	Parameters []Parameter
}

func NewParameterFetcher() ParameterFetcher {
	s := &AwsParameterFetcher{}

	return s
}

// Initialize loads up the parameters from aws
// and locally caches them for later retrieval
func (a *AwsParameterFetcher) Initialize(ctx context.Context, path string) error {
	log.WithFields(
		log.Fields{
			"path": path,
		}).Debug("Initializing ssm parameters")

	cfg, err := config.LoadDefaultConfig(ctx)
	awstrace.AppendMiddleware(&cfg)

	if err != nil {
		return err
	}

	var input = &ssm.GetParameterInput{
		Name:           aws.String(path),
		WithDecryption: aws.Bool(true),
	}

	ssmClient := ssm.NewFromConfig(cfg)

	req, err := ssmClient.GetParameter(ctx, input)

	if err != nil {
		return err
	}

	split := strings.Split(*req.Parameter.Name, "/")
	name := strings.ToUpper(split[len(split)-1])

	newParam := Parameter{
		Name:  name,
		Value: *req.Parameter.Value,
	}
	log.WithFields(log.Fields{
		"parameter": newParam}).Debug("Adding in new parameter")
	a.Parameters = append(a.Parameters, newParam)

	return nil
}

// GetParameterByName returns a pointer to the Parameter
// as found by the Name property
func (a *AwsParameterFetcher) GetParameterByName(ctx context.Context, path string, name string) (*Parameter, error) {
	if len(a.Parameters) == 0 {
		err := a.Initialize(ctx, fmt.Sprintf("%s/%s", path, name))
		if err != nil {
			return nil, err
		}
	}

	for _, p := range a.Parameters {
		if strings.EqualFold(p.Name, name) {
			return &p, nil
		}
	}

	return nil, nil
}
