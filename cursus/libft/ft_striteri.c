/*
ft_striteri

Aplica la función 'f' a cada carácter de la cadena 's'.
A 'f' se le pasa como primer argumento el índice del carácter dentro de 's'
y como segundo argumento la dirección del propio carácter, que puede ser
modificado directamente.

La iteración se realiza de izquierda a derecha, desde el primer carácter
hasta el carácter nulo final '\0'.

No reserva memoria dinámica y no devuelve ningún valor.
Si 's' o 'f' son NULL, la función no realiza ninguna acción.
*/

#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char *))
{
	unsigned int	i;

	if (!s || !f)
	{
		return; 
	}
	i = 0;
	while (s[i])
	{
		f(i, &s[i]);
		i++;
	}
}
/*
static void	ft_iter_toupper(unsigned int i,	char *c)
{
	(void)i;
	if (!c)
	{
		return;
	}
	*c = (char)ft_toupper((unsigned int)*c);
}

int	main(int argc, char **argv)
{
	char	*res;
	
	if (argc != 2)
	{
		printf("Use: %s <string>\n", argv[0]);
		return (1);
	}
	res = ft_strdup(argv[1]);
	if (!res)
	{
		return (1);
	}
	printf("Antes: %s\n", res);
	ft_striteri(res, ft_iter_toupper);
	printf("Despues: %s\n", res);
	free(res);
	return (0);
}
*/
