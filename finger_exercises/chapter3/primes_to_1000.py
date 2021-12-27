
def is_prime(number):
    ans = True
    for i in range(2, number):
        if number % i == 0:
            ans = False
            return ans
    return ans
 
solution = 0        
for num in range(3, 1000, 2):
    if is_prime(num):
        solution += num

print(solution)