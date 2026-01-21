/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 11:55:24 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:54:50 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char	*dst, const char *src, size_t n)
{
	size_t	i;
	size_t	src_len;

	src_len = 0;
	while (src[src_len])
	{
		src_len++;
	}
	if (n == 0)
	{
		return (src_len);
	}
	i = 0;
	while (i + 1 < n && src[i])
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (src_len);
}
/*
int	main(int argc, char **argv)
{
	char	buffer[20];
	size_t	n;
	size_t	result;

	if (argc != 3)
	{
		printf("Use: %s <string> <length>", argv[0]);	
		return (1);
	}
	n = (size_t)atoi(argv[2]);
	result = ft_strlcpy(buffer, argv[1], n);

	printf("dst: %s\n", buffer);
	printf("result: %zu\n", result);
	if (result >= n)
	{
		printf("Truncado");
	}
	return (0);
}
*/
