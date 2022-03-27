use lambda_http::{
    http::StatusCode, service_fn, Body, Error, IntoResponse, Request, RequestExt, Response,
};
use serde::{Deserialize, Serialize};
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        // this needs to be set to false, otherwise ANSI color codes will
        // show up in a confusing manner in CloudWatch logs.
        .with_ansi(false)
        // disabling time is handy because CloudWatch will add the ingestion time.
        .without_time()
        .init();

    lambda_http::run(service_fn(|event: Request| execute(event))).await?;
    Ok(())
}

pub async fn execute(event: Request) -> Result<impl IntoResponse, Error> {
    println!("EVENT {:?}", event);

    let body = event.payload::<MyPayload>()?;
    if let Some(request) = body {
        let response = Response::builder()
            .status(StatusCode::OK)
            .header("Content-Type", "application/json")
            .body(
                json!({
                  "message": "Hello World",
                  "payload": request,
                })
                .to_string(),
            )
            .unwrap();

        return Ok(response);
    }

    let response = Response::builder()
        .status(StatusCode::OK)
        .header("Content-Type", "application/json")
        .body(
            json!({
              "message": "Some error with the POST",
            })
            .to_string(),
        )
        .unwrap();
    Ok(response)
}

#[derive(Deserialize, Serialize, Debug, Clone)]
pub struct MyPayload {
    pub prop1: String,
    pub prop2: String,
}
