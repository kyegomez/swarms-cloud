import time
from typing import Callable
from functools import wraps
from fastapi import HTTPException

def rate_limiter(max_requests: int, time_span: int):
    """Rate limiter decorator

    Args:
        max_requests (int): _description_
        time_span (int): _description_
    """
    def decorator(func: Callable):
        last_called = {}
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            identifier = str(args[0].client.host)
            if identifier in last_called:
                time_diff = time.time() - last_called[identifier]
                if time_diff < time_span:
                    raise HTTPException(
                        status_code=429,
                        detail="Too many requests"
                    )
            last_called[identifier] = time.time()
            return await func(*args, **kwargs)
        return wrapper
    return decorator
