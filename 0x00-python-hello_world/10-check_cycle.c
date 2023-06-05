#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *calf = list;
	listint_t *cow = list;

	if (!list)
		return (0);

	while (calf && cow && cow->next)
	{
		calf = calf->next;
		cow = cow->next->next;
		if (calf == cow)
			return (1);
	}

	return (0);
}
