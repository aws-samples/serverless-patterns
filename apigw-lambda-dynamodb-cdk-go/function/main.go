package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"github.com/aws/aws-sdk-go/service/dynamodb/dynamodbattribute"
	"github.com/aws/jsii-runtime-go"
)

const dynamoDBTableNameEnvVar = "DYNAMODB_TABLE_NAME"
const conditionExpression = "attribute_not_exists(email)"

var tableName string

func init() {
	tableName = os.Getenv(dynamoDBTableNameEnvVar)
	if tableName == "" {
		log.Fatalf("missing environment variable %s\n", dynamoDBTableNameEnvVar)
	}
}

type User struct {
	EmailID string `json:"email"`
	Name    string `json:"username,omitempty" dynamodbav:"user_name,omitempty"`
}

func create(ctx context.Context, req events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	client := dynamodb.New(session.New())

	var u User

	err := json.Unmarshal([]byte(req.Body), &u)
	if err != nil {
		log.Printf("failed to unmarshal api gateway request. error - %s\n", err.Error())
		return events.APIGatewayProxyResponse{StatusCode: http.StatusInternalServerError}, nil
	}

	//log.Println("user struct", u.EmailID, u.Name)

	av, err := dynamodbattribute.MarshalMap(u)
	//log.Println("dynamodbattribute", *av["email"].S, *av["EmailID"].S, *av["user_name"].S, av["notthere"])

	if err != nil {
		log.Printf("failed to marshal struct into dynamodb record. error - %s\n", err.Error())
		return events.APIGatewayProxyResponse{StatusCode: http.StatusInternalServerError}, nil
	}

	_, err = client.PutItem(&dynamodb.PutItemInput{TableName: aws.String(tableName), Item: av, ConditionExpression: jsii.String(conditionExpression)})

	if err != nil {

		// if the user with same email already exists
		if strings.Contains(err.Error(), dynamodb.ErrCodeConditionalCheckFailedException) {
			log.Printf("user %s already exists. error - %s\n", u.EmailID, err.Error())
			return events.APIGatewayProxyResponse{StatusCode: http.StatusConflict}, nil
		}
		return events.APIGatewayProxyResponse{StatusCode: http.StatusInternalServerError, Body: fmt.Sprintf("failed to add new item. error - %s", err.Error())}, nil
	}

	log.Printf("successfully created user %s\n", u.EmailID)
	return events.APIGatewayProxyResponse{StatusCode: http.StatusCreated}, nil
}

func main() {
	lambda.Start(create)
}
