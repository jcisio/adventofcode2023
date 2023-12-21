"""
Advent Of Code
--- Day 21: Step Counter ---
https://adventofcode.com/2023/day/21
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        blocks = set()
        for r,line in enumerate(input):
            for c,p in enumerate(line):
                if p == '#':
                    blocks.add((r,c))
                elif p == 'S':
                    start = (r,c)
        self.blocks = blocks
        self.start = start
        self.r = len(input)
        self.c = len(input[0])

    def move(self, current):
        new = set()
        for r,c in current:
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = r+dr,c+dc
                if 0 <= nr < self.r and 0 <= nc < self.c and (nr,nc) not in self.blocks:
                    new.add((nr,nc))
        return new

    def solve(self):
        s = set([self.start])
        for i in range(64):
            s = self.move(s)
        return len(s)

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
