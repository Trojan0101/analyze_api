"""
###FILE DETAILS###
File name: main.py
Purpose: API entry point

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse

from analyze_api.core.pdf.pdf_reader_factory import PDFReaderFactory
from analyze_api.utilities.custom_exceptions.pdf_processing_exception import PDFProcessingException
from analyze_api.utilities.custom_logger import CustomLogging
from analyze_api.utilities.custom_messages.error_messages import ErrorMessages
from analyze_api.utilities.custom_messages.info_messages import InfoMessages
from analyze_api.utilities.helpers.file_helpers import FileHelpers
from analyze_api.utilities.helpers.general_helpers import generate_request_id

# Setup logging
LOGGER = CustomLogging.setup_logger("Main")

app = FastAPI()



@app.post("/analyze-pdf")
async def analyze_pdf(file: UploadFile, library: str = Form(...)):
    # Generate request id
    request_id = generate_request_id()
    LOGGER.info(f"{InfoMessages.INFO_ANALYZE_010.value}; Request_id -> {request_id}")

    # Initialize file name
    filename = "NULL"

    try:
        # Validate the file
        FileHelpers.validate_file(request_id=request_id, file=file)
        binary_file = file.file
        filename = file.filename

        # Download PDF file
        file_path = FileHelpers.save_temporary_file(request_id=request_id,
                                                    file = binary_file,
                                                    file_name=request_id,
                                                    file_extension="pdf")
        # Choose PDF reader instance
        pdf_reader = PDFReaderFactory.get_reader(request_id=request_id, library=library)
        # Process PDF
        result = pdf_reader.process_pdf(request_id=request_id, file_path=file_path)
        number_of_pages = result["num_pages"]
        data = result["data"]
        LOGGER.info(f"{InfoMessages.INFO_ANALYZE_001.value}; Filename: {filename}; "
                    f"Number of pages: {number_of_pages}; Request_id -> {request_id}")

        return JSONResponse(
            content={
                "status": "success",
                "request_id": request_id,
                "filename": filename,
                "num_pages": number_of_pages,
                "data": data,
            },
            status_code=200
        )
    except Exception as e:
        if not isinstance(e, PDFProcessingException):
            LOGGER.error(f"{ErrorMessages.ERROR_ANALYZE_001.value}; Filename: {filename}; "
                         f"Request_id -> {request_id}")
        else:
            pass

        return JSONResponse(
            content={
                "status": "failure",
                "request_id": request_id,
                "message": str(e),
                "filename": filename
            },
            status_code=400
        )
