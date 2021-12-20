#!/usr/bin/env python

import fileinput
from collections import defaultdict


def read_input():
    locations = defaultdict(lambda: set())
    for line in fileinput.input():
        line = line.strip()

        if line == "":
            raise "Empty line!"

        a, b = line.split("-")

        locations[a].add(b)
        locations[b].add(a)

    return locations


def traverse(locations, start, seen={}):
    if start == "end":
        return ["end"]

    if start == "start" and seen.get("start") == 1:
        return []

    if start.islower():
        if seen.get(start) == 2:
            return []
        if seen.get(start) == 1 and 2 in seen.values():
            return []

        seen[start] = seen.get(start, 0) + 1

    paths = []
    for followup in locations[start]:
        for path in traverse(locations, followup, dict(seen)):
            paths.append(f"{start}-{path}")

    return list(set(paths))


if __name__ == "__main__":
    locations = read_input()

    small_caves = {cave for cave in locations.keys() if cave.islower()}

    how_many = len(traverse(locations, "start"))

    print(f"Day 12, 2 : All possible paths visiting one cave twice : {how_many}")
