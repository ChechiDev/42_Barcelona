/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 18:53:16 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 19:13:09 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	long	nb;
	char	c;

	nb = (long)n;
	if (nb < 0)
	{
		write(fd, "-", 1);
		nb = -nb;
	}
	if (nb >= 10)
	{
		ft_putnbr_fd((int)(nb / 10), fd);
	}
	c = (char)('0' + (nb % 10));
	write(fd, &c, 1);
}
/*
int	main(int argc, char **argv)
{
	int	n;

	if (argc != 2)
	{
		printf("Use: %s <num>\n", argv[0]);
		return (1);
	}
	n = ft_atoi(argv[1]);
	ft_putnbr_fd(n, 1);
	write(1, "\n", 1);
	return (0);
}
*/
