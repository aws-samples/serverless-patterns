exports.handler = async function(event, context) {
  console.log(JSON.stringify(event, 0, null))
  return "hello world"
}