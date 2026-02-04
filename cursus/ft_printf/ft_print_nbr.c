/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_nbr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/04 10:50:21 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/04 13:10:09 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

int	ft_put_unsigned(unsigned long ln)
{
	int	count;
	
	count = 0;
	if (ln >= 10)
	{
		count += ft_put_unsigned(ln / 10);
	}
	ft_putchar_fd('0' + (ln % 10), 1);
	return (count + 1);
}

int	ft_print_nbr(va_list args, char spec)
{
	long	ln;
	int		count;

	count = 0;
	if (spec == 'u')
	{
		ln = (long)va_arg(args, unsigned int);
	}
	else
	{
		ln = (long)va_arg(args, int);
	}
	if (spec != 'u' && ln < 0)
	{
		ft_putchar_fd('-', 1);
		count++;
		ln = -ln;
	}
	return (count + ft_put_unsigned((unsigned long)ln));
}
