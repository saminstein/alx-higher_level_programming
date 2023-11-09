#include "lists.h"

void reverse_list(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;
  
  while (current != NULL)
  {
    next = current->next;
    current->next = prev;
    prev = current;
    current = next;
  }
  *head = prev;
}

/**
 * is_palindrome -function that checks if a 
 * singly linked list is a palindrome
 * @head: The head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it 
 * is a palindrome
 */
int is_palindrome(listint_t **head)
{
  listint_t *slow = *head;
  listint_t *fast = *head;
  
  while(fast != NULL && fast->next != NULL)
  {
    slow = slow->next;
    fast = fast->next->next;
  }
  if (fast != NULL)
    fast = slow->next;
    
  reverse_list(&fast);
  while (fast != NULL)
  {
    if (slow->n != fast->n)
    {
      return (0);
    }
    slow = slow->next;
    fast = fast->next;
  }
  return (1);
}
