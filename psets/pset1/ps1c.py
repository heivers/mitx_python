salary_raise = 0.07
r = 0.04
down_payment_pct = 0.25
total_cost = 1_000_000

down_payment = down_payment_pct * total_cost

low = 0
high = 1
guess = (high + low) / 2
epsilon = 100
num_steps = 0
current_savings = 0
initial_salary = int(input(("Enter the starting salary: ")))

while (abs(down_payment - current_savings) > epsilon):
    possible = True
    annual_salary = initial_salary
    current_savings = 0
    num_months = 0
    for i in range(36):
        current_savings += ((current_savings * r) / 12)
        current_savings += ((annual_salary/12) * (guess))
        num_months += 1
        if num_months % 6 == 0:
            annual_salary *= (1 + salary_raise)
    if current_savings > down_payment:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
    num_steps += 1
    if guess > 0.9999 and abs(down_payment - current_savings) > epsilon:
        possible = False
        break

if possible:
    print(f"You need to save {guess*100:.2f}% of your income.")
    print(f"I searched through {num_steps} different percentages.")
else:
    print("With this income it is not possible to save enough.")
    
