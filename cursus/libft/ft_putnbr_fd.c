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
	char	c;

	if (n == -2147483648)
	{
		write(fd, "-2147483648", 11);
		return;
	}
	if (n < 0)
	{
		write(fd, "-", 1);
		n = -n;
	}
	if (n >= 10)
	{
		ft_putnbr_fd(n / 10, fd);
	}
	c = (char)('0' + (n % 10));
	write(fd, &c, 1);
}
