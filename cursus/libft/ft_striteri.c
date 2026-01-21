/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 18:33:47 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 18:40:00 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char *))
{
	unsigned int	i;

	if (!s || !f)
	{
		return ;
	}
	i = 0;
	while (s[i])
	{
		f(i, &s[i]);
		i++;
	}
}
/*
static void	ft_iter_toupper(unsigned int i,	char *c)
{
	(void)i;
	if (!c)
	{
		return;
	}
	*c = (char)ft_toupper((unsigned int)*c);
}

int	main(int argc, char **argv)
{
	char	*res;
	
	if (argc != 2)
	{
		printf("Use: %s <string>\n", argv[0]);
		return (1);
	}
	res = ft_strdup(argv[1]);
	if (!res)
	{
		return (1);
	}
	printf("Antes: %s\n", res);
	ft_striteri(res, ft_iter_toupper);
	printf("Despues: %s\n", res);
	free(res);
	return (0);
}
*/
