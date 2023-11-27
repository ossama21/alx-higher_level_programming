#include "lists.h"

/**
 * check_cycle - checks is singly linked list has a cycle in it
 * @list: the list which cycle is checked
 * Return: 0 for no cycle and 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (!list)
		return(0);
	while (hare && tortoise && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}
