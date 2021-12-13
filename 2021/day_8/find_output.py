#!/usr/bin/env python

import fileinput

DIGITS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def read_input():
    result = []
    for line in fileinput.input():
        line = line.strip()

        if line == "":
            continue

        digits, output = line.split(" | ")

        result.append((list(map(set, digits.split())), output.split()))

    return result


def decode(entries, output):
    translation_table = {}

    digit_1 = [entry for entry in entries if len(entry) == 2][0]
    digit_4 = [entry for entry in entries if len(entry) == 4][0]
    digit_7 = [entry for entry in entries if len(entry) == 3][0]
    digit_8 = [entry for entry in entries if len(entry) == 7][0]

    # The only remaining element of removing digit 1 to 7 gives us the
    # 'a' segment
    translation_table[list(digit_7 - digit_1)[0]] = "a"

    digits_with_six_segments = [entry for entry in entries if len(entry) == 6]

    for i in digits_with_six_segments:
        remainder = digit_8 - i
        # If remainder is a subset of digit 1 we found digit 6
        if remainder.issubset(digit_1):
            # We can figure out 'c' from removing 6 from 8 if the remainder is in 1
            translation_table[list(remainder)[0]] = "c"
            # Now that we have 'c' we can figure out 'f'
            translation_table[list(digit_1 - remainder)[0]] = "f"
            # And we found digit 6
            digit_6 = i

    # We have digit 9 and 0 left here.
    digits_with_six_segments.remove(digit_6)

    for i in digits_with_six_segments:
        remainder = digit_6 - i
        # If remainder is subset of digit 4 we found digit 0 and 'd'
        if remainder.issubset(digit_4):
            translation_table[list(remainder)[0]] = "d"
            digit_0 = i

    # We now have only digit 9 here
    digits_with_six_segments.remove(digit_0)
    digit_9 = digits_with_six_segments[0]

    # Removing digit 0 to digit 8 gives us 'd'
    translation_table[list(digit_8 - digit_0)[0]] = "d"
    # Removing digit 9 to digit 8 gives us 'e'
    translation_table[list(digit_8 - digit_9)[0]] = "e"

    # Some set math to find 'b'
    translation_table[list(digit_4 - (digit_1 | (digit_8 - digit_0)))[0]] = "b"

    leftover = {"a", "b", "c", "d", "e", "f", "g"} - set(translation_table.keys())

    # We get 'g' by elimination
    translation_table[list(leftover)[0]] = "g"

    # Do actual translation
    result = 0
    multiplier = 1000
    for digit in output:
        translated_digit = "".join(sorted(translation_table[c] for c in digit))
        result += DIGITS[translated_digit] * multiplier
        multiplier = multiplier // 10

    return result


if __name__ == "__main__":
    entries = read_input()

    output = sum(decode(*entry) for entry in entries)

    print(f"Day 8, 2 : The sum of all output numbers is: {output}")
