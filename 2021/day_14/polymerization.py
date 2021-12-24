#!/usr/bin/env python

import fileinput
from collections import Counter, defaultdict


def read_input():
    input = fileinput.input()

    template = next(input).strip()

    # empty line
    next(input)

    code = defaultdict(lambda: "")

    for line in input:
        line = line.strip()

        if line == "":
            break

        pair, v = line.split(" -> ")
        code[pair] = v

    return template, code


def expand(template, code, times):
    expanded = template
    for step in range(times):
        expansion = ""

        for i in range(len(expanded) - 1):
            expansion += expanded[i]
            expansion += code[expanded[i : i + 2]]
        expansion += expanded[-1]

        expanded = expansion
    return expanded


if __name__ == "__main__":
    template, code = read_input()

    frequencies = dict(Counter(expand(template, code, 10)))

    print(
        f"Day 14, 1: Most common element minus least common: {max(*frequencies.values()) - min(*frequencies.values())}"
    )
