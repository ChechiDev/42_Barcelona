#!/usr/bin/env python3
import random
import typing

EVENTS = 1000
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


def consume_event(lista: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:

    while lista:
        idx = random.randint(0, len(lista) - 1)
        event = lista.pop(idx)
        yield event


def main() -> None:

    print("=== Game Data Stream Processor ===")
    # Part 1
    gen_1 = gen_event()
    for i in range(0, EVENTS):
        event_1 = next(gen_1)
        print(f"Event {i}: Player {event_1[0]} did action {event_1[1]}")

    # Part 2
    gen_2 = gen_event()
    list_event = [next(gen_2) for _ in range(10)]
    print(f"Built list of 10 events: {list_event}")

    # Part 3 
    for event in consume_event(list_event):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_event}")


if __name__ == "__main__":
    main()
