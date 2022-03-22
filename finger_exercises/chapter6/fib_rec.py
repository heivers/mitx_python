from functools import lru_cache
import sys

sys.setrecursionlimit(5000)

@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(1200))