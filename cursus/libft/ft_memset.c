
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

void *ft_memset(void *ptr, int c, size_t n)
{
	unsigned char *dst;
	unsigned char uc;
	size_t i;

	dst = (unsigned char *)ptr;
	uc = (unsigned char)c;
	i = 0;
	
	while (i < n)
	{
		dst[i] = uc;
		i++;
	}
	return (ptr);
}

int main(int argc, char **argv)
{
	char buffer[50];
	int value;
	size_t n;
	size_t i;

	if (argc != 3)
	{
		printf("Uso %s <valor_byte> <num_bytes>", argv[0]);
		return (1);
	}

	value = atoi(argv[1]);
	n = (size_t)atoi(argv[2]);

	ft_memset(buffer, value, n);

	while (i < n && i < sizeof(buffer))
	{
		printf("buffer[%zu] = %d\n", i, (unsigned char)buffer[i]);
		i++;
	}
	return (0);
}

