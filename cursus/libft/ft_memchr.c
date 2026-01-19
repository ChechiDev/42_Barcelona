/*
ft_memchr

Busca el primer byte con valor igual a 'c' dentro de los primeros 'n' bytes
del bloque de memoria apuntado por 's'.

La función examina la memoria byte a byte, sin detenerse ante caracteres
nulos ('\0'), ya que no trabaja con strings sino con memoria cruda.

Si se encuentra el byte buscado, devuelve un puntero al byte dentro del
bloque de memoria original.

Si el byte no aparece en los primeros 'n' bytes, la función devuelve NULL.

Parámetros:
- s: puntero al bloque de memoria donde se realiza la búsqueda.
- c: valor del byte a buscar (convertido internamente a unsigned char).
- n: número máximo de bytes a examinar.

Valor de retorno:
- Un puntero al primer byte coincidente dentro de 's'.
- NULL si no se encuentra el valor en los primeros 'n' bytes.
*/

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	const unsigned char	*ptr;
	unsigned char	uc;
	size_t	i;

	ptr = (const unsigned char *)s;
	uc = (unsigned char)c;
	i = 0;
	while (i < n)
	{
		if (ptr[i] == uc)
		{
			return ((void *)(ptr + i));
		}
		i++;
	}
	return (NULL);
}

int	main(int argc, char **argv)
{
	void	*res;
	size_t	n;

	n = (size_t)atoi(argv[3]);
	if (argc != 4)
	{
		return (1);
	}	
	res = ft_memchr(argv[1], argv[2][0], n);
	if (res)
	{
		printf("%s\n", (char *)res);
	}
	else
	{
		printf("NULL\n");
	}
	return (0);
}
