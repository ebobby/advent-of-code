#!/usr/bin/env python


import fileinput
from collections import namedtuple, defaultdict

Line = namedtuple("Line", ["x1", "y1", "x2", "y2"])


def read_input():
    def convert_line(line):
        coordinates = line.split(" -> ")
        p1 = list(map(int, coordinates[0].split(",")))
        p2 = list(map(int, coordinates[1].split(",")))
        # Sort points
        if p1[0] == p2[0]:
            p1, p2 = sorted([p1, p2], key=lambda p: p[1])
        if p1[1] == p2[1]:
            p1, p2 = sorted([p1, p2], key=lambda p: p[0])

        return Line(x1=p1[0], y1=p1[1], x2=p2[0], y2=p2[1])

    input = fileinput.input()

    lines = []
    for line in input:
        line = line.strip()

        if line == "":
            continue

        lines.append(convert_line(line))

    return lines


# Ode to my own stupidity.
# def overlapping_points(line1, line2, overlaps):
#    if line1.x1 == line1.x2 == line2.x1 == line2.x2:
#        line_min, line_max = sorted([line1, line2], key=lambda l: l.y1)
#
#        if min(line_min.y2, line_max.y2) >= line_max.y1:
#            for i in range(line_max.y1, min(line_min.y2, line_max.y2) + 1):
#                overlaps[(line_min.x1, i)] = overlaps.get((line_min.x1, i), 0) + 1
#
#    elif line1.y1 == line1.y2 == line2.y1 == line2.y2:
#        line_min, line_max = sorted([line1, line2], key=lambda l: l.x1)
#
#        if min(line_min.x2, line_max.x2) >= line_max.x1:
#            for i in range(line_max.x1, min(line_min.x2, line_max.x2) + 1):
#                overlaps[(i, line_min.y1)] = overlaps.get((i, line_min.y1), 0) + 1
#
#        return max(min(line_min.x2, line_max.x2) - line_max.x1 + 1, 0)
#    else:
#        line_min, line_max = sorted([line1, line2], key=lambda l: l.x1)
#
#        if line_max.x1 <= line_min.x2:
#            x = line_max.x1
#
#            line_min, line_max = sorted([line1, line2], key=lambda l: l.y1)
#            if line_max.y1 <= line_min.y2:
#                y = line_max.y1
#                overlaps[(x, y)] = overlaps.get((x, y), 0) + 1
#    return 0


def trace_line(line, accum):
    if line.x1 == line.x2:
        y1 = min(line.y1, line.y2)
        y2 = max(line.y1, line.y2)
        for y in range(y1, y2 + 1):
            accum[(line.x1, y)] += 1
    elif line.y1 == line.y2:
        x1 = min(line.x1, line.x2)
        x2 = max(line.x1, line.x2)
        for x in range(x1, x2 + 1):
            accum[(x, line.y1)] += 1
    else:
        p1, p2 = sorted([(line.x1, line.y1), (line.x2, line.y2)], key=lambda p: p[0])

        yadd = 1 if p1[1] < p2[1] else -1

        y = p1[1]
        for x in range(p1[0], p2[0] + 1):
            accum[(x, y)] += 1
            y += yadd


if __name__ == "__main__":
    lines = read_input()

    overlaps = defaultdict(lambda: 0)
    for line in lines:
        trace_line(line, overlaps)

    points = len([k for k, v in overlaps.items() if v > 1])

    print(f"Day 5: Overlapping points: {points}")
