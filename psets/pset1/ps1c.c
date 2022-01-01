#include<stdio.h>
#include<math.h>

int main(void)
{
    float salary_raise = 0.07;
    float r = 0.04;
    int down_payment = 250000;
    int possible;
    int num_months;

    //prepare for bisect search
    float low = 0.0;
    float high = 1.0;
    float guess = (high + low) / 2;
    int epsilon = 100;
    int num_steps = 0;
    float current_savings = 0.0;
    float initial_salary;
    float annual_salary;

    printf("Please enter your initial salary as a Float: ");
    scanf("%f", &initial_salary);

    while (fabs((down_payment - current_savings)) > epsilon)
    {
        possible = 1;
        current_savings = 0;
        annual_salary = initial_salary;
        num_months = 0;
        for (int i = 0; i < 36; i++)
        {
            current_savings += ((current_savings * r) /12);
            current_savings += ((annual_salary / 12) * guess);
            num_months++;
            if (num_months % 6 == 0)
            {
                annual_salary = annual_salary * (1 + salary_raise);
            }
        }
        if (current_savings > down_payment)
        {
            high = guess;
        }
        else
        {
            low = guess;
        }
        guess = (high + low) / 2;
        num_steps++;
        if ((guess > 0.999) && (fabs((down_payment - current_savings)) > epsilon))
        {
            possible = 0;
            break;
        }
    }
    if (possible == 1)
    {
        printf("Percentage of salary to save = %.2f%%\n", (guess*100));
        printf("Num steps=%d\n", num_steps);
    }
    else
    {
        printf("Not possible with this Salary.\n");
    }
    return 0;


}