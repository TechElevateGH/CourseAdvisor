
from ctypes import Union
from typing import List


def error_response(message: str, code: int):
  return {
    "response" : "error",
    "message" : message,
    "code" : code
  }

def success_response(data: Union[List, dict], code: int):
  return {
    "response" : "success",
    "message" : data,
    "code" : code
  }