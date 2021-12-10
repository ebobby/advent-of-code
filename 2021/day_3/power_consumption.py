#!/usr/bin/env python

import fileinput

frequency = [0] * 12

for line in fileinput.input():
    line = line.strip()

    if line == "":
        exit(1)

    for i, char in enumerate(line):
        frequency[i] += 1 if char == "1" else -1

gamma = 0
epsilon = 0
for i, remainder in enumerate(frequency):
    if remainder > 0:
        gamma |= 1 << (12 - i - 1)
    else:
        epsilon |= 1 << (12 - i - 1)

print(
    f"Day 3, 1: gamma: {gamma}, epsilon: {epsilon}, power consumption: {gamma * epsilon}"
)
