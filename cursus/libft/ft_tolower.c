/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 14:43:07 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 17:50:29 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_tolower(int c)
{
	if (c >= 'A' && c <= 'Z')
	{
		return (c + 32);
	}
	return (c);
}
/*
int	main(int argc, char **argv)
{
	int	res;

	if (argc != 2 && argv[1][0] != '\0')
	{
		printf("Use: %s <character> ", argv[0]);
		return (1);
	}
	res = ft_tolower(argv[1][0]);
	write(1, &res, 1);
	write(1, "\n", 1);
	return (0);
}
*/
