/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_utils.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 18:33:05 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/30 12:28:25 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

int	is_valid_spec(char spec)
{
	char	*valid;
	int		i;

	valid = "cspdiuxX%";
	i = 0;
	while (valid[i])
	{
		if (valid[i] == spec)
		{
			return (1);
		}
		i++;
	}
	return (0);
}

int	ft_putchar_fd(const char c, int fd)
{
	return (write(fd, &c, 1));
}

size_t	ft_strlen(const char *str)
{
	size_t	i;

	i = 0;
	if (!str)
	{
		return (0);
	}
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}
