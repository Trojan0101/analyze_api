"""
###FILE DETAILS###
File name: pdf_reader_factory.py
Purpose: Factory file for pdf readers

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from analyze_api.core.pdf.impl.pymupdf_reader import PyMuPDFReader
from analyze_api.core.pdf.impl.pypdf_reader import PyPDFReader
from analyze_api.core.pdf.pdf_reader_interface import PdfReaderInterface
from analyze_api.utilities.custom_exceptions.pdf_processing_exception import PDFProcessingException
from analyze_api.utilities.custom_logger import CustomLogging
from analyze_api.utilities.custom_messages.error_messages import ErrorMessages
from analyze_api.utilities.custom_messages.info_messages import InfoMessages

# Setup logging
LOGGER = CustomLogging.setup_logger("PDFReaderFactory")

class PDFReaderFactory:
    """PDFReaderFactory"""

    @staticmethod
    def get_reader(request_id: str, library: str = "pymupdf") -> PdfReaderInterface:
        """
        Method to get the correct reader

        :param request_id: Request id
        :param library: pymupdf or pypdf

        :return: PdfReaderInterface Instance of chosen library
        """
        if library == "pymupdf":
            LOGGER.info(InfoMessages.INFO_ANALYZE_003 + f" Request_id -> {request_id}")
            return PyMuPDFReader()
        elif library == "pypdf":
            LOGGER.info(InfoMessages.INFO_ANALYZE_004 + f" Request_id -> {request_id}")
            return PyPDFReader()
        else:
            LOGGER.error(ErrorMessages.ERROR_ANALYZE_003 + f" Request_id -> {request_id}")
            raise PDFProcessingException(ErrorMessages.ERROR_ANALYZE_003 + f" Request_id -> {request_id}")
