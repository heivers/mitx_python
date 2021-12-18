#include <stdio.h>

int main(void){
    int nums[3];
    int ans;
    for (int i = 0; i < 3; i++){
        printf("Enter an integer: ");
        scanf("%d", &nums[i]);
    }

    ans = nums[0];
    for (int i = 1; i < 2; i++)
    {
        if (nums[i] < ans)
            ans = nums[i];
    }
    

    if (nums[0] % 2 != 0)
        ans = nums[0];
    if ((nums[1] % 2 != 0) && (nums[1] > nums[0]))
        ans = nums[1];
    if ((nums[2] % 2 != 0) && (nums[2] > nums[1]))
        ans = nums[2];
    printf("%d\n", ans);

    return 0;
}