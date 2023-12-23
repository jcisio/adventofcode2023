"""
Advent Of Code
--- Day 23: A Long Walk ---
https://adventofcode.com/2023/day/23
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input
        self.r, self.c = len(input), len(input[0])

    def longest(self, start, end, visited):
        if start == end:
            #print(len(visited), '\n', visited)
            return 0
        if self.input[start[0]][start[1]] == '#':
            return 0
        if start in visited:
            return 0
        if start[0] < 0 or start[0] >= self.r or start[1] < 0 or start[1] >= self.c:
            return 0

        visited.add(start)

        next = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
        c = self.input[start[0]][start[1]]
        if c in next:
            return 1 + self.longest((start[0]+next[c][0], start[1]+next[c][1]), end, visited)

        lengths = {}
        for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            lengths[d] = self.longest((start[0]+d[0], start[1]+d[1]), end, visited.copy())
        return (1 + max(lengths.values())) if lengths else 0

    def solve(self):
        return self.longest((0, 1), (self.r-1, self.c-2), set())

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()

import sys
sys.setrecursionlimit(10000)

f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
