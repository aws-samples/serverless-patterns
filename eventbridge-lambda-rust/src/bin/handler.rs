use aws_lambda_events::event::cloudwatch_events::CloudWatchEvent;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    run(service_fn(|event: LambdaEvent<CloudWatchEvent>| {
        function_handler(event)
    }))
    .await
}

pub async fn function_handler(event: LambdaEvent<CloudWatchEvent>) -> Result<(), Error> {
    println!("{:?}", event);

    Ok(())
}
