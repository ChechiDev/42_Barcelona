/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 16:48:53 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:53:17 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	const unsigned char	*s;
	unsigned char		*d;
	size_t				i;

	d = (unsigned char *)dest;
	s = (const unsigned char *)src;
	i = 0;
	if (d < s)
	{
		while (i < n)
		{
			d[i] = s[i];
			i++;
		}
	}
	else
	{
		while (n > 0)
		{
			d[n - 1] = s[n - 1];
			n--;
		}
	}
	return (dest);
}
/*
int	main(int argc, char **argv)
{
	char	buffer[11];
	size_t	n;
	size_t	i;

	if (argc != 3)
	{
		printf("Use: %s <value> <num_bytes>", argv[0]);
		return (1);
	}

	n = (size_t)atoi(argv[2]);
	i = 0;
	if (n > sizeof(buffer))
	{
		n = sizeof(buffer);
	}
	printf("Antes: %s\n", argv[1]);

	ft_memmove(buffer, argv[1], n);

	while (i < n)
	{
		printf("buffer[%zu] = %c\n", i, buffer[i]);
		i++;
	}
	printf("Como string: %s\n", buffer);
	return (0);
}
*/
