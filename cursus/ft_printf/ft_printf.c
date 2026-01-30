/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/26 18:51:14 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/29 17:51:29 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

static int	ft_handle_format(const char *format, size_t *i, va_list args)
{
	size_t	spec_index;
	char	spec;
	int		print;

	spec_index = *i + 1;
	spec = format[spec_index];
	if (spec == '\0')
	{
		return (-1);
	}
	print = ft_print_format(spec, args);
	*i = spec_index;
	return (print);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	size_t	i;
	int		count;
	int		print;

	if (!format)
		return (0);
	va_start(args, format);
	i = 0;
	count = 0;
	while (format[i])
	{
		if (format[i] == '%')
			print = ft_handle_format(format, &i, args);
		else
			print = ft_putchar_fd(format[i], 1);
		if (print < 0)
			return (va_end(args), -1);
		count += print;
		i++;
	}
	va_end(args);
	return (count);
}
