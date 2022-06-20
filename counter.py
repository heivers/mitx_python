import time

# how long to count to a billion
start = time.perf_counter()
i = 0
while i < 1000000000:
    i += 1
stop = time.perf_counter()

print(stop - start)
