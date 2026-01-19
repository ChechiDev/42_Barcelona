/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isdigit.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 11:12:40 by sperez-l          #+#    #+#             */
/*   Updated: 2025/12/23 14:08:41 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
/*
#include "libft.h"
#include <stdio.h>
#include <ctype.h>
*/
int	ft_isdigit(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	if (uc >= '0' && uc <= '9')
	{
		return (1);
	}
	return (0);
}
/*
int	main(int argc, char **argv)
{
	char	c;
	
	if (argc != 2)
	{
		return (1);
	}
	c = (unsigned char)argv[1][0];
	printf("isdigit: %d\n", isdigit(c) != 0);
	printf("ft_isdigit: %d\n", ft_isdigit(c) != 0);
	return (0);
}
*/
