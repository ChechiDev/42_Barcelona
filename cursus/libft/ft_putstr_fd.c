/*
Envía la cadena de caracteres 's' al descriptor de archivo 'fd'.
Si 's' es NULL, la función no realiza ninguna acción.
No añade salto de línea.
*/

#include "libft.h"

void	ft_putstr_fd(char *s, int fd)
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
}
