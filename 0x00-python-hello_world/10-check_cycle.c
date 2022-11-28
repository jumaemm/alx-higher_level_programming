#include "lists.h"

/**
 * check_cycle - check if a cycle exists in a linked list
 * @list: list to be checked
 * Return: 1 if present, o if none
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);
	
	fast = fast->next;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
