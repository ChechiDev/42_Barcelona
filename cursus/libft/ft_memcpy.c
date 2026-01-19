/*
t_memcpy

Description:
Copia exactamente n bytes desde el área de memoria apuntada por src
al área de memoria apuntada por dst.

Parameters:
dst  -> puntero al bloque de memoria de destino
src  -> puntero al bloque de memoria de origen
n    -> número de bytes a copiar

Return value:
Devuelve el puntero dst.

Notes:
- El contenido copiado no se interpreta como caracteres ni como strings.
- La copia se realiza byte a byte.
- El comportamiento es indefinido si las áreas de memoria se solapan.
- Para memoria solapada debe utilizarse ft_memmove.
*/
#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*d;
	const unsigned char	*s;
	size_t	i;

	d = (unsigned char *)dest;
	s = (const unsigned char *)src;
	i = 0;
	while (i < n)
	{
		d[i] = s[i];
		i++;
	}
	return (dest);
}

int	main(int argc, char **argv)
{
	char	buffer[50];	
	size_t	n;
	size_t	i;

	if (argc != 3)
	{
		printf("Use: %s <value> <size>", argv[0]);
		return (1);
	}

	n = (size_t)atoi(argv[2]);
	if (n > sizeof(buffer))
	{
		n = sizeof(buffer);
	}

	ft_memcpy(buffer, argv[1], n);

	i = 0;
	while (i < n)
	{
		printf("Buffer[%zu] = %d\n", i, (unsigned char)buffer[i]);
		i++;
	}
	printf("Resultado Buffer: %s\n", buffer);
	return (0);

}
