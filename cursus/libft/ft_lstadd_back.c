/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 19:26:05 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 19:27:24 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*tmp;

	if (!lst || !new)
	{
		return ;
	}
	if (*lst == NULL)
	{
		*lst = new;
		return ;
	}
	tmp = *lst;
	while (tmp->next)
	{
		tmp = tmp->next;
	}
	tmp->next = new;
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
*/
