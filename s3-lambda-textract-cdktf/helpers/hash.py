"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import hashlib
from base64 import b64encode


def getB64FileSha256Hash(file: str) -> str:
    """
    Calculate the sha256 hash of a given file and return it in base64 format

    :param file: The full path to the file
    :return: base64 string representing the file hash in sha256
    """
    sha256Hash = hashlib.sha256()
    with open(file, "rb") as f:
        for byteBlock in iter(lambda: f.read(4096), b""):
            sha256Hash.update(byteBlock)

    return b64encode(sha256Hash.digest().strip()).decode("utf-8")


def getFileSha256Hash(file: str) -> str:
    """
    Calculate the sha256 hash of a given file

    :param file: The full path to the file
    :return: string representing the file hash in sha256
    """
    sha256Hash = hashlib.sha256()
    with open(file, "rb") as f:
        for byteBlock in iter(lambda: f.read(4096), b""):
            sha256Hash.update(byteBlock)

    return sha256Hash.hexdigest()
