"""
###FILE DETAILS###
File name: pdf_reader_interface.py
Purpose: Interface for pdf reader

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from abc import abstractmethod


class PdfReaderInterface:

    def __init__(self):
        """PdfReaderInterface"""
        pass

    @abstractmethod
    def process_pdf(self, request_id: str, file_path: str):
        """
        Method to process the pdf file

        :param request_id: Request id
        :param file_path: Path to pdf file

        :return: Dictionary containing number of pages, and extracted text
        """
        pass