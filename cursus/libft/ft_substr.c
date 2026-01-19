/*
ft_substr

Reserva memoria dinámica y devuelve una nueva cadena que es una subcadena
de la cadena original `s`.

La subcadena comienza en el índice `start` de `s` y tiene como longitud
máxima `len` caracteres.

Si `start` es mayor o igual que la longitud de `s`, la función devuelve
una cadena vacía.

Parámetros:
- s: cadena original desde la que se extrae la subcadena.
- start: índice inicial dentro de `s`.
- len: longitud máxima de la subcadena.

Retorno:
- Un puntero a la nueva subcadena terminada en '\0'.
- NULL si falla la reserva de memoria.

Notas:
- La cadena devuelta debe liberarse con free().
- No modifica la cadena original.
*/

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*ptr;
	size_t	i;
	size_t	len_s;

	if(!s)
	{
		return (NULL);
	}
	len_s = ft_strlen(s);
	if (start >= len_s)
	{
		len = 0;
	}
	else if (len > len_s - start)
	{
		len = len_s - start;
	}
	ptr = malloc(sizeof(char) * (len + 1));
	if (!ptr)
	{
		return (NULL);
	}
	i = 0;
	while (i < len)
	{
		ptr[i] = s[start + i];
		i++;
	}
	ptr[i] = '\0';
	return (ptr);
}

int	main(int argc, char **argv)
{
	char	*res;
	size_t	len;
	unsigned int	start;

	if (argc != 4)
	{
		printf("Use: %s <string> <start> <len> \n", argv[0]);
		return (1);
	}
	start = (unsigned int)ft_atoi(argv[2]);
	len = (size_t)ft_atoi(argv[3]);
	res = ft_substr(argv[1], start, len);
	if (!res)
	{
		printf("Error malloc o algo = NULL\n");
		return (1);
	}
	printf("Resultado: %s\n", res);
	free(res);
	return (0);
}
