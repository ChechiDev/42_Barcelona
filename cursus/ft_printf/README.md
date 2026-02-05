*This project has been created as part of the 42 curriculum by <sperez-l>.*

# ft_printf

## Description

`ft_printf` is a C library that reimplements the standard `printf()` function from the C standard library.
The goal of this project is to understand and correctly use variadic functions, manage formatted output, and design a modular and extensible architecture.

Unlike simple output helpers such as `ft_putnbr` or `ft_putstr`, `ft_printf` parses a format string at runtime, handles multiple conversion specifiers, prints different data types, and returns the total number of printed characters.

Once completed, this library can be integrated into `libft` and reused in future C projects.

## Supported Conversions

The mandatory part supports the following format specifiers:

- `%c` → character
- `%s` → string
- `%p` → pointer (hexadecimal format)
- `%d` → signed integer (base 10)
- `%i` → signed integer (base 10)
- `%u` → unsigned integer (base 10)
- `%x` → hexadecimal (lowercase)
- `%X` → hexadecimal (uppercase)
- `%%` → percent symbol

Buffer management from the original `printf` is intentionally not implemented, as specified in the subject.

## Project Structure

```
.
├── Makefile
├── ft_printf.h
├── ft_printf.c
├── ft_print_format.c
├── ft_print_char.c
├── ft_print_str.c
├── ft_print_nbr.c
├── ft_print_hex.c
├── ft_print_ptr.c
├── ft_print_utils.c
└── README.md
```

Each conversion is handled in a dedicated file to keep responsibilities separated and the codebase maintainable.

## Design and Implementation

The implementation is based on a dispatcher pattern that parses the format string character by character. When a '%' is encountered, the corresponding conversion specifier is identified and dispatched to a dedicated function.

Each conversion type is implemented in its own source file, which improves readability, simplifies debugging, and allows the project to scale without increasing complexity in the core `ft_printf` function.

No dynamic data structures are required. The design relies on sequential parsing, controlled use of variadic arguments, and direct output via `write()`, ensuring predictable behavior and compliance with the project constraints.

## Compilation

The project builds a static library named `libftprintf.a`.

To compile:

```bash
make
```

Mandatory Makefile rules included:
```bash
all
clean
fclean
re
```

Compilation uses the required flags:
```bash
-Wall -Wextra -Werror
```

and the cc compiler. Relinking is avoided.

## Usage

Include the header and link the library:
```c
#include "ft_printf.h"
```
Example:
```c
ft_printf("Hello %s, number: %d\n", "world", 42);
```

The function behaves like printf() and returns the number of characters printed.

## Technical Choices

Variadic arguments handled using `va_start`, `va_arg`, and `va_end`

No global state

No forbidden functions

No memory leaks

Clear dispatcher-based design for format handling

Output performed exclusively with write()

This design ensures extensibility (especially for the bonus part) and simplifies debugging.

## Resources

man 3 printf

man stdarg

GNU C Library documentation

42 intra documentation

## Evaluation Notes

The library is compared directly against the original printf()

Any unexpected behavior, memory leak, or norm violation results in failure

Bonus is evaluated only if the mandatory part is perfect
