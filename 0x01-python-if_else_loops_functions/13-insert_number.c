#include "lists.h"
#include <unistd.h>
#include <stdlib.h>

/**
 * insert_node - function that inserts a number in linked list
 * @head: pointer pointing to the linked list
 * @number: new node number
 * Return: return address of the new node, or NULL
**/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *nw = NULL;
	listint_t *tmp = NULL;

	if (!head)
		return (NULL);

	nw = malloc(sizeof(listint_t));
	if (!nw)
		return (NULL);
	nw->n = number;
	nw->next = NULL;

	if (!*head || (*head)->n > number)
	{
		nw->next = *head;
		return (*head = nw);
	}
	else
	{
		while (curr && curr->n < number)
		{
			tmp = curr;
			curr = curr->next;
		}
		tmp->next = nw;
		nw->next = curr;
	}

	return (nw);
}
