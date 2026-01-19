/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 18:57:08 by sperez-l          #+#    #+#             */
/*   Updated: 2025/12/29 18:49:36 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

void	*ft_memset(void *ptr, int c, size_t n)
{
	unsigned char	*dst;
	unsigned char	uc;
	size_t		i;

	dst = (unsigned char *)ptr;
	uc = (unsigned char)c;
	i = 0;
	while (i < n)
	{
		dst[i] = uc;
		i++;
	}
	return (ptr);
}
/*
int	main(int argc, char **argv)
{
	char buffer[50];
	int	value;
	size_t	n;
	size_t	i;

	if (argc != 3)
	{
		printf("Use: %s <value> <size>", argv[0]); 
		return (1);
	}

	value = atoi(argv[1]);
	n = (size_t)atoi(argv[2]);

	ft_memset(buffer, value, n);

	i = 0;

	while (i < n && i < sizeof(buffer))
	{
		printf("buffer[%zu] = %d\n", i, (unsigned char)buffer[i]);
		i++;
	}
	return (0);
}
*/
