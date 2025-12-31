#include "libft.h"
#include <unistd.h>

int ft_isalpha(int c)
{
	if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
	{
		return (1);
	}
	else
	{
		return (0);
	}
}

int main(int argc, char **argv)
{
	if (argc == 2)
	{
		if (ft_isalpha(argv[1][0]))
			write(1, "It's an alphabetic character.\n", 30);
		else
			write(1, "It's not an alphabetic character.\n", 34);
	}
	return (0);
}
