import awswrangler as wr
import boto3
import sys
import json
from datetime import datetime
from awsglue.utils import getResolvedOptions

import logging


def load_config(ssm_parameter_path):
    """
    Load parameters config stored in SSM Parameter Store
    :param ssm_parameter_path: Path/Name to etl config in SSM Parameter Store
    :return: dict holding loaded config
    """
    client = boto3.client("ssm")

    # Get ETL Parameters
    param_details = client.get_parameter(Name=ssm_parameter_path)
    return json.loads(param_details["Parameter"]["Value"])


if __name__ == "__main__":
    logger = logging.getLogger("<<fe-customers>>")
    logger.setLevel(logging.INFO)

    config_path = getResolvedOptions(sys.argv, ['config_path'])["config_path"]
    logger.warning(config_path)
    config = load_config(config_path)
    logger.warning("config: %s".format(config))
    last_update = datetime.strptime(config['last_update'], "%Y-%m-%d-%H-%M-%S")
    logger.warning("last update: %s".format(last_update))
    bucket = config['bucket']
    prefix = config['prefix']

    sys.exit(0)
