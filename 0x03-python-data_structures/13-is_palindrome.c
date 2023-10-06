#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer to the head of the list
 *
 * Return: pointer to the head of the reversed list
*/
static listint_t *reverse_list(listint_t **head)
{
	listint_t *reversed = NULL;
	listint_t *current = *head;
	listint_t *temp;

	while (current != NULL)
	{
		temp = malloc(sizeof(listint_t));

		if (temp == NULL)
			return (NULL);

		temp->n = current->n;
		temp->next = reversed;
		reversed = temp;

		current = current->next;
	}
	return (reversed);
}
/**
 * compare_lists - compares two linked lists
 * @list1: first linked list
 * @list2: second linked list
 *
 * Return: 1 if lists are equal, 0 otherwise
*/
static int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 *
 * Return: 1 if palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *reversed;

	if (*head == NULL)
		return (1);

	reversed = reverse_list(head);

	if (reversed == NULL)
		return (0);

	if (compare_lists(*head, reversed))
	{
		free_listint(reversed);
		return (1);
	}
	free_listint(reversed);
	return (0);
}
