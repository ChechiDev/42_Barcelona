#!/usr/bin/env python3

def ft_garden_intro() -> str:
    name = input("Enter the plant name: ")
    height = float(input("Enter the height plant: "))
    age = int(input("Enter the plant age: "))

    print(f"\nPlant Name: {name} \
            \nPlant Height: {height} \
            \nPlant Age: {age}")


if __name__ == "__main__":
    ft_garden_intro()
