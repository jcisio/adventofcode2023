"""
Advent Of Code
--- Day 8: Haunted Wasteland ---
https://adventofcode.com/2023/day/8
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.dest = input['dest']
        self.ins = input['instructions']

    def solve(self):
        s = 0
        here = 'AAA'
        while here != 'ZZZ':
            here = self.dest[here][0 if self.ins[s % len(self.ins)] == 'L' else 1]
            s += 1
        return s

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        dest = {}
        for i in range(2, len(input)):
            a, b, c = parse.parse("{} = ({}, {})", input[i]).fixed
            dest[a] = (b, c)
        self.input = {"instructions": input[0], "dest": dest}

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
