#!/usr/bin/env python

import fileinput


def read_input():
    result = []
    for line in fileinput.input():
        line = line.strip()

        if line == "":
            continue

        result.append(list(int(c) for c in line))

    return result


if __name__ == "__main__":
    heightmap = read_input()

    height = len(heightmap)
    width = len(heightmap[0])

    risk_levels = []

    for y in range(height):
        for x in range(width):

            low_point = True

            if x - 1 >= 0:
                low_point = low_point and (heightmap[y][x] < heightmap[y][x - 1])
            if x + 1 < width:
                low_point = low_point and (heightmap[y][x] < heightmap[y][x + 1])
            if y - 1 >= 0:
                low_point = low_point and (heightmap[y][x] < heightmap[y - 1][x])
            if y + 1 < height:
                low_point = low_point and (heightmap[y][x] < heightmap[y + 1][x])

            if low_point:
                risk_levels.append(heightmap[y][x] + 1)

    print(f"Day 9, 1 : Sum of risk levels: {sum(risk_levels)}")
