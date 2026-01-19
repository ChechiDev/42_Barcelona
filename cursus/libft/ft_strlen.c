/*
ft_strlen

Descripción:
  Calcula la longitud de una cadena de caracteres terminada en '\0'.
  La longitud corresponde al número de caracteres que preceden al
  carácter nulo final.

Parámetros:
  s: puntero a una cadena de caracteres válida terminada en '\0'.

Valor de retorno:
  Devuelve el número de caracteres de la cadena, sin contar el
  carácter nulo '\0'.

Comportamiento:
  Recorre la cadena carácter a carácter hasta encontrar '\0' y
  contabiliza cuántos caracteres se han leído.

Comportamiento indefinido:
  Si el puntero 's' es NULL, el comportamiento no está definido.
*/

#include "libft.h"

int	ft_strlen(const char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}

int	main(int argc, char **argv)
{
	char	*str;

	if (argc != 2)
	{
		return (0);
	}
	str = argv[1];
	printf("strlen: %ld\n", strlen(str));
	printf("ft_strlen: %d\n", ft_strlen(str));
	return (0);
}
