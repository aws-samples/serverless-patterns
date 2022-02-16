use aws_lambda_events::event::cloudwatch_events::CloudWatchEvent;
use lambda_runtime::{handler_fn, Context, Error};

#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_runtime::run(handler_fn(|event: CloudWatchEvent, ctx: Context| {
        execute(event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(event: CloudWatchEvent, _ctx: Context) -> Result<(), Error> {
    println!("{:?}", event);

    Ok(())
}