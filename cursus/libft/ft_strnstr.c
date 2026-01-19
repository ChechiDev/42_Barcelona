/*
ft_strnstr

Busca la primera aparición de la cadena `needle` dentro de la cadena `haystack`,
pero examinando como máximo `len` caracteres de `haystack`.

La búsqueda se detiene cuando:
- Se encuentra `needle` completamente.
- Se han comparado `len` caracteres de `haystack`.
- Se alcanza el carácter nulo '\0' de `haystack`.

Si `needle` es una cadena vacía, la función devuelve `haystack`.

Valor de retorno:
- Un puntero al comienzo de la primera ocurrencia de `needle` en `haystack`,
  dentro del límite `len`.
- NULL si `needle` no se encuentra en ese rango.

No modifica las cadenas de entrada.
*/

#include "libft.h"

char	*ft_strnstr(const char *big, const char *small, size_t n)
{
	size_t	i;
	size_t	j;

	if (*small == '\0')
	{
		return ((char *)big);
	}
	i = 0;
	while (big[i] && i < n)
	{
		j = 0;
		while (small[j] && (i + j) < n && big[i + j] && big[i + j] == small[j])
		{
			j++;
		}
		if (small[j] == '\0')
		{
			return ((char *)(big + i));
		}
		i++;
	}
	return (NULL);
}

int	main(int argc, char **argv)
{
	char	*res;
	size_t	n;

	if (argc != 4)
	{
		printf("Use: %s <big_str> <small_str> <n>\n", argv[0]);
		return (1);
	}
	n = (size_t)atoi(&argv[3][0]);
	res = ft_strnstr(argv[1], argv[2], n);
	if (res)
	{
		printf("Result: %s\n", res);
	}
	else
	{
		printf("NULL\n");
	}
	return (0);
}
