use lambda_http::{service_fn, Error, IntoResponse, Request, RequestExt, http::StatusCode, Response};
use serde::{Deserialize, Serialize};
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_http::run(service_fn(|event: Request| {
        execute(event)
    }))
    .await?;
    Ok(())
}

pub async fn execute(event: Request) -> Result<impl IntoResponse, Error> {
    println!("EVENT {:?}", event);

    let body = event.payload::<MyPayload>()?;

    let response = Response::builder()
            .status(StatusCode::OK)
            .header("Content-Type", "application/json")
            .body(json!({
                "message": "Hello World",
                "payload": body, 
              }).to_string())
            .unwrap();

    Ok(response)
}


#[derive(Deserialize, Serialize, Debug, Clone)]
pub struct MyPayload {
    pub prop1: String,
    pub prop2: String,
}