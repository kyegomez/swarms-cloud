from fastapi import FastAPI
from typing import Callable, Any
from loguru import logger

class SwarmCloud:
    def __init__(self, title: str = "SwarmCloud", version: str = "0.1.0"):
        self.app = FastAPI(title=title, version=version)

    def add(self, path: str, method: str = "post"):
        """
        Add a route to the FastAPI app.
        """
        def decorator(func: Callable):
            method_lower = method.lower()
            if method_lower == "get":
                self.app.get(path)(func)
            elif method_lower == "post":
                self.app.post(path)(func)
            elif method_lower == "put":
                self.app.put(path)(func)
            elif method_lower == "delete":
                self.app.delete(path)(func)
            elif method_lower == "patch":
                self.app.patch(path)(func)
            else:
                logger.error(f"Error in {func.__name__}: Invalid method: {method}")
                raise ValueError(f"Invalid method: {method}")
            return func
        return decorator
