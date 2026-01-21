/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:38:56 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 17:48:21 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isalnum(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	if ((uc >= 'a' && uc <= 'z')
		|| (uc >= 'A' && uc <= 'Z')
		|| (uc >= '0' && uc <= '9'))
		return (1);
	return (0);
}
/*
int	main(int argc, char **argv)
{
	int	c;

	if (argc != 2)
	{
		return (1);
	}
	c = (unsigned char)argv[1][0];
	printf("isalnum: %d\n", isalnum(c) != 0);
	printf("ft_isalnum: %d\n", ft_isalnum(c) != 0);
	return (0);
}
*/
