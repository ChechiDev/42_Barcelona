/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_char.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 16:45:12 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/29 17:34:40 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

int	ft_print_char(va_list args)
{
	char	c;
	int		print;

	c = (char)va_arg(args, int);
	print = ft_putchar_fd(c, 1);
	if (print < 0)
	{
		return (-1);
	}
	return (1);
}
