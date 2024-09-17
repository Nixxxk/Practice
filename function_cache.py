import functools
import time

@functools.lru_cache(maxsize=None)

def fx(n):
    time.sleep(3)
    return n*5

print(fx(5))