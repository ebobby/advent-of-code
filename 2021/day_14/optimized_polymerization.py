#!/usr/bin/env python

import fileinput
from collections import Counter, defaultdict


def read_input():
    input = fileinput.input()

    template_s = next(input).strip()

    template = defaultdict(lambda: 0)
    for i in range(len(template_s) - 1):
        template[template_s[i : i + 2]] += 1
    template[template_s[-1]] = 1

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
        expansion = defaultdict(lambda: 0)

        for pair, how_many in expanded.items():
            if pair in code:
                x = code[pair]
                a, b = list(pair)
                expansion[f"{a}{x}"] += how_many
                expansion[f"{x}{b}"] += how_many
            else:
                expansion[pair] += how_many

        expanded = expansion
    return expanded


def frequencies(expansion):
    freq = defaultdict(lambda: 0)

    for pair, how_many in expansion.items():
        freq[pair[0]] += how_many

    return freq


if __name__ == "__main__":
    template, code = read_input()

    freq = frequencies(expand(template, code, 40))

    print(
        f"Day 14, 2: Most common element minus least common: {max(*freq.values()) - min(*freq.values())}"
    )
