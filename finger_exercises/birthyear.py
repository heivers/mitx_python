"""Ask user to enter birthdate in format mm/dd/yyyy and print birthyear"""

birthdate = input("Please input your birthdate in the format mm/dd/yyyy: ")
print(f"You were born in the year {birthdate[-4:]}.")