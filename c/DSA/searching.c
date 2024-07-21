#include <stdio.h>
#include <search.h>
int index_sequential(int arr[],int num,int size);
int binary_recursion(int arr[],int low,int high,int num);
int binary(int arr[],int low,int high,int num);
int linear(int arr[], int num, int size);
int main(){
    int num;
    int arr[] = {1,2,3,4,5,6,7,8,9,10};
    int size = sizeof(arr)/sizeof(arr[0]);
    printf("Enter the number to search: ");
    scanf("%d",&num);
    linear(arr,num,size); // linear search
    int low = 0, high = size-1; 
    printf("Binary Search using Recursion\n");
    binary_recursion(arr,low,high,num); // binary search
    binary(arr,low,high,num); // binary search without recursion
    index_sequential(arr,num,size); // sequential search
    return 0;
}

int index_sequential(int arr[], int num, int size)
{
    printf("Index Sequential Search\n");
    int gs = 3;
    int arr1[size / gs]; 
    int index_size = sizeof(arr1) / sizeof(arr1[0]);

    for (int i = 0; i < index_size; i++)
    {
        arr1[i] = i * gs;
        // printf("%d\n", arr1[i]);
    }
    for (int i = 0; i < index_size; i++)
    {
        if (num == arr[arr1[i]])
        {
            printf("Number found at position %d\n", arr1[i] + 1);
            return 1; 
        }
        else if (num < arr[arr1[i]])
        {
            for (int j = arr1[i-1]; j <= arr[i]; j++)
            {
                if (num == arr[j])
                {
                    printf("Number found at position %d\n", j + 1);
                    return 1; 
                }
            }
            printf("Number not found\n");
            return 0; 
        }
    }

    printf("Number not found\n");
    return 0; 
}

int binary(int arr[],int low,int high,int num){
    printf("Binary search without recursion\n");
    while(low <= high)
    {
        int mid = (low+high)/2;
        if (num == arr[mid])
        {
            printf("Number found at position %d\n",mid+1);
            break;
        }
        else if (num < arr[mid])
        {
            high = mid-1;
        }
        else if (num > arr[mid])
        {
            low = mid+1;
        }
        else
        {
            printf("Number not found\n");      
        }
    }
}

int binary_recursion(int arr[],int low,int high,int num){
        int mid = (low+high)/2;
        if (num == arr[mid])
        {
            printf("Number found at position %d\n",mid+1);
        }
        else if (num < arr[mid])
        {
            binary_recursion(arr,low,mid-1,num);
        }
        else if (num > arr[mid])
        {
            binary_recursion(arr,mid+1,high,num);
        }
        else
        {
            printf("Number not found\n");
        }
    }
int linear(int arr[], int num, int size){
    printf("Linear or sequential Search\n");
    
    for (int i = 0; i < size; i++)
    {
        if(arr[i] == num)
        {
            printf("Number found at position %d\n",i+1);
            break;
        }
        else if (i == size)
        {   
            printf("Number not found\n");
        }
    }
}