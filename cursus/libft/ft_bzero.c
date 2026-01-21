/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 17:45:20 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:32:51 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_bzero(void *ptr, size_t n)
{
	unsigned char	*dst;
	size_t			i;

	dst = (unsigned char *)ptr;
	i = 0;
	while (i < n)
	{
		dst[i] = '\0';
		i++;
	}
}
/*
int	main(int argc, char **argv)
{
	unsigned char	buffer[50];
	size_t	n;
	size_t	i;

	if (argc != 2)
	{
		printf("Use: %s <value_bytes> ", argv[0]);
		return (1);
	}

	n = (size_t)atoi(argv[1]);
	i = 0;

	if (n > sizeof(buffer))
	{
		n = sizeof(buffer);
	}

	ft_bzero(buffer, n);
	
	while (i < n)
	{
		printf("buffer[%zu] = %d\n", i, buffer[i]);
		i++;
	}
	return (0);
}
*/
