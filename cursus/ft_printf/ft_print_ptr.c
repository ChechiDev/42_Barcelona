/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_ptr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 10:25:23 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/30 12:22:20 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

static int	ft_val_and_print_char(char c, int *count)
{
	int	print;

	print = ft_putchar_fd(c, 1);
	if (print < 0)
	{
		return (-1);
	}
	*count += print;
	return (0);
}

int	ft_print_hex_ptr(unsigned long n, int *count)
{
	char	base;

	base = "0123456789abcdef";
	if (n >= 16)
	{
		if (ft_print_hex_ptr(n / 16, count) < 0)
		{
			return (-1);
		}
	}
	return (ft_val_and_print_char(base[n % 16], count));
}

int	ft_print_ptr(va_list args)
{
	int				count;
	void			*ptr;
	unsigned long	address;

	ptr = va_arg(args, void *);
	address = (unsigned long)ptr;
	count = 0;
	if (ft_val_and_print_char('0', &count) < 0
		|| ft_val_and_print_char('x', &count) < 0)
	{
		return (-1);
	}
	if (address == 0)
	{
		if (ft_val_and_print_char('0', &count) < 0)
			return (-1);
		return (count);
	}
	if (ft_print_hex_ptr(addres, count) < 0)
		return (-1);
	return (count);
}
