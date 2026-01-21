/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isascii.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:16:42 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 17:48:47 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isascii(int c)
{
	if (c >= 0 && c <= 127)
	{
		return (1);
	}
	return (0);
}
/*
int	main(int argc, char **argv)
{
	int	c;

	if (argc != 2)
	{
		return (0);
	}
	c = atoi(argv[1]);
	printf("isascii: %d\n", isascii(c) != 0);
	printf("ft_isascii: %d\n", isascii(c) != 0);
	return (0);
}
*/
