#!/usr/bin/env python

import fileinput
from collections import defaultdict

AUTOCOMPLETE_VALUE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

closing = {"}": "{", ")": "(", "]": "[", ">": "<"}

opening = {"{": "}", "(": ")", "[": "]", "<": ">"}


def read_input():
    return [line.strip() for line in fileinput.input() if line != ""]


if __name__ == "__main__":
    lines = read_input()

    incomplete_lines = []

    for line in lines:
        chunks = []
        corrupted = False

        for char in line:
            if char in opening.keys():
                chunks.append(char)
            else:
                last_chunk = chunks.pop()

                if last_chunk != closing[char]:
                    corrupted = True
                    break

        if not corrupted:
            incomplete_lines.append(chunks)

    scores = []
    for incomplete in incomplete_lines:
        incomplete.reverse()
        completion = "".join(opening[c] for c in incomplete)

        score = 0
        for char in completion:
            score *= 5
            score += AUTOCOMPLETE_VALUE[char]

        scores.append(score)

    scores = sorted(scores)

    print(f"Day 10, 2 : Autocomplete score: {scores[len(scores)//2]}")
