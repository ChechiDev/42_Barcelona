/*
ft_isprint

Comprueba si el carácter pasado como argumento es un carácter imprimible
según la tabla ASCII.

Un carácter se considera imprimible si su valor ASCII está comprendido
entre 32 (espacio) y 126 (~), ambos inclusive.

Parámetro:
- c: carácter a comprobar, pasado como int.

Valor de retorno:
- 1 si el carácter es imprimible.
- 0 si el carácter no es imprimible.
*/

#include "libft.h"

int	ft_isprint(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	if (uc >= 32 && uc <= 126)
	{
		return (1);
	}
	return (0);
}

int	main(int argc, char **argv)
{
	int	c;
	
	if (argc != 2)
	{
		return (0);
	}
	c = (unsigned char)argv[1][0];
	printf("isprint: %d\n", isprint(c) != 0);
	printf("ft_isprint: %d\n", ft_isprint(c) != 0);
	return (0);
}
