/*
ft_lstadd_front

Añade el nodo 'new' al principio de la lista 'lst'.
'lst' es la dirección del puntero al primer nodo de la lista.
Si la lista estaba vacía, 'new' pasa a ser el primer nodo.
No reserva ni libera memoria.
*/

#include "libft.h"

void ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!lst || !new)
	{
		return;
	}
	new->next = *lst;
	*lst = new;
}
/*
int	main(int argc, char **argv)
{
	t_list	*lst;
	t_list	*node1;
	t_list	*node2;

	if (argc != 3)
	{
		printf("Use: %s <str1> <str2>\n", argv[0]);
		return (1);
	}
	lst = NULL;
	node1 = ft_lstnew(argv[1]);
	node2 = ft_lstnew(argv[2]);
	if (!node1 || !node2)
	{
		printf("Error\n");
		return (1);
	}
	ft_lstadd_front(&lst, node1);
	ft_lstadd_front(&lst, node2);
	printf("Contenido del primer nodo: %s\n", (char *)lst->content);
	printf("Contenido del segundo nodo: %s\n", (char *)lst->next->content);
	return (0);
}
*/
