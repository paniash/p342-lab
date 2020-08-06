// Sum over 1+1/2+1/3+... till the sume does not change by more than 0.001
#include <stdio.h>
#include <stdlib.h>

void main()
{
    float temp, total;
    for(int n=1; n<10000; n++)
    {
        temp = 0;
        total = 0;
        for(float i=1; i<=n; i++)
            temp+=1/i;

        for(float j=1; j<=n+1; j++)
            total+=1/j;

        float num=total-temp;
        if(num <= 0.001)
        {
            printf("SUM: %f", total);
            exit(0);
        }
    }
}
