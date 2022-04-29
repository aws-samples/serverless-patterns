"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import urllib3
import shutil
import zipfile
from .hash import getFileSha256Hash
import os

PILLOW_MODULE_DOWNLOAD_FILE_NAME = "pillow_layer_module.zip"


def downloadPillowLayerFile(directory: str, url: str, file_hash: str):
    """
    Download the Pillow layer

    :param directory: Target directory to store the downloaded file
    :param url: The url for the download
    :param file_hash: The verification sha256 hash
    :return: None
    """
    if not os.path.exists(directory):
        os.mkdir(directory)

    http = urllib3.PoolManager()

    try:
        with http.request('GET', url, preload_content=False) as r, open(
                f"{directory}/{PILLOW_MODULE_DOWNLOAD_FILE_NAME}", 'wb') as f:
            shutil.copyfileobj(r, f)
    except Exception as err:
        raise IOError(err)

    if getFileSha256Hash(f"{directory}/{PILLOW_MODULE_DOWNLOAD_FILE_NAME}") != file_hash:
        os.unlink(f"{directory}/{PILLOW_MODULE_DOWNLOAD_FILE_NAME}")
        raise ImportError(f"Bad Pillow module file sha256 signature : {url}")

    try:
        with zipfile.ZipFile(f"{directory}/{PILLOW_MODULE_DOWNLOAD_FILE_NAME}", 'r') as f:
            f.extractall(f"{directory}/python")
    except Exception as err:
        raise IOError(err)

    os.unlink(f"{directory}/{PILLOW_MODULE_DOWNLOAD_FILE_NAME}")
