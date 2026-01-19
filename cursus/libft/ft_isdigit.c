/*
ft_isdigit

Comprueba si el carácter pasado como argumento es un dígito decimal.

La función recibe un entero que representa un carácter (normalmente un
char promovido a int) y verifica si su valor ASCII se encuentra dentro
del rango correspondiente a los caracteres '0' a '9'.

Valor de retorno:
- Devuelve 1 si el carácter es un dígito ('0'–'9').
- Devuelve 0 en cualquier otro caso.

Esta función no realiza ninguna conversión numérica, únicamente compara
valores de caracteres según la tabla ASCII.
*/

#include "libft.h"

int	ft_isdigit(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	if (uc >= '0' && uc <= '9')
	{
		return (1);
	}
	return (0);
}

int	main(int argc, char **argv)
{
	char	c;
	
	if (argc != 2)
	{
		return (1);
	}
	c = (unsigned char)argv[1][0];
	printf("isdigit: %d\n", isdigit(c) != 0);
	printf("ft_isdigit: %d\n", ft_isdigit(c) != 0);
	return (0);
}
