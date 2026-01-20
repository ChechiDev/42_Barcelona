/*
ft_putnbr_fd

Escribe el número entero 'n' en el descriptor de archivo 'fd'.
El número se imprime en base decimal, incluyendo el signo si es negativo.

No reserva memoria dinámica.
No devuelve ningún valor.

En caso de que 'n' sea INT_MIN, debe imprimirse correctamente.
*/

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	long	nb;
	char	c;
	
	nb = (long)n;
	if (nb < 0)
	{
		write(fd, "-", 1);
		nb = -nb;
	}
	if (nb >= 10)
	{
		ft_putnbr_fd((int)(nb / 10), fd);
	}
	c = (char)('0' + (nb % 10));
	write(fd, &c, 1);
}
/*
int	main(int argc, char **argv)
{
	int	n;

	if (argc != 2)
	{
		printf("Use: %s <num>\n", argv[0]);
		return (1);
	}
	n = ft_atoi(argv[1]);
	ft_putnbr_fd(n, 1);
	write(1, "\n", 1);
	return (0);
}
*/
