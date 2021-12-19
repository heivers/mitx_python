"""Write a program that asks the user to input 10 intergers, and prints
the largest odd number that was entered. If no odd number was entered, print
a message to that effect (Use a while loop)"""

ans = False
i = 0

while (i < 10):
    num = int(input("Enter an integer: "))
    if num % 2 != 0 and num > ans:
        ans = num
    i+=1

if ans:
    print(f"The largest odd number is {ans}.")
else:
    print("No odd number was entered.")