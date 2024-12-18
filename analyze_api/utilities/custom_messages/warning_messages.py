"""
###FILE DETAILS###
File name: warning_messages.py
Purpose: Enum's for analyze_api warning messages

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from enum import Enum


class WarningMessages(Enum):
    WARNING_ANALYZE_001: str = "WARNING_ANALYZE_001 -> File not found or path is None."

    def __add__(self, other_string: str):
        """
        Dunder method for string concatenation

        :param other_string: String value to be concatenated

        :return: Concatenated string
        """
        if isinstance(other_string, str):
            return f"{self.value} {other_string}"
        raise TypeError(f"Cannot concatenate '{type(self)}' with '{type(other_string)}'")