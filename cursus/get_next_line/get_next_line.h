/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 13:16:17 by sperez-l          #+#    #+#             */
/*   Updated: 2026/02/11 18:37:31 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <unistd.h>
# include <stdlib.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif

char 	*get_next_line(int fd);

/* Utils */
void	ft_free_stash(char **stash);
void	ft_free_buffer(char **buffer);
size_t	ft_strlen(const char *stash);
char	*ft_strjoin(const char *s1, const char *s2);
char	*ft_strchr(const char *stash, int c);
char	*ft_strdup(const char stash);

#endif
