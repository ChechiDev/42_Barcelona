
#include "get_next_line.h"

int	main(void)
{
	int	fd;
	int	line_number;
	char	*line;

	fd = open("test.txt", O_RDONLY);
	if (!fd)
	{
		printf("Error opening file\n");
		return (1);
	}
	line = get_next_line(fd);
	line_number = 1;
	while (line)
	{
		printf("[LINE %d]: %s\n", line_number, line);
		free(line);
		line = get_next_line(fd);
		line_number++;
	}
	close(fd);
	return (0);
}
