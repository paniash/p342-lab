#include <stdio.h>

void main()
{
    int sum;
    sum = 0;
    for(int i=1;i<=100;i++)
    {
        sum+=i;
    }

    printf("%d", sum);
}
