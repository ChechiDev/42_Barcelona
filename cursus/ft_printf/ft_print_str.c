/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_str.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 18:25:48 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/30 12:27:02 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

int	ft_print_str(const char *str)
{
	int		len;
	ssize_t	result;

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
	return (len);
}
