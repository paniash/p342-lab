// To find the factorial of a number n and to trap cases where the number is negative
#include <stdio.h>
#include <stdlib.h>

void main()
{
    int n, prod;
    prod = 1;
    printf("Enter a number\n");
    scanf("%d", &n);
    if(n<0)
    {
        printf("This number is NEGATIVE. Please enter a another number!!!");
        exit(0);
    }
    else if(n==0)
    {
        printf("FACTORIAL: 1");
    }
    else
    {
        for(int i=1; i<=n; i++)
        {
            prod *= i;
        }
    }
    printf("The factorial is %d", prod);
}
