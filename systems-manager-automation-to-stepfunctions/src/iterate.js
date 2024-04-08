exports.handler = function iterator (event, context, callback) {
  let step = event.iterator.step
  let count = event.iterator.count
 
  step += 1
 
  callback(null, {
    step,
    count,
    continue: step < count
  })
}