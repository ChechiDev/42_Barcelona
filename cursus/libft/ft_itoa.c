/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 18:29:45 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 18:31:49 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_intlen(long n)
{
	int	len;

	len = 0;
	if (n <= 0)
	{
		len = 1;
	}
	while (n != 0)
	{
		len++;
		n /= 10;
	}
	return (len);
}

char	*ft_itoa(int n)
{
	char	*s;
	long	nb;
	size_t	i;

	nb = (long)n;
	i = ft_intlen(nb);
	s = (char *)malloc(i + 1);
	if (!s)
		return (NULL);
	s[i] = '\0';
	if (nb == 0)
		s[0] = '0';
	if (nb < 0)
	{
		s[0] = '-';
		nb = -nb;
	}
	while (nb > 0)
	{
		i--;
		s[i] = (char)('0' + (nb % 10));
		nb /= 10;
	}
	return (s);
}
/*
int	main(int argc, char **argv)
{
	char	*res;
	int	n;

	if (argc != 2)
	{
		printf("Use: %s <int>\n", argv[0]);
		return (1);
	}
	n = ft_atoi(argv[1]);
	res = ft_itoa(n);
	if (!res)
	{
		printf("Error Malloc\n");
		return (1);
	}
	printf("%s\n", res);
	free(res);
	return (0);
}
*/
