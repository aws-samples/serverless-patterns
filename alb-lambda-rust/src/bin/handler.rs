use lambda_http::{
    http::StatusCode, run, service_fn, Error, IntoResponse, Request, RequestExt, Response,
};
use serde::{Deserialize, Serialize};
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    run(service_fn(|event: Request| function_handler(event))).await
}

pub async fn function_handler(event: Request) -> Result<impl IntoResponse, Error> {
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
