#!/usr/bin/env python

import fileinput
import sys


def read_input():
    input = fileinput.input()

    # Read number list
    return list(map(int, next(input).split(",")))


if __name__ == "__main__":
    crab_positions = read_input()

    min_pos = min(crab_positions)
    max_pos = max(crab_positions)

    most_efficient_pos = 0
    minimum_fuel = sys.maxsize

    for i in range(min_pos, max_pos + 1):
        current_fuel_comsumption = 0
        for crab in crab_positions:
            current_fuel_comsumption += abs(crab - i)
        if current_fuel_comsumption < minimum_fuel:
            minimum_fuel = current_fuel_comsumption
            most_efficient_pos = i

    print(f"Day 7, 1: Most efficient consumption: {minimum_fuel}")
