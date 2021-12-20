#include <stdio.h>
#include <math.h>

int main(void){
    int x;
    int y;

    printf("Enter a number x: ");
    scanf("%d", &x);
    printf("Enter a number y: ");
    scanf("%d", &y);
    printf("%d**%d = %.1f\n", x, y, pow((double)x,(double)y));
    printf("log(%d) = %.1f", x, (log((double)x)/log(2)));
    printf("\n");
    return 0;
    }