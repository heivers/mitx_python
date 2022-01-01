portion_down_payment = 0.25
current_savings = 0
r = 0.04

annual_salary = int(input("Enter your annual salary as an integer: "))
portion_saved = float(input("Enter the portion to be saved as a float: "))
total_cost = int(input("Enter the total cost of the house as an integer: "))
salary_raise = float(input("Enter your semi annual raise as a float: "))

num_months = 0
to_be_saved = total_cost * portion_down_payment

while current_savings < to_be_saved:
    current_savings += ((current_savings * r) / 12)
    current_savings += ((annual_salary/12) * portion_saved)
    #print("Current Savings:", current_savings)
    num_months += 1
    if num_months % 6 == 0:
        annual_salary *= (1 + salary_raise)
        
print("Number of months:", num_months)
