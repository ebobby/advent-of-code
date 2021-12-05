#!/usr/bin/env python

import fileinput

position = 0
depth = 0
aim = 0

for line in fileinput.input():
    line = line.strip()

    if line == "":
        exit(1)

    direction, amount = line.split(" ")

    if direction == "forward":
        position += int(amount)
        depth += aim * int(amount)
    elif direction == "up":
        aim -= int(amount)
    elif direction == "down":
        aim += int(amount)

print(
    f"Day 2, 2: position: {position}, depth: {depth}, aim: {aim}, pos: {position*depth}"
)
