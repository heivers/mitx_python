def sum_digits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    """
    ans = 0
    for e in s:
        try:
            e = int(e)
            ans += e
        except (TypeError, ValueError):
            print("Print an annoying message.....")
    return ans

print("Sum of digits is:", sum_digits("a2b3c"))