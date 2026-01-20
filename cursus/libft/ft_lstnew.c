/*
ft_lstnew

Reserva memoria para un nuevo nodo de lista enlazada.
Inicializa el campo `content` con el valor recibido como parámetro
y el campo `next` con NULL.

@param content: puntero al contenido a almacenar en el nodo.
@return puntero al nuevo nodo creado o NULL si falla malloc.
*/

#include "libft.h"

t_list *ft_lstnew(void *content)
{
	t_list	*lst;

	lst = malloc(sizeof(t_list));
	if (!lst)
	{
		return (NULL);
	}
	lst->content = content;
	lst->next= NULL;
	return (lst);
}
/*
int	main(int argc, char **argv)
{
	t_list	*node;

	if (argc != 2)
	{
		printf("Use: %s <string>\n", argv[0]);
		return (1);
	}
	node = ft_lstnew(argv[1]);
	if (!node)
	{
		printf("Error\n");
		return (1);
	}
	printf("content: %s\n", (char *)node->content);
	printf("next: %p\n", (void *)node->next);
	free(node);
	return (0);
}
*/
