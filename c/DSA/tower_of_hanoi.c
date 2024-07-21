#include <stdio.h>
#include <stdlib.h>

// Structure to represent a stack
typedef struct {
    int *array;
    int capacity;
    int top;
} Stack;

// Function to initialize a stack
Stack *initializeStack(int capacity) {
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    stack->array = (int *)malloc(capacity * sizeof(int));
    stack->capacity = capacity;
    stack->top = -1;
    return stack;
}

// Function to check if a stack is empty
int isEmpty(Stack *stack) {
    return stack->top == -1;
}

// Function to push an element onto the stack
void push(Stack *stack, int item) {
    stack->array[++stack->top] = item;
}

// Function to pop an element from the stack
int pop(Stack *stack) {
    return stack->array[stack->top--];
}

// Function to solve Tower of Hanoi iteratively
void iterativeHanoi(int num_disks, char source, char auxiliary, char destination) {
    Stack *stack = initializeStack(num_disks * 3); // Maximum possible size of the stack
    int moves = 0;

    // Push initial values to the stack
    push(stack, destination);
    push(stack, auxiliary);
    push(stack, source);
    push(stack, num_disks);

    while (!isEmpty(stack)) {
        num_disks = pop(stack);
        source = pop(stack);
        auxiliary = pop(stack);
        destination = pop(stack);

        if (num_disks > 0) {
            // Push the next recursive calls to the stack
            push(stack, destination);
            push(stack, auxiliary);
            push(stack, source);
            push(stack, num_disks - 1);

            // Move the disk from source to destination
            printf("Move disk %d from %c to %c\n", num_disks, source, destination);
            moves++;

            // Push the next recursive calls to the stack
            push(stack, auxiliary);
            push(stack, source);
            push(stack, destination);
            push(stack, num_disks - 1);
        }
    }

    printf("Number of moves: %d\n", moves);

    free(stack->array);
    free(stack);
}

int main() {
    int num_disks;

    // Input the number of disks
    printf("Enter the number of disks: ");
    scanf("%d", &num_disks);

    // Solve Tower of Hanoi iteratively
    iterativeHanoi(num_disks, 'A', 'B', 'C');

    return 0;
}
