/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 18:35:34 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 16:40:54 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isalpha(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	if ((uc >= 'A' && uc <= 'Z') || (uc >= 'a' && uc <= 'z'))
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
	printf("isalpha: %d\n", isalpha(c) != 0);
	printf("ft_isalpha: %d\n", ft_isalpha(c) != 0);
	return (0);
}
*/
