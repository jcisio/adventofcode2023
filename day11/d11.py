"""
Advent Of Code
--- Day 11: Cosmic Expansion ---
https://adventofcode.com/2023/day/11
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.galaxies = input

    def solve(self, part=1):
        rows = set()
        cols = set()
        max_r = max_c = 0
        for (r,c) in self.galaxies:
            rows.add(r)
            cols.add(c)
            max_r = max(max_r, r)
            max_c = max(max_c, c)

        lower_r = []
        lower_c = []
        for r in range(max_r+1):
            lower_r.append(sum([1 for i in range(r) if i not in rows]))
        for c in range(max_c+1):
            lower_c.append(sum([1 for i in range(c) if i not in cols]))
        x = 1 if part == 1 else 999999
        galaxies = [(r+lower_r[r]*x, c+lower_c[c]*x) for (r,c) in self.galaxies]
        s = 0
        for i in range(len(galaxies)):
            for j in range(i+1, len(galaxies)):
                s += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])
        return s


class Solver:
    def __init__(self, input) -> None:
        galaxies = []
        for r,line in enumerate(input):
            for c,cell in enumerate(line):
                if cell == '#':
                    galaxies.append((r,c))
        self.input = galaxies

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve(part)


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
