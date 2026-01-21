/*
ft_lstiter

Itera la lista enlazada apuntada por `lst` y aplica la función `f`
al contenido (`content`) de cada uno de sus nodos.

La función `f` recibe un puntero al contenido del nodo y puede
modificarlo si es necesario.

Esta función no crea ni elimina nodos, no reserva ni libera memoria
y no modifica la estructura de la lista.

Si `lst` o `f` son NULL, la función no realiza ninguna operación.
*/

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!lst || !f)
	{
		return;
	}
	while (lst)
	{
		f(lst->content);
		lst = lst->next;
	}
}
/*
static void	ft_print_content(void *content)
{
	if (!content)
	{
		return;
	}
	ft_putendl_fd((char *)content, 1);
}

int	main(int argc, char **argv)
{
	t_list	*test_lst;
	int	i;

	if (argc < 2)
	{
		printf("Use %s <string>", argv[0]);
		return (1);
	}
	test_lst = NULL;
	i = 1;
	while (i < argc)
	{
		ft_lstadd_back(&test_lst, ft_lstnew(argv[i]));
		i++;
	}
	ft_lstiter(test_lst, ft_print_content);
	return (0);
}
*/
