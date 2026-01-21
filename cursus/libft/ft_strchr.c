/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 14:55:00 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:36:16 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	while (*s)
	{
		if (*s == uc)
		{
			return ((char *)s);
		}
		s++;
	}
	if (uc == '\0')
	{
		return ((char *)s);
	}
	return (NULL);
}
/*
int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 3)
	{
		printf("Use: %s <string> <character>", argv[0]);
		return (1);
	}
	res = ft_strchr(argv[1], argv[2][0]);
	if (res)
	{
		printf("Result: %s\n", res);
	}
	else
	{
		printf("No encontrado");
	}
	return (0);
}
*/
