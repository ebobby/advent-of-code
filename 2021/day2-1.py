#!/usr/bin/env python

import fileinput

position = 0
depth = 0

for line in fileinput.input():
    line = line.strip()

    if line == "":
        exit(1)

    direction, amount = line.split(" ")

    if direction == "forward":
        position += int(amount)
    elif direction == "up":
        depth -= int(amount)
    elif direction == "down":
        depth += int(amount)


print(f"Day 2, 1: position: {position}, depth: {depth} pos: {position*depth}")
