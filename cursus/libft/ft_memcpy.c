/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/29 18:52:31 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:30:41 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char		*d;
	const unsigned char	*s;
	size_t				i;

	d = (unsigned char *)dest;
	s = (const unsigned char *)src;
	i = 0;
	while (i < n)
	{
		d[i] = s[i];
		i++;
	}
	return (dest);
}
/*
int	main(int argc, char **argv)
{
	char	buffer[50];	
	size_t	n;
	size_t	i;

	if (argc != 3)
	{
		printf("Use: %s <value> <size>", argv[0]);
		return (1);
	}

	n = (size_t)atoi(argv[2]);
	if (n > sizeof(buffer))
	{
		n = sizeof(buffer);
	}

	ft_memcpy(buffer, argv[1], n);

	i = 0;
	while (i < n)
	{
		printf("Buffer[%zu] = %d\n", i, (unsigned char)buffer[i]);
		i++;
	}
	printf("Resultado Buffer: %s\n", buffer);
	return (0);

}
*/
