#!/usr/bin/env python

import fileinput


def read_input():
    input = fileinput.input()

    # Read number list
    numbers = list(map(int, next(input).split(",")))
    # Skip empty line.
    next(input)

    boards = []
    current_board = []
    for line in input:
        line = line.strip()

        if line == "":
            if len(current_board) != 5:
                raise RuntimeError(
                    f"Error with current_board: {len(current_board)}, boards: {len(boards)}"
                )

            boards.append(current_board)
            current_board = []
            continue

        current_board.append([(int(n), False) for n in line.split()])
    return numbers, boards


def mark_board(board, n):
    for j in range(5):
        for i in range(5):
            if board[j][i][0] == n:
                board[j][i] = (n, True)


def is_winner(board):
    for j in range(5):
        if all(sq[1] for sq in board[j]):
            return True
    for i in range(5):
        if all(row[i][1] for row in board):
            return True


def sum_unmarked(board):
    s = 0
    for j in range(5):
        for i in range(5):
            if not board[j][i][1]:
                s += board[j][i][0]
    return s


if __name__ == "__main__":
    numbers, boards = read_input()

    for n in numbers:
        for board in boards:
            mark_board(board, n)

            if is_winner(board):
                print(f"Day 4, 1: Score of winning board: {sum_unmarked(board) * n}")
                exit(0)
