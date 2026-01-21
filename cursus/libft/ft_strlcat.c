/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 12:54:07 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:42:15 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t n)
{
	size_t	dst_len;
	size_t	src_len;
	size_t	i;

	dst_len = 0;
	while (dst_len < n && dst[dst_len])
	{
		dst_len++;
	}
	src_len = 0;
	while (src[src_len])
	{
		src_len++;
	}
	if (dst_len == n)
		return (n + src_len);
	i = 0;
	while (src[i] && (dst_len + i + 1) < n)
	{
		dst[dst_len + i] = src[i];
		i++;
	}
	dst[dst_len + i] = '\0';
	return (dst_len + src_len);
}
/*
int	main(int argc, char **argv)
{
	char	buffer[20];
	size_t	n;
	size_t	i;
	size_t	result;
	
	if (argc != 4)
	{
		printf("Use: %s <dst> <src> <size>", argv[0]);
		return (1);
	}
	n = (size_t)atoi(argv[3]);
	buffer[0] = '\0';
	i = 0;
	while (argv[1][i] && i < sizeof(buffer) - 1)
	{
		buffer[i] = argv[1][i];
		i++;
	}
	buffer[i] = '\0';
	result = ft_strlcat(buffer, argv[2], n);

	printf("dst: %s\n", buffer);
	printf("result: %zu\n", result);
	return (0);
}
*/
