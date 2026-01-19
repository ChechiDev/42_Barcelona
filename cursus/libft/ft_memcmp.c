/*
ft_memcmp

Compara los primeros `n` bytes de las áreas de memoria apuntadas por `s1` y `s2`.
La comparación se realiza byte a byte, interpretando cada byte como `unsigned char`.

Devuelve:
 - Un valor menor que 0 si el primer byte distinto en `s1` es menor que el de `s2`.
 - Un valor mayor que 0 si el primer byte distinto en `s1` es mayor que el de `s2`.
 - 0 si los primeros `n` bytes de ambas áreas de memoria son idénticos.

Si `n` es 0, la función devuelve 0.

El comportamiento es indefinido si las áreas de memoria no son válidas
para al menos `n` bytes.
*/

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	const unsigned char	*uc1;
	const unsigned char	*uc2;
	size_t	i;

	uc1 = (const unsigned char *)s1;
	uc2 = (const unsigned char *)s2;
	i = 0;
	while (i < n)
	{
		if (uc1[i] != uc2[i])
		{
			return (uc1[i] - uc2[2]);
		}
		i++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	size_t	n;
	int	res;
	
	if (argc != 4)
	{
		printf("Use: %s <str1> <str2> <n>", argv[0]);
		return (1);
	}
	n = (size_t)atoi(&argv[3][0]);
	res = ft_memcmp(argv[1], argv[2], n);
	printf("result: %d\n", res);
	return (0);
}
