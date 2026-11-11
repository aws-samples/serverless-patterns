"""Merges the three specialist answers into one report.

Some models, such as Amazon Nova Lite, start a reply with a <thinking> block
even when the prompt asks for the answer only. Remove it, and the
SECTION_COMPLETE marker the workflow checked, before the report is stored.
"""
import re

THINKING = re.compile(r"<thinking>.*?</thinking>", re.DOTALL)


def _clean(text):
    return THINKING.sub("", text).replace("SECTION_COMPLETE", "").strip()


def handler(event, context):
    return {
        "documentKey": event["documentKey"],
        "summary": _clean(event["summary"]),
        "risks": _clean(event["risks"]),
        "actions": _clean(event["actions"]),
    }
