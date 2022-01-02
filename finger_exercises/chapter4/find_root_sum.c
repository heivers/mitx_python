#include <stdio.h>
#include <math.h>

float find_root(int x, int power, float epsilon)
{
    float low;
    float high;
    float ans;
    if (x < -1)
    {
        low = x;
    }
    else
    {
        low = -1;
    }
    if (x > 1)
    {
        high = x;
    }
    else
    {
        high = 1;
    }
    ans = (high + low) / 2;
    //negative numbers do not have an even-powered root
    if ((x < 0) && (power % 2 == 0))
    {
        printf("Not possible\n");
        return 0;
    }
    while (fabs(pow(ans, power) - x) > epsilon)
    {
        if (pow(ans, power) > x)
        {
            high = ans;
        }
        else
        {
            low = ans;
        }
        ans = (high + low) / 2;
    }
    return ans;


}

int main(void)
{
    int xs[] = {25, -8, 16};
    int powers[] = {2,3,4};
    float epsilon = 0.001;
    float ans;
    float sum;
    for (int i = 0; i < 3; i++)
    {
        ans = find_root(xs[i], powers[i], epsilon);
        if (ans != 0)
        {
            sum += ans;
        }
    }
    printf("%f\n", sum);
    return 0;
}
