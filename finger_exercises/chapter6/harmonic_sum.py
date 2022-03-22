def harmonic_sum_iter(n):
    """returns the harmonic sum of n.
    constraints: n is an int and n > 0"""
    ans = 1
    while n > 1:
        ans += (1/n)
        n-=1
    return ans

print(harmonic_sum_iter(4))

def harmonic_sum_rec(n):
    if n == 1:
        return n
    else:
        return 1 / n + harmonic_sum_rec(n-1)

print(harmonic_sum_rec(5))