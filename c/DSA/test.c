#include <stdio.h>

int index_sequential(int arr[], int num, int size)
{
    printf("Index Sequential Search\n");
    int gs = 3;
    int arr1[size / gs]; // Define arr1 with appropriate size
    int index_size = sizeof(arr1) / sizeof(arr1[0]);

    // Fill arr1 with indices
    for (int i = 0; i < index_size; i++)
    {
        arr1[i] = i * gs;
        printf("%d\n", arr1[i]);
    }

    // Search for num in arr using indices from arr1
    for (int i = 0; i < index_size; i++)
    {
        if (num == arr[arr1[i]])
        {
            printf("Number found at position %d\n", arr1[i] + 1);
            return 1; // Return 1 if number is found
        }
        else if (num < arr[arr1[i]])
        {
            // Perform linear search within the current block
            // int start = (i == 0) ? 0 : arr1[i - 1] + 1;
            // int end = (i == index_size - 1) ? size - 1 : arr1[i];
            for (int j = arr1[i-1]; j <= arr[i]; j++)
            {
                if (num == arr[j])
                {
                    printf("Number found at position %d\n", j + 1);
                    return 1; // Return 1 if number is found
                }
            }
            printf("Number not found\n");
            return 0; // Return 0 if number is not found
        }
    }

    printf("Number not found\n");
    return 0; // Return 0 if number is not found
}

int main()
{
    int num;
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(arr[0]);
    printf("Enter the number to search: ");
    scanf("%d", &num);

    // Call the index_sequential function
    index_sequential(arr, num, size);

    return 0;
}
