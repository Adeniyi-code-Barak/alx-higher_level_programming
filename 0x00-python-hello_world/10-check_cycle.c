#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle
 * @list: A pointer to the head of the linked list.
 *
 * Return: Return 1 if there is a cycle, 0 if there is no cycle.
 **/
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	if (!list)
		return (0);

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}

	return (0);
}
