#include <stdio.h>

int main(void){
    int num[10];
    int ans = 0;
    int i = 0;

    while (i < 10){
        printf("Please enter an integer: ");
        scanf("%d", &num[i]);
        if ((num[i] % 2 != 0) && (num[i] > ans)){
            ans=num[i];
            printf("%d\n", num[i]);
        }
        i++;
    }
    if (ans != 0){
        printf("The largest odd number is: %d\n", ans);
    }
    else{
        printf("No odd number.\n");
    }
}