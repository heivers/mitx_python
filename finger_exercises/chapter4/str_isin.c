#include <stdio.h>
#include <string.h>


int main(void)
{
    char needle[100];
    char haystack[100];
    char *ret;

    printf("Enter a string value: ");
    gets(needle);
    printf("Enter a string to search in: ");
    gets(haystack);

    ret = strstr(haystack, needle);

    if (ret != NULL)
    {
        printf("%s is in %s\n.", needle, haystack);
    }
    else
    {
        printf("%s does not contain %s\n", haystack, needle);

    }

}