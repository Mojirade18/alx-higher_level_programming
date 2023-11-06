#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    if (!*head || !(*head)->next)
        return (1);

    while (fast && fast->next)
    {
        fast = fast->next->next;
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    if (fast)
        slow = slow->next;

    while (prev && prev->n == slow->n)
    {
        prev = prev->next;
        slow = slow->next;
    }

    if (!prev)
        return (1);

    return (0);
}

