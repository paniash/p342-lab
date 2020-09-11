#include <stdio.h>

// Partial pivoting
void partial_pivot(int &a[][], int &b[], int n = 3)
{
    for(int i=0; i<n; i++)
        if (abs(a[i][i]) == 0)
            for(int j=i+1; j<n; j++)
                if (abs(a[j][i]) > abs(a[i][i]))
                {
                    for(int k=0; k<n; k++)  // interchange ith and jth rows of matrix 'a'
                    {
                        int temp = a[i][k];
                        a[i][k] = a[j][k];
                        a[j][k] = temp;
                    }

                    temp = b[i];
                    b[i] = b[j];
                    b[j] = temp;
                }
}

int gauss_jordan(int &a[][], int &b[], int n=3)
{
    partial_pivot(a,b);
    for(int i=0; i<n; i++)
    {
        int pivot = a[i][i];
        b[i] = b[i]/pivot;
        for(int c=i; c<n; c++)
            a[i][c] = a[i][c]/pivot;

        for(int k=0; k<n; k++)
            if (k!=i && a[k][i] != 0)
            {
                int factor = a[k][i];
                b[k] -= factor*b[i];
                for (int j=i; j<n; j++)
                    a[k][j] -= factor*a[i][j];
            }
    }
}

int main()
{
    int A[3][3], b[3];
    int n=3;

    FILE *a;
    a = fopen("a1.txt", "r");

}
