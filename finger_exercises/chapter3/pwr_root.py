"""Write a program that asks the user to enter an integer
and prints two integers, root and pwr such that 1< pwr < 6 and root**pwr == integer"""

x = int(input("Enter an integer: "))

ans = None
for i in range(1, x):
    if ans != None:
        break
    for j in range(2,6):
        if i**j == x:
            ans = (i, j)
            break
if ans != None:
    print(f"Root = {ans[0]}, Power = {ans[1]}")
else:
    print("No answer found!")