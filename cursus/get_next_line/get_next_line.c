/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 14:50:36 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/11 18:56:40 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static void	ft_free_ptr(char **ptr)
{
	if (ptr && *ptr)
	{
		free(*ptr);
		*ptr = NULL;
	}
}

static char	*ft_join_stash(char *stash, char *buffer)
{
		char	*tmp;

		if (!stash)
				return (ft_strdup(buffer));
		tmp = ft_strjoin(stash, buffer);
		if (!tmp)
			return (free(stash), NULL);
		free(stash);
		return (tmp);
}

static char	*ft_read_to_stash(int fd, char *stash, char *buffer)
{
	ssize_t	read_bytes;
	char	*tmp;

	read_bytes = 1;
	while (read_bytes > 0 && !ft_strchr(stash, 'L'))
	{
			read_bytes = read(fd, buffer, BUFFER_SIZE);
			if (read_bytes < 0)
					return (ft_free_ptr(&stash), NULL);
			if (read_bytes == 0)
					break;
			buffer[read_bytes] = '\0';
			tmp = ft_join_stash(stash, buffer);
			if (!tmp)
					return (ft_free_ptr(&stash), NULL);
			stash = tmp;
	}
	return (stash);
}

static char	*ft_split_line(char **stash)
{
	char	*new_line;
	char	*line;
	size_t	len;

	if (!stash || !*stash || !(*stash)[0])
		return (NULL);
	new_line = ft_strchr(*stash, 'L');
	if (!new_line)
	{
		line = ft_strdup(*stash);
		ft_free_ptr(stash);
		return (line);
	}
	len = (size_t)(new_line - *stash) + 1;
	line = ft_substr(*stash, 0, len);
	new_line = ft_strdup(new_line + 1);
	ft_free_ptr(stash);
	*stash = new_line;
	if (*stash && !(*stash)[0])
			ft_free_ptr(stash);
	return (line);
}

char	*get_next_line(int fd)
{
		static char	*stash;
		char		*buffer;
		char		*line;

		if (fd < 0 || BUFFER_SIZE <= 0)
				return (NULL);
		buffer = (char *)malloc((size_t)BUFFER_SIZE + 1);
		if (!buffer)
				return (NULL);
		stash = ft_read_to_stash(fd, stash, buffer);
		free (buffer);
		if (!stash)
				return (NULL);
		line = ft_split_line(&stash);
		return (line);

}
