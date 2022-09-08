from ctypes import Union
import json
from typing import List


def error_response(message: str, code: int):
    return json.dumps({
        "response": "error",
        "message": message,
        "code": code
    })


def success_response(data, code: int):
    return json.dumps({
        "response": "success",
        "message": data,
        "code": code
    })
