/*
ft_lstdelone

Libera la memoria de un nodo de una lista enlazada.

Recibe un puntero al nodo `lst` y una función `del` que se encarga de
liberar correctamente el contenido almacenado en `lst->content`.
Primero se llama a la función `del` sobre el contenido del nodo y,
a continuación, se libera el propio nodo con `free`.

Esta función no libera ni modifica el nodo siguiente (`lst->next`).
La gestión del encadenamiento de la lista debe realizarse fuera de
esta función.

Si `lst` o `del` son NULL, la función no realiza ninguna operación.
*/

#include "libft.h"

void ft_lstdelone(t_list *lst, void (*del)(void *))
{
	if (!lst || !del)
	{
		return;
	}
	del(lst->content);
	free(lst);
}
/*
static void	ft_del_content(void *content)
{
	free(content);
}

int	main(int argc, char **argv)
{
	t_list	*test_node;

	if (argc != 2)
	{
		printf("Use: %s <str>\n", argv[0]);
		return (1);
	}
	test_node = ft_lstnew(ft_strdup(argv[1]));
	if (!test_node)
	{
		return (1);
	}
	printf("antes de borrar:\n");
	printf("content = %s\n", (char *)test_node->content);
	ft_lstdelone(test_node, ft_del_content);
	printf("Nodo eliminado\n");
	return (0);
}
*/
