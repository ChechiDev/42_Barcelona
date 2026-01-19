/*
ft_memset

Rellena los primeros `len` bytes del bloque de memoria apuntado por `b`
con el valor `c`, convertido a `unsigned char`.

La función escribe byte a byte sin tener en cuenta el tipo de datos
almacenado en la memoria ni la presencia de caracteres nulos ('\0').

Parámetros:
- b: puntero al bloque de memoria que se va a modificar.
- c: valor que se copiará en cada byte (se trunca a un byte).
- len: número de bytes que se deben rellenar.

Valor de retorno:
- Devuelve el mismo puntero `b`.

Comportamiento indefinido:
- Si `b` es NULL y `len` es mayor que 0.
*/

#include "libft.h"

void	*ft_memset(void *ptr, int c, size_t n)
{
	unsigned char	*dst;
	unsigned char	uc;
	size_t		i;

	dst = (unsigned char *)ptr;
	uc = (unsigned char)c;
	i = 0;
	while (i < n)
	{
		dst[i] = uc;
		i++;
	}
	return (ptr);
}

int	main(int argc, char **argv)
{
	char buffer[50];
	int	value;
	size_t	n;
	size_t	i;

	if (argc != 3)
	{
		printf("Use: %s <value> <size>", argv[0]); 
		return (1);
	}

	value = atoi(argv[1]);
	n = (size_t)atoi(argv[2]);

	ft_memset(buffer, value, n);

	i = 0;

	while (i < n && i < sizeof(buffer))
	{
		printf("buffer[%zu] = %d\n", i, (unsigned char)buffer[i]);
		i++;
	}
	return (0);
}
