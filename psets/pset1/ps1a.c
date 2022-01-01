#include<stdio.h>

int main(void)
{
    float portion_down_payment = 0.25;
    float current_savings = 0.0;
    float r = 0.04;
    float portion_saved;
    int annual_salary;
    int total_cost;
    float interest;
    float monthly_savings;
    int num_months = 0;

    printf("Enter your annual salary as an integer: ");
    scanf("%d", &annual_salary);
    printf("Enter the portion to be saved as an float: ");
    scanf("%f", &portion_saved);
    printf("Enter the total cost of the house as an integer: ");
    scanf("%d", &total_cost);

    while (current_savings < (total_cost * portion_down_payment))
    {
        interest = ((current_savings * r) / 12);
        monthly_savings = portion_saved * (annual_salary / 12);
        current_savings += interest;
        current_savings += monthly_savings;
        num_months++;
    }
    printf("Number of months needed %d\n", num_months);
    return 0;

}