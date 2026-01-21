/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 18:10:57 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:49:51 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	const unsigned char	*ptr;
	unsigned char		uc;
	size_t				i;

	ptr = (const unsigned char *)s;
	uc = (unsigned char)c;
	i = 0;
	while (i < n)
	{
		if (ptr[i] == uc)
		{
			return ((void *)(ptr + i));
		}
		i++;
	}
	return (NULL);
}
/*
int	main(int argc, char **argv)
{
	void	*res;
	size_t	n;

	n = (size_t)atoi(argv[3]);
	if (argc != 4)
	{
		return (1);
	}	
	res = ft_memchr(argv[1], argv[2][0], n);
	if (res)
	{
		printf("%s\n", (char *)res);
	}
	else
	{
		printf("NULL\n");
	}
	return (0);
}
*/
