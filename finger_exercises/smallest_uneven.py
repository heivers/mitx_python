x, y, z, a, b, c, d, e = 2, 3, 5, 8, 1, 4, 2, 9
answer = max((x,y,z, a, b, c, d, e))

uneven = False
for num in (x,y,z, a, b, c, d, e):
    if num % 2 != 0:
        uneven = True
        if num < answer:
            answer = num
print(answer)