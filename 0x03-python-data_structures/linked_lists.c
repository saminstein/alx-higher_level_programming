#include <stdlib.h>
#include "lists.h"


/**
 * print_listint - function that prints all the elements of a "listin
 * t_t" list.
 * @h: The head of the linked list
 * Return: the number of nodes of the linked list
 */
size_t print_listint(const listint_t *h)
{
	size_t nodes = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		nodes++;
	}
	return (nodes);
}

/**
 * add_nodeint_end - a function that adds a new
 * node at the end of a "listint_t" list.
 * @head: The head of the linked list
 * @n: The value to add at the end of the linked
 * list
 * Return: the address of the new element, or 
 * NULL if it failed
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *temp, *ptr;

	temp = malloc(sizeof(listint_t));

	ptr = *head;
	if (temp == NULL)
	{
		return (NULL);
	}
	temp->n = n;
	temp->next = NULL;

	if (*head == NULL)
	{
		*head = temp;
	}
	else
	{
		while (ptr->next != NULL)
		{
			ptr = ptr->next;
		}
		ptr->next = temp;
	}
	return (*head);
}


/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
