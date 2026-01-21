/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 19:30:09 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 19:30:48 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!lst || !f)
	{
		return ;
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
