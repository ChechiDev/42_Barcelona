/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libftprintf.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/23 14:21:23 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/30 12:29:36 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFTPRINTF_H
# define LIBFTPRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
# include <stddef.h>

int	ft_printf(const char *format, ...);
int	ft_print_format(char spec, va_list args);
int	ft_print_char(va_list args);
int	ft_print_str(const char *str);
int	ft_print_ptr(va_list args);

//UTILS:
int	ft_putchar_fd(const char c, int fd);
int	is_valid_spec(char spec);
size_t	ft_strlen(const char *str);

#endif
