// Rotating matrix of n order 90 degree clockwise

#include <stdio.h>

int main() {
    int r,c;
    printf("Enter the number of Rows:\n");
    scanf("%d",&r);
    printf("Enter number of columns:\n");
    scanf("%d",&c);
    int matrix[r][c];
    printf("Enter elements of the matrix\n");
    for (int i = 0; i< r; i++){
        for(int j = 0; j < c; j++){
            printf("Enter element matrix[%d][%d] ",i,j);
            scanf("%d",&matrix[i][j]);
        }
    }
    printf("Your matrix is:\n ");
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }
    int transpose[c][r];
    printf("transpose of your given matrix is:\n");
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            transpose[j][i] = matrix[i][j];
        }
    }
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            printf("%d ",transpose[i][j]);
        }
        printf("\n");
    }
    int temp;
    for(int i = 0; i< r;i++){
        for(int j =0 ; j < c/2; j++){
        temp = transpose[i][j];
        transpose[i][j] = transpose[i][c-j-1];
        transpose[i][c-j-1] = temp;

        }
    }
    printf("Rotating your matrix by 90 degrees:\n");
    for(int i = 0; i < r; i++){
        for(int j = 0; j < c; j++){
            printf("%d ",transpose[i][j]);
        }
        printf("\n");
    }
    return 0;    
}