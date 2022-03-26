def fib(n):
    """returns the fibonaci number for n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


with open("first_ten_fib.txt", "w") as f:
    for i in range(10):
        f.write(str(fib(i)) + "\n")

with open("first_ten_fib.txt", "r") as f:
    for line in f.readlines():
        print(line[:-1])