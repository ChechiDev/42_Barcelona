/*
ft_isalnum

Comprueba si el carácter recibido como argumento es alfanumérico.

Un carácter se considera alfanumérico si es:
- Una letra mayúscula (A–Z)
- Una letra minúscula (a–z)
- Un dígito (0–9)

Parámetro:
- c: el carácter a comprobar, representado como un int.

Valor de retorno:
- 1 si el carácter es alfanumérico.
- 0 si el carácter no es alfanumérico.

Esta función reproduce el comportamiento de isalnum() de la libc,
adaptado a los requisitos del proyecto libft.
*/

#include "libft.h"

int	ft_isalnum(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	if ((uc >= 'a' && uc <= 'z')
		|| (uc >= 'A' && uc <= 'Z')
		|| (uc >= '0' && uc <= '9'))
		return (1);
	return (0);
}

int	main(int argc, char **argv)
{
	int	c;

	if (argc != 2)
	{
		return (1);
	}
	c = (unsigned char)argv[1][0];
	printf("isalnum: %d\n", isalnum(c) != 0);
	printf("ft_isalnum: %d\n", ft_isalnum(c) != 0);
	return (0);
}
