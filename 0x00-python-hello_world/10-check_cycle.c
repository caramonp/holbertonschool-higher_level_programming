#include "lists.h"

/**
 * check_cycle - check if the link list has a cycle
 * @list: list
 * Return: 0 if there is no cylce 1 if there is
 */

int check_cycle(listint_t *list)
{

listint_t *head, *new;
if (list == NULL || list->next == NULL)
	return (0);
else
	head = list;
	new = list->next;
	while (head != NULL && new->next != NULL && new->next->next != NULL)
	{
		if (new == head)
			return (1);
		new = new->next->next;
		head = head->next;
	}
	return (0);
}
