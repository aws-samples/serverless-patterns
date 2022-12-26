use lambda_http::{
    http::StatusCode, run, service_fn, Error, IntoResponse, Request, RequestExt, Response,
};
use serde::{Deserialize, Serialize};
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Error> {
    run(service_fn(|event: Request| function_handler(event))).await
}

pub async fn function_handler(event: Request) -> Result<impl IntoResponse, Error> {
    println!("EVENT {:?}", event);

    let body = event.payload::<MyPayload>()?;

    let response = Response::builder()
        .status(StatusCode::OK)
        .header("Content-Type", "application/json")
        .body(
            json!({
              "message": "Hello World",
              "payload": body,
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
