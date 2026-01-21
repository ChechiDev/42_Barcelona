/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 16:13:38 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:50:29 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	const unsigned char	*uc1;
	const unsigned char	*uc2;
	size_t				i;

	uc1 = (const unsigned char *)s1;
	uc2 = (const unsigned char *)s2;
	i = 0;
	while (i < n)
	{
		if (uc1[i] != uc2[i])
		{
			return (uc1[i] - uc2[2]);
		}
		i++;
	}
	return (0);
}
/*
int	main(int argc, char **argv)
{
	size_t	n;
	int	res;
	
	if (argc != 4)
	{
		printf("Use: %s <str1> <str2> <n>", argv[0]);
		return (1);
	}
	n = (size_t)atoi(&argv[3][0]);
	res = ft_memcmp(argv[1], argv[2], n);
	printf("result: %d\n", res);
	return (0);
}
*/
