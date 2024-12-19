"""
###FILE DETAILS###
File name: custom_logger.py
Purpose: Custom logger for analyze api

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
import logging
import os


class CustomLogging:
    """CustomLogging"""

    @staticmethod
    def setup_logger(name: str, log_file: str = "./logs/analyze_api_logs.log", level: int = logging.INFO):
        """
        Method to setup custom logging

        :param name: Name of the file
        :param log_file: File where the log should be written
        :param level: INFO, DEBUG, ERROR

        :return: Logger instance
        """
        # Check and create log file if it is not present
        log_file_path = os.path.join(log_file)
        log_dir = os.path.dirname(log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger(name)

        # Prevent adding duplicate handlers
        if not logger.hasHandlers():
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler = logging.FileHandler(log_file)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(level)

        return logger
