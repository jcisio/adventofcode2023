"""
Advent Of Code
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3
"""
from __future__ import annotations
import functools
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input
        self.M, self.N = len(input), len(input[0])

    def is_symbol(self, i, j):
        return not self.input[i][j] in '0123456789.'

    def is_part_number(self, i, j):
        return i > 0 and self.is_symbol(i-1, j) or \
            i < self.M - 1 and self.is_symbol(i+1, j) or \
            j > 0 and self.is_symbol(i, j-1) or \
            j < self.N - 1 and self.is_symbol(i, j+1) or \
            i > 0 and j > 0 and self.is_symbol(i-1, j-1) or \
            i < self.M - 1 and j > 0 and self.is_symbol(i+1, j-1) or \
            i > 0 and j < self.N - 1 and self.is_symbol(i-1, j+1) or \
            i < self.M - 1 and j < self.N - 1 and self.is_symbol(i+1, j+1)

    def solve(self):
        s = 0
        for i, line in enumerate(self.input):
            number = 0
            is_adjacent = False
            for j, char in enumerate(line):
                if char.isdigit():
                    number = number * 10 + int(char)
                    if self.is_part_number(i, j):
                        is_adjacent = True
                if not char.isdigit() or j == self.N - 1:
                    if is_adjacent:
                        s += number
                    number = 0
                    is_adjacent = False
        return s

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
