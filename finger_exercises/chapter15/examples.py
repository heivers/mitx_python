"""fibonnaci"""
import time


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fast_fib(n, memo=None):
    if memo == None:
        memo = {}
    if n == 0 or n ==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n-1, memo) + fast_fib(n-2, memo)
        memo[n] = result
        return result

def fib_tab(n):
    """Assumes n is an int >=0
    Returns Fibonacci of n"""
    tab = [1]*(n+1) #only first two values matter
    for i in range(2, n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]

""" start = time.perf_counter()
for i in range(35):
    print(f"fib of {i} = {fib(i)}")
stop = time.perf_counter()
print(f"Slow fib took {stop-start} time") """

start = time.perf_counter()
for i in range(500):
    fast_fib(i)
stop = time.perf_counter()
print(f"Fast fib took {stop - start} time.")

start = time.perf_counter()
for i in range(500):
    fib_tab(i)
stop = time.perf_counter()
print(f"Tab fib took {stop - start} time.")