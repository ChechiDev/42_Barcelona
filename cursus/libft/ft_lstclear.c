/*
ft_lstclear

Elimina y libera todos los nodos de una lista enlazada.
Para cada nodo, aplica la función `del` sobre el contenido
y libera el propio nodo. Al finalizar, el puntero de la lista
se establece a NULL.

Parámetros:
- lst: dirección del puntero al primer nodo de la lista.
- del: función que libera el contenido de cada nodo.

Retorno:
- Ninguno.
*/

#include "libft.h"

void    ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*next;

	if (!lst || !del)
	{
		return;
	}
	while (*lst)
	{
		next = (*lst)->next;
		ft_lstdelone(*lst, del);
		*lst = next;
	}
	*lst = NULL;
}
/*
static void	del(void *content)
{
	free(content);
}

int	main(int argc, char **argv)
{
	t_list	*test_lst;
	int	i;

	if (argc < 2)
	{
		printf("Use %s <argN...>", argv[0]);
		return (1);
	}
	test_lst = NULL;
	i = 1;
	while (i < argc)
	{
		ft_lstadd_back(&test_lst, ft_lstnew(ft_strdup(argv[1])));
		i++;
	}
	printf("lista creada\n");
	ft_lstclear(&test_lst, del);
	printf("lista eliminada: %s\n", (test_lst == NULL) ? "OK" : "Error");
	return (0);
}
*/
