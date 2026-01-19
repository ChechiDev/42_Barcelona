/*
ft_tolower

Convierte una letra mayúscula ASCII en su equivalente en minúscula.

Si el carácter recibido corresponde a una letra entre 'A' y 'Z',
la función devuelve el mismo carácter convertido a minúscula.

Si el carácter no es una letra mayúscula, se devuelve sin modificar.

La función no realiza ninguna asignación de memoria y trabaja
exclusivamente con valores ASCII.

Parámetro:
- c: carácter a evaluar, representado como int.

Valor de retorno:
- El carácter convertido a minúscula si procede, o el mismo valor
  de entrada si no se cumple la condición.
*/

#include "libft.h"

int	ft_tolower(int c)
{
	if (c >= 'A' && c <= 'Z')
	{
		return (c + 32);
	}
	return (c);
}

int	main(int argc, char **argv)
{
	int	res;

	if (argc != 2 && argv[1][0] != '\0')
	{
		printf("Use: %s <character> ", argv[0]);
		return (1);
	}
	res = ft_tolower(argv[1][0]);
	write(1, &res, 1);
	write(1, "\n", 1);
	return (0);
}
