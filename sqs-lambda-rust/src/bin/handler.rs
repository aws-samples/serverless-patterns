use aws_lambda_events::event::sqs::SqsEvent;
use lambda_runtime::{handler_fn, Context, Error};

#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_runtime::run(handler_fn(|event: SqsEvent, ctx: Context| {
        execute(event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(event: SqsEvent, _ctx: Context) -> Result<(), Error> {
    println!("{:?}", event);

    Ok(())
}
