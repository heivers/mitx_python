""" Write a program that examines three variables (x,y,z) and
prints the largest odd number among them. If none are odd, print the smallest value"""

data = input("Please enter three numbers, followed by a space: ")
nums = data.split(" ")
x, y, z = [int(x) for x in nums]

ans = min(x,y,z)
if x % 2 != 0:
    ans = x
if y % 2 != 0 and y > ans:
    ans = y
if z % 2 != 0 and z > ans:
    ans = z

print(ans)