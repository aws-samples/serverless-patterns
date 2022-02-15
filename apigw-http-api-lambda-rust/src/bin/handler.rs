use lambda_http::{
    handler,
    lambda_runtime::{self, Context, Error},
    IntoResponse, Request, RequestExt,
};

#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_runtime::run(handler(|event: Request, ctx: Context| execute(event, ctx))).await?;
    Ok(())
}

pub async fn execute(event: Request, _ctx: Context) -> Result<impl IntoResponse, Error> {
    println!("EVENT {:?}", event);

    Ok(format!(
        "hello {}",
        event  // access information provided directly from the underlying trigger events using the RequestExt trait
            .query_string_parameters()
            .get("name")
            .unwrap_or_else(|| "stranger")
    ))
}
