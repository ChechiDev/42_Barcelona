/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 19:22:16 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 19:23:33 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!lst || !new)
	{
		return ;
	}
	new->next = *lst;
	*lst = new;
}
/*
int	main(int argc, char **argv)
{
	t_list	*lst;
	t_list	*node1;
	t_list	*node2;

	if (argc != 3)
	{
		printf("Use: %s <str1> <str2>\n", argv[0]);
		return (1);
	}
	lst = NULL;
	node1 = ft_lstnew(argv[1]);
	node2 = ft_lstnew(argv[2]);
	if (!node1 || !node2)
	{
		printf("Error\n");
		return (1);
	}
	ft_lstadd_front(&lst, node1);
	ft_lstadd_front(&lst, node2);
	printf("Contenido del primer nodo: %s\n", (char *)lst->content);
	printf("Contenido del segundo nodo: %s\n", (char *)lst->next->content);
	return (0);
}
*/
