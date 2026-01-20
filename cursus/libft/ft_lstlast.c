/*
ft_lstlast

Devuelve un puntero al último nodo de una lista enlazada.

Recorre la lista empezando por el nodo inicial `lst` hasta encontrar
el nodo cuyo campo `next` es NULL, lo que indica que es el último
elemento de la lista.

Si la lista está vacía (`lst == NULL`), la función devuelve NULL.

La lista no se modifica y no se realiza ninguna reserva de memoria.
*/

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
	{
		return (NULL);
	}
	while (lst->next)
	{
		lst = lst->next;
	}
	return (lst);
}
/*
int	main(int argc, char **argv)
{
	t_list	*test_lst;
	t_list	*last;
	int	i;

	if (argc < 2)
	{
		printf("Use: %s <argN>\n", argv[0]);
		return (1);
	}
	test_lst = NULL;
	i = 1;
	while (i < argc)
	{
		ft_lstadd_front(&test_lst, ft_lstnew(argv[i]));
		i++;
	}
	last = ft_lstlast(test_lst);
	if (last)
	{
		printf("ultimo node: %s\n", (char *)last->content);
	}
	else
	{
		printf("Lista vacia\n");
	}
	return (0);
}
*/
