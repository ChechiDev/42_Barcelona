/*
ft_strlcpy

Copia una cadena de caracteres desde `src` hacia `dst` garantizando
la correcta terminación en null ('\0') siempre que `dstsize` sea mayor
que 0.

La función copia como máximo `dstsize - 1` caracteres desde `src` a
`dst` y añade el carácter nulo al final del buffer destino.

No realiza ninguna reserva de memoria: `dst` debe apuntar a un buffer
válido con un tamaño de al menos `dstsize` bytes.

Valor de retorno:
Devuelve la longitud total de la cadena `src`. Este valor permite
detectar si la copia ha sido truncada comparándolo con `dstsize`.

Comportamiento especial:
- Si `dstsize` es 0, no se copia ningún carácter y `dst` no se modifica.
- Si el valor devuelto es mayor o igual que `dstsize`, la copia ha sido truncada.
*/

#include "libft.h"

size_t	ft_strlcpy(char	*dst, const char *src, size_t n)
{
	size_t	i;
	size_t	src_len;

	src_len = 0;
	while(src[src_len])
	{
		src_len++;
	}
	if (n == 0)
	{
		return (src_len);
	}
	i = 0;
	while(i + 1 < n && src[i])
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (src_len);
}

int	main(int argc, char **argv)
{
	char	buffer[20];
	size_t	n;
	size_t	result;

	if (argc != 3)
	{
		printf("Use: %s <string> <length>", argv[0]);	
		return (1);
	}
	n = (size_t)atoi(argv[2]);
	result = ft_strlcpy(buffer, argv[1], n);

	printf("dst: %s\n", buffer);
	printf("result: %zu\n", result);
	if (result >= n)
	{
		printf("Truncado");
	}
	return (0);
}
