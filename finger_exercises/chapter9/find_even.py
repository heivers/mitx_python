def find_an_even(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if LE does not contain an even Number"""
    ans = []
    for x in L:
        if type(x) == int and x % 2 == 0:
            ans.append(x)
    if not ans:
        raise ValueError("No even number in list")
    else:
        return ans[0]

print(find_an_even([1,"a",3,"b",5,]))