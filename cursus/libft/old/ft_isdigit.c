

#include "libft.h"
#include <stdio.h>

int	ft_isdigit(int c)
{
	if (c >= '0' && c <= '9')
	{
		return (1);
	}
	return (0);
}
/*
int	main(int argc, char **argv)
{
	char	c;

	c = argv[1][0];
	if (argc != 2)
	{
		printf("Use: %s <digit_value>", argv[0]);
		return (1);
	}
	printf("%d\n", ft_isdigit(c));
	return (0);
}
*/
