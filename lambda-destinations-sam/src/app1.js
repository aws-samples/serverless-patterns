exports.handler = async function(event, context) {
  
  console.log(JSON.stringify(event, 0, null))
  
  if (event.type === "failure") {
    throw new Error('an expected error occured')
  }

  return "hello world"

}