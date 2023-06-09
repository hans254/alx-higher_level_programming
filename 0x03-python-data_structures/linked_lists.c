#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *print_listint - prints all the elements of a linked_t list
 *@h: pointer to head of list
 *Return: number of node
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *recent;
	unsigned int t; /*number of nodes*/

	recent = h;
	t = 0;
	while (recent!= NULL)
	{
		printf("%i\n",recent->t);
		recent = recent->next;
		t++;
	}
	return (t);
}
/**
 *add_node_end - adds a new node at the end of a listint_t list
 *@head: pointer to pointer of first node of listint_t list
 *@n: integer to be included in new node
 *Return: address of the new or NULL if it fails
 */
listint_t *add_node_int_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next  = new;
	}
	return (new);
}

/**
 *free_listint - frees a listint_t list
 *@head: pointer to list to be freed
 *Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
