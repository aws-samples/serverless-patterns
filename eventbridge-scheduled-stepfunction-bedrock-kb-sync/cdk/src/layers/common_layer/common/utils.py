"""
Misc Util Helper Methods and Classes
"""

from enum import Enum


class MAPPING_STATUS(str, Enum):
    MAPPING_CREATED = "MAPPING_CREATED"
    MAPPING_FAILED = "MAPPING_FAILED"
    PENDING = "PENDING"
    DELETED = "DELETED"

    @classmethod
    def mapping_status_list(cls):
        values = set(item.value for item in MAPPING_STATUS)
        return values
