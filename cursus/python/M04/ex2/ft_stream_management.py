#!/usr/bin/env python3

import sys
import typing


def process_content(content: str) -> str:
    """ Add the archive marker at the end of each line """

    result = ""
    has_content = False
    last_was_newline = False

    for char in content:
        has_content = True
        if char == "\n":
            result += "#\n"
            last_was_newline = True
        else:
            result += char
            last_was_newline = False

    if has_content and not last_was_newline:
        result += "#"

    return result


def read_line() -> str:
    """ Read one line from standard input without using input """

    # readline lee desde stdin sin mostrar un prompt automático como input().
    line = sys.stdin.readline()
    if len(line) > 0 and line[-1] == "\n":
        return line[:-1]
    return line


def print_error(message: str) -> None:
    """ Print a prefixed error message to standard error """

    # stderr separa los errores de la salida normal del programa.
    print(f"[STDERR] {message}", file=sys.stderr)


def read_file(filename: str) -> str | None:
    """ Read and display the requested archive file """

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename)
    except OSError as e:
        print_error(f"Error opening file '{filename}': {e}")
        return None

    try:
        content = file.read()
        print("---")
        print(content, end="")
        print("---")
        return content
    finally:
        file.close()
        print(f"File '{filename}' closed.")


def save_content(filename: str, content: str) -> bool:
    """ Save transformed archive content into the target file """

    print(f"Saving data to '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "w")
    except OSError as e:
        print_error(f"Error opening file '{filename}': {e}")
        return False

    try:
        file.write(content)
    finally:
        file.close()

    print(f"Data saved in file '{filename}'.")
    return True


def process_archive(filename: str) -> None:
    """ Read archive data and optionally save transformed content """

    content = read_file(filename)
    if content is None:
        return

    transformed_content = process_content(content)
    print("Transform data:")
    print("---")
    print(transformed_content, end="")
    print("---")

    print("Enter new file name (or empty): ", end="")
    # flush muestra el prompt antes de esperar la lectura desde stdin.
    sys.stdout.flush()
    new_filename = read_line()
    if not new_filename:
        print("Not saving data.")
        return

    if not save_content(new_filename, transformed_content):
        # El booleano permite reaccionar sin lanzar excepciones al llamador.
        print("Data not saved.")


def main() -> None:
    """ Validate arguments and launch the stream workflow """

    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    process_archive(sys.argv[1])


if __name__ == "__main__":
    main()
