/*
ft_toupper

Convierte un carácter alfabético minúsculo en su equivalente en mayúscula.

Si el carácter recibido está en el rango de letras minúsculas ('a' a 'z'),
la función devuelve el carácter correspondiente en mayúscula ('A' a 'Z').

Si el carácter no es una letra minúscula, se devuelve sin modificar.

Parámetro:
- c: carácter representado como un int (normalmente un unsigned char).

Valor devuelto:
- El carácter convertido a mayúscula si procede.
- El mismo valor de entrada si no se realiza conversión.

No reserva memoria ni produce efectos secundarios.
*/

#include "libft.h"

int	ft_toupper(int c)
{
	if (c >= 'a' && c <= 'z')
	{
		return (c - 32);
	}
	return (c);
}

int	main(int argc, char **argv)
{
	int	res;

	if (argc != 2 && argv[1][0] != '\0')
	{
		printf("Use: %s <character>", argv[0]);
		return (1);
	}
	res = ft_toupper(argv[1][0]);
	write(1, &res, 1);
	write(1, "\n", 1);
	return (0);
}
