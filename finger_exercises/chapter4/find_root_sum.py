"""Use the find root function to print the sum of approximations
to the square root of 25, cube root of -8 and fourth root of 16,
use epsilon 0.001"""

def find_root(x, power, epsilon):
    """find interval containing answer"""
    if x < 0 and (power % 2 == 0):
        return None #negative number has no even-powered root
    low = min(-1,x)
    high = max(1, x)
    # Use bisection search
    ans = (high + low) / 2
    while (abs(ans**power - x) >= epsilon):
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

e = 0.001
print(sum([find_root(25, 2, e), find_root(-8, 3, e), find_root(16, 4, e)]))
