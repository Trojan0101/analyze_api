"""
###FILE DETAILS###
File name: pdf_processing_exception.py
Purpose: Custom exception for pdf processing errors

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""


class PDFProcessingException(Exception):

    def __init__(self, message: str):
        """
        Custom Exception for PDF Processing

        :param message: Message to show during exception raise
        """
        super().__init__(message)
        self.message: str = message

    def __str__(self) -> str:
        """
        Dunder method for returning the exception message

        :return: Exception message
        """
        return self.message
