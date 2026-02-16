*This project has been created as part of the 42 curriculum by sperez-l.*

# Get Next Line

## Description

**Get Next Line** is a core project from the 42 curriculum.  
Its objective is to implement the following function in C:

```c
char *get_next_line(int fd);
```

This function reads and returns **one line at a time** from a given file descriptor (`fd`).  
Each returned line includes the terminating newline character `\n` if it exists.  
If there is nothing more to read or an error occurs, the function returns `NULL`.

This project focuses on:

- Low-level file descriptor handling
- Incremental reading using `read`
- Dynamic memory management (`malloc`, `free`)
- Persistent state management using **static variables**
- Leak-free memory design
- Robust behavior with variable buffer sizes

---

## Project Objectives

- Read from a file descriptor without loading the entire file into memory.
- Return exactly one line per function call.
- Handle any `BUFFER_SIZE` value.
- Avoid memory leaks.
- Work correctly with both files and `stdin`.
- Use only authorized functions:  
  `read`, `malloc`, `free`.

---

## Algorithm Overview

### Problem

The `read()` function does not guarantee:
- Reading a full line
- Reading only one line
- Reading until a newline

Therefore, partial reads must be handled safely and accumulated.

### Solution Strategy

The implementation uses a **static pointer**:

```c
static char *stash;
```

This variable:

- Persists between function calls
- Stores leftover data
- Allows incremental accumulation of input
- Maintains state without global variables

### Execution Flow

1. Validate `fd` and `BUFFER_SIZE`.
2. Allocate a temporary buffer.
3. Read from `fd` until:
   - A newline is found, or
   - End of file is reached.
4. Append the read content to `stash`.
5. Extract one full line from `stash`.
6. Update `stash` with remaining content.
7. Return the extracted line.

This ensures minimal reading per call and efficient memory usage.

---

## Project Structure

```
get_next_line.c
get_next_line_utils.c
get_next_line.h
```

### get_next_line.c
Contains the main logic of the function:
- File reading loop
- Static storage management
- Line extraction control

### get_next_line_utils.c
Helper functions such as:
- `ft_strlen`
- `ft_strjoin`
- `ft_strchr`
- Memory helpers
- Line extraction utilities

### get_next_line.h
Contains:
- Function prototype
- Required headers
- `BUFFER_SIZE` definition (if not defined externally)

---

## Compilation

The project must compile with:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c
```

It must also compile without explicitly defining `BUFFER_SIZE`:

```bash
cc -Wall -Wextra -Werror get_next_line.c get_next_line_utils.c
```

---

## Example Usage

```c
int fd = open("file.txt", O_RDONLY);
char *line;

while ((line = get_next_line(fd)) != NULL)
{
    printf("%s", line);
    free(line);
}
close(fd);
```

---

## Edge Cases Covered

- Empty files
- Files without a trailing newline
- `BUFFER_SIZE = 1`
- Very large `BUFFER_SIZE`
- Reading from `stdin`
- Proper EOF handling
- No memory leaks (verified with Valgrind)

---

## Bonus Features (If Implemented)

- Support for multiple file descriptors simultaneously
- Single static variable constraint
- Separate `_bonus.c` and `_bonus.h` files

---

## Technical Decisions

- No use of `libft` (as prohibited by the subject)
- No use of `lseek`
- No global variables
- Strict memory control
- Modular design
- Error-safe `read` handling

---

## Resources

- `man 2 read`
- `man 3 malloc`
- POSIX documentation on file descriptors
- Documentation on static variables in C

---

## Learning Outcomes

This project demonstrates:

- Deep understanding of file descriptors
- Proper memory lifecycle management
- Static variable usage in C
- Robust incremental file reading
- Clean modular code structure
- Defensive programming practices

---

**Status:** Completed (Mandatory Part)  
**Language:** C  
**Curriculum:** 42

