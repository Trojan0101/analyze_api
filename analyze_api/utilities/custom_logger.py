"""
###FILE DETAILS###
File name: custom_logger.py
Purpose: Custom logger for analyze api

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
import logging

class CustomLogging:
    """CustomLogging"""

    @staticmethod
    def setup_logger(name: str, log_file: str = "../logs/analyze_api_logs.log", level: int = logging.INFO):
        """
        Method to setup custom logging

        :param name: Name of the file
        :param log_file: File where the log should be written
        :param level: INFO, DEBUG, ERROR

        :return: Logger instance
        """
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
