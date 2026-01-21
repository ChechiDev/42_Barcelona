/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 19:29:03 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 19:29:46 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*next;

	if (!lst || !del)
	{
		return ;
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
