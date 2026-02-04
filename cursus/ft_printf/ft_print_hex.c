/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_hex.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/04 13:50:07 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/04 16:58:41 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

int	ft_print_hex(va_list args, char spec)
{
	unsigned int	n;
	const char		*base;

	n = va_arg(args, unsigned int);
	base = ft_hex_base(spec);
	return (ft_put_hex((unsigned long)n, base));
}
