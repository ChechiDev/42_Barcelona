/*
ft_strdup

Contrato:
Reserva memoria suficiente para crear una copia exacta de la cadena
terminada en '\0' apuntada por `s`.
Copia carácter a carácter el contenido de `s` en la nueva zona de memoria
y añade el terminador nulo al final.

Parámetros:
- s: puntero a una cadena válida terminada en '\0'.

Valor de retorno:
- Un puntero a la nueva cadena duplicada.
- NULL si la reserva de memoria falla.

Notas:
- La memoria devuelta debe liberarse con `free()`.
- El comportamiento es indefinido si `s` es NULL.
*/

#include "libft.h"

char	*ft_strdup(const char *s)
{
	size_t	i;
	char	*new;

	if (!s)
	{
		return (NULL);
	}
	i = 0;
	new = (char *)malloc(sizeof(char) * ft_strlen((char *)s) + 1);
	if (!new)
	{
		return (NULL);
	}
	while (*s)
	{
		new[i++] = *s++;
	}
	new[i] = '\0';
	return (new);
}

int	main(int argc, char **argv)
{
	char	*copy;
	if (argc != 2)
	{
		printf("Use: %s <string> ", argv[0]);
		return (1);
	}
	copy = ft_strdup(argv[1]);
	if (!copy)
	{
		printf("Malloc failed");
		return (1);
	}
	printf("Original: %s\n", argv[1]);
	printf("ft_strdup: %s\n", copy);
	free(copy);
	return (0);
}
