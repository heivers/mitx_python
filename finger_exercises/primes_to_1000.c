#include <stdio.h>

int main(void){
    int n;
    int stop = 1000;
    int summation = 0;
    int j;
    int counter;

    for (n = 2; n < stop; n++){
        if (n % 2 != 0){
            counter = 0;
            for (j = 2; j < n; j++)
            {
                if (n % j == 0){
                    counter++;
                    break;
                }
            }
            if (counter == 0){
                summation += n;
            }
            
        }
    }
    printf("Sum = %d: ", (summation + 2));
}