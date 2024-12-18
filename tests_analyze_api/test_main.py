"""
###FILE DETAILS###
File name: test_main.py
Purpose: Unit tests for main.py file

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from fastapi.testclient import TestClient
from analyze_api.main import app

client = TestClient(app)


def test_analyze_pdf():
    pass
