#include <stdio.h>
int print_array(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
}
int bubble_sort(int arr[], int size)
{
    printf("Bubble Sort\n");
    int temp;
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - 1 - i; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    print_array(arr, size);
}
int selection_sort(int arr[], int size)
{
    printf("\nSelection Sort\n");
    int min, temp;
    min = arr[0];
    for (int j = 0; j < size - 1; j++)
    {
        for (int i = 0 + i; i < size - 1; i++)
        {
            if (min > arr[i])
            {
                min = arr[i];
                temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }
    print_array(arr, size);
}
int insertion_sort(int arr[], int size)
{
    printf("\nInsertion Sort\n");
    int temp, j;
    for (int i = 1; i < size; i++)
    {
        temp = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > temp)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = temp;
    }
    print_array(arr, size);
}
int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, size);
    selection_sort(arr, size);
    insertion_sort(arr, size);  
    return 0;
}