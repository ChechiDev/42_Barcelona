#!/usr/bin/env python3


READ_MODE = "read"
WRITE_MODE = "write"
SUCCESS_MESSAGE = "Content successfully written to file"
INVALID_ACTION_MESSAGE = "Invalid archive action"


def is_write_action(action: str) -> bool:
    """ Return whether the requested archive action is write """

    return action == WRITE_MODE


def is_read_action(action: str) -> bool:
    """ Return whether the requested archive action is read """

    return action == READ_MODE


def read_archive(filename: str) -> tuple[bool, str]:
    """ Safely read all content from an archive file """

    with open(filename) as file:
        # La tupla combina estado de éxito y dato leído en un retorno.
        return True, file.read()


def write_archive(filename: str, content: str) -> tuple[bool, str]:
    """ Safely write content into an archive file """

    # with cierra el archivo automáticamente al salir del bloque.
    with open(filename, "w") as file:
        file.write(content)
    return True, SUCCESS_MESSAGE


def secure_archive(
    filename: str,
    action: str = READ_MODE,
    content: str = "",
) -> tuple[bool, str]:
    """ Safely read from or write to an archive file """

    try:
        if is_write_action(action):
            return write_archive(filename, content)
        if is_read_action(action):
            return read_archive(filename)
        return False, INVALID_ACTION_MESSAGE
    except OSError as e:
        # Capturar OSError concentra errores de permisos, rutas y E/S.
        return False, f"{e}"


def main() -> None:
    """ Display the secure archive demonstration outputs """

    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        # El primer elemento decide si el contenido es reutilizable.
        print(secure_archive("new_fragment.txt", WRITE_MODE, result[1]))
    else:
        print(secure_archive("new_fragment.txt", WRITE_MODE, ""))


if __name__ == "__main__":
    main()
