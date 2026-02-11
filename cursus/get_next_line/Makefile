NAME = get_next_line.a
SOURCES = \
	  get_next_line.c \
	  get_next_line_utils.c

OBJECTS = $(SOURCES:.c=.o)

CC = cc
CFLAGS = -g -O0 -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f

all: $(NAME)

$(NAME): $(OBJECTS)
	$(AR) $(NAME) $(OBJECTS)

%.o: %.c Makefile get_next_line.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJECTS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
