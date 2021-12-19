#include <stdio.h>

int main(void){
    char birthdate[11];
    char year[5];
    int j;

    printf("Enter your birtdate in the dd/mm/yyyy format: ");
    scanf("%s", birthdate);

    for (int i = 0; i < 11; i++){
        if (i > 5){
            j = i - 6;
            year[j] = birthdate[i];
        }
    }
    printf("You were born in the year %s.\n", year);
    return 0;
}