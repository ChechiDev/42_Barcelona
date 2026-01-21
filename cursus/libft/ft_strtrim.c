/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/14 18:38:06 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 17:58:19 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	start;
	size_t	end;

	if (s1 == NULL || set == NULL)
	{
		return (NULL);
	}
	if (set[0] == '\0')
	{
		return (ft_strdup(s1));
	}
	start = 0;
	end = ft_strlen(s1);
	while (start < end && ft_strchr(set, s1[start]))
	{
		start++;
	}
	while (end > start && ft_strchr(set, s1[end - 1]))
	{
		end--;
	}
	return (ft_substr(s1, (unsigned int)start, end - start));
}
/*
int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 3)
	{
		printf("Use: %s <string> <set>\n", argv[0]);
		return (1);
	}
	res = ft_strtrim(argv[1], argv[2]);
	if (!res)
	{
		printf("Error");
		return (1);
	}
	printf("Result: %s\n", res);
	free(res);
	return (0);
}
*/
