/*
ft_strrchr

Busca la última aparición del carácter 'c' en la cadena de caracteres 's'.

Recorre la cadena 's' de principio a fin y devuelve un puntero a la última
posición donde aparece el carácter 'c'.

Si el carácter 'c' es '\0', la función devuelve un puntero al carácter nulo
que marca el final de la cadena.

Si el carácter 'c' no se encuentra en la cadena, la función devuelve NULL.

El valor de 'c' se compara tras ser convertido a unsigned char.

La función no reserva memoria dinámica.
*/

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	unsigned char	uc;
	char	*last;

	uc = (unsigned char)c;
	last = NULL;
	while (*s)
	{
		if ((unsigned char)*s == uc)
		{
			last = (char *)s;
		}
		s++;
	}
	if (uc == '\0')
	{
		return ((char *)s);
	}
	return (last);
}

int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 3)
	{
		printf("Use: %s <string> <character>", argv[0]);
	}
	res = ft_strrchr(argv[1], (unsigned char)argv[2][0]);
	if (res)
	{
		printf("Result: %s\n", res);
		printf("Posicion: %ld\n", (long)(res - argv[1]));
	}
	else
	{
		printf("No encontrado\n");
	}
	return (0);
}
