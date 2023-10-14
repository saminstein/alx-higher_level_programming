#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly list has a cycle
 * in it
 * @list: The singly list to check
 * Return: 0 if there is no cycle, 1 if there is a
 * cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	while (turtle != NULL && hare != NULL && hare->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (turtle == hare)
		{
			return (1);
		}
	}
	return (0);
}
