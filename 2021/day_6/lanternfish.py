#!/usr/bin/env python

import fileinput


def read_input():
    input = fileinput.input()

    # Read number list
    return list(map(int, next(input).split(",")))


if __name__ == "__main__":
    fish = read_input()

    for i in range(0, 80):
        new_fish = []
        for i, f in enumerate(fish):
            if f == 0:
                new_fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
        fish.extend(new_fish)

    print(f"Day 6, 1 : {len(fish)} lanternfishes after 80 days.")
