#include "lists.h"
/**
 * insert_node - Inserts number into singly linked list
 * @head: pointer to head of list
 * @number: value of num to insert
 * Return: pointer to new node, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current->next)
	{
		if ((current->next)->n >= number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current  = current->next;
	}
	new->next = NULL;
	current->next = new;
	return (new);
}
