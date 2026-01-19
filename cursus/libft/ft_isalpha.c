/*
 ft_isalpha

 Descripción:
 Comprueba si el carácter pasado como argumento es un carácter alfabético
 según la tabla ASCII.

 Se consideran caracteres alfabéticos:
 - Letras mayúsculas: 'A' a 'Z'
 - Letras minúsculas: 'a' a 'z'

 Parámetros:
 - c: entero que representa un carácter (normalmente un unsigned char
   convertido a int).

 Valor de retorno:
 - Devuelve 1 si el carácter es alfabético.
 - Devuelve 0 si el carácter no es alfabético.

 Notas:
 - No reconoce caracteres acentuados ni Unicode.
 - El comportamiento replica el de la función isalpha de la libc.
*/

#include "libft.h"

int	ft_isalpha(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	if ((uc >= 'A' && uc <= 'Z') || (uc >= 'a' && uc <= 'z'))
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
	printf("isalpha: %d\n", isalpha(c) != 0);
	printf("ft_isalpha: %d\n", ft_isalpha(c) != 0);
	return (0);
}
