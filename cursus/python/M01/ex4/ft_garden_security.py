#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int
    ) -> None:
        self._name = name
        self._height = height if height >= 0 else 0.0
        self._age = age if age > 0 else 0

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value >= 0:
            self._height = value
            print(f"Height updated: {self._height:.0f}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, value: int) -> None:
        if value > 0:
            self._age = value
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> None:
        print("=== Garden Security System ===")
        print(
            f"Plant created: {self._name}: "
            f"{self._height:.1f}cm, "
            f"{self._age} days old"
        )


def main() -> None:
    p = Plant("Rose", 15.0, 10)
    p.show()
    print()
    # p.set_height(10)
    # p.set_age(20)
    p.set_height(-1)
    p.set_age(-1)
    print()
    print(
        f"Current state: {p._name}: "
        f"{p.get_height():.1f}cm, "
        f"{p.get_age()} days old"
    )


if __name__ == "__main__":
    main()
