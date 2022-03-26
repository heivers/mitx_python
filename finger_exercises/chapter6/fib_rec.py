from functools import lru_cache
import sys

sys.setrecursionlimit(5000)

#@lru_cache
def fib(n):
    global num_fib_calls
    num_fib_calls+=1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def test_fib(n):
    for i in range(n+1):
        global num_fib_calls
        num_fib_calls = 0
        print("fib of i", i, "=", fib(i))
        print("fib called", num_fib_calls, "times.")


test_fib(20)
