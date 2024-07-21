#include <stdio.h>
#include <stdlib.h>
#define MAX_size 100
typedef struct queue_array
{
    int arr[MAX_size];
    int front;
    int rear;
} queue_array;
typedef struct node
{
    int data;
    struct node *next;
} node;
typedef struct
{
    node *front;
    node *rear;

} queue_linkedlist;
void initialise(queue_array *queue)
{
    queue->front = -1;
    queue->rear = -1;
}
void isempty(queue_array *queue, int implementation)
{
    if (implementation == 1)
    {
        if (queue->front == -1 && queue->rear == -1)
        {
            printf("Queue is empty\n");
            exit(1);
        }
    }
    else if (implementation == 2)
    {
        if (queue->front == NULL && queue->rear == NULL)
        {
            printf("Queue is empty\n");
            exit(1);
        }
    }
    else
    {
        printf("Invalid choice\n");
        exit(1);
    }
}
void isfull(queue_array *queue)
{
    if (queue->rear == MAX_size - 1)
    {
        printf("Queue is full\n");
        exit(1);
    }
}
void enqueue(queue_array *queue, int data, int implementation)
{
    if (implementation == 1)
    {
        isfull(queue);
    if (queue->front == -1)
    {
        queue->front = 0;
    }
    queue->rear++;
    queue->arr[queue->rear] = data;
    exit(1);
    }
    else if (implementation == 2)
    {
        node *newnode = (node *)malloc(sizeof(node));
        if(!newnode)
        {
            printf("Memory allocation error\n");
            exit(1);
        }
        newnode->data = data;
        newnode->next = NULL;
        if(queue->front == NULL)
        {
            queue->front = queue->rear = newnode;
            
        }
        else
        {
            queue->rear->next = newnode;        
        }
        queue->rear = newnode;
    }
    else
    {
        printf("Invalid choice\n");
        exit(1);
    }
    
    
}
void dequeue(queue_array *queue, int implementation)
{
    if (implementation ==1)
    {
        isempty(queue, implementation);
    if (queue->front == queue->rear)
    {
        queue->front = queue->rear = -1;
    }
    else
    {
        queue->front++;
    }
    }
    else if (implementation ==2)
    {
       isempty(queue, implementation);
       node *temp = queue->front;
       int data = temp->data;
         queue->front = queue->front->next;
         if (queue->front == NULL)
         {
             queue->rear = NULL;
         }
            free(temp); 
    }
    
    
    
}
void peek(queue_array *queue, int implementation)
{
    isempty(queue, implementation);
    printf("%d\n", queue->arr[queue->front]);
}
void traverse(queue_array *queue, int implementation)
{
    isempty(queue, implementation);
    for (int i = queue->front; i <= queue->rear; i++)
    {
        printf("%d ", queue->arr[i]);
    }
    printf("\n");
}
void tasks(queue_array *queue, int implementation)
{
    int choice, data;
    while (1)
    {
        printf("Enter 1 for insertion\nEnter 2 for deletion\nEnter 3 for peek\nEnter 4 for traverse\nEnter 5 for exit\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter the data: ");
            scanf("%d", &data);
            enqueue(queue, data, implementation);
            break;
        case 2:
            dequeue(queue, implementation);
            break;
        case 3:
            peek(queue, implementation);
            break;
        case 4:
            traverse(queue, implementation);
            break;
        case 5:
            exit(1);
        default:
            printf("Invalid choice\n");
        }
    }
}
int main()
{
    int implementation;
    printf("enter 1 for array implementation\nenter 2 for linkedlist implementation\n");
    scanf("%d", &implementation);
    switch (implementation)
    {
    case 1:
        queue_array *queue = (queue_array *)malloc(sizeof(queue_array));
        if (!queue)
        {
            printf("Memory allocation error\n");
            exit(1);
        }
        initialise(queue);
        tasks(queue, implementation);
        break;
    case 2:
        queue_linkedlist *queue = (queue_linkedlist *)malloc(sizeof(queue_linkedlist));
        if (!queue)
        {
            printf("Memory allocation error\n");
            exit(1);
        }
        queue->front = NULL;
        queue->rear = NULL;
        tasks(queue, implementation);
        break;
    default:
        printf("Invalid choice\n");
        exit(1);
    }

    return 0;
}
