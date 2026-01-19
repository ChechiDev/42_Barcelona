/*
ft_strjoin

Contrato:
Reserva memoria dinámica y devuelve una nueva cadena de caracteres
resultante de la concatenación de las cadenas `s1` y `s2`.

- La nueva cadena contiene primero el contenido de `s1` y a continuación
  el contenido de `s2`, en el mismo orden.
- La cadena devuelta termina siempre en carácter nulo (`'\0'`).
- Si `s1` o `s2` son NULL, el comportamiento es indefinido
  (en libft se suele devolver NULL de forma defensiva).
- Si la reserva de memoria falla, la función devuelve NULL.

La memoria devuelta debe ser liberada por el llamador.
*/

#include "libft.h"

static void	ft_copy_to(char *dst, const char *src, size_t offset)
{
	size_t	i;

	i = 0;
	while (src[i])
	{
		dst[offset + i] = src[i];
		i++;
	}
}

char	*ft_strjoin(const char *s1, const char *s2)
{
	char	*res;
	size_t	s1_len;
	size_t	s2_len;

	if (s1 == NULL || s2 == NULL)
	{
		return (NULL);
	}
	s1_len = (size_t)ft_strlen(s1);
	s2_len = (size_t)ft_strlen(s2);
	res = (char *)malloc(s1_len + s2_len + 1);
	if (!res)
	{
		return (NULL);
	}
	ft_copy_to(res, s1, 0);
	ft_copy_to(res, s2, s1_len);
	res[s1_len + s2_len] = '\0';
	return (res);
}

int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 3)
	{
		printf("Use: %s <string1> <string2> \n", argv[0]);
		return (1);
	}
	res = ft_strjoin(argv[1], argv[2]);
	if (!res)
	{
		return (1);
	}
	printf("Result; %s\n", res);
	free(res);
	return (0);
}
