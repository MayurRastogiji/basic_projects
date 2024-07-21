#include <stdio.h>
#include <stdlib.h>
typedef struct node
{
    int data;
    struct node * next;
}node;
typedef struct node_doubly
{
    int data;
    struct node_doubly * next;
    struct node_doubly * prev;
}node_doubly;
node * createnode(int data)
{
    node* newnode = (node*)malloc(sizeof(node));
    if(!newnode)
    {
        printf("Memory allocation error\n");
        exit(1);
    }
    newnode->data = data;
    newnode->next = NULL;
    return (newnode);
}
void traverse(node *head)
{
    if(!head)
    {
        printf("List is empty\n");
        return;
    }
    while(head)
    {
        printf("%d ",head->data);
        head = head->next;
    }
}
void insert_at_beginning(node **head,int data)
{
    node *newnode = createnode(data);
    newnode->next = *head;
    *head = newnode;
}
void insert_at_end(node **head,int data)
{
    node *newnode = createnode(data);
    if(!*head)
    {
        *head = newnode;
        return;
    }
    node *temp = *head;
    while(temp->next)
        temp = temp->next;
    temp->next = newnode;
}
void insert_at_position(node **head,int data,int pos)
{
    if(pos == 1 || pos == NULL)
    {
        insert_at_beginning(head,data);
        return;
    }
    node *newnode = createnode(data);
    node *temp = *head;
    int i = 1;
    while(i < pos-1 && temp)
    {
        temp = temp->next;
        i++;
    }
    if(!temp)
    {
        printf("Invalid position\n");
        return;
    }
    newnode->next = temp->next;
    temp->next = newnode;
}
void delete_at_beginning(node **head)
{
    if(!*head)
    {
        printf("List is empty\n");
        return;
    }
    node *temp = *head;
    *head = (*head)->next;
    free(temp);
}
void delete_at_end(node **head)
{
    if(!*head)
    {
        printf("List is empty\n");
        return;
    }
    node *temp = *head;
    node *prev = NULL;
    while(temp->next)
    {
        prev = temp;
        temp = temp->next;
    }
    if(!prev)
        *head = NULL;
    else
        prev->next = NULL;
    free(temp);
}
void delete_at_position(node **head,int pos)
{
    if(!*head)
    {
        printf("List is empty\n");
        return;
    }
    if(pos == 1)
    {
        delete_at_beginning(head);
        return;
    }
    node *temp = *head;
    node *prev = NULL;
    int i = 1;
    while(i < pos && temp)
    {
        prev = temp;
        temp = temp->next;
        i++;
    }
    if(!temp)
    {
        printf("Invalid position\n");
        return;
    }
    prev->next = temp->next;
    free(temp);
}
void reverse(node **head)
{
    if(!*head)
    {
        printf("List is empty\n");
        return;
    }
    node *prev = NULL;
    node *curr = *head;
    node *next = NULL;
    while(curr)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    *head = prev;
}
void reverse_recursive(node **head,node *prev,node *curr)
{
    if(!curr)
    {
        *head = prev;
        return;
    }
    node *next = curr->next;
    curr->next = prev;
    reverse_recursive(head,curr,next);
}
void reverse_recursive_caller(node **head)
{
    if(!*head)
    {
        printf("List is empty\n");
        return;
    }
    reverse_recursive(head,NULL,*head);
}
void reverse_k_nodes(node **head,int k)
{
    if(!*head)
    {
        printf("List is empty\n");
        return;
    }
    node *prev = NULL;
    node *curr = *head;
    node *next = NULL;
    int i = 0;
    while(curr && i < k)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
        i++;
    }
    *head = prev;
}
void reverse_k_nodes_recursive(node **head,int k)
{
    if(!*head)
    {
        printf("List is empty\n");
        return;
    }
    node *prev = NULL;
    node *curr = *head;
    node *next = NULL;
    int i = 0;
    while(curr && i < k)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
        i++;
    }
    (*head)->next = curr;
    *head = prev;
}
void reverse_k_nodes_recursive_caller(node **head,int k)
{
    if(!*head)
    {
        printf("List is empty\n");
        return;
    }
    node *prev = NULL;
    node *curr = *head;
    node *next = NULL;
    int i = 0;
    while(curr && i < k)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
        i++;
    }
    (*head)->next = curr;
    *head = prev;
    reverse_k_nodes_recursive_caller(&(*head)->next,k);
}
void traverse_recursive(node *head)
{
    if(!head)
        return;
    printf("%d ",head->data);
    traverse_recursive(head->next);
}
void reverseList(node *current, node *prev) {
    if (current == NULL) {
        return prev;
    }

    node *nextNode = current->next;     
    current->next = prev;

    return reverseList(nextNode, current);
}
int main()
{
    // its singly linked list
    node * head = NULL;
    head = createnode(10);
    head->next = createnode(20);
    head->next->next = createnode(30);
    head->next->next->next = createnode(40);
    node * a = head->next->next->next->next = createnode(50);
    a -> next = createnode(60);
    // if a -> next -> next = head then it will be circular linked list
    while(head)
    {
        printf("%d ",head->data);
        head = head->next;
    }
    printf("%d",a -> next ->data);
    return 0;

}
