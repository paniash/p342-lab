// To create two vectors A=(a1, a2, a3) and B=(b1, b2, b3) with numbers as user input
#include <stdio.h>

int main()
{
    int vect_a[3], vect_b[3];  // define arrays of size 3
    // vect_a = [1, 4, 9];
    // vect_b = [2, 17, 26];
    vect_a[0] = 1;
    vect_a[1] = 4;
    vect_a[2] = 9;

    vect_b[0] = 2;
    vect_b[1] = 17;
    vect_b[2] = 26;


    // prints the vectors
    printf("The vectors are:\n");
    printf("A = [ ");
    for(int i=0; i<3; i++)
    {
        printf("%d,", vect_a[i]);
    }
    printf("]\n");
    printf("B = [ ");
    for(int j=0; j<3; j++)
    {
        printf("%d,", vect_b[j]);
    }
    printf("]\n");

    // calculates the sum i.e., A+B
    int sum[3];
    for(int k=0; k<3; k++)
    {
        sum[k] = vect_a[k] + vect_b[k];
    }

    // calculates the dot product i.e., A.B
    int prod = 0;
    for(int l=0; l<3; l++)
    {
        prod += vect_a[l]*vect_b[l];
    }

    // displays the sum and dot product
    printf("\nCalculated results:");
    printf("\nA+B = [");
    for(int i=0; i<3; i++)
    {
        printf("%d,", sum[i]);
    }
    printf("]\n");
    printf("A.B = %d", prod);
    return 0;
}
