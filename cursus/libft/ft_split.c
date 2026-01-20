/*
ft_split

Divide la cadena de caracteres `s` en un conjunto de subcadenas utilizando
el carácter `c` como delimitador.

Reserva memoria y devuelve un array de strings terminado en NULL, donde
cada string corresponde a una subcadena de `s` separada por `c`.

No se incluyen subcadenas vacías: los delimitadores consecutivos, así como
los delimitadores al inicio o al final de la cadena, se ignoran.

Parámetros:
- s: cadena de caracteres a dividir.
- c: carácter delimitador.

Valor devuelto:
- Un array de strings terminado en NULL.
- NULL si `s` es NULL o si falla alguna reserva de memoria.

En caso de error durante la reserva, toda la memoria previamente asignada
debe liberarse correctamente.
*/

#include "libft.h"

static int	ft_word_count(const char *s, char c)
{
	size_t	i;
	size_t	count;
	size_t	in_word;

	i = 0;
	count = 0;
	in_word = 0;
	while (s[i])
	{
		if (s[i] != c && in_word == 0)
		{
			count++;
			in_word = 1;
		}
		else if (s[i] == c)
		{
			in_word = 0;
		}
		i++;
	}
	return (count);
}

char	**ft_split(char const *s, char c)
{
	char	**arr;
	size_t	word;
	size_t	i;

	arr = (char **)malloc((ft_word_count(s, c) + 1) * sizeof(char *)); 
	if (!s || !arr)
	{
		return (NULL);
	}
	i = 0;
	while (*s)
	{
		while (*s == c && *s)
		{
			s++;
		}
		if (*s)
		{
			if (!ft_strchr(s, c))
			{
				word = ft_strlen(s);
			}
			else
			{
				word = ft_strchr(s, c) - s;
			}
			arr[i++] = ft_substr(s, 0, word);
			s = s + word;
		}
	}
	arr[i] = NULL;
	return (arr);
}
/*
int	main(int argc, char **argv)
{
	char	**res;
	int	i;

	i = 0;
	if (argc != 3)
	{
		return (1);
	}
	res = ft_split(argv[1], argv[2][0]);
	if (!res)
	{
		printf("Error");
		return (1);
	}
	while (res[i])
	{
		printf("%s\n", res[i]);
		free(res[i]);
		i++;
	}
	free(res);
	return (0);
}
*/
