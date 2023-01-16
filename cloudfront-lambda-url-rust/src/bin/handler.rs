use lambda_http::{
    http::StatusCode, run, service_fn, Error, IntoResponse, Request, RequestExt, Response,
};

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
    let ip_address = get_ip_address(&event).unwrap_or("stranger".to_string());

    let mut body = format!("hello {}", ip_address);
    if let Some(allowed_query_string_param) = event
        .query_string_parameters()
        .first("allowed_query_string_param")
    {
        body = format!("hello {} ip: {}", allowed_query_string_param, ip_address);
    }

    let response = Response::builder()
        .status(StatusCode::OK)
        .header("Content-Type", "application/json")
        .body(body)
        .unwrap();

    Ok(response)
}

fn get_ip_address(event: &Request) -> Option<String> {
    let header_ip_address = event.headers().get("x-forwarded-for");
    if let Some(header_ip_address) = header_ip_address {
        let ips: Vec<&str> = header_ip_address.to_str().unwrap().split(",").collect();
        return Some(ips[0].to_string());
    }
    None
}
