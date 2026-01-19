/*
ft_atoi

Convierte una cadena de caracteres en un entero de tipo int.

La función ignora los espacios en blanco iniciales (según isspace),
reconoce un signo opcional ('+' o '-'), y procesa los caracteres
numéricos consecutivos para construir el valor entero resultante.

La conversión se detiene en el primer carácter no numérico.

Si la cadena no contiene una secuencia válida de dígitos tras los
espacios y el signo opcional, el resultado es 0.

El comportamiento en caso de desbordamiento o subdesbordamiento
está indefinido, igual que en la función atoi de la libc.

Parámetros:
- str: puntero a la cadena de caracteres a convertir.

Valor de retorno:
- El valor entero representado por la cadena.
*/

#include "libft.h"

int	ft_atoi(const char *str)
{
	int	sign;
	int	res;

	sign = 1;
	res = 0;
	while (*str == ' ' || (*str >= 9 && *str <= 13))
	{
		str++;
	}
	if (*str == '-' || *str == '+')
	{
		if (*str == '-')
		{
			sign = -1;
		}
		str++;
	}
	while (*str >= '0' && *str <= '9')
	{
		res = res * 10 + (*str - '0');
		str++;
	}
	return (res * sign);
}

int	main(int argc, char **argv)
{
	int	res;

	if (argc != 2)
	{
		printf("Use: %s <string> \n", argv[0]);
		return (1);
	}
	res = ft_atoi(argv[1]);
	printf("atoi: %d\n", atoi(argv[1]));
	printf("ft_atoi: %d\n", res);
	return (0);
}
