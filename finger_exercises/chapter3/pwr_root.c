#include <stdio.h>
#include <math.h>

int main(void){
    int x;
    int pwr;
    int root;
    
    printf("Enter an integer: ");
    scanf("%d", &x);

    for (root=2; root < x; root++)
    {
        for (pwr = 2; pwr < 6; pwr++)
        {
            if (pow((double)root, (double)pwr) == x)
            {
                printf("Root = %d, Power = %d.\n", root, pwr);
                return 0;
            }
        }
    }
    
    printf("No combination found\n.");
    
    return 0;
}