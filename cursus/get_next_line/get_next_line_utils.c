/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 17:41:38 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/11 18:42:07 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *str)
{
	size_t	i;

	if (!str)
	{
		return (0);
	}
	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}

char	*ft_strjoin(const char *s1, const char *s2)
{
	char	*new;
	size_t	i;
	size_t	j;

	if (!s1 || !s2)
		return (NULL);
	new = (char *)malloc(ft_strlen(s1) + ft_strlen(s2) + 1);
	if (!new)
	{
		return (NULL);
	}
	i = 0;
	while (s1[i])
	{
		new[i] = s1[i];
		i++;
	}
	j = 0;
	while (s2[j])
	{
		new[i + j] = s2[j];
		j++;
	}
	new[i + j] = '\0';
	return (new);
}

char	*ft_strchr(const char *str, int c)
{
	unsigned char	uc;

	if (!str)
	{
		return (NULL);
	}
	uc = (unsigned char)c;
	while (*str)
	{
		if (*str == uc)
		{
			return ((char *)str);
		}
		str++;
	}
	if (uc == '\0')
	{
		return ((char *)str);
	}
	return (NULL);
}

char	*ft_strdup(const char *str)
{
	char	*dup;
	size_t	i;

	if (!str)
	{
		return (NULL);
	}
	dup = (char *)malloc((ft_strlen(str) + 1) * sizeof(char));
	if (!dup)
	{
		return (NULL);
	}
	i = 0;
	while (str[i])
	{
		dup[i] = str[i];
		i++;
	}
	dup[i] = '\0';
	return (dup);
}

char	*ft_substr(char const *str, unsigned int start, size_t len)
{
	char	*sub;
	size_t	i;
	size_t	str_len;

	if (!str)
		return (NULL);
	str_len = ft_strlen(str);
	if (start >= str_len)
		len = 0;
	else if (len > str_len - start)
		len = str_len - start;
	sub = (char *)malloc(sizeof(char) * (len + 1));
	if (!sub)
	{
		return (NULL);
	}
	i = 0;
	while (i < len)
	{
		sub[i] = str[start + i];
		i++;
	}
	sub[i] = '\0';
	return (sub);
}
