/*
ft_strchr

Busca la primera aparición del carácter 'c' en la cadena 's'.

Parámetros:
- s: puntero a una cadena de caracteres terminada en '\0'.
- c: carácter a buscar (se interpreta como unsigned char).

Retorno:
- Devuelve un puntero a la primera ocurrencia de 'c' en 's'.
- Si 'c' es '\0', devuelve un puntero al terminador nulo de la cadena.
- Si el carácter no se encuentra, devuelve NULL.

Notas:
- La cadena 's' no se modifica.
- El recorrido se realiza de izquierda a derecha.
*/

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	while (*s)
	{
		if (*s == uc)
		{
			return ((char *)s);
		}
		s++;	
	}
	if (uc == '\0')
	{
		return ((char *)s);
	}
	return (NULL);
}

int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 3)
	{
		printf("Use: %s <string> <character>", argv[0]);
		return (1);
	}
	res = ft_strchr(argv[1], argv[2][0]);
	if (res)
	{
		printf("Result: %s\n", res);
	}
	else
	{
		printf("No encontrado");
	}
	return (0);
}
