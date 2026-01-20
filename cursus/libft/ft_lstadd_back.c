/*
ft_lstadd_back

Añade el nodo `new` al final de la lista enlazada `lst`.

Si la lista está vacía (`*lst == NULL`), el nodo `new` pasa a ser
el primer elemento de la lista.

En caso contrario, la función recorre la lista hasta encontrar
el último nodo y enlaza `new` como su siguiente elemento.

No reserva ni libera memoria.

Parámetros:
- lst: dirección del puntero al primer nodo de la lista.
- new: puntero al nodo que se desea añadir al final.

Valor de retorno:
- Ninguno.
*/

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*tmp;

	if (!lst || !new)
	{
		return;
	}
	if (*lst == NULL)
	{
		*lst = new;
		return;
	}
	tmp = *lst;
	while (tmp->next)
	{
		tmp = tmp->next;
	}
	tmp->next = new;
}

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
		ft_lstadd_back(&test_lst, ft_lstnew(argv[i]));
		i++;
	}
	last = ft_lstlast(test_lst);
	if (last)
	{
		printf("ultimo node: %s\n", (char *)last->content);
	}
	else
	{
		printf("lista vacia\n");
	}
	return (0);
}
