/*
ft_lstmap

Itera la lista 'lst' y aplica la función 'f' al contenido de cada nodo.
Crea una nueva lista con los contenidos resultantes, almacenados en
nodos nuevos.

La lista original no se modifica.

En caso de error de reserva de memoria, libera correctamente toda la
nueva lista creada hasta el momento usando la función 'del' y
devuelve NULL.

Parámetros:
- lst: puntero al primer nodo de la lista original.
- f: función que transforma el contenido de cada nodo.
- del: función para liberar el contenido en caso de error.

Retorno:
- Puntero al primer nodo de la nueva lista, o NULL si falla.
*/

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_lst;
	t_list	*new_node;
	void	*new_content;

	if (!lst || !f || !del)
	{
		return (NULL);
	}
	new_lst = NULL;
	while (lst)
	{
		new_content = f(lst->content);
		if (!new_content)
		{
			ft_lstclear(&new_lst, del);
			return (NULL);
		}
		new_node = ft_lstnew(new_content);
		if (!new_node)
		{
			del(new_content);
			ft_lstclear(&new_lst, del);
			return (NULL);
		}
		ft_lstadd_back(&new_lst, new_node);
		lst = lst->next;
	}
	return (new_lst);
}
/*
static void	*ft_map(void *content)
{
	return (ft_strdup((char *)content));
}

static void	ft_del(void *content)
{
	free(content);
}

int	main(int argc, char **argv)
{
	t_list	*lst;
	t_list	*res;
	int	i;

	if (argc < 2)
	{
		printf("Use: %s <argN..>", argv[0]);
		return (1);
	}
	lst = NULL;
	i = 1;
	while (i < argc)
	{
		ft_lstadd_back(&lst, ft_lstnew(argv[i]));
		i++;
	}
	res = ft_lstmap(lst, ft_map, ft_del);
	if (!res)
	{
		printf("Error\n");
		return (1);
	}
	while (res)
	{
		printf("%s\n", (char *)res->content);
		res = res->next;
	}
	return (0);
}
*/
