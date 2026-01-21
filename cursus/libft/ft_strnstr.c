/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 16:40:03 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/08 19:18:49 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *small, size_t n)
{
	size_t	i;
	size_t	j;

	if (*small == '\0')
	{
		return ((char *)big);
	}
	i = 0;
	while (big[i] && i < n)
	{
		j = 0;
		while (small[j] && (i + j) < n && big[i + j] && big[i + j] == small[j])
		{
			j++;
		}
		if (small[j] == '\0')
		{
			return ((char *)(big + i));
		}
		i++;
	}
	return (NULL);
}
/*
int	main(int argc, char **argv)
{
	char	*res;
	size_t	n;

	if (argc != 4)
	{
		printf("Use: %s <big_str> <small_str> <n>\n", argv[0]);
		return (1);
	}
	n = (size_t)atoi(&argv[3][0]);
	res = ft_strnstr(argv[1], argv[2], n);
	if (res)
	{
		printf("Result: %s\n", res);
	}
	else
	{
		printf("NULL\n");
	}
	return (0);
}
*/
