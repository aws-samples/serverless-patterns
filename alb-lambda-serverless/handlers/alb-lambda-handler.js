exports.handler=async(event, context) =>{
    const response = {
        statusCode: 200,
        headers:{
            contentType:'text/html'
        },
        body:'<p>Lambda function integrated with ALB called</p>'
    }
    console.log('response obj---', response)
    return response
}