import logging

log = logging.getLogger()
log.setLevel(logging.INFO)


def handler(event, context):
    log.info("Event: %s", event)
    log.info("Context: %s", context)

    if "knowledgeBaseId" in event:
        log.info("Knowledge base id found in the event: %s", event["knowledgeBaseId"])
        response = {
            "knowledgeBaseIds": [{"knowledgeBaseId": event["knowledgeBaseId"]}],
        }
        return response
    if "knowledgeBaseIds" in event:
        log.info("Knowledge base ids found in the event: %s", event["knowledgeBaseIds"])
        response = {
            "knowledgeBaseIds": [{"knowledgeBaseId": kb_id} for kb_id in event["knowledgeBaseIds"]],
        }
        return response
    else:
        log.error("No knowledge base ids found in the event.")
        raise ValueError("No knowledge base ids found in the event.")
