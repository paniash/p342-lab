// To find the average distance between 2 points on a straight line made of discrete N (=6) points

#include <stdio.h>
#include <stdlib.h>

int main()
{
    double avg, sum=0;
    for(int i=1; i<=6; i++)
    {
        for(int j=1; j<=6; j++)
            sum += abs(i-j);
    }

    avg = sum/36;
    printf("Average distance: %lf", avg);
    return 0;
}
