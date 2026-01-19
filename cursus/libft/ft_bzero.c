/*
ft_bzero

Descripción:
Pone a cero (valor 0) los primeros `n` bytes del bloque de memoria
apuntado por `s`.

Parámetros:
- s: puntero al bloque de memoria que se va a inicializar.
- n: número de bytes a poner a cero.

Comportamiento:
- Si `n` es mayor que 0, todos los bytes desde `s[0]` hasta `s[n - 1]`
  se establecen a 0.
- Si `n` es 0, la función no realiza ninguna operación.

Valor de retorno:
- Ninguno.

Nota:
Esta función es equivalente a llamar a ft_memset(s, 0, n).
*/

#include "libft.h"

void	ft_bzero(void *ptr, size_t n)
{
	unsigned char *dst;
	size_t	i;

	dst = (unsigned char *)ptr;
	i = 0;
	while (i < n)
	{
		dst[i] = '\0';
		i++;
	}
}

int	main(int argc, char **argv)
{
	unsigned char	buffer[50];
	size_t	n;
	size_t	i;

	if (argc != 2)
	{
		printf("Use: %s <value_bytes> ", argv[0]);
		return (1);
	}

	n = (size_t)atoi(argv[1]);
	i = 0;

	if (n > sizeof(buffer))
	{
		n = sizeof(buffer);
	}

	ft_bzero(buffer, n);
	
	while (i < n)
	{
		printf("buffer[%zu] = %d\n", i, buffer[i]);
		i++;
	}
	return (0);

