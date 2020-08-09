// Sum over 1+1/2+1/3+... till the sume does not change by more than 0.001
#include <stdio.h>

/* This is bad coding practice since you're adding an extra layer of parameter n which really is not necessary, let the computer do the work!!!
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
        printf("%f\n", num);
        if(num <= 0.001)
        {
            printf("SUM: %f", total);
            exit(0);
        }
    }
}
*/

void main()
{
    float sum, add;
    sum = 0;
    float num = 1;
    add = 1/num;
    while (add > 0.001)
    {
        sum += add;
        // printf("The sum:%f", sum);
        add = 1/(++num);
    }
    printf("%f\n", sum);
}
