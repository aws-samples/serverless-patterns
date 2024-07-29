package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
)

type User struct {
	Id        string `json:"id" dynamodbav:"id"`
	FirstName string `json:"first_name" dynamodbav:"first_name"`
	LastName  string `json:"last_name" dynamodbav:"last_name"`
}

func PutUser(user User) error {
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		return fmt.Errorf("unable to load AWS config: %v", err)
	}

	svc := dynamodb.NewFromConfig(cfg)

	// USERS_TABLE_NAME is an environment variable
	table := os.Getenv("USERS_TABLE_NAME")
	if table == "" {
		return fmt.Errorf("USERS_TABLE_NAME is not set")
	}

	_, err = svc.PutItem(context.TODO(), &dynamodb.PutItemInput{
		TableName: &table,
		Item: map[string]types.AttributeValue{
			"id":         &types.AttributeValueMemberS{Value: user.Id},
			"first_name": &types.AttributeValueMemberS{Value: user.FirstName},
			"last_name":  &types.AttributeValueMemberS{Value: user.LastName},
		},
	})
	if err != nil {
		return fmt.Errorf("unable to put item: %v", err)
	}

	return nil

}

func handler(ctx context.Context, req events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	// get post data from request body
	user := User{}

	err := json.Unmarshal([]byte(req.Body), &user)
	if err != nil {
		log.Printf("failed to unmarshal api gateway request. error - %s\n", err.Error())
		return events.APIGatewayProxyResponse{StatusCode: http.StatusInternalServerError}, nil
	}

	// put user in dynamodb
	err = PutUser(user)
	if err != nil {
		return events.APIGatewayProxyResponse{}, err
	}

	return events.APIGatewayProxyResponse{
		StatusCode: 200,
		Body:       "User added successfully",
	}, nil
}

func main() {
	lambda.Start(handler)
}
