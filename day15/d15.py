"""
Advent Of Code
--- Day 15: Lens Library ---
https://adventofcode.com/2023/day/15
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self):
        total = 0
        for m in self.input.split(','):
            s = 0
            for c in m:
                s = (s + ord(c)) * 17 % 256
            total += s
#            print(m, s)
        return total

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip())
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
