#include <stdio.h>

int main(void){
    int x;
    int largest_divisor = 1;
    int guess = 3;
    int result;

    printf("Enter an integer greater than 2: ");
    scanf("%d", &x);

    if (x % 2 == 0){
        largest_divisor = x / 2;
    }
    else{
        while (guess < x)
    {
        result = x % guess;
        if (result == 0)
        {
            largest_divisor = x / guess;
            //printf("largest_divisor is %d\n", largest_divisor);
            break;
        }
        guess++;
    }

    }
    
    if (largest_divisor == 1)
    {
        printf("%d is prime\n", x);
    }
    else{
        printf("Largest divisior is %d\n", largest_divisor);

    return 0;
    
    }
}