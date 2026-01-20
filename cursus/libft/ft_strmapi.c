/*
ft_strmapi

Aplica la función 'f' a cada carácter de la cadena 's', pasando como
primer argumento el índice del carácter dentro de la cadena y como
segundo argumento el propio carácter.

La función crea una nueva cadena, reservando memoria dinámica, en la
que se almacenan los resultados de aplicar 'f' a cada carácter de 's'.

La cadena original 's' no se modifica.

Devuelve un puntero a la nueva cadena resultante.
Devuelve NULL si la reserva de memoria falla.
*/

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	i;
	char	*res;

	if (!s || !f)
	{
		return (NULL);
	}
	res = malloc(ft_strlen(s) + 1);
	if (!res)
	{
		return (NULL);
	}
	i = 0;
	while (s[i])
	{
		res[i] = f(i, s[i]);
		i++;
	}
	res[i] = '\0';
	return (res);
}
/*
static char	ft_map_toupper(unsigned int i, char c)
{
	(void)i;
	return ((char)ft_toupper((int)c));
}

int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 2)
	{
		printf("Use: %s <string>\n", argv[0]);
		return (1);
	}
	res = ft_strmapi(argv[1], ft_map_toupper);
	if (!res)
	{
		printf("Error Malloc");
		return (1);
	}
	printf("%s\n", res);
	free(res);
	return (0);
}
*/
