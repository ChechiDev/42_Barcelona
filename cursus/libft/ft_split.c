/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 17:59:33 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/21 18:41:31 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_word_count(const char *s, char c)
{
	size_t	i;
	size_t	count;
	size_t	in_word;

	i = 0;
	count = 0;
	in_word = 0;
	while (s[i])
	{
		if (s[i] != c && in_word == 0)
		{
			count++;
			in_word = 1;
		}
		else if (s[i] == c)
		{
			in_word = 0;
		}
		i++;
	}
	return (count);
}

char	**ft_split(char const *s, char c)
{
	char	**arr;
	size_t	word;
	size_t	i;

	arr = (char **)malloc((ft_word_count(s, c) + 1) * sizeof(char *));
	if (!s || !arr)
		return (NULL);
	i = 0;
	while (*s)
	{
		while (*s == c && *s)
			s++;
		if (*s)
		{
			if (!ft_strchr(s, c))
				word = ft_strlen(s);
			else
				word = ft_strchr(s, c) - s;
			arr[i++] = ft_substr(s, 0, word);
			s = s + word;
		}
	}
	arr[i] = NULL;
	return (arr);
}
/*
int	main(int argc, char **argv)
{
	char	**res;
	int	i;

	i = 0;
	if (argc != 3)
	{
		return (1);
	}
	res = ft_split(argv[1], argv[2][0]);
	if (!res)
	{
		printf("Error");
		return (1);
	}
	while (res[i])
	{
		printf("%s\n", res[i]);
		free(res[i]);
		i++;
	}
	free(res);
	return (0);
}
*/
