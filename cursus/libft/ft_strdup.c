/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/09 13:51:43 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/13 17:50:55 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	size_t	i;
	char	*new;

	if (!s)
	{
		return (NULL);
	}
	i = 0;
	new = (char *)malloc(sizeof(char) * ft_strlen((char *)s) + 1);
	if (!new)
	{
		return (NULL);
	}
	while (*s)
	{
		new[i++] = *s++;
	}
	new[i] = '\0';
	return (new);
}
/*
int	main(int argc, char **argv)
{
	char	*copy;
	if (argc != 2)
	{
		printf("Use: %s <string> ", argv[0]);
		return (1);
	}
	copy = ft_strdup(argv[1]);
	if (!copy)
	{
		printf("Malloc failed");
		return (1);
	}
	printf("Original: %s\n", argv[1]);
	printf("ft_strdup: %s\n", copy);
	free(copy);
	return (0);
}
*/
