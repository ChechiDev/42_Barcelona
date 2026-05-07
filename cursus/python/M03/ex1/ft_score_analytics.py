#!/usr/bin/env python3

import sys


def main() -> None:

    scores = []
    print("=== Player Score Analytics ===")
    for i in sys.argv[1:]:
        try:
            scores.append(int(i))
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    if not scores:
        print(
            f"No scores provided. "
            f"Usage: python3 {sys.argv[0]} "
            f"<score1> <score2>... "
        )
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores)-min(scores)}")


if __name__ == "__main__":
    main()
