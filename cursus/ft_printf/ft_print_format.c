/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_format.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 17:16:03 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/04 13:49:31 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

int	ft_print_format(char spec, va_list args)
{
	if (!is_valid_spec(spec))
		return (0);
	if (spec == 'c')
		return (ft_print_char(args));
	if (spec == 's')
		return (ft_print_str(args));
	if (spec == 'p')
		return (ft_print_ptr(args));
	if (spec == 'i' || spec == 'd' || spec == 'u')
		return (ft_print_nbr(args, spec));
	if (spec == 'x' || spec == 'X')
		return (ft_print_hex(args, spec));
	return (0);
}
