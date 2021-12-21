"""Test if an int x > 2 is prime. If not, print the largest divisor of x"""

x = int(input("Enter an integer greater than 2: "))
largest_divisor = None
if x % 2 == 0:
    largest_divisor = x / 2
for guess in range(3, x, 2):
    #print(guess)
    if x % guess == 0:
        largest_divisor = x / guess
        break
if largest_divisor != None:
    print(f"Largest divisor of {x} is {largest_divisor:.0f}.")
else:
    print(f"{x} is prime.")