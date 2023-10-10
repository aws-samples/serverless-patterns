use lambda_http::{run, service_fn, Error, IntoResponse, Request, RequestExt};

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

    Ok(format!(
        "hello {}",
        event
            .query_string_parameters()
            .first("name")
            .unwrap_or_else(|| "stranger")
    ))
}
