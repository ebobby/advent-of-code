#!/usr/bin/env python

import fileinput


def read_input():
    input = fileinput.input()

    # Read number list
    return list(map(int, next(input).split(",")))


if __name__ == "__main__":
    first_gen = read_input()

    states = [0] * 9

    for i, f in enumerate(first_gen):
        states[f] += 1

    for day in range(256):
        new_fishes = states[0]
        states[0] = states[1]
        states[1] = states[2]
        states[2] = states[3]
        states[3] = states[4]
        states[4] = states[5]
        states[5] = states[6]
        states[6] = states[7] + new_fishes
        states[7] = states[8]
        states[8] = new_fishes

    print(f"Day 6, 2 : {sum(states)} lanternfishes after 256 days.")
