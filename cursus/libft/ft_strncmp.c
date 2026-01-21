/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 17:35:43 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:42:58 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t			i;
	unsigned char	uc1;
	unsigned char	uc2;

	i = 0;
	if (n == 0)
	{
		return (0);
	}
	while (i < n)
	{
		uc1 = (unsigned char)s1[i];
		uc2 = (unsigned char)s2[i];
		if (uc1 != uc2)
		{
			return (uc1 - uc2);
		}
		if (uc1 == '\0')
		{
			return (0);
		}
		i++;
	}
	return (0);
}
/*
int	main(int argc, char **argv)
{
	int	res;

	if (argc != 4)
	{
		printf("Use: %s <string1> <string2> <n>", argv[0]);
		return (1);
	}

	res = ft_strncmp(argv[1], argv[2], (size_t)atoi(argv[3]));
	printf("Result: %d\n", res);
	return (0);
}
*/
