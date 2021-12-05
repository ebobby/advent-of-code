#!/usr/bin/env python

import fileinput
import sys

increasing = 0
window = []
last_size = sys.maxsize

for line in fileinput.input():
    line = line.strip()

    if line == "":
        exit(1)

    window.append(int(line))

    if len(window) >= 3:
        size = sum(window[-3:])

        if size > last_size:
            increasing += 1

        last_size = size

print(f"Day 1, 2: increasing measurements (3-window): {increasing}.")
