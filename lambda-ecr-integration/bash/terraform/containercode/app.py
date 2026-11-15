import sys
import os
import time
import logging
import logging.config


def handler(event, context):
    env = os.getenv("ENV")
    organization = os.getenv("ORGANIZATION")
    log_level = logging.getLevelName(os.getenv("LOGGING_LEVEL"))

    logging.basicConfig(
        format="%(asctime)s : %(levelname)s : %(message)s", level=log_level, force=True
    )
    logs = ""

    try:
        logging.info("Lambda Function Started.")
        logging.info("")

        logging.info("Sending Control to Shell Script...")
        os.system("sh sample-bash.sh ")
        logging.info("...Control is back in Python")

        logging.info("")
        logging.info("Lambda Function Finished.")

    except:
        logs = logs + str(sys.exc_info()[1])
        print(logs)
