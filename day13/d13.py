"""
Advent Of Code
--- Day 13: Point of Incidence ---
https://adventofcode.com/2023/day/13
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.grid = input['grid']
        self.r = input['r']
        self.c = input['c']

    # Is mirror BEFORE col c
    def is_mirror_h(self, c):
        l = min(c, self.c - c)
        if l <= 0:
            return self.c
        smudges = []
        for r in range(self.r):
            if len(smudges) > 1:
                break
            for i in range(l):
                if self.grid[r][c-i-1] != self.grid[r][c+i]:
                    smudges.append((r, c-i-1))
                    if len(smudges) > 1:
                        break
        return len(smudges)

    # Is mirror BEFORE row r
    def is_mirror_v(self, r):
        l = min(r, self.r - r)
        if l <= 0:
            return self.c
        smudges = []
        for c in range(self.c):
            if len(smudges) > 1:
                break
            for i in range(l):
                if self.grid[r-i-1][c] != self.grid[r+i][c]:
                    smudges.append((r-i-1, c))
                    if len(smudges) > 1:
                        break
        return len(smudges)

    def get_value(self, part=1):
        r, c = 0, 0
        for i in range(self.c):
            if self.is_mirror_h(i+1)==part-1:
                c = i + 1
        for i in range(self.r):
            if self.is_mirror_v(i+1)==part-1:
                r = i + 1
#        print('\n'.join(self.grid), '\n', r, c, '\n')
        return c + r*100


class Solver:
    def __init__(self, input) -> None:
        notes = []
        grid = []
        input.append('')
        for line in input:
            if line == '':
                notes.append({'grid': grid, 'r': len(grid), 'c': len(grid[0])})
                grid = []
            else:
                grid.append(line)
        self.input = notes

    def solve(self, part=1):
        s = 0
        for note in self.input:
            problem = Problem(note)
            s += problem.get_value(part)
        return s


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
