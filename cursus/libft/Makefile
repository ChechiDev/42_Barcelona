NAME = libft.a
SOURCES = \
	  ft_isalpha.c ft_isdigit.c

OBJECTS = $(SOURCES:.c=.o)

CC = gcc
CFLAGS = -g -O0 -Wall -Wextra -Werror
AR = ar rcs

all: $(NAME)

$(NAME): $(OBJECTS)
	$(AR) $(NAME) $(OBJECTS)

%.o: %.c Makefile libft.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJECTS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
