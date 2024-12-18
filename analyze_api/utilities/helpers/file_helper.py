"""
###FILE DETAILS###
File name: file_validator.py
Purpose: File validator for input files

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
import os
import shutil
from typing import Optional, BinaryIO

from fastapi import UploadFile

from analyze_api.utilities.custom_exceptions.pdf_processing_exception import PDFProcessingException
from analyze_api.utilities.custom_logger import CustomLogging
from analyze_api.utilities.custom_messages.error_messages import ErrorMessages
from analyze_api.utilities.custom_messages.info_messages import InfoMessages
from analyze_api.utilities.custom_messages.warning_messages import WarningMessages

# Setup logging
LOGGER = CustomLogging.setup_logger("FileValidator")

class FileHelper:
    """Validator to validate the type of file"""

    @staticmethod
    def validate_file(request_id: str, file: UploadFile):
        """
        Method to validate the file type

        :param request_id: Request id
        :param file: Input file

        :raises: PDFProcessingException
        """
        if file.filename.endswith(".pdf"):
            LOGGER.info(InfoMessages.INFO_ANALYZE_002 + f" Request_id -> {request_id}")
        else:
            LOGGER.error(ErrorMessages.ERROR_ANALYZE_002 + f" Request_id -> {request_id}")
            raise PDFProcessingException(ErrorMessages.ERROR_ANALYZE_002 + f" Request_id -> {request_id}")

    @staticmethod
    def save_temporary_file(request_id: str, file: BinaryIO, file_name: str, file_extension: str,
                            temp_dir: str = "../temp_pdf_files") -> str:
        """
        Save an uploaded file temporarily and return the file path.

        :param request_id: Request id
        :param file: The file object to save.
        :param file_name: Name of the file to save.
        :param file_extension: File extension for the file
        :param temp_dir: Directory to save the temporary file.

        :return: The path to the saved temporary file.

        :raises PDFProcessingException: If there are issues with file operations.
        """
        try:
            os.makedirs(temp_dir, exist_ok=True)
            file_path = os.path.join(temp_dir, file_name + f".{file_extension}")
            with open(file_path, "wb") as temp_file:
                shutil.copyfileobj(file, temp_file)

            LOGGER.info(InfoMessages.INFO_ANALYZE_007 + f" Request_id -> {request_id}")
            return file_path
        except Exception as e:
            LOGGER.error(ErrorMessages.ERROR_ANALYZE_006 + f" Request_id -> {request_id}")
            raise PDFProcessingException(ErrorMessages.ERROR_ANALYZE_006 + f" Request_id -> {request_id}")

    @staticmethod
    def cleanup_file(request_id: str, file_path: Optional[str]):
        """
        Delete the temporary file if it exists.

        :param request_id: Request id
        :param file_path: Path to the file to be deleted.

        :raises PDFProcessingException: If there are issues deleting the file (e.g., permission errors).
        """
        try:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
                LOGGER.info(InfoMessages.INFO_ANALYZE_008 + f" Request_id -> {request_id}")
            else:
                LOGGER.warning(WarningMessages.WARNING_ANALYZE_001 + f" Request_id -> {request_id}")
        except Exception as e:
            LOGGER.error(ErrorMessages.ERROR_ANALYZE_007 + f" Request_id -> {request_id}")
            raise PDFProcessingException(ErrorMessages.ERROR_ANALYZE_007 + f" Request_id -> {request_id}")
