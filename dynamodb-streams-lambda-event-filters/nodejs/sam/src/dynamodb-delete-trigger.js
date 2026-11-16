
const processPutItem = async (item) => {
    console.log(JSON.stringify(item, null, 2))
    return true;
}

exports.deleteItemTriggerHandler = async (event) => {
    console.log(JSON.stringify(event), null, 2)
    for (let i = 0; i < event.Records.length; i++) {
        await processPutItem(event.Records[i].dynamodb)
    }
    return true;
}
