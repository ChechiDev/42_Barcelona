/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 16:35:24 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:36:56 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	unsigned char	uc;
	char			*last;

	uc = (unsigned char)c;
	last = NULL;
	while (*s)
	{
		if ((unsigned char)*s == uc)
		{
			last = (char *)s;
		}
		s++;
	}
	if (uc == '\0')
	{
		return ((char *)s);
	}
	return (last);
}
/*
int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 3)
	{
		printf("Use: %s <string> <character>", argv[0]);
	}
	res = ft_strrchr(argv[1], (unsigned char)argv[2][0]);
	if (res)
	{
		printf("Result: %s\n", res);
		printf("Posicion: %ld\n", (long)(res - argv[1]));
	}
	else
	{
		printf("No encontrado\n");
	}
	return (0);
}
*/
