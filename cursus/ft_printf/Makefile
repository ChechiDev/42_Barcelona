NAME = libftprintf.a
SOURCES = \
	  ft_printf.c \
	  ft_print_char.c \
	  ft_print_str.c \
	  ft_print_ptr.c \
	  ft_print_nbr.c \
	  ft_print_hex.c \
	  ft_print_format.c \
	  ft_print_utils.c 

OBJECTS = $(SOURCES:.c=.o)

CC = cc
CFLAGS = -g -O0 -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f

all: $(NAME)

$(NAME): $(OBJECTS)
	$(AR) $(NAME) $(OBJECTS)

%.o: %.c Makefile libftprintf.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJECTS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
