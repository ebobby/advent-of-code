#!/usr/bin/env python

import fileinput


def read_input():
    result = []
    for line in fileinput.input():
        line = line.strip()

        if line == "":
            continue

        digits, output = line.split(" | ")

        result.append((digits.split(), output.split()))

    return result


if __name__ == "__main__":
    entries = read_input()

    digits = 0
    for entry in entries:
        digits += len([output for output in entry[1] if len(output) in [2, 3, 4, 7]])

    print(f"Day 8, 1 : Digits 1, 4, 7, and 8 appear {digits} times.")
