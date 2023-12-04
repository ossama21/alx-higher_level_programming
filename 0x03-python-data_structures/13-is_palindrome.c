#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *tortoise = *head, *hare = *head, *temp;
    int n;

    /* Traverse the linked list and push elements onto the stack */
    while (hare != NULL && hare->next != NULL)
    {
        n = tortoise->n;
        temp = malloc(sizeof(listint_t));
        if (temp == NULL)
            return (0);
        temp->n = n;
        temp->next = stack_top;
        stack_top = temp;
        tortoise = tortoise->next;
        hare = hare->next->next;
    }

    /* If the length of the linked list is odd, skip the middle element */
    if (hare != NULL)
        tortoise = tortoise->next;

    /* Traverse the remaining linked list and compare with the elements on the stack */
    while (tortoise != NULL)
    {
        if (stack_top == NULL || stack_top->n != tortoise->n)
            return (0);
        temp = stack_top;
        stack_top = stack_top->next;
        free(temp);
        tortoise = tortoise->next;
    }

    return (1);
}
