"use strict";

module.exports.handler = async(event) => {
    // TODO implement
    console.log("enrichment function called")
    console.log(JSON.stringify(event[0]));
    console.log("Event Name: ", event[0]?.eventName)
    return event
};