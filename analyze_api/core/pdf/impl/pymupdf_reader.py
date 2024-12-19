"""
###FILE DETAILS###
File name: pymupdf_reader.py
Purpose: Pdf functions with pymupdf python library

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
import fitz

from analyze_api.core.pdf.pdf_reader_interface import PdfReaderInterface

from analyze_api.utilities.custom_exceptions.pdf_processing_exception import PDFProcessingException
from analyze_api.utilities.custom_logger import CustomLogging
from analyze_api.utilities.custom_messages.error_messages import ErrorMessages
from analyze_api.utilities.custom_messages.info_messages import InfoMessages

# Setup logging
LOGGER = CustomLogging.setup_logger("PyMuPDFReader")


class PyMuPDFReader(PdfReaderInterface):

    def __init__(self):
        """PyMuPDFReader"""
        super().__init__()

    def process_pdf(self, request_id: str, file_path: str):
        """
        Method to process the pdf file

        :param request_id: Request id
        :param file_path: Path to pdf file

        :return: Dictionary containing number of pages, and extracted text
        """
        try:
            doc = fitz.open(file_path)
            num_pages = len(doc)
            text_content = [page.get_text("text") for page in doc]
            LOGGER.info(f"{InfoMessages.INFO_ANALYZE_005.value}; Request_id -> {request_id}")
            return {"num_pages": num_pages, "data": text_content}
        except PDFProcessingException as e:
            LOGGER.error(f"{ErrorMessages.ERROR_ANALYZE_004.value}; Error_message: {str(e)}; "
                         f"Request_id -> {request_id}")
            raise PDFProcessingException(f"{ErrorMessages.ERROR_ANALYZE_004.value}; Error_message: {str(e)}; "
                                         f"Request_id -> {request_id}")
