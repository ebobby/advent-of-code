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


def find_basin(x, y, heightmap, seen):
    height = len(heightmap)
    width = len(heightmap[0])

    if (
        x < 0
        or y < 0
        or x >= width
        or y >= height
        or heightmap[y][x] == 9
        or (x, y) in seen
    ):
        return []

    basin = [(x, y)]

    seen.add((x, y))

    basin.extend(find_basin(x - 1, y, heightmap, seen))
    basin.extend(find_basin(x + 1, y, heightmap, seen))
    basin.extend(find_basin(x, y - 1, heightmap, seen))
    basin.extend(find_basin(x, y + 1, heightmap, seen))

    return basin


if __name__ == "__main__":
    heightmap = read_input()

    height = len(heightmap)
    width = len(heightmap[0])

    basins = []
    seen = set()

    for y in range(height):
        for x in range(width):
            if (x, y) not in seen:
                basin = set(find_basin(x, y, heightmap, seen))

                if basin:
                    basins.append(basin)

    basins_sizes = sorted((len(b) for b in basins), reverse=True)

    print(
        f"Day 9, 2 : 3 largest basins sizes multiplication: {basins_sizes[0] * basins_sizes[1] * basins_sizes[2]}"
    )
