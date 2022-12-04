#include "lists.h"

/**
 * reverse_linked_list - reverses a singly linked list
 * @head: pointer to linked list head
 *
 * Return: Always 0
 */
void reverse_linked_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - check if linked list is a palindrome
 * @head: pointer to head of linked list
 *
 * Return: 1 if list is palindrome; else 0
 */
int is_palindrome(listint_t **head)
{
	/*Floyd's algorithm*/
	listint_t *slow = *head, *fast = *head, *temp = *head, *temp_two = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			temp_two = slow->next;
			break;
		}
		if (!fast->next)
		{
			temp_two = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_linked_list(&temp_two);

	while (temp && temp_two)
	{
		if (temp->n == temp_two->n)
		{
			temp_two = temp_two->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!temp_two)
		return (1);

	return (0);
}
