#include <stdio.h>

int main(void){
    int num_x;
    char to_print = 'x';
    int i = 0;

    printf("How many times should I print x? ");
    scanf("%d", &num_x);

    while (i < num_x){
        printf("%c", to_print);
        i++;
    }
    printf("\n");
}