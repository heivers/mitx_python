#include <stdio.h>

int main(void)
{
    int prime_sum = 0;
    int is_prime;

    for (int i = 3; i < 1000; i = i +2)
    {
        is_prime = 1;
        for (int j = 2; j < i; j++)
        {
            if (i % j == 0)
            {
                is_prime = 0;
            }
        }
        if (is_prime == 1)
        {
            prime_sum += i;
        }
    }
    printf("%d\n", prime_sum);
    return 0;
}