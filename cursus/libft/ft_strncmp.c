/*
ft_strncmp

Compara como máximo los primeros `n` caracteres de las cadenas `s1` y `s2`.

La comparación se realiza carácter a carácter, interpretando cada uno como
`unsigned char`. El proceso se detiene cuando:
- se alcanza un carácter distinto,
- se encuentra el carácter nulo '\0',
- o se han comparado `n` caracteres.

Valor de retorno:
- 0   si las cadenas son iguales en los primeros `n` caracteres.
- < 0 si el primer carácter distinto en `s1` es menor que el correspondiente en `s2`.
- > 0 si el primer carácter distinto en `s1` es mayor que el correspondiente en `s2`.

Si `n` es 0, la función devuelve 0 sin realizar ninguna comparación.
*/

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	i;
	unsigned char	uc1;
	unsigned char	uc2;

	i = 0;
	if (n == 0)
	{
		return (0);
	}
	while (i < n)
	{
		uc1 = (unsigned char)s1[i];
		uc2 = (unsigned char)s2[i];
		if (uc1 != uc2)
		{
			return (uc1 - uc2);
		}
		if (uc1 == '\0')
		{
			return (0);
		}
		i++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	int	res;

	if (argc != 4)
	{
		printf("Use: %s <string1> <string2> <n>", argv[0]);
		return (1);
	}

	res = ft_strncmp(argv[1], argv[2], (size_t)atoi(argv[3]));
	printf("Result: %d\n", res);
	return (0);
}
