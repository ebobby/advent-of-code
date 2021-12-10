#!/usr/bin/env python

import fileinput
import sys

last_depth = sys.maxsize
increasing = 0


for line in fileinput.input():
    line = line.strip()

    if line == "":
        exit(1)

    depth = int(line)
    if depth > last_depth:
        increasing += 1
    last_depth = depth

print(f"Day 1, 1: increasing measurements: {increasing}.")
