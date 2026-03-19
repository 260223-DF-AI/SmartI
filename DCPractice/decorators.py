from functools import wraps
from collections import OrderedDict
import logging
import time

log = logging.getLogger(__name__)

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    def timewrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func} took {start-end} seconds")
    return timewrapper

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    @wraps(func)
    def logWrapper(*args):
        start = f"Calling {func}{args}"
        funcRet = func()
        end = f"{func} returned {funcRet}"
        return start, end
    return logWrapper

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    def decorator(func):
        @wraps(func)
        def retryWrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    func(*args, **kwargs)
                except exceptions as e:
                    if(attempt == max_attempts - 1):
                        raise e
                    print(f"Attempt {attempt + 1} failed, retrying...")
                    time.sleep(delay)
        return retryWrapper
    return decorator


def cache(max_size=128):
    """
    Cache function results.
    Similar to lru_cache but with visible cache inspection.
    
    Usage:
        @cache(max_size=100)
        def expensive_computation(x):
            return x ** 2
        
        expensive_computation(5)  # Computes
        expensive_computation(5)  # Returns cached
        
        # Inspect cache
        expensive_computation.cache_info()
        expensive_computation.cache_clear()
    """
    cached_results = OrderedDict()

    def cacheDecorator(func): # go back and refactor
        @wraps(func)
        def cacheWrapper(*args, **kwargs):
            if((args,kwargs) in cached_results):
                return cached_results[(args,kwargs)]
            if(len(cached_results) == max_size):
                cached_results.popitem(last=False)
            else:    
                cached_results[((args,kwargs))] = func(*args,**kwargs)
        return cacheWrapper
    return cacheDecorator