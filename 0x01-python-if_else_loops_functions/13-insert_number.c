#include "lists.h"

/**
 *insert_node - insert node at position
 *@head: head Node
 *@n: number to insert
 *Return: the pointer to this list
*/

listint_t *insert_node(listint_t **head, int n)
{
	listint_t *current, *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = n;
	node->next = NULL;

	current = *head;

	while (current && current->next && current->next->n <= n)
		current = current->next;

	if (current == NULL)
		*head = node;
	else if (current->next == NULL)
		current->next = node;
	else
		{
			node->next = current->next;
			current->next = node;
		}

	return (node);
}
