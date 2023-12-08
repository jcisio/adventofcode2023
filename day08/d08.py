"""
Advent Of Code
--- Day 8: Haunted Wasteland ---
https://adventofcode.com/2023/day/8
"""
from __future__ import annotations
import parse
import math


class Problem:
    def __init__(self, input) -> None:
        self.dest = input['dest']
        self.ins = input['instructions']

    def move(self, here, step):
        return self.dest[here][0 if self.ins[step % len(self.ins)] == 'L' else 1]

    def solve(self, start='AAA'):
        s = 0
        here = start
        while here[-1] != 'Z':
            here = self.move(here, s)
            s += 1
        return s

    def solve2(self):
        total = 1
        for here in self.dest.keys():
            if here[-1] == 'A':
                next = self.solve(here)
                total = total * next // math.gcd(total, next)
        return total


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


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
