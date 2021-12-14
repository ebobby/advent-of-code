#!/usr/bin/env python

from collections import defaultdict
import fileinput

ERROR_VALUE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


operators = {"}": "{", ")": "(", "]": "[", ">": "<"}


def read_input():
    return [line.strip() for line in fileinput.input() if line != ""]


if __name__ == "__main__":
    lines = read_input()

    total_errors = defaultdict(lambda: 0)
    opening = operators.values()
    for line in lines:
        chunks = []
        for char in line:
            if char in opening:
                chunks.append(char)
            else:
                last_chunk = chunks.pop()

                if last_chunk != operators[char]:
                    total_errors[char] += 1
                    break

    error_score = sum(ERROR_VALUE[err] * count for err, count in total_errors.items())

    print(f"Day 10, 1 : Error score: {error_score}")
