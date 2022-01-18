"""Use the algorithm of chapter 3, write a log function"""

def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 and power >=1,
    returns float y such that base ** y is within epsilon of x."""
    lower_bound = 0
    while base ** lower_bound < x:
        lower_bound += 1
    low = lower_bound
    high = lower_bound + 1

    #perform bisection search
    ans = (high + low) / 2
    while abs(base ** ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2

    print(f"{ans} is close to the log base {base} of {x}")

print(log(16, 2, 0.001))


"""Write a lambda expression that has 2 numeric parameters. If the second argument equals zero, it should return None,
otherwise the value of first divided by second"""
f = lambda x, y: x / y if y != 0 else None
print(f"f(3,2) = {f(3,2)}")
print(f"f(7, 0) = {f(7,0)}")

print(f"What does str.find(sub) return if sub not in s?")
s = "nosu in this text, you know the one with the b"
print(s.find("sub"))


def find_last(s, sub):
    """s and sub are non-empty strings.
    Reutrns the index of the last occurence of sub in s, returns None if sub does not occur in s"""
    idx = s.rfind(sub)
    return idx if idx != -1 else None

print(find_last("blablablablabla", "bla"))
print(find_last("Nothing here", "two"))
