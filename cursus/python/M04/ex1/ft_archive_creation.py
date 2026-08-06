#!/usr/bin/env python3

import sys
import typing


def get_open_file(
    filename: str,
    mode: str = "r",
) -> typing.IO[str] | None:
    """ Return an opened file or None when opening fails """

    try:
        return open(filename, mode)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None


def process_content(content: str) -> str:
    """ Add the archive marker at the end of each line """

    result = ""
    has_content = False
    last_was_newline = False

    for char in content:
        # Procesar carácter a carácter permite detectar cada salto de línea.
        has_content = True
        if char == "\n":
            result += "#\n"
            last_was_newline = True
        else:
            result += char
            last_was_newline = False

    # Si no termina en salto de línea, se agrega el marcador pendiente.
    if has_content and not last_was_newline:
        result += "#"

    return result


def print_archive_content(content: str) -> None:
    """ Print archive content between recovery separators """

    print("---")
    print(content, end="")
    print("---")


def read_file(filename: str) -> str | None:
    """ Read and display the requested archive file """

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file = get_open_file(filename)
    if file is None:
        return None

    try:
        content = file.read()
        print_archive_content(content)
        return content
    finally:
        file.close()
        print(f"File '{filename}' closed.")


def save_content(filename: str, content: str) -> None:
    """ Save transformed archive content into the target file """

    print(f"Saving data to '{filename}'")

    # El modo "w" crea el archivo o reemplaza su contenido existente.
    file = get_open_file(filename, "w")
    if file is None:
        return

    try:
        file.write(content)
    finally:
        file.close()

    print(f"Data saved in file '{filename}'.")


def ask_output_filename() -> str:
    """ Ask for the optional output archive filename """

    return input("Enter new file name (or empty): ")


def print_transformed_content(content: str) -> None:
    """ Print transformed archive content with its heading """

    print("Transform data:")
    print_archive_content(content)


def process_archive(filename: str) -> None:
    """ Read archive data and optionally save transformed content """

    content = read_file(filename)
    if content is None:
        return

    transformed_content = process_content(content)
    print_transformed_content(transformed_content)

    # Una entrada vacía decide explícitamente no persistir la transformación.
    new_filename = ask_output_filename()
    if not new_filename:
        print("Not saving data.")
        return

    save_content(new_filename, transformed_content)


def main() -> None:
    """ Validate arguments and launch the archive workflow """

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    process_archive(sys.argv[1])


if __name__ == "__main__":
    main()
