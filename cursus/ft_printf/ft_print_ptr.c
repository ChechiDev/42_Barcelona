/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_ptr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/30 10:25:23 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/05 16:19:02 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_ptr(va_list args)
{
	void			*ptr;
	unsigned long	address;
	ssize_t			w;
	int				res;

	ptr = va_arg(args, void *);
	if (ptr == NULL)
	{
		w = write(1, "(nil)", 5);
		if (w < 0)
			return (-1);
		return (5);
	}
	w = write(1, "0x", 2);
	if (w < 0)
	{
		return (-1);
	}
	address = (unsigned long)ptr;
	res = ft_put_hex(address, ft_hex_base('x'));
	if (res < 0)
	{
		return (-1);
	}
	return (2 + res);
}
