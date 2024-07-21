#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node * next;
}node;
typedef struct 
{
    node * top;
}stack;
stack *new_stack() {
    stack *new_stack = (stack *)malloc(sizeof(stack));
    if (!new_stack) {
        printf("Memory allocation error\n");
        exit(1);
    }
    new_stack->top = NULL;
    return new_stack;
}
void peek(stack *stack)
{
    if (stack->top ==NULL)
    {
        printf("Stack in underflow\n");
        exit(1);
    }
    printf("%d\n",stack->top->data);
}
void traverse(stack * stack)
{
    if (stack ->top ==NULL)
    {
        printf("Stack is underflow\n");
        exit(1);
    }
    node *temp =stack -> top;
    while(temp)
    {
        printf("%d ",temp->data);
        temp = temp -> next;
    }
    printf("\n");
}
void initialised (stack * stack)
{
    stack -> top = NULL;
}
void isempty(stack * stack)
{
    if(stack -> top == NULL)
    {
        printf("Stack is empty\n");
        exit(1);
    }
}
void push(stack * stack, int data)
{
    node * newnode = (node*)malloc(sizeof(node));
    if(!newnode)
    {
        printf("Memory allocation error\n");
        exit(1);
    }
    else if (newnode == NULL)
    {
        printf("Stack is overflow\n");
        exit(1);
    }
    newnode -> data = data;
    newnode -> next = stack -> top;
    stack -> top = newnode;
}
void pop(stack * stack)
{
    isempty(stack);
    node * temp = stack -> top;
    stack -> top = stack -> top -> next;
    free(temp);
}
int main()
{
    stack * stack = new_stack();
    initialised(stack);
    int choice,data;
    while(1)
    {
        printf("Enter 1 for push\nEnter 2 for pop\nEnter 3 for peek\nEnter 4 for traverse\nEnter 5 for exit\n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
                printf("Enter the data: ");
                scanf("%d",&data);
                push(stack,data);
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
                exit(1);
                default:
                printf("Invalid choice\n");    
        }
    }
    return 0;
}
