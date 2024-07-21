#include <stdio.h>
#include <stdlib.h>
#define MAX_size 100
typedef struct stack_array
{
    int arr[MAX_size];
    int top;
}stack_array;

stack_array * new_array_stack(int size) 
{
    stack_array *new_array_stack = (stack_array*)malloc(sizeof(stack_array));
    if(!new_array_stack)
    {
        printf("Memory allocation error\n");
        exit(1);
    }
    new_array_stack->top = -1;
    for (int i = 0; i < size; i++)
    {
        new_array_stack->arr[i] = 0; // Initializing to zero or any default value
    }
    if(!new_array_stack -> arr)
    {
        printf("Memory allocation error\n");
        exit(1);
    }
    new_array_stack -> top = -1;
    return new_array_stack;
}
void if_full(stack_array * stack,int size)
{
    if(stack -> top == size - 1)
    {
        printf("Stack is overflow\n");
        exit(1);
    }
}
void if_empty(stack_array * stack)
{
    if(stack -> top == -1)
    {
        printf("Stack is underflow\n");
        exit(1);
    }
}
void push(stack_array * stack,int data,int size)
{
    if_full(stack,size);
    stack -> arr[++stack -> top] = data;
}
void pop(stack_array * stack)
{
    if_empty(stack);
    stack -> arr[stack -> top--];
}
void peek(stack_array * stack)
{
    if_empty(stack);
    printf("%d\n",stack -> arr[stack -> top]);
}
void traverse(stack_array * stack)
{
    if_empty(stack);
    for(int i = 0;i <= stack -> top;i++)
        printf("%d ",stack -> arr[i]);
    printf("\n");
}
int main()
{
    int size;
    printf("Enter the size of stack: ");
    scanf("%d",&size);
    stack_array * stack = new_array_stack(size);
    int choice,data;
    while(1)
    {
        printf("1.Push\n2.Pop\n3.Peek\n4.Traverse\n5.Exit\n");
        printf("Enter your choice: ");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
                printf("Enter the data: ");
                scanf("%d",&data);
                push(stack,data,size);
                break;
            case 2:
                pop(stack);
                break;
            case 3:
                peek(stack);
                break;
            case 4:
                traverse(stack);
                break;
            case 5:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}