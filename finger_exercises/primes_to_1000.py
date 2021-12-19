"""Write a program that prints the sum of the prime numbers greater than 2
and less than 1000."""

summation = 0
for num in range(2, 1000):
    if num % 2 != 0:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime == True:
            summation += num
# 2 is a prime number            
print(summation + 2)
print()
