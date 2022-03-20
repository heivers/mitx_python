def f(L1, L2):
    """L1, L2 lists of the same length of numbers.
    returns the sum of raising each element in L1 to 
    the power of the element at the same index in L2"""
    return sum(map(lambda x, y: x**y, L1, L2))

print(f([1,2], [2, 3]))