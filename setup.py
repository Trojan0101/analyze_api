"""
###FILE DETAILS###
File name: setup.py
Purpose: Configurations for package creation

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius]
"""
from setuptools import setup, find_packages

setup(
    name="analyze_api",
    version="1.0.0",
    description="Extract, analyze, and answer questions about single or multiple page PDFs using a combination of OCR, machine learning, and large language models.",
    author="Aloysius",
    author_email="aloysius.job.05@gmail.com",
    license="MIT License",
    packages=find_packages(),
    install_requires=[
        # Production dependencies
        "fastapi>=0.115.6",
        "uvicorn>=0.34.0"
    ],
    extras_require={
        # Development dependencies
        "dev": [
            "black>=24.10.0",
            "flake8>=7.1.1",
            "mypy>=1.13.0",
            "pytest>=8.3.4",
            "pytest-cov>=6.0.0",
            "pytest-mock>=3.14.0",
            "debugpy>=1.8.11",
            "radon>=6.0.1",
            "pylint>=3.3.2",
            "pre-commit>=4.0.1",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11.9",
    ],
    entry_points={
        "console_scripts": [
            "start-analyze-api=uvicorn analyze_api.main:app",
        ]
    },
)

