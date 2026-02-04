/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_utils.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 18:33:05 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/04 17:56:46 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

const char	*ft_hex_base(char spec)
{
	if (spec == 'X')
	{
		return ("0123456789ABCDEF");
	}
	return ("0123456789abcdef");
}

int	ft_put_hex(unsigned int n, const char *base)
{
	int	count;
	int	res;

	count = 0;
	if (n >= 16)
	{
		res = ft_put_hex(n / 16, base);
		if (res < 0)
		{
			return (-1);
		}
		count += res;
	}
	res = write(1, &base[n % 16], 1);
	if (res < 0)
	{
		return (-1);
	}
	return (count + 1);
}

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
