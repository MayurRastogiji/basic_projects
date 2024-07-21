// #include <stdio.h>
// int main()
// {
//     int i, j, k, l, n, d;
//     printf("enter the length of pattern :\n");
//     scanf("%d", &n);
//     printf("which type of pattern do your want to print.\n");
// start:
// {
//     printf("enter 1 to upper right triangle\n");
//     printf("enter 2 to upper left triangle\n");
//     printf("enter 3 to lower left triangle\n");
//     printf("enter 4 to lower right triangle\n");
//     printf("enter 5 to make diamond like structure\n");
//     printf("enter 6 to draw a pattern of numbers\n");
//     printf("enter 7 to end the program\n");
//     scanf("%d", &d);
// }
//     switch (d)
//     {
//     case 1:
//         for (int i = n; i >= 1; i--)
//         {
//             for (int j = i; j <= n; j++)
//             {
//                 printf("  ");
//             }
//             for (int k = 1; k <= i; k++)
//             {
//                 printf("* ");
//             }
//             printf("\n");
//         }
//         goto start;
//         break;
//     case 2:
//         for (int i = n; i >= 1; i--)
//         {
//             for (int j = 1; j <= i; j++)
//             {
//                 printf("* ");
//             }
//             printf("\n");
//         }
//         goto start;
//         break;
//     case 3:
//         for (int i = 0; i < n; i++)
//         {
//             for (int j = 0; j <= i; j++)
//             {
//                 printf("* ");
//             }
//             printf("\n");
//         }
//         goto start;
//         break;
//     case 4:
//         for (int i = n; i >= 1; i--)
//         {
//             for (int j = 1; j <= i; j++)
//             {
//                 printf("  ");
//             }
//             for (int k = i; k < n + 1; k++)
//             {
//                 printf("* ");
//             }
//             printf("\n");
//         }
//         goto start;
//         break;
//     case 5:
//         for (i = 1; i < n; i++)
//         {
//             for (j = 0; j < n - i; j++)
//             {
//                 printf("  ");
//             }
//             for (k = 1; k <= i; k++)
//             {
//                 printf("* ");
//             }
//             for (l = 1; l < i; l++)
//             {
//                 printf("* ");
//             }
//             printf("\n");
//         }
//         for (int i = 1; i < n; i++)
//         {
//             for (int j = 0; j <= i; j++)
//             {
//                 printf("  ");
//             }
//             for (int k = 1; k < n - i - 1; k++)
//             {
//                 printf("* ");
//             }
//             for (l = 1; l < n - i; l++)
//             {
//                 printf("* ");
//             }
//             printf("\n");
//         }
//         goto start;
//         break;
//     case 6:
//         int len = (2 * n) - 1;
//         int pat[len][len];
//         int k = n;
//         for (int i = 0; i < n; i++)
//         {
//             for (int j = i; j < len - i; j++)
//             {
//                 for (int k = i; k < len - i; k++)
//                 {
//                     pat[j][k] = n - i;
//                 }
//             }
//         }
//         for (int j = 0; j < len; j++)
//         {
//             for (int k = 0; k < len; k++)
//             {
//                 printf("%d ", pat[j][k]);
//             }
//             printf("\n");
//         }
//         goto start;
//         break;
//     case 7:
//         goto end;
//         break;

//     default:
//         printf("input given is wrong\n");
//         break;
//     }
// end:
//     printf("our program is ended successfully");
//     return 0;
// }






#include <stdio.h>

// Function to print upper right triangle
void printUpperRightTriangle(int n) {
    for (int i = n; i >= 1; i--) {
        for (int j = i; j <= n; j++) {
            printf("  ");
        }
        for (int k = 1; k <= i; k++) {
            printf("* ");
        }
        printf("\n");
    }
}

// Function to print upper left triangle
void printUpperLeftTriangle(int n) {
    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

// Function to print lower left triangle
void printLowerLeftTriangle(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

// Function to print lower right triangle
void printLowerRightTriangle(int n) {
    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("  ");
        }
        for (int k = i; k < n + 1; k++) {
            printf("* ");
        }
        printf("\n");
    }
}

// Function to print diamond-like structure
void printDiamondLikeStructure(int n) {
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            printf("  ");
        }
        for (int k = 1; k <= i; k++) {
            printf("* ");
        }
        for (int l = 1; l < i; l++) {
            printf("* ");
        }
        printf("\n");
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            printf("  ");
        }
        for (int k = 1; k < n - i - 1; k++) {
            printf("* ");
        }
        for (int l = 1; l < n - i; l++) {
            printf("* ");
        }
        printf("\n");
    }
}

// Function to print a pattern of numbers
void printNumberPattern(int n) {
    int len = (2 * n) - 1;
    int pat[len][len];
    for (int i = 0; i < n; i++) {
        for (int j = i; j < len - i; j++) {
            for (int k = i; k < len - i; k++) {
                pat[j][k] = n - i;
            }
        }
    }
    for (int j = 0; j < len; j++) {
        for (int k = 0; k < len; k++) {
            printf("%d ", pat[j][k]);
        }
        printf("\n");
    }
}

int main() {
    int n, d;
    printf("Enter the length of pattern: ");
    scanf("%d", &n);
    
    while (1) {
        printf("Which type of pattern do you want to print?\n");
        printf("1. Upper Right Triangle\n");
        printf("2. Upper Left Triangle\n");
        printf("3. Lower Left Triangle\n");
        printf("4. Lower Right Triangle\n");
        printf("5. Diamond-like Structure\n");
        printf("6. Pattern of Numbers\n");
        printf("7. End the program\n");
        printf("Enter your choice: ");
        scanf("%d", &d);
        
        switch (d) {
            case 1:
                printUpperRightTriangle(n);
                break;
            case 2:
                printUpperLeftTriangle(n);
                break;
            case 3:
                printLowerLeftTriangle(n);
                break;
            case 4:
                printLowerRightTriangle(n);
                break;
            case 5:
                printDiamondLikeStructure(n);
                break;
            case 6:
                printNumberPattern(n);
                break;
            case 7:
                printf("Program ended successfully\n");
                return 0;
            default:
                printf("Invalid choice! Please enter a valid option.\n");
        }
    }
    
    return 0;
}
