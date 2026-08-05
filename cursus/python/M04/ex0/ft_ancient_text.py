#!/usr/bin/env python3

import sys
import typing


def get_open_file(filename: str) -> typing.IO[str] | None:
    """ Return an opened file or None when opening fails """

    try:
        # Abrir puede fallar por permisos, rutas o ausencia del archivo.
        return open(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None


def display_file(filename: str) -> None:
    """ Display the target file with archive recovery headers """

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file = get_open_file(filename)
    if file is None:
        return

    try:
        print("---")
        print(file.read(), end="")
        print("---")
    finally:
        # finally garantiza el cierre incluso ante errores de lectura.
        file.close()
        print(f"File '{filename}' closed.")


def main() -> None:
    """ Validate arguments and launch the file display workflow """

    if len(sys.argv) != 2:
        # Validar argumentos evita acceder a una posición inexistente.
        print("Usage: ft_ancient_text.py <file>")
        return

    display_file(sys.argv[1])


if __name__ == "__main__":
    main()
