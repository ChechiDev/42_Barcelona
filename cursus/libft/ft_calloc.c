/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sperez-l <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/09 12:22:31 by sperez-l          #+#    #+#             */
/*   Updated: 2026/01/22 13:17:30 by sperez-l         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	char	*ptr;
	size_t	res;
	size_t	i;

	if (size != 0 && nmemb > (size_t)(-1) / size)
	{
		return (NULL);
	}
	res = nmemb * size;
	ptr = (char *)malloc(res);
	if (!ptr)
	{
		return (NULL);
	}
	i = 0;
	while (i < res)
	{
		ptr[i] = 0;
		i++;
	}
	return (ptr);
}
/*
int	main(int argc, char **argv)
{
	int	*arr;
	size_t nmemb;
	size_t size;
	size_t i;

	if (argc != 3)
	{
		printf("Use: %s <nmemb> <size> \n", argv[0]);
		return (1);
	}
	nmemb = (size_t)ft_atoi(argv[1]);
	size = (size_t)ft_atoi(argv[2]);
	arr = (int *)ft_calloc(nmemb, size);
	if (!arr)
	{
		printf("Error\n");
		return (1);
	}
	i = 0;
	while (i < nmemb && size == sizeof(int))
	{
		printf("arr[%zu] = %d\n", i, arr[i]);
		i++;
	}
	free(arr);
	return(0);
}
*/
