#!/usr/bin/env python3


READ_MODE = "read"
WRITE_MODE = "write"
SUCCESS_MESSAGE = "Content successfully written to file"


def secure_archive(
    filename: str,
    action: str = READ_MODE,
    content: str = "",
) -> tuple[bool, str]:
    """ Safely read from or write to an archive file """

    try:
        if action == WRITE_MODE:
            # with cierra el archivo automáticamente al salir del bloque.
            with open(filename, "w") as file:
                file.write(content)
            return True, SUCCESS_MESSAGE

        with open(filename) as file:
            # La tupla combina estado de éxito y dato leído en un retorno.
            return True, file.read()
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
