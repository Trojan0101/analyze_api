"""
###FILE DETAILS###
File name: pypdf_reader.py
Purpose: Pdf functions with PyPDF2 python library

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from PyPDF2 import PdfReader

from analyze_api.core.pdf.pdf_reader_interface import PdfReaderInterface
from analyze_api.utilities.custom_exceptions.pdf_processing_exception import PDFProcessingException
from analyze_api.utilities.custom_logger import CustomLogging
from analyze_api.utilities.custom_messages.error_messages import ErrorMessages
from analyze_api.utilities.custom_messages.info_messages import InfoMessages

# Setup logging
LOGGER = CustomLogging.setup_logger("PyPDFReader")


class PyPDFReader(PdfReaderInterface):

    def __init__(self):
        """PyPDFReader"""
        super().__init__()

    def process_pdf(self, request_id: str, file_path: str):
        """
        Method to process the pdf file

        :param request_id: Request id
        :param file_path: Path to pdf file

        :return: Dictionary containing number of pages, and extracted text
        """
        try:
            reader = PdfReader(file_path)
            num_pages = len(reader.pages)
            text_content = [page.extract_text() for page in reader.pages]
            LOGGER.info(InfoMessages.INFO_ANALYZE_006 + f" Request_id -> {request_id}")
            return {"num_pages": num_pages, "data": text_content}
        except PDFProcessingException as e:
            LOGGER.error(ErrorMessages.ERROR_ANALYZE_005 + f" Request_id -> {request_id}" + f" Error: {str(e)}")
            raise PDFProcessingException(ErrorMessages.ERROR_ANALYZE_005 + f" Request_id -> {request_id}" + f" Error: {str(e)}")
