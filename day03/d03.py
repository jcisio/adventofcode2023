"""
Advent Of Code
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3
"""
from __future__ import annotations
from collections import defaultdict

class Problem:
    def __init__(self, input) -> None:
        self.input = input
        self.M, self.N = len(input), len(input[0])
        self.gears = defaultdict(list)

    def is_symbol(self, i, j):
        return not self.input[i][j] in '0123456789.'

    def is_gear(self, i, j):
        return self.input[i][j] == '*'

    def check_adjacent(self, i, j, func):
        if i > 0 and func(i-1, j):
            return (i-1, j)
        if i < self.M - 1 and func(i+1, j):
            return (i+1, j)
        if j > 0 and func(i, j-1):
            return (i, j-1)
        if j < self.N - 1 and func(i, j+1):
            return (i, j+1)
        if i > 0 and j > 0 and func(i-1, j-1):
            return (i-1, j-1)
        if i < self.M - 1 and j > 0 and func(i+1, j-1):
            return (i+1, j-1)
        if i > 0 and j < self.N - 1 and func(i-1, j+1):
            return (i-1, j+1)
        if i < self.M - 1 and j < self.N - 1 and func(i+1, j+1):
            return (i+1, j+1)
        return False

    def is_part_number(self, i, j):
        return self.check_adjacent(i, j, self.is_symbol)

    def is_gear_ratio(self, i, j):
        return self.check_adjacent(i, j, self.is_gear)

    def solve(self):
        s = 0
        for i, line in enumerate(self.input):
            number = 0
            is_part_number = False
            current_gears = set()
            for j, char in enumerate(line):
                if char.isdigit():
                    number = number * 10 + int(char)
                    if self.is_part_number(i, j):
                        is_part_number = True
                    gear = self.is_gear_ratio(i, j)
                    if gear:
                        current_gears.add(gear)
                if not char.isdigit() or j == self.N - 1:
                    if is_part_number:
                        s += number
                    if current_gears:
                        for gear in current_gears:
                            self.gears[gear].append(number)
                    number = 0
                    is_part_number = False
                    current_gears = set()
        return s

    def solve2(self):
        self.solve()
        return sum([0 if len(g) != 2 else g[0]*g[1] for g in self.gears.values()])


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
