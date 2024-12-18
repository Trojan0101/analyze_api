"""
###FILE DETAILS###
File name: main.py
Purpose: API entry point

###LICENSE DETAILS###
License: MIT License
Copyright (c) 2024 [Aloysius aka Trojan]
"""

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
