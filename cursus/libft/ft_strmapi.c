/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 18:32:28 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 18:33:22 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	i;
	char			*res;

	if (!s || !f)
	{
		return (NULL);
	}
	res = malloc(ft_strlen(s) + 1);
	if (!res)
	{
		return (NULL);
	}
	i = 0;
	while (s[i])
	{
		res[i] = f(i, s[i]);
		i++;
	}
	res[i] = '\0';
	return (res);
}
/*
static char	ft_map_toupper(unsigned int i, char c)
{
	(void)i;
	return ((char)ft_toupper((int)c));
}

int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 2)
	{
		printf("Use: %s <string>\n", argv[0]);
		return (1);
	}
	res = ft_strmapi(argv[1], ft_map_toupper);
	if (!res)
	{
		printf("Error Malloc");
		return (1);
	}
	printf("%s\n", res);
	free(res);
	return (0);
}
*/
