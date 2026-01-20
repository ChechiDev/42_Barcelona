/*
ft_strtrim

Reserva memoria y devuelve una nueva cadena que resulta de eliminar
todos los caracteres presentes en `set` tanto al inicio como al final
de la cadena `s1`.

El recorte se realiza únicamente en los extremos de la cadena; los
caracteres intermedios, aunque pertenezcan a `set`, no se eliminan.

Parámetros:
- s1: cadena original que se desea recortar.
- set: conjunto de caracteres a eliminar en los extremos de `s1`.

Valor de retorno:
- Un puntero a la nueva cadena recortada.
- NULL si falla la reserva de memoria.

Notas:
- La cadena devuelta está terminada en '\0'.
- El llamador es responsable de liberar la memoria devuelta.
*/

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	start;
	size_t	end;

	if (s1 == NULL || set == NULL)
	{
		return (NULL);
	}
	if (set[0] == '\0')
	{
		return ft_strdup(s1);
	}
	start = 0;
	end = ft_strlen(s1);
	while (start < end && ft_strchr(set, s1[start]))
	{
		start++;
	}
	while (end > start && ft_strchr(set, s1[end - 1]))
	{
		end--;
	}
	return (ft_substr(s1, (unsigned int)start, end - start));
}
/*
int	main(int argc, char **argv)
{
	char	*res;

	if (argc != 3)
	{
		printf("Use: %s <string> <set>\n", argv[0]);
		return (1);
	}
	res = ft_strtrim(argv[1], argv[2]);
	if (!res)
	{
		printf("Error");
		return (1);
	}
	printf("Result: %s\n", res);
	free(res);
	return (0);
}
*/
