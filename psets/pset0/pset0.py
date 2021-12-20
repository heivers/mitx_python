"""Write a program that does the following in order:
    1. Asks the user to enter a number "x".
    2. Asks the user to enter a numer "y".
    3. Prints out the number "x", raised to the power "y".
    4. Prints out the log (base 2) of "X"."""
import math

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
print(f"{x}**{y} = {x**y}")
print(f"log({x}) = {math.log(x, 2)}")