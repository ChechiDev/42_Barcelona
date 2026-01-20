/*
ft_putendl_fd

Escribe la cadena de caracteres 's' en el descriptor de archivo 'fd',
seguida de un salto de línea ('\n').

Si 's' es NULL, la función no realiza ninguna acción.

Parámetros:
- s: cadena a escribir.
- fd: descriptor de archivo destino.

Valor devuelto:
- Ninguno.

Funciones autorizadas:
- write
*/

#include "libft.h"

void	ft_putendl_fd(char *s, int fd)
{
	size_t	i;

	if (!s)
	{
		return;
	}
	i = 0;
	while (s[i])
	{
		write(fd, &s[i], 1);
		i++;
	}
	write(fd, "\n", 1);
}
