/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 18:11:15 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 17:50:04 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strlen(const char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}
/*
int	main(int argc, char **argv)
{
	char	*str;

	if (argc != 2)
	{
		return (0);
	}
	str = argv[1];
	printf("strlen: %ld\n", strlen(str));
	printf("ft_strlen: %d\n", ft_strlen(str));
	return (0);
}
*/
