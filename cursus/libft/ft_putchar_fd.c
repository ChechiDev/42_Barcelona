/*
ft_putchar_fd

Envía el carácter 'c' al descriptor de archivo especificado por 'fd'.

Escribe exactamente un byte en el file descriptor dado utilizando la
función write(). No realiza ninguna gestión de errores ni validación
del descriptor; se asume que 'fd' es válido según el contrato de la
función.

Parámetros:
- c: carácter a escribir.
- fd: descriptor de archivo sobre el que se escribe.

Valor de retorno:
- Ninguno.
*/

#include "libft.h"

void	ft_putchar_fd(char c, int fd)
{
	write(fd, &c, 1);
}
