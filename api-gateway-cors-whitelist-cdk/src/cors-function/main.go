package main

import (
	"context"
	"encoding/json"
	"errors"
	"os"
	"strconv"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	log "github.com/sirupsen/logrus"
)

var ssmClient ParameterFetcher

/*
*
Good ole main
*/
func main() {
	lambda.Start(handler)
}

func init() {
	ssmClient = NewParameterFetcher()
	isLocal, _ := strconv.ParseBool(os.Getenv("IS_LOCAL"))

	log.SetFormatter(&log.JSONFormatter{
		PrettyPrint: isLocal,
	})

	switch os.Getenv("LOG_LEVEL") {
	case "error":
		log.SetLevel(log.ErrorLevel)
	case "info":
		log.SetLevel(log.InfoLevel)
	case "debug":
		log.SetLevel(log.DebugLevel)
	case "trace":
		log.SetLevel(log.TraceLevel)
	default:
		log.SetLevel(log.DebugLevel)
	}
}

// handler the input root function
func handler(ctx context.Context, request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	log.WithFields(log.Fields{
		"path":     request.Path,
		"resource": request.Resource,
	}).Debug("Printing path and resource")
	corsParameter, err := ssmClient.GetParameterByName(ctx, "/cors", "ALLOWED_ORIGINS")

	if err != nil {
		log.WithFields(log.Fields{
			"err": err,
		}).Error("Could not fetch parameters")
		return events.APIGatewayProxyResponse{
			StatusCode: 500,
		}, nil
	}

	var allowedOrigins []string

	err = json.Unmarshal([]byte(corsParameter.Value), &allowedOrigins)

	if err != nil {
		log.WithFields(log.Fields{
			"err":   err,
			"value": corsParameter.Value,
		}).Error("Could not parse /cors/ALLOWED_ORIGINS. FATAL.")
		return events.APIGatewayProxyResponse{
			StatusCode: 500,
		}, nil
	}

	val, err := checkOrigin(request.Headers)

	if err != nil {
		log.WithFields(log.Fields{"error": err}).Error("Origin is not present and is required")
		return events.APIGatewayProxyResponse{
			StatusCode: 400,
		}, nil
	}

	for _, v := range allowedOrigins {
		if v == val {
			return events.APIGatewayProxyResponse{
				StatusCode: 200,
				Headers: map[string]string{
					"Access-Control-Allow-Origin":      v,
					"Access-Control-Allow-Headers":     "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
					"Access-Control-Allow-Methods":     "GET, PUT, PATCH, DELETE, POST, OPTIONS",
					"Access-Control-Allow-Credentials": "true",
				},
			}, nil
		}
	}

	log.WithFields(log.Fields{"error": err}).Error("Unmatched Origin")
	return events.APIGatewayProxyResponse{
		StatusCode: 400,
	}, nil
}

func checkOrigin(headers map[string]string) (string, error) {
	val, ok := headers["origin"]

	if ok {
		return val, nil
	}

	val, ok = headers["Origin"]

	if ok {
		return val, nil
	}

	return "", errors.New("origin is required")
}
