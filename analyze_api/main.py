"""
###FILE DETAILS###
File name: main.py
Purpose: API entry point

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from fastapi import FastAPI, UploadFile, HTTPException

from analyze_api.core.pdf.pdf_reader_factory import PDFReaderFactory
from analyze_api.utilities.custom_logger import CustomLogging
from analyze_api.utilities.custom_messages.error_messages import ErrorMessages
from analyze_api.utilities.file_helper import FileHelper
from analyze_api.utilities.general_helpers import generate_request_id
from analyze_api.utilities.info_messages import InfoMessages

# Setup logging
LOGGER = CustomLogging.setup_logger("Main")

app = FastAPI()



@app.post("/analyze-pdf")
async def analyze_pdf(file: UploadFile):
    try:
        # Generate request id
        request_id = generate_request_id()

        # Validate the file
        FileHelper.validate_file(request_id=request_id, file=file)

        # Download PDF file
        file_path = FileHelper.save_temporary_file(request_id=request_id,
                                                   file = file.file,
                                                   file_name=request_id,
                                                   file_extension="pdf")

        # Choose PDF processing library (default: PyMuPDF)
        pdf_reader = PDFReaderFactory.get_reader(request_id=request_id, library="pymupdf")

        # Process PDF
        result = pdf_reader.process_pdf(request_id=request_id, file_path=file_path)
        number_of_pages = result["num_pages"]
        data = result["data"]

        # Log success
        LOGGER.info(InfoMessages.INFO_ANALYZE_001 + " " + f"Filename: {file.filename}. Number of pages: {number_of_pages}")

        return result

    except Exception as e:
        LOGGER.error(ErrorMessages.ERROR_ANALYZE_001 + f"Filename: {file.filename}.")
        raise HTTPException(status_code=400, detail=str(e))
