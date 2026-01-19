/*
ft_isascii

Descripción:
 Comprueba si el valor entero recibido representa un carácter ASCII válido.
 Un carácter ASCII válido está comprendido entre los valores 0 y 127
 (inclusive), según el estándar ASCII.

Parámetros:
 c -> valor entero a comprobar.

Valor de retorno:
 Devuelve 1 si c pertenece al rango ASCII (0–127).
 Devuelve 0 en caso contrario.

Notas:
- Esta función no verifica si el carácter es imprimible.
- Solo valida la pertenencia al conjunto ASCII estándar.
*/

#include "libft.h"

int	ft_isascii(int c)
{
	if (c >= 0 && c <= 127)
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
	c = atoi(argv[1]);
	printf("isascii: %d\n", isascii(c) != 0);
	printf("ft_isascii: %d\n", isascii(c) != 0);
	return (0);
}
