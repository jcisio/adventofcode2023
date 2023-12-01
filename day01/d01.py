"""
Advent Of Code
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1
"""
from __future__ import annotations
import re


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def get_number_from_line(self, line):
        c = re.sub(r'[a-z]*(.+?)[a-z]*$', r'\1', line)
        n = int(c[0] + c[-1])
        return n if n > 9 else n*11

    def solve(self):
        return sum(map(self.get_number_from_line, self.input))

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
