// To find the average distance between 2 points in a 6x6 two-dimensional grid

#include <stdio.h>
#include <stdlib.h>

int main()
{
    double sum=0, avg;
    for(int i=1; i<=6; i++)  // point of reference as (i,j)
    {
        for(int j=1; j<=6; j++)
        {
            for(int k=1; k<=6; k++)  // test point as (k,l)
            {
                for(int l=1; l<=6; l++)
                    sum += abs(i-k) + abs(j-l);
            }
        }
    }

    avg = sum/(36*36);
    printf("Average distance: %lf", avg);
    return 0;
}
