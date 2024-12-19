"""
###FILE DETAILS###
File name: info_messages.py
Purpose: Enum's for analyze_api info messages

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from enum import Enum


class InfoMessages(Enum):
    INFO_ANALYZE_001: str = "INFO_ANALYZE_001 -> File successfully processed"
    INFO_ANALYZE_002: str = "INFO_ANALYZE_002 -> Valid file type"
    INFO_ANALYZE_003: str = "INFO_ANALYZE_003 -> Instance selected - pymupdf"
    INFO_ANALYZE_004: str = "INFO_ANALYZE_003 -> Instance selected - pypdf"
    INFO_ANALYZE_005: str = "INFO_ANALYZE_004 -> Number of pages and data is extracted"
    INFO_ANALYZE_006: str = "INFO_ANALYZE_006 -> Number of pages and data is extracted"
    INFO_ANALYZE_007: str = "INFO_ANALYZE_007 -> File saved successfully"
    INFO_ANALYZE_008: str = "INFO_ANALYZE_008 -> Successfully deleted the file"
    INFO_ANALYZE_009: str = "INFO_ANALYZE_009 -> Request id generated"
    INFO_ANALYZE_010: str = "INFO_ANALYZE_010 -> Request received"

    def __add__(self, other_string: str):
        """
        Dunder method for string concatenation

        :param other_string: String value to be concatenated

        :return: Concatenated string
        """
        if isinstance(other_string, str):
            return f"{self.value} {other_string}"
        raise TypeError(f"Cannot concatenate '{type(self)}' with '{type(other_string)}'")