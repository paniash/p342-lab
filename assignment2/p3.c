// To create 3x3 matrices in through user input for the elements in 2 separate files and to read these matrices from the file and calculate MxA and MxN where the 2 matrices are M and N. (A from question 2)

#include <stdio.h>
int main()
{
    int num_m[3][3], num_n[3][3];
    int vect_a[3];
    vect_a[0] = 1;
    vect_a[1] = 4;
    vect_a[2] = 9;

    FILE *m, *n;
    m = fopen("m_c.txt", "r");
    n = fopen("n_c.txt", "r");

    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            fscanf(m, "%d", &num_m[i][j]);
            fscanf(n, "%d", &num_n[i][j]);
        }
    }

    // print the matrices
    printf("The matrices are \n");
    printf("M = \n");
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
            printf("%d\t", num_m[i][j]);
        printf("\n");
    }

    printf("\n");
    printf("N = \n");

    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
            printf("%d\t", num_n[i][j]);
        printf("\n");
    }

    printf("\nA = \n");
    for(int i=0; i<3; i++)
        printf("%d\t", vect_a[i], "\n");

    // calculate MxN (matrix multiplication)
    int prod[3][3] = {0};
    for(int i=0; i<3; i++)
        for(int j=0; j<3; j++)
        {
            for(int k=0; k<3; k++)
                prod[i][j] += num_m[i][k] * num_n[k][j];
        }

    // calculate MxA (matrix multiplication)
    int vec[3] = {0};
    for(int i=0; i<3; i++)
        for(int k=0; k<3; k++)
            vec[i] += num_m[i][k] * vect_a[k];


    // print MxN
    printf("\n\nM x N = \n");
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
            printf("%d\t", prod[i][j]);
        printf("\n");
    }

    // print MxA
    printf("\nM x A = \n");
    for(int i=0; i<3; i++)
    {
        printf("%d\t", vec[i], "\n");
    }

    fclose(m);
    fclose(n);
    return 0;
}
