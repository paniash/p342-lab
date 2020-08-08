// To add 1+2+...+n for a given input n from the user
#include <stdio.h>

void main()
{
    int sum, n;
    sum = 0;
    printf("Enter a number\n");
    scanf("%d", &n);
    for(int i=1; i<=n; i++)
    {
        sum+=i;
    }

    printf("SUM: %d", sum);
}
