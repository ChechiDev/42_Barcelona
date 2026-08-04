#!/usr/bin/ev python3

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
        self._grow_rate = 0.8

    def grow(self) -> None:
        self._height = round(self._height + self._grow_rate, 1)

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"=== {self.__class__.__name__}")
        print(
            f"{self._name}: "
            f"{self._height:.1f}cm, "
            f"{self._age} days old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False
        self._grow_rate = 0.8

    def bloom(self) -> None:
        self._blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._grow_rate = 0.8

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        grow_rate: float = 2.1
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0
        self._grow_rate = grow_rate

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    f = Flower("Rose", 15, 10, "red")
    f.show()
    print()
    print("[asking the rose to bloom]")
    print()
    f.bloom()
    f.show()

    print()
    t = Tree("Oak", 200, 365, 5.0)
    t.show()
    print()
    print("[asking the oak to produce shade]")
    print()
    t.produce_shade()

    print()
    v = Vegetable("Tomato", 5, 10, "April", 2.1)
    v.show()
    print()
    print("[make tomato grow and age for 20 days]")
    print()
    for _ in range(20):
        v.grow()
        v.age()
    v.show()


if __name__ == "__main__":
    main()
