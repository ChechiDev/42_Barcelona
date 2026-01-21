*This project was created as part of the 42 curriculum by sperez-l.*

# libft

## Description

**libft** is a custom C library developed as part of the 42 curriculum.  
The objective of this project is to reimplement a subset of standard C library functions and to build additional utility functions that will be reused throughout future C projects.

This project focuses on:
- Understanding how common libc functions work internally
- Practicing manual memory management
- Writing clean, reusable, and norm-compliant C code
- Building a solid foundation for low-level programming

The final result is a static library named `libft.a`.

---

## Instructions

### Compilation

To compile the library, run:

```bash
make
```

This will generate the static library:

```bash
libft.a
```

Available Makefile rules:

```bash
make        # Compile the library
make clean  # Remove object files
make fclean # Remove object files and libft.a
make re     # Recompile everything
```

Usage

To use libft in another project:

1. Include the header file:

```c
#include "libft.h"
```

2. Compile your own source files together with *libft.a*:

```bash
cc your_program.c libft.a
```

## Library Overview

The library is divided into three main parts.

## Core Files

- [`Makefile`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/Makefile)  
  Defines the build rules to compile the library into `libft.a` using the required flags  
  (`-Wall -Wextra -Werror`) and standard targets (`all`, `clean`, `fclean`, `re`).

- [`libft.h`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/libft.h)  
  Main header file of the library.  
  It contains all function prototypes, required includes, and the definition of the  
  `t_list` structure used for linked list utilities.

---

## Part 1 – Libc Functions

Reimplementations of standard C library functions.
All functions reproduce the behavior of their libc counterparts and are prefixed with *ft_.*

- [`ft_isalpha`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_isalpha.c)
- [`ft_isdigit`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_isdigit.c)
- [`ft_isalnum`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_isalnum.c)
- [`ft_isascii`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_isascii.c)
- [`ft_isprint`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_isprint.c)
- [`ft_strlen`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strlen.c)
- [`ft_memset`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_memset.c)
- [`ft_bzero`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_bzero.c)
- [`ft_memcpy`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_memcpy.c)
- [`ft_memmove`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_memmove.c)
- [`ft_strlcpy`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strlcpy.c)
- [`ft_strlcat`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strlcat.c)
- [`ft_toupper`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_toupper.c)
- [`ft_tolower`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_tolower.c)
- [`ft_strchr`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strchr.c)
- [`ft_strrchr`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strrchr.c)
- [`ft_strncmp`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strncmp.c)
- [`ft_memchr`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_memchr.c)
- [`ft_memcmp`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_memcmp.c)
- [`ft_strnstr`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strnstr.c)
- [`ft_atoi`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_atoi.c)
- [`ft_calloc`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_calloc.c)
- [`ft_strdup`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strdup.c)a

---

## Part 2 – Additional Functions

Utility functions not present in libc or implemented differently.

- [`ft_substr`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_substr.c)  
  Creates a substring from a given string.

- [`ft_strjoin`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strjoin.c)  
  Concatenates two strings into a new one.

- [`ft_strtrim`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strtrim.c)  
  Trims characters from the beginning and end of a string.

- [`ft_split`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_split.c)  
  Splits a string using a delimiter.

- [`ft_itoa`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_itoa.c)  
  Converts an integer to a string.

- [`ft_strmapi`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_strmapi.c)  
  Applies a function to each character of a string and returns a new string.

- [`ft_striteri`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_striteri.c)  
  Applies a function to each character of a string in place.

- [`ft_putchar_fd`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_putchar_fd.c)

- [`ft_putstr_fd`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_putstr_fd.c)

- [`ft_putendl_fd`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_putendl_fd.c)

- [`ft_putnbr_fd`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_putnbr_fd.c)

---

## Part 3 – Linked Lists

Implementation of a simple singly linked list using the *t_list* structure.

- [`ft_lstnew`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstnew.c)
- [`ft_lstadd_front`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstadd_front.c)
- [`ft_lstsize`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstsize.c)
- [`ft_lstlast`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstlast.c)
- [`ft_lstadd_back`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstadd_back.c)
- [`ft_lstdelone`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstdelone.c)
- [`ft_lstclear`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstclear.c)
- [`ft_lstiter`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstiter.c)
- [`ft_lstmap`](https://github.com/ChechiDev/42_Barcelona/blob/main/cursus/libft/ft_lstmap.c)

These functions allow creation, traversal, modification, and deletion of linked lists.
