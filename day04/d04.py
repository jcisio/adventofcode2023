"""
Advent Of Code
--- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4
"""
from __future__ import annotations
import functools
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def count_points(self, numbers):
        x = sum([1 if n in numbers[0] else 0 for n in numbers[1]])
        return 0 if x == 0 else pow(2, x-1)

    def solve(self):
        return sum([self.count_points(c) for c in self.input])

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        cards = []
        for line in input:
            _, win, have = parse.parse("Card {}: {} | {}", line)
            cards.append((list(map(int, win.split())), list(map(int, have.split()))))
        self.input = cards

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
