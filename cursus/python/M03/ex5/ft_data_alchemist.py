#!/usr/bin/env python3
import random
import typing


INITIAL_PLAYERS = (
    "alice",
    "bob",
    "charlie",
    "dylan",
)

ACTIONS = (
    "run",
    "move",
    "swim",
    "climb",
    "grab",
    "release",
    "use",
    "eat",
    "sleep",
)

def gen_event() -> typing.Generator[tuple[str, str], None, None]:

    while True:
        name = random.choice(INITIAL_PLAYERS)       
        action = random.choice(ACTIONS)       
        yield (name, action)

def consume_event() -> tuple[str, str]:
    pass


def main() -> None:

    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for i in range(0, 1001):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")


if __name__ == "__main__":
    main()
