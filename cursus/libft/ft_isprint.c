/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isprint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 12:47:15 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 17:49:28 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isprint(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	if (uc >= 32 && uc <= 126)
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
	c = (unsigned char)argv[1][0];
	printf("isprint: %d\n", isprint(c) != 0);
	printf("ft_isprint: %d\n", ft_isprint(c) != 0);
	return (0);
}
*/
