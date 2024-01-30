#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node at a given pos
 * ition
 * @head: This is a pointer to a pointer to
 * the head of the linked list
 * @number: This is the integer value that you
 * want to insert into the linked list.
 * Return: returning a pointer to a node in
 * the linked list.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp && temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;

	return (new);
}
