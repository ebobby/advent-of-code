#!/usr/bin/env python

import fileinput


def read_input():
    input = fileinput.input()

    points = set()
    for line in input:
        line = line.strip()

        if line == "":
            break

        points.add(tuple(map(int, line.split(","))))

    folds = []
    for line in input:
        line = line.strip()

        if line == "":
            break

        loc = line.split()[-1].split("=")
        folds.append((0 if loc[0] == "x" else 1, int(loc[1])))

    return points, folds


def fold(points, axis, value):
    to_be_folded = [list(point) for point in points if point[axis] > value]

    remains = {point for point in points if point[axis] < value}

    for folded in to_be_folded:
        folded[axis] = (2 * value) - folded[axis]
        remains.add(tuple(folded))

    return remains


if __name__ == "__main__":
    points, folds = read_input()

    points = fold(points, folds[0][0], folds[0][1])

    print(f"Day 13, 1 : Remaining points: {len(points)}")
