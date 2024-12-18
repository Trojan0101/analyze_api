"""
###FILE DETAILS###
File name: general_helpers.py
Purpose: General helper functionalities

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
import uuid

from analyze_api.utilities.custom_logger import CustomLogging
from analyze_api.utilities.custom_messages.info_messages import InfoMessages

# Setup logging
LOGGER = CustomLogging.setup_logger("FileValidator")

def generate_request_id():
    """
    Generates random request id

    :return: Request id
    """
    request_id = uuid.uuid4()
    LOGGER.info(InfoMessages.INFO_ANALYZE_009 + f"Request_id -> {request_id}")
    return request_id
