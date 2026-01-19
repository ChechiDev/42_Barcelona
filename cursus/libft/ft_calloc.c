/*
ft_calloc

Reserva memoria para un array de `nmemb` elementos de `size` bytes cada uno,
inicializando todos los bytes de la zona reservada a 0.

Comportamiento:
- Reserva `nmemb * size` bytes en el heap.
- Si la reserva tiene éxito, todos los bytes quedan a cero.
- Si `nmemb` o `size` es 0, devuelve un puntero válido que puede pasarse a free().
- Si ocurre un overflow en la multiplicación `nmemb * size` o falla la reserva,
  devuelve NULL.

Valor de retorno:
- Puntero a la memoria reservada e inicializada a 0.
- NULL en caso de error.
*/

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*ptr;
	size_t	res;
	size_t	i;

	if (nmemb == 0 || size == 0)
	{
		ptr = malloc(1);
		if (!ptr)
		{
			return (NULL);
		}
		return (ptr);
	}
	res = (nmemb * size);
	if (size != 0 && res / size != nmemb)
	{
		return (NULL);
	}
	ptr = malloc(res);
	i = 0;
	while (i < res)
	{
		((unsigned char *)ptr)[i] = 0;
		i++;
	}
	return (ptr);
}

int	main(int argc, char **argv)
{
	int	*arr;
	size_t nmemb;
	size_t size;
	size_t i;

	if (argc != 3)
	{
		printf("Use: %s <nmemb> <size> \n", argv[0]);
		return (1);
	}
	nmemb = (size_t)ft_atoi(argv[1]);
	size = (size_t)ft_atoi(argv[2]);
	arr = (int *)ft_calloc(nmemb, size);
	if (!arr)
	{
		printf("Error\n");
		return (1);
	}
	i = 0;
	while (i < nmemb && size == sizeof(int))
	{
		printf("arr[%zu] = %d\n", i, arr[i]);
		i++;
	}
	free(arr);
	return(0);
}
