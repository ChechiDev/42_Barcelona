/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_format.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 17:16:03 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/30 11:24:59 by sperez-l         ###   ########.fr       */
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
		return (ft_print_str(va_arg(args, char *)));
	if (spec == 'p')
		return (ft_print_ptr(args));
	return (0);
}
