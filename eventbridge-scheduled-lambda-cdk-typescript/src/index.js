'use strict';
console.log("Starting...")
exports.handler = (event, context, callback) => {
    let interval_in_minutes = process.env.interval_in_minutes
    console.log("This function runs every " + interval_in_minutes + " minutes")
    callback(null, 'Complete - OK');
};