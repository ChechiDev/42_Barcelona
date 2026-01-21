/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 17:53:07 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 17:52:05 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*ptr;
	size_t	i;
	size_t	len_s;

	if (!s)
		return (NULL);
	len_s = ft_strlen(s);
	if (start >= len_s)
		len = 0;
	else if (len > len_s - start)
		len = len_s - start;
	ptr = malloc(sizeof(char) * (len + 1));
	if (!ptr)
		return (NULL);
	i = 0;
	while (i < len)
	{
		ptr[i] = s[start + i];
		i++;
	}
	ptr[i] = '\0';
	return (ptr);
}
/*
int	main(int argc, char **argv)
{
	char			*res;
	size_t			len;
	unsigned int	start;

	if (argc != 4)
	{
		printf("Use: %s <string> <start> <len> \n", argv[0]);
		return (1);
	}
	start = (unsigned int)ft_atoi(argv[2]);
	len = (size_t)ft_atoi(argv[3]);
	res = ft_substr(argv[1], start, len);
	if (!res)
	{
		printf("Error malloc o algo = NULL\n");
		return (1);
	}
	printf("Resultado: %s\n", res);
	free(res);
	return (0);
}
*/
