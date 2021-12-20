#!/usr/bin/env python

import fileinput


def read_input():
    lines = []
    for line in fileinput.input():
        line = line.strip()

        if line == "":
            raise "Empty line!"

        lines.append(list(map(int, (ch for ch in line))))
    return lines


def increase_energy(octopi, x, y, flashed):
    height = len(octopi)
    width = len(octopi[0])

    if x < 0 or y < 0 or x >= width or y >= height or (x, y) in flashed:
        return 0

    if octopi[y][x] == 9:
        octopi[y][x] = 0

        flashed.add((x, y))

        flashes = 1
        for j in range(-1, 2):
            for i in range(-1, 2):
                flashes += increase_energy(octopi, x + i, y + j, flashed)
        return flashes
    else:
        octopi[y][x] += 1

        return 0


if __name__ == "__main__":
    octopi = read_input()

    height = len(octopi)
    width = len(octopi[0])

    step = 1
    while True:
        flashed = set()
        for y in range(height):
            for x in range(width):
                increase_energy(octopi, x, y, flashed)

        if len(flashed) == height * width:
            break

        step += 1

    print(f"Day 11, 2 : Octopi synchronized in step: {step}")
