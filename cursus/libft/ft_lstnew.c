/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 19:04:44 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 19:21:03 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list	*lst;

	lst = malloc(sizeof(t_list));
	if (!lst)
	{
		return (NULL);
	}
	lst->content = content;
	lst->next = NULL;
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
