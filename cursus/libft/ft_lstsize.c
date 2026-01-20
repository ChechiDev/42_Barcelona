/*
ft_lstsize

Cuenta el número de nodos de una lista enlazada.

Parámetro:
- lst: puntero al primer nodo de la lista.

Retorno:
- Número total de nodos de la lista.
- 0 si la lista está vacía (lst == NULL).

Notas:
- No modifica la lista.
- No reserva ni libera memoria.
*/

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	int	count;

	count = 0;
	while (lst)
	{
		count++;
		lst = lst->next;
	}
	return (count);
}
/*
int	main(int argc, char **argv)
{
	t_list	*lst_empty;
	t_list	*lst_one;
	t_list	*lst_args;
	int	i;

	lst_empty = NULL;
	printf("lista vacia -> size = %d\n", ft_lstsize(lst_empty));
	lst_one = ft_lstnew("solo");
	printf("Lista con 1 node -> size = %d\n", ft_lstsize(lst_one));
	lst_args = NULL;
	i = 1;
	while (i < argc)
	{
		ft_lstadd_front(&lst_args, ft_lstnew(argv[i]));
		i++;
	}
	printf("Lista creada con args (front) -> size = %d\n", ft_lstsize(lst_args));
	return (0);
}
*/
