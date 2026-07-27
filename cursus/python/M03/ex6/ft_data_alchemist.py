#!/usr/bin/env python3
import random

INITIAL_PLAYERS = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {INITIAL_PLAYERS}")
    players = [x.title() for x in INITIAL_PLAYERS]
    print(f"New list with all names capitalized: {players}")
    players_cap = [x for x in INITIAL_PLAYERS if x[0].isupper()]
    print(f"New list of capitalized names only: {players_cap}")
    scores = {x: random.randint(0, 1000) for x in players}
    print(f"Score dict: {scores}")
    score_avg = round((sum(scores.values()) / len(scores)), 2)
    print(f"Score average is: {score_avg}")
    high_scores = {x: scores[x] for x in scores if scores[x] > score_avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
