/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 19:25:09 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 19:25:30 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
	{
		return (NULL);
	}
	while (lst->next)
	{
		lst = lst->next;
	}
	return (lst);
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
		ft_lstadd_front(&test_lst, ft_lstnew(argv[i]));
		i++;
	}
	last = ft_lstlast(test_lst);
	if (last)
	{
		printf("ultimo node: %s\n", (char *)last->content);
	}
	else
	{
		printf("Lista vacia\n");
	}
	return (0);
}
*/
