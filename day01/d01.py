"""
Advent Of Code
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1
"""
from __future__ import annotations
import re


class Problem:
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    def __init__(self, input) -> None:
        self.input = input

    def get_first_number(self, s, parse_text=False):
        i = 0
        while i < len(s):
            if s[i].isdigit():
                return int(s[i])
            if parse_text:
                for c in self.numbers:
                    if s[i:i+len(c)] == c:
                        return self.numbers[c]
            i += 1
        raise Exception("No number found: " + s)

    def get_last_number(self, s, parse_text=False):
        i = len(s) - 1
        while i >= 0:
            if s[i].isdigit():
                return int(s[i])
            if parse_text:
                for c in self.numbers:
                    if s[i:i+len(c)] == c:
                        return self.numbers[c]
            i -= 1
        raise Exception("No number found: " + s)

    def get_value(self, s, parse_text=False):
        return self.get_first_number(s, parse_text) * 10 + self.get_last_number(s, parse_text)

    def solve(self):
        return sum(map(self.get_value, self.input))

    def solve2(self):
        return sum(map(lambda s: self.get_value(s, True), self.input))


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
