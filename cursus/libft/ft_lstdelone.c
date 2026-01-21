/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 19:27:40 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 19:28:43 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdelone(t_list *lst, void (*del)(void *))
{
	if (!lst || !del)
	{
		return ;
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
