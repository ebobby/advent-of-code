#!/usr/bin/env python

import fileinput

frequency = [0] * 12

oxigen = []
co2_scrubber = []

for line in fileinput.input():
    line = line.strip()

    if line == "":
        raise "Empty line!"

    oxigen.append(line)
    co2_scrubber.append(line)

for i in range(12):
    if len(oxigen) > 1:
        frequency = 0
        for n in oxigen:
            frequency += 1 if n[i] == "1" else -1

        oxigen = [n for n in oxigen if n[i] == ("1" if frequency >= 0 else "0")]

for i in range(12):
    if len(co2_scrubber) > 1:
        frequency = 0
        for n in co2_scrubber:
            frequency += 1 if n[i] == "1" else -1

        co2_scrubber = [
            n for n in co2_scrubber if n[i] == ("0" if frequency >= 0 else "1")
        ]

print(
    f"Day 3, 2: o: {oxigen}, co2: {co2_scrubber}, life support: {int(oxigen[0], base=2) * int(co2_scrubber[0], base=2)}"
)
