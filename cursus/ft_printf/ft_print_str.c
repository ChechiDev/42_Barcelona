/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_str.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 18:25:48 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/05 16:19:15 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_str(va_list args)
{
	char	*str;
	size_t	len;
	ssize_t	result;

	str = va_arg(args, char *);
	if (str == NULL)
	{
		result = write(1, "(null)", 6);
		if (result < 0)
		{
			return (-1);
		}
		return (6);
	}
	len = ft_strlen(str);
	result = write(1, str, len);
	if (result < 0)
	{
		return (-1);
	}
	return ((int)len);
}
