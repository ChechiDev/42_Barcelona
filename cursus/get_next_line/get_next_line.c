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

static void	ft_free_stash(char **stash)
{
	if (stash && *stash)
	{
		free (*stash);
		*stash == NULL;
	}
}

static void	ft_free_buffer(char **buffer)
{
	if (buffer && *buffer)
	{
		free (*buffer);
		*buffer == NULL;
	}
}

char *get_next_line(int fd)
{
	static char	*stash;
	char		*buffer;
	ssize_t		bytes_read;

	if (fd < 0 || BUFFER_SIZE <= 0)
	{
		return (NULL); 
	}
	buffer = (char *)malloc(((size_t)BUFFER_SIZE + 1));
	if (!buffer)
	{
		return (NULL);
	}
	bytes_read = 1;
	while ()
	{
	}










	return (0);
}
