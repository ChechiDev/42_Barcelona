#!/usr/bin/env python3

_YEAR = 365
_GROW_RATE = 0.8


class Plant:
    """ Base plant class with internal tracking """
    def __init__(
        self,
        name: str,
        height: float,
        age: int
    ) -> None:
        self._name = name
        self._height = height if height >= 0 else 0.0
        self._age = age if age > 0 else 0
        self._stats = self._Stats()

    class _Stats:
        """ Encapsulates call counters for each tracked method """
        _LABELS = ["grow", "age", "show"]

        def __init__(self) -> None:
            self._counts = {label: 0 for label in self._LABELS}
   
        def increment(self, method: str) -> None:
            """ Increment the counter for the given method name """
            if method in self._counts:
                self._counts[method] += 1

        def show(self) -> None:
            """ Display all method call counters """
            parts = [
                f"{self._counts[label]} {label}"
                for label in self._LABELS
            ]
            print(f"Stats: {', '.join(parts)}")
 
    @staticmethod
    def _is_older(age: int) -> str:
        """ Return a string indicating if age exceeds one year """
        if age < _YEAR:
            return f"Is {age} days more than a year? -> False"
        return f"Is {age} days more than a year? -> True"

    @classmethod
    def anonymous(cls) -> "Plant":
        """ Create an anonymous plant when full info is not available """
        return cls("Unknown plant", 0.0, 0)

    def grow(self, grow_rate: float = None) -> None:
        """ Grow the plant by grow_rate or by its default rate """
        rate = grow_rate if grow_rate is not None else self._grow_rate
        self._height = round(self._height + rate, 1)
        self._stats.increment("grow")

    def age(self) -> None:
        """Increment the plant age by one day."""
        self._age += 1
        self._stats.increment("age")

    def simulate(self, days: int, grow_rate: float = None) -> None:
        """ Grow and age the plant for the given number of days """
        for _ in range(days):
            self.grow(grow_rate)
            self.age()

    def show(self) -> None:
        """ Display the plant basic information """
        print(f"=== {self.__class__.__name__}")
        print(
            f"{self._name}: "
            f"{self._height:.1f}cm, "
            f"{self._age} days old"
        )
        self._stats.increment("show")


class Flower(Plant):
    """ Flower plant with bloom capability """
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
        self._grow_rate = _GROW_RATE
  
    def bloom(self) -> None:
        """ Set the flower to blooming state """
        self._blooming = True

    def _bloom_status(self) -> str:
        """ Return a string describing the current bloom state """
        if self._blooming:
            return f"{self._name} is blooming beautifully!"
        return f"{self._name} has not bloomed yet"

    def show(self) -> None:
        """ Display flower information including color and bloom state """
        super().show()
        print(f"Color: {self._color}")
        print(self._bloom_status())


class Seed(Flower):
    """ Seed inherits from Flower and tracks the number of seeds produced """
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_count: int = 0
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = seed_count

    def _bloom_status(self) -> str:
        """ Return bloom status including seed count if blooming """
        if self._blooming:
            return f"Seeds: {self._seed_count}"
        return "Seeds: 0"

    def show(self) -> None:
        """ Display seed information including bloom state and seed count """
        super().show()


class Tree(Plant):
    """ Tree plant with shade production and extended statistics """
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._grow_rate = _GROW_RATE
        self._stats = self._TreeStats()

    class _TreeStats(Plant._Stats):
        """ Extends _Stats with a produce_shade() counter """

        def __init__(self) -> None:
            super().__init__()
            self._counts["shade"] = 0

        def show(self) -> None:
            """ Display stats with shade counter on a separate line """
            super().show()
            print(f"{self._counts['shade']} shade")

    def produce_shade(self) -> None:
        """ Print shade info and increment the shade counter """
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )
        self._stats.increment("shade")

    def show(self) -> None:
        """ Display tree information including trunk diameter """
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    """ Vegetable plant with nutritional value tracking """
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

    def grow(self, grow_rate: float = None) -> None:
        """ Grow the vegetable and increment its nutritional value """
        super().grow(grow_rate)
        self._nutritional_value += 1

    def show(self) -> None:
        """ Display vegetable info including harvest season and nutrition """
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def _display_stats(plant: Plant) -> None:
    """ Display call statistics for any kind of plant """
    print(f"[Statistics for {plant._name}]")
    plant._stats.show()


def _show_and_stats(plant: Plant, show_plant: bool = True) -> None:
    """ Show a plant and its statistics """
    if show_plant:
        plant.show()
        print()
    _display_stats(plant)
    print()


def main():
    print("=== Garden stadistics ===")
    print("=== Check year-old")
    print(Plant._is_older(30))
    print(Plant._is_older(400))
    print()

    f = Flower("Rose", 15.0, 10, "red")
    _show_and_stats(f)
    print(f"[asking the {f._name} to bloom]")
    print()
    f.simulate(1, 8.0)
    f.bloom()
    _show_and_stats(f)

    t = Tree("Oak", 200.0, 365, 5.0)
    _show_and_stats(t)
    print(f"[asking the {t._name} to produce shade]")
    print()
    t.produce_shade()
    _show_and_stats(t, show_plant=False)

    s = Seed("Sunflower", 80.0, 45, "yellow", seed_count=0)
    _show_and_stats(s)
    print(f"[make {s._name} grow, age and bloom]")
    print()
    s.simulate(20)
    s._seed_count = 42
    s.bloom()
    _show_and_stats(s)

    a = Plant.anonymous()
    _show_and_stats(a)


if __name__ == "__main__":
    main()
