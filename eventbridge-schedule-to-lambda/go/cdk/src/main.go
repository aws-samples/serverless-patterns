package main

import (
    "context"
    "encoding/json"
    "fmt"
    "github.com/aws/aws-lambda-go/lambda"
)

func HandleRequest(ctx context.Context, event interface{}) error {
    // Convert event object into JSON string
    eventJSON, err := json.Marshal(event)
    if err != nil {
        return err
    }

    // Print the event JSON string received from EventBridge
    fmt.Printf("Received event: %s\n", string(eventJSON))

    return nil
}

func main() {
    lambda.Start(HandleRequest)
}





