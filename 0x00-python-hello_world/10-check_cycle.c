#include "lists.h"

/**
* check_cycle - check  the likend list have cycle
* @list: head of linked list
*
* Return: 0 if no cycle , 1 if have
*/

int check_cycle(listint_t *list)
{
	listint_t *n, *nn;

	if (!list || !list->next)
		return (0);

	n = list->next;
	nn = list->next->next;

	while (n && nn && nn->next)
	{
		if (n == nn)
			return (1);


		n = n->next;
		nn = nn->next->next;
	}
	return (0);
}
