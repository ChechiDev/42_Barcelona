/*
ft_memmove

Copia `n` bytes desde la zona de memoria apuntada por `src` a la zona
de memoria apuntada por `dest`.

A diferencia de ft_memcpy, esta función garantiza un comportamiento
correcto incluso cuando las zonas de memoria de `src` y `dest` se
solapan.

La copia se realiza:
- de izquierda a derecha si `dest` está antes que `src`,
- de derecha a izquierda si `dest` está después que `src`,
  evitando así la sobrescritura de datos aún no copiados.

Parámetros:
- dest: puntero a la zona de memoria destino.
- src:  puntero a la zona de memoria origen.
- n:    número de bytes a copiar.

Valor de retorno:
- Devuelve el puntero `dest`.

Comportamiento indefinido:
- Si `dest` o `src` son punteros inválidos.
*/

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	const unsigned char *s;
	unsigned char	*d;
	size_t	i;

	d = (unsigned char *)dest;
	s = (const unsigned char *)src;
	i = 0;

	if (d < s)
	{
		while(i < n)
		{
			d[i] = s[i];
			i++;
		}
	}
	else
	{
		while(n > 0)
		{
			d[n - 1] = s[n - 1];
			n--;
		}
	}
	return (dest);
}

int	main(int argc, char **argv)
{
	char	buffer[11];
	size_t	n;
	size_t	i;

	if (argc != 3)
	{
		printf("Use: %s <value> <num_bytes>", argv[0]);
		return (1);
	}

	n = (size_t)atoi(argv[2]);
	i = 0;
	if (n > sizeof(buffer))
	{
		n = sizeof(buffer);
	}
	printf("Antes: %s\n", argv[1]);

	ft_memmove(buffer, argv[1], n);

	while (i < n)
	{
		printf("buffer[%zu] = %c\n", i, buffer[i]);
		i++;
	}
	printf("Como string: %s\n", buffer);
	return (0);
}
