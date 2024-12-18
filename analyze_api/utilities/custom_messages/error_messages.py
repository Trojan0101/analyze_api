"""
###FILE DETAILS###
File name: error_messages.py
Purpose: Enum's for analyze_api error messages

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from enum import Enum


class ErrorMessages(Enum):
    ERROR_ANALYZE_001: str = "ERROR_ANALYZE_001 -> Error processing file."
    ERROR_ANALYZE_002: str = "ERROR_ANALYZE_002 -> Invalid file type. Only PDF files are supported!"
    ERROR_ANALYZE_003: str = "ERROR_ANALYZE_003 -> Unsupported PDF library. Choose 'pymupdf' or 'pypdf'."
    ERROR_ANALYZE_004: str = "ERROR_ANALYZE_004 -> Error processing PDF with PyMuPDF."
    ERROR_ANALYZE_005: str = "ERROR_ANALYZE_005 -> Error processing PDF with PyPDF."
    ERROR_ANALYZE_006: str = "ERROR_ANALYZE_006 -> Unexpected error while saving the file."
    ERROR_ANALYZE_007: str = "ERROR_ANALYZE_007 -> Unexpected error while deleting the file."

    def __add__(self, other_string: str):
        """
        Dunder method for string concatenation

        :param other_string: String value to be concatenated

        :return: Concatenated string
        """
        if isinstance(other_string, str):
            return f"{self.value} {other_string}"
        raise TypeError(f"Cannot concatenate '{type(self)}' with '{type(other_string)}'")