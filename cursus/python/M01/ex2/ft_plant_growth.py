#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        grow_rate: float = 0.8

    ) -> None:
        self._name = name
        self._height = height if height >= 0 else 0.0
        self._age = age if age > 0 else 0
        self._grow_rate = grow_rate

    def grow(self) -> None:
        self._height = round(self._height + self._grow_rate, 1)

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(
            f"{self._name}: "
            f"{self._height:.1f}cm, "
            f"{self._age} days old"
        )


def main():
    p = Plant("Rose", 25, 30, 0.8)
    start_height = p._height

    print("=== Garden Plant Growth ===")
    p.show()

    for d in range(1, 8):
        p.grow()
        p.age()
        print(f"=== Day {d} ===")
        p.show()

    growth = round(p._height - start_height, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    main()
